# Base Image
FROM python:3.8-slim

WORKDIR /app

COPY . /app

RUN pip install virtualenv

RUN virtualenv venv

RUN /bin/bash -c "source venv/bin/activate"

RUN pip install --no-cache-dir -r requirements.txt
EXPOSE 5000

ENV FLASK_APP=app.py

ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run"]
