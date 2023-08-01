# Use the official Python image as the base image
FROM python:3.9

# Copy the Python script into the container
COPY send_email_script.py /app/send_email_script.py

# Set the working directory
WORKDIR /app

# Install required dependencies
RUN pip install -r requirements.txt

# Run the Python script when the container starts
CMD ["python", "send_email_script.py"]
