import asyncio

from app.models.onboarding_job import OnboardingJob
from app.services.providers.base import InvitationProvider


class SlackProvider(InvitationProvider):
    async def send_invitation(
    self, 
    company_email: str, 
    job: OnboardingJob
    ) -> str:
        await asyncio.sleep(0.2)

        return f"Invited {company_email} to Slack."