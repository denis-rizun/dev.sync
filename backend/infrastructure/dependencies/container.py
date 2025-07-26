from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Resource, Factory

from backend.application.auth import AuthService
from backend.application.history import HistoryService
from backend.application.server import ServerService
from backend.application.session import SessionService
from backend.application.user import UserService
from backend.application.webhook import WebhookService
from backend.infrastructure.database.initialisation import DatabaseInitializer
from backend.infrastructure.database.repositories.history import HistoryRepository
from backend.infrastructure.database.repositories.server import ServerRepository
from backend.infrastructure.database.repositories.session import SessionRepository
from backend.infrastructure.database.repositories.user import UserRepository
from backend.infrastructure.database.repositories.webhook import WebhookRepository
from backend.infrastructure.tasks.initialisation import CeleryInitializer


class Container(DeclarativeContainer):
    session_factory = Resource(DatabaseInitializer.initialize, echo=True, expire=False)
    session = Resource(lambda session_factory: session_factory(), session_factory=session_factory)
    celery = Resource(CeleryInitializer.initialize)

    user_repository = Factory(UserRepository, session=session)
    session_repository = Factory(SessionRepository, session=session)
    server_repository = Factory(ServerRepository, session=session)
    webhook_repository = Factory(WebhookRepository, session=session)
    history_repository = Factory(HistoryRepository, session=session)

    user_service = Factory(UserService, user_repo=user_repository)
    auth_service = Factory(AuthService, user_repo=user_repository, session_repo=session_repository)
    server_service = Factory(ServerService, server_repo=server_repository)
    webhook_service = Factory(
        WebhookService,
        webhook_repo=webhook_repository,
        server_repo=server_repository,
    )
    history_service = Factory(HistoryService, history_repo=history_repository)
    session_service = Factory(SessionService, session_repo=session_repository)

container = Container()
