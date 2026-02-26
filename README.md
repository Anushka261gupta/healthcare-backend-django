# Healthcare Backend (Django + DRF)

This project implements a backend system for a healthcare application using Django REST Framework and PostgreSQL.

## Implemented APIs

### Authentication
- POST /api/auth/register/
- POST /api/auth/login/

### Patient Management
- POST /api/patients/
- GET /api/patients/
- GET /api/patients/<id>/
- PUT /api/patients/<id>/
- DELETE /api/patients/<id>/

### Doctor Management
- POST /api/doctors/
- GET /api/doctors/
- GET /api/doctors/<id>/
- PUT /api/doctors/<id>/
- DELETE /api/doctors/<id>/

### Patient–Doctor Mapping
- POST /api/mappings/
- GET /api/mappings/
- GET /api/mappings/<patient_id>/
- DELETE /api/mappings/<id>/

## Tech Stack
- Django, Django REST Framework
- JWT Authentication (SimpleJWT)
- PostgreSQL
- Postman (for API testing)

## Setup
1. Create virtualenv & install dependencies  
2. Create `.env` with DB credentials  
3. Run:
    python manage.py migrate
    python manage.py runserver

## Future Scope
- Integrate ML model for breast cancer prediction from medical images.
- Add image upload API for patient reports/scans.
- Role-based access (Doctor, Admin, Patient).
- Email notifications for doctor assignment & diagnosis updates.
- Simple frontend dashboard to visualize patients and predictions.
- Deployment on cloud (AWS / Render) with production-ready setup.

## Notes
All APIs are secured with JWT authentication and tested using Postman. Data persistence verified via PostgreSQL (pgAdmin).
