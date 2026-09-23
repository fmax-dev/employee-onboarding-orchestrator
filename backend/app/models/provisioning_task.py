import uuid
from datetime import datetime
from enum import Enum
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, ForeignKey, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.onboarding_job import OnboardingJob


class TaskKind(str, Enum):
    identity = "identity"
    invitation = "invitation"


class ServiceName(str, Enum):
    google_workspace = "google_workspace"
    slack = "slack"
    github = "github"


class TaskStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    retrying = "retrying"
    completed = "completed"
    failed = "failed"
    skipped = "skipped"


class ProvisioningTask(Base):
    __tablename__ = "provisioning_task"

    id: Mapped[int] = mapped_column(primary_key=True)
    onboarding_job_id: Mapped[uuid.UUID] = mapped_column(
        Uuid, ForeignKey("onboarding_job.id")
    )
    job: Mapped["OnboardingJob"] = relationship(back_populates="tasks")
    service: Mapped[ServiceName]
    kind: Mapped[TaskKind]
    status: Mapped[TaskStatus] = mapped_column(default=TaskStatus.pending)
    attempts: Mapped[int] = mapped_column(default=0)
    account_email: Mapped[str | None]
    details: Mapped[str | None]
    error_message: Mapped[str | None]
    created_at: Mapped[datetime] = mapped_column(DateTime, server_default=func.now())
    updated_at: Mapped[datetime] = mapped_column(
        DateTime, server_default=func.now(), onupdate=func.now()
    )
