import bcrypt


class AuthService:
    @staticmethod
    def hash_password(password):
        password_bytes = password.encode("utf-8")
        salt = bcrypt.gensalt()
        hashed_password = bcrypt.hashpw(password_bytes, salt)
        return hashed_password.decode("utf-8")

    @staticmethod
    def verify_password(password, stored_hash):
        password_bytes = password.encode("utf-8")
        stored_hash_bytes = stored_hash.encode("utf-8")
        return bcrypt.checkpw(password_bytes, stored_hash_bytes)