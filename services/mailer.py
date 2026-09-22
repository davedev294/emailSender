import smtplib
from email.mime.text import MIMEText

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

    def send_email(self, subject, newsletter, sender, recipient, password):
        msg = MIMEText(newsletter, "html", "utf-8")
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smpt_server:
            smpt_server.login(sender, password)
            smpt_server.sendmail(sender, recipient, msg.as_string())

        return True
        
