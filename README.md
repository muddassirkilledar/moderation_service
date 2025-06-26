# moderation_service

A Django-based microservice for detecting and flagging inappropriate user content (comments or reviews) using Hugging Face Moderation API. Designed for use in social platforms, forums, and UGC websites.

---

## 🚀 Features

- ✅ User Signup & Login (JWT-based authentication)
- 📝 Submit comments or reviews
- 🤖 Auto-detect inappropriate content using OpenAI's Moderation API
- ⚠️ Flag and store inappropriate content for moderation
- 🔐 JWT authentication (via `djangorestframework-simplejwt`)
- 🐘 PostgreSQL backend
- 🐳 Dockerized for easy setup
- 📦 API-ready for frontend or other services

---

## 🧱 Tech Stack

- Backend: **Django + Django REST Framework**
- Authentication: **JWT (SimpleJWT)**
- AI Moderation: **Hugging Face**
- Database: **PostgreSQL**
- Containerization: **Docker & Docker Compose**

---
## Run With Docker

docker-compose up --build
Then open: http://localhost:8000

## Run Migrations

docker-compose exec web python manage.py migrate

