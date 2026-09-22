import json
import os

from dotenv import load_dotenv
from services.csv_manager import CSVManager
from services.mailer import Mailer

#Config
with open("config/config.json", "r", encoding="utf-8") as f:
    config = json.load(f)

load_dotenv("config/.env")

SENDER = config["sender"]
PASSWORD = os.getenv("MAIL_PASSWORD")
SUBJECT = config["subject"]

NEWSLETTER_FILE = "newsletter/newsletter.html"
CSV_FILE = "destinatarios/destinatarios.csv"

BATCH_SIZE = config["batch_size"]

print("SENDER:", SENDER)
print("PASSWORD existe:", PASSWORD is not None)
print("LONGITUD PASSWORD:", len(PASSWORD) if PASSWORD else 0)

#Objects
csv_manager = CSVManager(CSV_FILE)
mailer = Mailer()

#Data
csv_manager.load()

pendientes = csv_manager.pending()

newsletter = mailer.load_newsletter(NEWSLETTER_FILE)

print("Newsletter cargado correctamente.")

# PREPARAR LOTE

while pendientes:

    lote = pendientes[:BATCH_SIZE]

    print(f"Pendientes: {len(pendientes)}")
    print(f"Lote de pendientes: {len(lote)}")

    for pendiente in lote:

        email = pendiente["email"]

        try:
            resultado = mailer.send_email(SUBJECT, newsletter, SENDER, email, PASSWORD)

            if resultado:
                csv_manager.set_as_sent(email)
                sendMessage = f"Correo enviado correctamente a {email}."
                print(sendMessage)

                with open ("logs/envio.log", "a", encoding="utf-8") as log_file:
                    log_file.write(sendMessage + "\n")

        except Exception as error:
            csv_manager.error(email, error)
            errorMessage =f"Error al enviar correo a {email}: {error}"
            print(errorMessage)

            with open ("logs/envio.log", "a", encoding="utf-8") as log_file:
                log_file.write(errorMessage + "\n")

    print("Lote procesado. Guardando cambios en el CSV...")
    csv_manager.save()

    pendientes = csv_manager.pending()