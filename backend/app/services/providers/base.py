from abc import ABC, abstractmethod
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from app.models.onboarding_job import OnboardingJob


class ProviderError(Exception):
    """Base exception for provider failures."""


class ProviderRateLimited(ProviderError):  # Safe to retry
    """The provider asked us to retry later"""


class ProviderTransientError(ProviderError): # Safe to retry
    """A temporary provider failure that may succeed on retry"""


class ProviderPermanentError(ProviderError): # Do NOT retry
    """A non-retryable provider failure"""


class ProviderAuthError(ProviderError): # Do not retry but log loudly -- it's a misconfiguration
    """Provider authentication or configuration failed."""


class IdentityProvider(ABC):

    @abstractmethod
    async def create_account(
    self, 
    job: "OnboardingJob"
    ) -> str:
        """Create an account and return its company email"""
        raise NotImplementedError


class InvitationProvider(ABC):

    @abstractmethod
    async def send_invitation(
    self, 
    company_email: str, 
    job: "OnboardingJob"
    ) -> str:
        """Send an invitatation with the newly created account and return a short description"""
        raise NotImplementedError