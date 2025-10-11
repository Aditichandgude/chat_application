from backend.DataAccessLayer.User import UserDAL
from backend.DataAccessLayer.Otp import OtpDAL
import asyncio

user=UserDAL()
otp=OtpDAL()

# asyncio.run(otp.create_otp(5, 10, 'f4dc5d1e-60d9-47cb-b681-c2cb70feff86'))

o=asyncio.run(otp.verify_otp('f4dc5d1e-60d9-47cb-b681-c2cb70feff86','79320'))
asyncio.run(otp.use_otp(o.id))
# if o:
#     print("check code: ", o.code)