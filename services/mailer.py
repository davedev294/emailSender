import smtplib
from email.mime.text import MIMEText

class Mailer:

    def load_newsletter(self, file):

        with open (file, "r", encoding="utf-8") as file:
            return file.read()

    def send_email(self, subject, newsletter, sender, recipient, password):
        msg = MIMEText(newsletter, "html", "utf-8")
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = recipient

        with smtplib.SMTP('smtp.gmail.com', 587) as smpt_server:
            smpt_server.ehlo()
            smpt_server.starttls()
            smpt_server.ehlo()
            smpt_server.login(sender, password)
            smpt_server.sendmail(sender, recipient, msg.as_string())

        return True
        
