FROM python:3.8-buster

RUN mkdir /app

COPY . /app

WORKDIR /app

RUN python -m pip install --upgrade pip

RUN pip install --default-timeout=100 future

RUN pip install -r requirements.txt

CMD ["python", "src/main.py"]