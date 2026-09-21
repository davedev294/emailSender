class Mailer:

    def load_newsletter(self, file):

        with open (file, "r", encoding="utf-8") as file:
            return file.read()

    def send_test(self, email):

        print(f"Enviando correo de prueba a {email}...")
        print("Correo de prueba enviado correctamente.")

        if email == "pedro@ejemplo.com":
            raise Exception("Simulación de error al enviar correo.")

    
        return True