import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def send_error_email(subject, message, recipient_emails):
    # Email configuration
    sender_email = "<sender_email_id>"  # Replace with your sender email
    sender_password = "<sender_email_password>"      # Replace with your sender password
    smtp_server = "smtp.gmail.com"  # Use the SMTP server for your email provider
    smtp_port = 587  # Port for SMTP

    for recipient_email in recipient_emails:
        # Create the email message
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
        msg.attach(MIMEText(message, 'plain'))

        try:
            # Connect to the SMTP server
            server = smtplib.SMTP(smtp_server, smtp_port)
            server.starttls()
            server.login(sender_email, sender_password)

            # Send the email
            server.sendmail(sender_email, recipient_email, msg.as_string())
            server.quit()

            print(f"Error email notification sent to {recipient_email} successfully.")
        except Exception as e:
            print(f"Error sending email notification to {recipient_email}: {str(e)}")

# List of recipient email addresses
recipient_emails = ["<recipient_emails>"]

# Example usage
try:
    # Your Ray Serve code here
    # ...
    # If an error occurs, raise an exception
    raise Exception("An error occurred in the Ray Serve application.")

except Exception as e:
    error_subject = "Ray Serve Error Notification"
    error_message = f"An error occurred in the Ray Serve application:\n{str(e)}"
    send_error_email(error_subject, error_message, recipient_emails)
