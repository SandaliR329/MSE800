class User:
    def __init__(self, full_name, date_of_birth, email, password_hash):
        self.full_name = full_name
        self.date_of_birth = date_of_birth
        self.email = email
        self.password_hash = password_hash