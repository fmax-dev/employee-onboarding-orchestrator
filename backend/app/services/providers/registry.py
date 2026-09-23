from app.core.config import settings
from app.services.providers.github import GitHubProvider
from app.services.providers.google_workspace import GoogleWorkspaceProvider
from app.services.providers.slack import SlackProvider


def get_identity_provider():
    if settings.IDENTITY_PROVIDER == "google_workspace":
        return GoogleWorkspaceProvider()

    raise ValueError(
        f"Unsupported identity provider: {settings.IDENTITY_PROVIDER}"
    )


def get_invitation_providers():
    return [
        SlackProvider(),
        GitHubProvider(),
    ]