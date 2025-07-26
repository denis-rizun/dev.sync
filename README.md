# DevSync

## 📄 Reason for Missing Final Documentation

At this stage, the project is still under active development. While the backend part is already complete, the frontend has not yet been implemented. Since the addition of the client-side will likely lead to changes in the API, user flows, and overall architecture, it was decided to **postpone writing the final documentation** until all core components of the system are finished.

This approach ensures that the final documentation will be accurate, up-to-date, and fully aligned with the finalized structure of the project.

---

## 🛠️ About the Project

This project is designed to **automate continuous delivery (CD) to a remote server**. Its main goal is to streamline and speed up the deployment of applications by providing a stable and secure way to deliver changes to production or test environments.

**Key features:**
- Authorization using JWT and dev tokens.
- Fully asynchronous stack: FastAPI + SQLAlchemy (async).
- Extensible architecture based on **Domain-Driven Design (DDD)** principles.
- Ready for integration with Celery for background task processing.