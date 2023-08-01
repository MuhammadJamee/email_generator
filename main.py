import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

# Get the environment variables for email content
from_email = os.environ.get('FROM_EMAIL')
to_email = os.environ.get('TO_EMAIL')
subject = os.environ.get('SUBJECT')
body = os.environ.get('BODY')

# Check if any of the environment variables are not set
if not from_email or not to_email or not subject or not body:
    raise ValueError("One or more required environment variables are not set.")

# Get the SendGrid API key from the environment variable
sendgrid_api_key = os.environ.get('SENDGRID_API_KEY')

# Check if the API key is available
if not sendgrid_api_key:
    raise ValueError("SendGrid API key is not set. Please set the environment variable SENDGRID_API_KEY.")

# Create the SendGrid client
sg = SendGridAPIClient(api_key=sendgrid_api_key)

# Prepare the email
message = Mail(
    from_email=from_email,
    to_emails=to_email,
    subject=subject,
    html_content=body
)

# Add attachments if needed
file_path = "testfile"
with open(file_path, "rb") as file:
    file_data = file.read()
    file_name = os.path.basename(file_path)

# Encode the attachment content using Base64
encoded_file_data = base64.b64encode(file_data).decode()

attachment = Attachment(
    FileContent(encoded_file_data),
    FileName(file_name),
    FileType("application/text"),
    Disposition("attachment")
)

message.attachment = attachment

# Send the email
try:
    response = sg.send(message)
    print("Email sent successfully!")
except Exception as e:
    print(f"Error sending email: {str(e)}")
