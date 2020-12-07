FROM python:3.9

RUN mkdir /app
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY users.json .
COPY login.py .
COPY app.py .
EXPOSE 5001
CMD ["python", "/app/app.py"]