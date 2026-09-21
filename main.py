from services.csv_manager import CSVManager
from services.mailer import Mailer

csv_manager = CSVManager("destinatarios/destinatarios.csv")
mailer = Mailer()

csv_manager.load()
pendientes = csv_manager.pending()

message = mailer.load_newsletter("newsletter/newsletter.html")
print("Newsletter cargado correctamente.")

BATCH_SIZE = 50

lote = pendientes[:BATCH_SIZE]

print(f"Pendientes: {len(pendientes)}")
print(f"Lote de pendientes: {len(lote)}")

#Esta sería la parte de envio de correos, pero por ahora solo es una simulación.
for pendiente in lote:

    email = pendiente["email"]

    try:
        resultado = mailer.send_test(email, message)

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


#csv_manager.save()