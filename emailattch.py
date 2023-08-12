import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# Email details
sender_email = 'janaranjani.venkatesan@isteer.com'
receiver_email = 'dhaya1245@gmail.com'
subject = 'test email'
message = 'Please find the attached file.'

# File details
attachment_path = '/path/to/attachment/file.txt'

# Create a multipart message
msg = MIMEMultipart()
msg['From'] = sender_email
msg['To'] = receiver_email
msg['Subject'] = subject

# Add the message body
msg.attach(MIMEText(message, 'plain'))

# Open the file in bynary
with open(attachment_path, 'rb') as attachment:
    # Add file as application/octet-stream
    # Email clients can usually download this automatically as an attachment
    part = MIMEBase('application', 'octet-stream')
    part.set_payload(attachment.read())

# Encode file in ASCII characters to send by email
encoders.encode_base64(part)
# Add header as key/value pair to attachment part
part.add_header(
    'Content-Disposition',
    f'attachment; filename= {attachment_path.split("/")[-1]}',
)

# Add attachment to message and convert message to string
msg.attach(part)
text = msg.as_string()

# Sending the email
try:
    with smtplib.SMTP('smtp.example.com', 587) as server:
        server.ehlo()
        server.starttls()
        server.login('your_username', 'your_password')
        server.sendmail(sender_email, receiver_email, text)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error: {str(e)}")
