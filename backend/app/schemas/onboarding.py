from datetime import date
from uuid import UUID

from pydantic import BaseModel, ConfigDict, EmailStr, Field

from app.models.onboarding_job import JobStatus
from app.models.provisioning_task import ServiceName, TaskStatus


class HROnboardRequest(BaseModel):
    employee_id: str = Field(min_length=1, max_length=100)
    first_name: str = Field(min_length=1, max_length=100)
    last_name: str = Field(min_length=1, max_length=100)
    personal_email: EmailStr
    department: str = Field(min_length=1, max_length=100)
    start_date: date


class OnboardingAccepted(BaseModel):
    onboarding_job_id: UUID
    status: JobStatus


class ProvisioningTaskRead(BaseModel):
    service: ServiceName
    status: TaskStatus
    account_email: str | None = None
    details: str | None = None
    error_message: str | None = None

    model_config = ConfigDict(from_attributes=True)


class OnboardingStatusResponse(BaseModel):
    onboarding_job_id: UUID
    status: JobStatus
    company_email: str | None
    tasks: list[ProvisioningTaskRead]
