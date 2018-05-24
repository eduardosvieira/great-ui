
class User():
    def __init__(self, id=0, name="", email="", password=""):
        self.id = id
        self.name = name
        self.email = email
        self.password = password


    def signUpUser(self, user=None):
        try:
            db.users.insert({
                "name": user.name,
                "email": user.email,
                "password": user.password
            })

            return True;

        except:
            return False;


    def loginUser(self, email="", password=""):
        try:
            user = db.users.find_one({
                "email": email,
                "password": password
            })

            if user:
                return True
            else:
                return False
        except:
            return False
