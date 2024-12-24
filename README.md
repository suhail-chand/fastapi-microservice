# FastAPI Microservices

This project demonstrates how to build scalable and maintainable microservices using FastAPI. The service includes basic CRUD operations for managing user information, integrated with a SQLite database.

## Features

- **User Management:** Create, retrieve, update, and delete user records.
- **Interactive Documentation:** Automatically generated Swagger UI and ReDoc.
- **Database Integration:** SQLite database for persistent storage.
- **Docker Support:** Ready-to-deploy Docker configuration.
- **Kubernetes Deployment:** Scalable deployment using Kubernetes.

## Requirements

- Python 3.10+
- SQLite
- FastAPI
- SQLAlchemy
- Uvicorn
- Docker (optional for containerization)
- Kubernetes (optional for deployment)

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/suhail-chand/fastapi-microservice
   cd fastapi-microservices
   ```

2. Install dependencies:

   ```bash
   pip install -r requirements.txt
   ```

3. Run the application:

   ```bash
   uvicorn app.main:app --reload
   ```

   The API will be available at `http://127.0.0.1:8000`.

4. Access the interactive API documentation:

   - Swagger UI: `http://127.0.0.1:8000/docs`
   - ReDoc: `http://127.0.0.1:8000/redoc`

## Usage

### Endpoints

- `POST /users/` - Create a new user.
- `GET /users/` - Retrieve all users.
- `GET /users/{user_id}` - Retrieve a specific user by ID.
- `PUT /users/{user_id}` - Update user details.
- `DELETE /users/{user_id}` - Delete a user.

### Example Request

**Create a User:**

```bash
curl -X POST "http://127.0.0.1:8000/users/" \
-H "Content-Type: application/json" \
-d '{"name": "John Doe", "email": "john.doe@example.com"}'
```

## Docker Support

1. Build the Docker image:

   ```bash
   docker build -t fastapi-microservice .
   ```

2. Run the container:

   ```bash
   docker run -d -p 8000:80 fastapi-microservice
   ```

## Kubernetes Deployment

1. Apply the Kubernetes manifest:

   ```bash
   kubectl apply -f deployment.yaml
   ```

2. Access the service using the LoadBalancer IP.
