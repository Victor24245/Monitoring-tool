import smtplib
import sys

# Email Configuration
EMAIL_SENDER = "your-email@example.com"
EMAIL_RECEIVER = "admin@example.com"
EMAIL_PASSWORD = "your-email-password"
SMTP_SERVER = "smtp.example.com"
SMTP_PORT = 587

# Get alert message from Bash script
alert_message = sys.argv[1]

def send_email(subject, message):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        email_message = f"Subject: {subject}\n\n{message}"
        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message)
        server.quit()
        print("Email sent successfully")
    except Exception as e:
        print(f"Error sending email: {e}")

# Send the alert
send_email("Server Alert", alert_message)

