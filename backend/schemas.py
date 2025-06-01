from pydantic import BaseModel


class StudentCreate(BaseModel):
    name: str
    email: str
    password: str


class StudentLogin(BaseModel):
    email: str
    password: str


class OrganizationCreate(BaseModel):
    name: str
    docs_url: str


class CertificateIssue(BaseModel):
    student_id: int
    organization_id: int
    course_name: str
