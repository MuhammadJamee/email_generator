import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

# Read environment variables for email details
from_email = os.environ.get("FROM_EMAIL")
to_email = os.environ.get("TO_EMAIL")
subject = os.environ.get("EMAIL_SUBJECT")
body = os.environ.get("EMAIL_BODY")

# Set your SendGrid API key using an environment variable
sendgrid_api_key = os.environ.get("SENDGRID_API_KEY")

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
file_path = os.environ.get("ATTACHMENT_FILE_PATH")
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
