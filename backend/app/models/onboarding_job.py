import uuid
from datetime import date, datetime
from enum import Enum
from hashlib import sha256
from typing import TYPE_CHECKING

from sqlalchemy import DateTime, Uuid, func
from sqlalchemy.orm import Mapped, mapped_column, relationship

from app.db.base import Base

if TYPE_CHECKING:
    from app.models.provisioning_task import ProvisioningTask


class JobStatus(str, Enum):
    pending = "pending"
    in_progress = "in_progress"
    completed = "completed"
    partial_success = "partial_success"
    failed = "failed"


class OnboardingJob(Base):
    __tablename__ = "onboarding_job"

    id: Mapped[uuid.UUID] = mapped_column(
        Uuid, 
        primary_key=True, 
        default=uuid.uuid4
    )
    employee_id: Mapped[str]
    first_name: Mapped[str]
    last_name: Mapped[str]
    personal_email: Mapped[str]
    department: Mapped[str]
    start_date: Mapped[date]
    company_email: Mapped[str | None]
    dedupe_key: Mapped[str] = mapped_column(
        unique=True,
        index=True,
        default=lambda context: sha256(
            context.get_current_parameters()["employee_id"].encode()
        ).hexdigest(),
    )
    status: Mapped[JobStatus] = mapped_column(default=JobStatus.pending)
    created_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now()
    )
    updated_at: Mapped[datetime] = mapped_column(
        DateTime,
        server_default=func.now(),
        onupdate=func.now()
    )
    tasks: Mapped[list["ProvisioningTask"]] = relationship(
        back_populates="job", cascade="all, delete-orphan"
    )