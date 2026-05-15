from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

from api.config import settings

engine = create_async_engine(settings.database_url, echo=False)
AsyncSessionLocal = async_sessionmaker(engine, expire_on_commit=False)


class Base(DeclarativeBase):
    pass


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


# Pessimistic locking pattern — use for any financial mutation to prevent race conditions.
# Locks the row for the duration of the transaction; no concurrent update can proceed until commit.
#
# Example:
#   result = await session.execute(select(Model).where(Model.id == id).with_for_update())
#   record = result.scalar_one()
#   record.status = "processed"
#   await session.commit()
