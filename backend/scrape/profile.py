class Profile:
    def __init__(self,
        name: str = "", phone_number: str = "", email: str = ""
    ):
        self.name = name
        self.phone_number = phone_number
        self.email = email
    
    def __str__(self) -> str:
        return f"{self.name} - phone num: {self.phone_number} | email: {self.email}"
