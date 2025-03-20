import smtplib
import sys
import os
import logging

# Configure logging
LOG_FILE = "/var/log/email_alert.log"
logging.basicConfig(filename=LOG_FILE, level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s")

# Load email credentials from environment variables
EMAIL_SENDER = os.getenv("EMAIL_SENDER")
EMAIL_RECEIVER = os.getenv("EMAIL_RECEIVER", "admin@example.com")
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")
SMTP_SERVER = os.getenv("SMTP_SERVER", "smtp.example.com")
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))

# Validate email settings
if not EMAIL_SENDER or not EMAIL_PASSWORD:
    logging.error("❌ Email credentials are missing. Set EMAIL_SENDER and EMAIL_PASSWORD.")
    print("❌ Email credentials are missing. Check your environment variables.")
    sys.exit(1)

# Ensure an alert message is provided
if len(sys.argv) < 2:
    logging.error("❌ No alert message provided.")
    print("❌ No alert message provided.")
    sys.exit(1)

alert_message = sys.argv[1]

def send_email(subject, message):
    try:
        server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT, timeout=10)
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)

        # Proper email formatting
        email_message = f"From: {EMAIL_SENDER}\nTo: {EMAIL_RECEIVER}\nSubject: {subject}\n\n{message}"

        server.sendmail(EMAIL_SENDER, EMAIL_RECEIVER, email_message)
        server.quit()

        logging.info("✅ Email sent successfully to %s", EMAIL_RECEIVER)
        print("✅ Email sent successfully!")
    
    except smtplib.SMTPAuthenticationError:
        logging.error("❌ Authentication failed. Check EMAIL_SENDER and EMAIL_PASSWORD.")
        print("❌ Authentication failed. Check EMAIL_SENDER and EMAIL_PASSWORD.")
    
    except smtplib.SMTPConnectError:
        logging.error("❌ Unable to connect to the SMTP server.")
        print("❌ Unable to connect to the SMTP server.")
    
    except Exception as e:
        logging.error("❌ Error sending email: %s", str(e))
        print(f"❌ Error sending email: {e}")

# Send alert
send_email("🚨 Server Alert 🚨", alert_message)

