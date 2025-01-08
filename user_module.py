import hashlib
class User:



    def __init__(self,first_name,last_name,password):
        self.first_name = first_name
        self.last_name = last_name
        self.password = password

    
    def hash_password(self,password):
        return hashlib.sha256(password.encode()).hexdigest()



    def verify_password(self,password):
        return self.hash_password(password) == self.password



