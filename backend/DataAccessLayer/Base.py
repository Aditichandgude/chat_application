from backend.database import async_session
from sqlalchemy import select
from contextlib import asynccontextmanager
class BaseDAL():
    _session_factory=async_session

    def __init__(self, model):
        self.model=model


    @asynccontextmanager
    async def session_scope(self):
        async with self._session_factory() as session:
            try:
                yield session
                await session.commit()
            except:
                await session.rollback()
                raise
    
    async def get_by_id(self, id_):
        async with self.session_scope() as session:
            return await session.get(self.model, id_)

    async def get_all(self, filters=None):
        async with self.session_scope() as session:
            statement=select(self.model)

            if filters:
                for k, v in filters.items():
                    statement=statement.where(getattr(self.model, k)== v)
    
            result=await session.execute(statement)
            return result.scalars().all()
        

    async def add(self, obj):
        async with self.session_scope() as session:
            session.add(obj)
            await session.flush()
            await session.refresh(obj)
            return obj
        
    async def update(self, obj):
        async with self.session_scope() as session:
            obj=await session.merge(obj)
            await session.flush()
            await session.refresh(obj)
            return obj
        
    async def delete(self, obj):
        async with self.session_scope() as session:
            obj=await session.merge(obj)
            await session.delete(obj)
        