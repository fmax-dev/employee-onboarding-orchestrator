from httpx import AsyncClient

from app.core.config import settings
from app.models.onboarding_job import OnboardingJob
from app.services.providers.base import (
    InvitationProvider,
    ProviderAuthError,
    ProviderPermanentError,
    ProviderRateLimited,
    ProviderTransientError,
)


class GitHubProvider(InvitationProvider):
    async def send_invitation(
    self,
    company_email: str,
    job: OnboardingJob
    ) -> str:
        if settings.GITHUB_SIMULATE:
            return f"Simulated GitHub invitation sent for {company_email}"

        # Now real httpx request
        github_token = settings.GITHUB_TOKEN
        if github_token is None:
            raise ProviderAuthError("GitHub token is not configured")

        async with AsyncClient() as client:
            response = await client.post(
                url=f"https://api.github.com/orgs/{settings.GITHUB_ORG}/invitations",
                headers={"Authorization": f"Bearer {github_token.get_secret_value()}"},
                json={"email": company_email},
            )

            if response.status_code == 201:
                return f"Invited {company_email} to GitHub."

            if response.status_code == 429:
                raise ProviderRateLimited("GitHub rate limit reached")

            if response.status_code >= 500:
                raise ProviderTransientError("GitHub server error")

            if response.status_code in {401, 403}:
                raise ProviderAuthError("GitHub Authentication failed")

            if response.status_code >= 400:
                raise ProviderPermanentError("GitHub reject the invitation")

            raise ProviderPermanentError(
                f"Unexpected GitHub response status: {response.status_code}"
            )