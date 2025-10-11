from backend.DataAccessLayer.Base import BaseDAL
from backend.Entities.Otp import Otp
import random
import string
from uuid import UUID
import datetime

class OtpDAL(BaseDAL):

    def __init__(self):
        super().__init__(Otp)

    async def create_otp(self, length: int, expires_in_minutes: int, user_id: UUID):
        characters='0123456789'
        otp = ''.join(random.choice(characters) for _ in range(length))
        curr_date_time=datetime.datetime.now(datetime.timezone.utc)
        otpObj=Otp(
            user_id=user_id,
            code=otp,
            expires_at=curr_date_time + datetime.timedelta(minutes=expires_in_minutes)
        )

        return await self.add(otpObj)

    async def get_otp_by_id(self, id: UUID):
        try:
            otp = await self.get_by_id(id)
            return otp
        except Exception as e:
            print(f"Error verifying OTP: {e}")
            return False
        
    async def verify_otp(self, user_id: UUID, otp: str):
        try:
            matching_otps = await self.get_all({"user_id": user_id, "code": otp, "is_used": False})

            if not matching_otps:
                return False 

            now_utc = datetime.datetime.now(datetime.timezone.utc)

            valid_otps = []
            for otp_entry in matching_otps:
                expires_at = otp_entry.expires_at

                if expires_at.tzinfo is None:
                    expires_at = expires_at.replace(tzinfo=datetime.timezone.utc)

                if expires_at >= now_utc:
                    valid_otps.append((expires_at, otp_entry))

            if not valid_otps:
                return False

            _, latest_valid_otp = max(valid_otps, key=lambda x: x[0])

            return latest_valid_otp

        except Exception as e:
            print(f"Error verifying OTP: {e}")
            return False
        
    async def use_otp(self, otp_id: UUID):
        otp = await self.get_otp_by_id(otp_id)
        if not otp:
            print(f"OTP with ID {otp_id} not found.")
            return False

        otp.is_used = True
        return await self.update(otp)