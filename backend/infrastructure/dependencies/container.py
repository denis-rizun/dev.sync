from dependency_injector.containers import DeclarativeContainer
from dependency_injector.providers import Resource, Factory

from backend.infrastructure.database.initialisation import DatabaseInitializer
from backend.infrastructure.database.repositories.user import UserRepository
from backend.application.user import UserService


class Container(DeclarativeContainer):
    session_factory = Resource(DatabaseInitializer.initialize, echo=True, expire=False)
    session = Resource(lambda session_factory: session_factory(), session_factory=session_factory)

    user_repository = Factory(UserRepository, session=session)
    user_service = Factory(UserService, user_repo=user_repository)


container = Container()
