from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Resource, Factory

from backend.application.auth import AuthService
from backend.infrastructure.database.initialisation import DatabaseInitializer
from backend.infrastructure.database.repositories.session import SessionRepository
from backend.infrastructure.database.repositories.user import UserRepository
from backend.application.user import UserService


class Container(DeclarativeContainer):
    session_factory = Resource(DatabaseInitializer.initialize, echo=True, expire=False)
    session = Resource(lambda session_factory: session_factory(), session_factory=session_factory)

    user_repository = Factory(UserRepository, session=session)
    session_repository = Factory(SessionRepository, session=session)

    user_service = Factory(UserService, user_repo=user_repository)
    auth_service = Factory(AuthService, user_repo=user_repository, session_repo=session_repository)

container = Container()
