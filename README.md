Sending Email with SendGrid

This Python-based SendGrid workflow allows you to send emails with both body content and attachments. The workflow utilizes the SendGrid API to send emails efficiently and reliably.

Key Features:
- Simple Command-Line Interface: The workflow uses argparse to accept command-line arguments, making it easy to specify the recipient, subject, body content in markdown format, sender's email address, and the SendGrid API key.

- Markdown Support: You can compose the body content of the email using markdown syntax, allowing for easy formatting of the email's text.

- Multiple Recipients: The workflow supports sending emails to multiple recipients simultaneously, making it convenient for reaching multiple recipients with a single command.

- Attachment Support: You can attach files to the email by providing the file path as an argument, making it possible to send important files along with the email.

To use the workflow, ensure that you have the necessary dependencies installed by checking the `requirements.txt` file. Make sure to set up your SendGrid API key and replace `YOUR_SENDGRID_API_KEY` with your actual API key in the command-line arguments.

Example Usage:
```bash
python send_email_script.py \
    --to recipient@example.com \
    --subject "Your Subject" \
    --markdown-body "Hello, **This is a sample email** using *markdown*." \
    --from-email sender@example.com \
    --api-key YOUR_SENDGRID_API_KEY
```

Please note that this script requires a compatible environment with the correct Python version and dependencies installed. It is recommended to use a virtual environment to manage dependencies effectively.

Enjoy sending emails effortlessly with SendGrid using this Python workflow! If you encounter any issues or errors, refer to the troubleshooting section or check the compatibility of the script with your system's architecture and operating system. Happy emailing!
