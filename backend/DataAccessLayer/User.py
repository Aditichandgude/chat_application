from backend.DataAccessLayer.Base import BaseDAL
from backend.Entities.User import User
import datetime

class UserDAL(BaseDAL):

    def __init__(self):
        super().__init__(User)


    async def get_by_property(self, property: str, value):
        users = await self.get_all({property: value})
        return users if users else None
        
    async def create_user(self, username: str, name: str, email: str, password: str, date_of_birth: datetime.date, gender: str):
        existing_user_by_email=await self.get_by_property("email", email)
        existing_user_by_username=await self.get_by_property("username", username)

        if existing_user_by_email:
            raise ValueError(f"user with email '{email}' already exists")
        
        if existing_user_by_username:
            raise ValueError(f"user with username '{username}' already exists")
        
        user=User(
            username=username,
            email=email,
            name=name,
            password=password,
            date_of_birth=date_of_birth,
            gender=gender,
            updated_at=datetime.datetime.utcnow()
        )

        return await self.add(user)

    async def get_by_email(self, email: str):
        users=await self.get_by_property("email", email)

        return users[0] if users else None



    