from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from api.config import settings

engine = create_async_engine(settings.async_database_url, echo=False)
AsyncSessionLocal = async_sessionmaker(
    engine, class_=AsyncSession, expire_on_commit=False
)


async def get_session() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        yield session


# Define models by extending SQLModel with table=True — no separate Base needed.
# The same class works as both a Pydantic schema and a DB table.
#
# Example:
#   class Loan(SQLModel, table=True):
#       id: int | None = Field(default=None, primary_key=True)
#       amount: float
#       status: str = "pending"
#
# Pessimistic locking pattern — use for financial mutations to prevent race conditions.
#   result = await session.execute(select(Loan).where(Loan.id == id).with_for_update())
#   loan = result.scalar_one()
#   loan.status = "disbursed"
#   await session.commit()
