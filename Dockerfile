FROM python:3.10-alpine

LABEL author="M Jamee Ghouri <jameeghouri@gmail.com>"

ENV PYTHONUNBUFFERED=1

RUN pip install -U pip

COPY . .

RUN pip install -r requirements.txt

ENTRYPOINT ["/send_email_script.py"]
