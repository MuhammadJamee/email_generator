import argparse
import os
import base64
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition

# Create an argument parser
parser = argparse.ArgumentParser(description="Send an email with attachment using SendGrid.")
parser.add_argument("--from-email", required=True, help="The sender's email address.")
parser.add_argument("--to-email", required=True, help="The recipient's email address.")
parser.add_argument("--subject", required=True, help="The subject of the email.")
parser.add_argument("--body", required=True, help="The body content of the email.")
parser.add_argument("--sendgrid-api-key", help="The SendGrid API key.")
parser.add_argument("--attachment-file-path", required=True, help="The path to the attachment file.")

# Parse the command-line arguments
args = parser.parse_args()

# Set your SendGrid API key using the command-line argument or environment variable
sendgrid_api_key = args.sendgrid_api_key or os.environ.get("SENDGRID_API_KEY")

# Create the SendGrid client
sg = SendGridAPIClient(api_key=sendgrid_api_key)

# Prepare the email
message = Mail(
    from_email=args.from_email,
    to_emails=args.to_email,
    subject=args.subject,
    html_content=args.body
)

# Add attachments if needed
file_path = args.attachment_file_path
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
