from backend.DataAccessLayer.User import UserDAL
import asyncio

user=UserDAL()


asyncio.run(user.create_user("aditi", "aditi","aditi@gmail.com", "asdfasdf", "2004-10-24", "female"))

