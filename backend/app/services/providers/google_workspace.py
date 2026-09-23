import asyncio

from app.core.config import settings
from app.models.onboarding_job import OnboardingJob
from app.services.providers.base import IdentityProvider


class GoogleWorkspaceProvider(IdentityProvider):

    async def create_account(
    self, 
    job: OnboardingJob
    ) -> str:
        await asyncio.sleep(0.2)

        company_email = (
            f"{job.first_name}.{job.last_name}@{settings.COMPANY_DOMAIN}"
        ).lower()

        return company_email