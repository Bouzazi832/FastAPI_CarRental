# 🚗 FastAPI Car Rental System - Backend

A modern REST API for a car rental management system built with FastAPI, PostgreSQL, and SQLModel. Manage vehicles, renters, and rental transactions efficiently.

## 📋 Project Overview

This is the backend service for a comprehensive car rental platform. It provides APIs for:
- **Vehicle Management** - Add, update, delete, and track vehicles
- **Renter Management** - Manage customer information and rental history
- **Rental Operations** - Create, track, and complete vehicle rentals
- **Analytics** - Get statistics on vehicles, rental status, and mileage

## 🛠️ Tech Stack

| Technology | Version |
|-----------|---------|
| **FastAPI** | 0.110.0+ |
| **Python** | 3.9+ |
| **SQLModel** | 0.0.16 |
| **PostgreSQL** | 15 |
| **Uvicorn** | 0.29.0+ |
| **Faker** | 24.0.0 |

## 📦 Requirements

- Docker & Docker Compose
- Python 3.9+
- PostgreSQL 15

## 🚀 Quick Start

### 1. Clone the Repository
```bash
git clone https://github.com/Bouzazi832/FastAPI_CarRental.git
cd FastAPI_CarRental
```

### 2. Environment Setup
Create a `.env` file in the project root:
```env
POSTGRES_USER=postgres
POSTGRES_PASSWORD=your_password
POSTGRES_DB=car_rental
DATABASE_URL=postgresql://postgres:your_password@db:5432/car_rental
```

### 3. Build and Start Docker Services
```bash
docker-compose up --build
```

The backend will be available at: **http://localhost:8000**


## 📚 API Documentation

Once the server is running, visit:
- **Swagger UI**: http://localhost:8000/docs
- **ReDoc**: http://localhost:8000/redoc

### Core Endpoints

#### Vehicles (`/voitures/`)
- `GET /voitures` - List all vehicles
- `GET /voitures/nombre` - Get total number of vehicles
- `GET /voitures/nombreLoue` - Get number of rented vehicles
- `GET /voitures/kilometrage%20moyenne` - Get average mileage
- `GET /voitures/{num_imma}` - Get vehicle by registration number
- `POST /voitures` - Add new vehicle
- `PUT /voitures/{num_imma}` - Update vehicle
- `DELETE /voitures/{num_imma}` - Delete vehicle

#### Renters (`/locataires/`)
- `GET /locataires` - List all renters
- `GET /locataires/{id}` - Get renter by ID
- `POST /locataires` - Add new renter
- `PUT /locataires/{id}` - Update renter
- `DELETE /locataires/{id}` - Delete renter

#### Rentals (`/locations/`)
- `POST /locations/louer` - Create new rental
- `POST /locations/rendre` - Return rented vehicle
- `GET /locations/{id}` - Get renter's vehicles

## 🔧 Project Structure

```
FastAPI_CarRental/
├── app/
│   ├── main.py                 # FastAPI app & CORS configuration
│   ├── database.py             # SQLModel & database setup
│   ├── seed.py                 # Database seeding script
│   ├── requirements.txt         # Python dependencies
│   ├── Dockerfile              # Docker configuration
│   ├── routers/
│   │   ├── voiture.py          # Vehicle endpoints
│   │   ├── locataire.py        # Renter endpoints
│   │   └── location.py         # Rental endpoints
│   └── services/
│       ├── crud_voiture.py     # Vehicle database operations
│       ├── crud_locataire.py   # Renter database operations
│       └── location.py         # Rental business logic
├── docker-compose.yml          # Docker Compose configuration
└── README.md                   # This file
```
## 👤 Author

**Ahmed Bouzazi**

- Backend: [FastAPI_CarRental](https://github.com/Bouzazi832/FastAPI_CarRental)
- Frontend: [CarRental-Front](https://github.com/Bouzazi832/CarRental-Front)
