class cliente:
    def __init__(self, name, email, tel):
        self.name = name
        self.email = email
        self.tel = tel

    def message(self):
        print(f"Mensaje para el cliente: {self.name}.")
        print(f"Con el email: {self.email} y el telefono: {self.tel}")