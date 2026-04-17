from src.application.exceptions import UserNotFoundError
from src.application.ports.uow import UnitOfWork
from src.application.ports.usecases import GetUserPort
from src.domain.entities import User


class GetUser(GetUserPort):
    def __init__(self, uow: UnitOfWork) -> None:
        self._uow = uow

    async def execute(self, user_id: int) -> User:
        async with self._uow:
            existing = await self._uow.users.get_by_id(user_id)
            if not existing:
                raise UserNotFoundError
            return existing
