import argparse
import base64
import os  # Add this line to import the 'os' module
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail, Attachment, FileContent, FileName, FileType, Disposition


def send_email(from_email, to_email, subject, body, sendgrid_api_key, attachment_file_path):
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
    with open(attachment_file_path, "rb") as file:
        file_data = file.read()
        file_name = os.path.basename(attachment_file_path)

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


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Send an email with attachment using SendGrid.")
    parser.add_argument("--from-email", required=True, help="Sender's email address")
    parser.add_argument("--to-email", required=True, help="Recipient's email address")
    parser.add_argument("--subject", required=True, help="Email subject")
    parser.add_argument("--body", required=True, help="Email body content")
    parser.add_argument("--sendgrid-api-key", required=True, help="SendGrid API key")
    parser.add_argument("--attachment-file-path", required=True, help="Path to the attachment file")

    args = parser.parse_args()

    send_email(
        args.from_email,
        args.to_email,
        args.subject,
        args.body,
        args.sendgrid_api_key,
        args.attachment_file_path
    )
