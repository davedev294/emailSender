Newsletter Mailer

Aplicación en Python para enviar newsletters por correo electrónico a una lista de destinatarios.

La aplicación permite cargar los destinatarios desde un archivo CSV, cargar una newsletter escrita en HTML y enviar los correos automáticamente mediante SMTP de Gmail.




Configuración

Antes de ejecutar el programa, hay que configurar los archivos de la carpeta config.

1. config.json

Este archivo contiene la configuración general del envío:

{
    "sender": "correo@gmail.com",
    "subject": "Asunto de la newsletter",
    "batch_size": 50
}

2. .env

Este archivo contiene la contraseña de aplicación de la cuenta de Gmail utilizada para enviar los correos.

MAIL_PASSWORD=contraseña_de_aplicacion

La contraseña debe ser una contraseña de aplicación de Google, no la contraseña normal de la cuenta.

Importante

No compartir este archivo ni subirlo a GitHub.

El archivo .env está incluido en .gitignore para evitar publicar accidentalmente las credenciales.



3. Destinatarios

Los destinatarios se encuentran en:

destinatarios/destinatarios.csv

El archivo utiliza las siguientes columnas:

nombre,email,enviado
Juan,juan@gmail.com,false
Ana,ana@gmail.com,false

4. Newsletter

La newsletter que se enviará se encuentra en:

newsletter/newsletter.html

El contenido de este archivo es HTML.



5. Funcionamiento

Al ejecutar:

python main.py

el programa realiza los siguientes pasos:

Carga la configuración.
Carga las credenciales desde .env.
Carga los destinatarios del CSV.
Busca los destinatarios pendientes.
Carga la newsletter HTML.
Crea un lote de destinatarios según batch_size.
Se conecta al servidor SMTP de Gmail.
Envía los correos.
Marca como enviados los correos enviados correctamente.
Registra los errores en logs/envio.log.