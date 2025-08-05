# Taskify API

Taskify is a simple RESTful API built with FastAPI to manage tasks with prioritization. It demonstrates basic backend principles like CRUD operations, request validation, error handling, and clean architecture using Pydantic models.

## Features

- Built with FastAPI (Python 3.10+)
- Full CRUD support for task management
- Task prioritization using Enums
- Data validation using Pydantic
- In-memory data store (no database)
- Automatic interactive API docs (Swagger UI)

## Requirements

- Python 3.10+
- FastAPI
- Uvicorn

## Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/mamoonzaheer/taskify-api.git
   cd taskify-api
   ```

2. **Create a virtual environment (optional but recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run the server:**
   ```bash
   uvicorn main:api --reload
   ```

## API Endpoints

| Method | Endpoint       | Description               |
|--------|----------------|---------------------------|
| GET    | `/todos`       | Get all tasks             |
| GET    | `/todos/{id}`  | Get a task by ID          |
| POST   | `/todos`       | Create a new task         |
| PUT    | `/todos/{id}`  | Update an existing task   |
| DELETE | `/todos/{id}`  | Delete a task             |

## Folder Structure

- `main.py` - Main FastAPI application file with route definitions and logic
- `models.py` *(optional refactor)* - For Pydantic models and Enums

## License

MIT
