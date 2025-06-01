# Achievo Backend

This module implements the backend APIs for stage 1 of the Achievo platform. It exposes RESTful endpoints for user and organisation registration, login and certificate issuance.

The API is built with **FastAPI** and uses **SQLModel** with a SQLite database. Passwords are hashed using SHA256 for demonstration purposes.

## Main Endpoints
- `POST /students/register` – Register a new student.
- `POST /students/login` – Student login.
- `POST /organizations/register` – Register an organisation.
- `POST /certificates/issue` – Issue a certificate NFT (stubbed).
- `GET /certificates/{certificate_id}` – Retrieve certificate details.

Tests use `pytest` and the `TestClient` from FastAPI to validate API behaviour.
