# Healthcare Backend API

A Django REST Framework-based backend system for a healthcare application. This system allows users to register, log in, and securely manage patient and doctor records.

## 🚀 Features

- User Authentication with JWT Tokens
- Patient Management
- Doctor Management
- Patient-Doctor Mapping
- Secure API endpoints
- PostgreSQL database integration

## 🔧 Tech Stack

- **Django**: Web framework
- **Django REST Framework**: API building toolkit
- **djangorestframework-simplejwt**: JWT authentication
- **PostgreSQL**: Database
- **python-dotenv**: Environment variable management

## 📋 API Endpoints

### Authentication APIs

- **POST** `/api/auth/register/` - Register a new user with name, email, and password
- **POST** `/api/auth/login/` - Log in a user and return a JWT token
- **POST** `/api/auth/refresh/` - Refresh JWT token

### Patient Management APIs

- **POST** `/api/patients/` - Add a new patient (Authenticated users only)
- **GET** `/api/patients/` - Retrieve all patients created by the authenticated user
- **GET** `/api/patients/{id}/` - Get details of a specific patient
- **PUT** `/api/patients/{id}/` - Update patient details
- **DELETE** `/api/patients/{id}/` - Delete a patient record

### Doctor Management APIs

- **POST** `/api/doctors/` - Add a new doctor (Authenticated users only)
- **GET** `/api/doctors/` - Retrieve all doctors
- **GET** `/api/doctors/{id}/` - Get details of a specific doctor
- **PUT** `/api/doctors/{id}/` - Update doctor details
- **DELETE** `/api/doctors/{id}/` - Delete a doctor record

### Patient-Doctor Mapping APIs

- **POST** `/api/mappings/` - Assign a doctor to a patient
- **GET** `/api/mappings/` - Retrieve all patient-doctor mappings
- **GET** `/api/mappings/?patient_id={id}` - Get all doctors assigned to a specific patient
- **DELETE** `/api/mappings/{id}/` - Remove a doctor from a patient

## 🛠️ Setup and Installation

1. Clone the repository
   ```bash
   git clone <repository-url>
   cd healthcare
   ```

2. Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies
   ```bash
   pip install -r requirements.txt
   ```

4. Create a `.env` file in the project root with the following variables:
   ```
   DB_NAME=healthcare_db
   DB_USER=postgres
   DB_PASSWORD=your_password
   DB_HOST=localhost
   DB_PORT=5432
   ```

5. Create the PostgreSQL database
   ```bash
   # Connect to PostgreSQL
   psql -U postgres
   
   # Inside PostgreSQL shell
   CREATE DATABASE healthcare_db;
   
   # Exit PostgreSQL shell
   \q
   ```

6. Apply migrations
   ```bash
   python manage.py migrate
   ```

7. Create a superuser
   ```bash
   python manage.py createsuperuser
   ```

8. Run the development server
   ```bash
   python manage.py runserver
   ```

## 📝 Usage Examples

### Register a User

```bash
curl -X POST http://localhost:8000/api/auth/register/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "email": "test@example.com", "password": "securepassword", "first_name": "John", "last_name": "Doe"}'
```

### Login

```bash
curl -X POST http://localhost:8000/api/auth/login/ \
  -H "Content-Type: application/json" \
  -d '{"username": "testuser", "password": "securepassword"}'
```

### Create a Patient

```bash
curl -X POST http://localhost:8000/api/patients/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_access_token>" \
  -d '{"first_name": "Jane", "last_name": "Smith", "date_of_birth": "1990-05-15", "gender": "Female", "phone": "123-456-7890", "address": "123 Main St"}'
```

### Create a Doctor

```bash
curl -X POST http://localhost:8000/api/doctors/ \
  -H "Content-Type: application/json" \
  -H "Authorization: Bearer <your_access_token>" \
  -d '{"first_name": "Dr", "last_name": "House", "specialization": "Cardiology", "license_number": "MED12345", "phone": "987-654-3210", "email": "dr.house@example.com"}'
```

## 📄 Project Structure

```
healthcare/
├── .env                  # Environment variables
├── .gitignore            # Git ignore file
├── manage.py             # Django management script
├── core/                 # Core application
│   ├── admin.py          # Admin panel configuration
│   ├── apps.py           # App configuration
│   ├── models.py         # Database models
│   ├── serializers.py    # API serializers
│   ├── urls.py           # API URL routing
│   ├── views.py          # API views
│   └── migrations/       # Database migrations
└── healthcare/           # Project settings
    ├── asgi.py           # ASGI configuration
    ├── settings.py       # Project settings
    ├── urls.py           # Main URL routing
    └── wsgi.py           # WSGI configuration
```

## 🔒 Security Features

- JWT token-based authentication
- Password hashing
- User-specific patient records
- Required authentication for sensitive endpoints
- Environment variables for sensitive configuration

## 👨‍💻 Author

[Your Name]

## 📝 License

This project is licensed under the MIT License.
