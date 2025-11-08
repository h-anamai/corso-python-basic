class User:
    def __init__(self, name, email):
        if not name or not email:
            raise ValueError("Name and email must be not empty.")
        self.name = name
        self.email = email
        self.logged = False
        
    def login(self):
        self.logged = True
        
    def logout(self):
        self.logged = False