FROM python:3.12.10-slim-bookworm

WORKDIR /usr/src/app

RUN pip install uv

COPY . .

CMD [ "python", "./app/src/main.py" ]