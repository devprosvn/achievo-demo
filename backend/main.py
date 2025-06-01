from fastapi import Depends, FastAPI, HTTPException
from sqlmodel import Session, select

from .db import init_db, get_session
from .models import Student, Organization, Certificate
from .schemas import (
    StudentCreate,
    StudentLogin,
    OrganizationCreate,
    CertificateIssue,
)
from .auth import hash_password, verify_password

app = FastAPI(title="Achievo API")


@app.on_event("startup")
def on_startup() -> None:
    init_db()


@app.post("/students/register", status_code=201)
def register_student(data: StudentCreate, session: Session = Depends(get_session)):
    if session.exec(select(Student).where(Student.email == data.email)).first():
        raise HTTPException(status_code=400, detail="Email already registered")
    student = Student(
        name=data.name,
        email=data.email,
        password_hash=hash_password(data.password),
    )
    session.add(student)
    session.commit()
    session.refresh(student)
    return {"id": student.id, "email": student.email}


@app.post("/students/login")
def login_student(data: StudentLogin, session: Session = Depends(get_session)):
    student = session.exec(select(Student).where(Student.email == data.email)).first()
    if not student or not verify_password(data.password, student.password_hash):
        raise HTTPException(status_code=403, detail="Invalid credentials")
    return {"message": "login successful"}


@app.post("/organizations/register", status_code=201)
def register_org(data: OrganizationCreate, session: Session = Depends(get_session)):
    org = Organization(name=data.name, docs_url=data.docs_url)
    session.add(org)
    session.commit()
    session.refresh(org)
    return {"id": org.id, "name": org.name}


@app.post("/certificates/issue", status_code=201)
def issue_certificate(data: CertificateIssue, session: Session = Depends(get_session)):
    cert = Certificate(
        student_id=data.student_id,
        organization_id=data.organization_id,
        course_name=data.course_name,
        hash="placeholder-hash",
    )
    session.add(cert)
    session.commit()
    session.refresh(cert)
    return {"id": cert.id, "hash": cert.hash}


@app.get("/certificates/{certificate_id}")
def get_certificate(certificate_id: int, session: Session = Depends(get_session)):
    cert = session.get(Certificate, certificate_id)
    if not cert:
        raise HTTPException(status_code=404, detail="Certificate not found")
    return cert
