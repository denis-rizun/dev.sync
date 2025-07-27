<h1 style="text-align: center; font-size: 3em; font-weight: bold; margin-bottom: 0.2em;">
  DevSync
</h1>

<p style="text-align: center; font-style: italic; font-size: 1.2em;">
  Streamlining Deployment, Empowering Innovation Seamlessly
</p>

<p style="text-align: center;">
  <img src="https://img.shields.io/github/last-commit/denis-rizun/dev.sync?color=blue&style=flat-square" alt="Last Commit" height="20" />
  <img src="https://img.shields.io/github/languages/top/denis-rizun/dev.sync?style=flat-square" alt="Top Language" height="20" />
  <img src="https://img.shields.io/github/languages/count/denis-rizun/dev.sync?style=flat-square" alt="Languages Count" height="20" />
</p>

<p style="text-align: center; font-style: italic; font-size: 1.2em;">
  Built with the tools and technologies:
</p>
<p style="text-align: center;">
    <img
        src="https://img.shields.io/badge/Python-3776AB?style=flat-square&logo=python&logoColor=white"
        alt="Python"
        height="20"
        style="margin: 0 3px;"
    />
    <img
        src="https://img.shields.io/badge/FastAPI-009688?style=flat-square&logo=fastapi&logoColor=white"
        alt="FastAPI"
        height="20"
        style="margin: 0 3px;"
    />
    <img
        src="https://img.shields.io/badge/SQLAlchemy-1766A5?style=flat-square&logo=postgresql&logoColor=white"
        alt="SQLAlchemy"
        height="20"
        style="margin: 0 3px;"
    />
    <img
        src="https://img.shields.io/badge/Celery-3A4E55?style=flat-square&logo=celery&logoColor=white"
        alt="Celery"
        height="20"
        style="margin: 0 3px;"
    />
    <img
        src="https://img.shields.io/badge/Docker-2496ED?style=flat-square&logo=docker&logoColor=white"
        alt="Docker"
        height="20"
        style="margin: 0 3px;"
    />
</p>

---

## Contents

- [1. Overview](#overview)
- [2. Installation](#installation)
- [3. Testing](#testing)
- [4. Architecture](#architecture)
- [5. Stack](#stack)

---

## <a id="overview"></a>1. Overview

DevSync is a developer tool designed to automate and optimize continuous delivery workflows, providing secure and asynchronous deployment processes. Built on FastAPI and SQLAlchemy foundations, it ensures scalable and reproducible environments — essential for modern backend development.

### Why DevSync?

- **Automated Deployment:** Simplifies and accelerates secure asynchronous application deployments.  
- **Background Task Orchestration:** Uses Celery for reliable scheduled and asynchronous task execution.  
- **Extensible Architecture:** Implements Domain-Driven Design (DDD) for flexible and maintainable codebases.  
- **Robust Security:** JWT-based authentication and password hashing for secure access.  
- **Comprehensive Data Management:** Detailed mappers, schemas, and repositories ensure smooth data flow.  
- **Scalable Environments:** Manages interconnected services with Docker Compose for consistent development and deployment.

---

## <a id="installation"></a>2. Installation

### Setup

```bash
git clone https://github.com/denis-rizun/dev.sync.git
```
- Then navigate to the repository and fill the .env file based on .env.example
```bash
cd dev.sync
```
- Don't forget to generate RSA .pem keys required for JWT authorization:
```bash
# Generate a 4096-bit private key
openssl genrsa -out private.pem 4096

# Extract the public key from the private key
openssl rsa -in private.pem -pubout -out public.pem
```
Place these .pem files in the appropriate config folder (check your .env or config settings).
- Start the project:
```bash
docker-compose up --build
```

---

## <a id="testing"></a>3. Testing
Unfortunately, there are no tests available currently, but they will be added in the future.

---

## <a id="architecture"></a>4. Architecture

DevSync is built with a focus on clean and extensible architecture:

**Domain-Driven Design (DDD):** \
Business logic is divided into domains with clear boundaries, making the project easier to maintain and scale.

---

## <a id="stack"></a>5. Stack

- **FastAPI**: \
A high-performance web framework for building REST APIs with automatic documentation generation.

- **SQLAlchemy**: \
ORM for database management using the Repository pattern to isolate data access layers.

- **Celery**: \
Background task queue for asynchronous and scheduled task execution.

- **JWT Authentication**: \
Provides secure API access via token-based authentication.
