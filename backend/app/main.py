from fastapi import FastAPI
from scalar_fastapi import get_scalar_api_reference

app = FastAPI(
    title="Employee Onboarding Orchestrator",
    description="Orchestrates account provisioning across Slack, GitHub, and AWS.",
    version="1.0.0"
)

@app.get("/health")
def health_check():
    return {"status": "healthy", "service": "onboarding-orchestrator"}

@app.get("/scalar", include_in_schema=False)
def scalar_docs():
    return get_scalar_api_reference(
        openapi_url=app.openapi_url,
        title=app.title,
    )


