FROM python:3.8-alpine3.17

WORKDIR /flask-examples

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

EXPOSE 3000 5000
CMD ["python3", "-m", "flask", "--app", "server.py", "run", "--host=0.0.0.0"]