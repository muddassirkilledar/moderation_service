# 🛡️ AI-Powered Moderation Microservice

This microservice scans user-generated content (comments) for inappropriate or toxic content using AI-based moderation. It is designed for integration into websites or social media platforms to automatically flag toxic comments and alert moderators.

---

## 🚀 Features

- 🔐 User Registration & JWT Authentication
- 💬 Post and Store Comments
- 🤖 AI-Based Content Moderation (Hugging Face `unitary/toxic-bert`)
- 🚩 Flagging Inappropriate Comments (confidence > 0.5)
- 📬 Email Notification for Flagged Comments
- 🪄 Asynchronous Task Handling (Celery + Redis)
- 🐳 Dockerized for Easy Deployment
- 🧑‍💼 Django Admin Interface for Moderators

---

## 📦 Tech Stack

- Python, Django REST Framework
- Celery + Redis (for async task queue)
- Hugging Face Inference API
- Docker & Docker Compose
- PostgreSQL (via Docker)
- AWS EC2 (for deployment)

---

## 🧪 API Endpoints

| Endpoint | Method | Description |
|---------|--------|-------------|
| `/api/signup/` | `POST` | User Registration |
| `/api/login/` | `POST` | User Login (JWT) |
| `/api/comments/` | `POST` | Post a Comment (Moderation Applied) |

### 🔗 Postman Collection

[Click here to access the API collection](https://interstellar-firefly-414100.postman.co/workspace/My-Workspace~e0df8bc6-21ef-42f0-8185-34cdb4082ace/collection/37449109-074ecca6-a0e8-4507-a5d0-1bc10f3a79c0?action=share&creator=37449109)

---
## 🧰 Running Locally (Docker)

```bash
# Clone repo
git clone https://github.com/muddassirkilledar/moderation_service.git
cd moderation_service

# Build and run containers
docker-compose up --build

# Run DB migrations
docker-compose exec web python manage.py migrate

# Create superuser
docker-compose exec web python manage.py createsuperuser
