import csv

class CSVManager:

    def __init__(self, file):
        self.file = file
        self.destinatarios = []

    # Lo que hace es que abres el archivo CSV y lo lee, luego lo guarda en filas
    # pasa de correo, true, error
    # A: Correo - tal \n enviado - true \n error - error
    # Y luego lo guarda en la lista de destinatarios
    def load(self):
        with open(self.file, "r", newline="", encoding="utf-8") as files:
            reader = csv.DictReader(files)
            self.destinatarios = list(reader)

    # mira a ver el campo del csv que tiene "enviado" y si es false lo guarda en resultado
    def pending(self):

        resultado = []

        for destinatario in self.destinatarios:
            if destinatario["enviado"].lower() == "false":
                resultado.append(destinatario)

        return resultado

    # Mira a ver si el correo se ha enviado
    def set_as_sent(self, email):

        for destinatario in self.destinatarios:
            if destinatario["email"] == email:
                destinatario["enviado"] = "true"

                return True

        return False

    def error(self, email, error):

        for destinatario in self.destinatarios:
            if destinatario["email"] == email:
                destinatario["error"] = str(error)

                return True

        return False

    # Guarda los cambios en el csv
    def save(self):

        with open(self.file, "w", newline="", encoding="utf-8") as files:

            campos = ["email", "enviado", "error"]

            writer = csv.DictWriter(
                files,
                fieldnames=campos
            )

            writer.writeheader()
            writer.writerows(self.destinatarios)