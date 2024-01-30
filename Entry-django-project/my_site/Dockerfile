FROM python:3.11

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONBUFFERED=1

COPY . /app

WORKDIR /app

RUN pip install -r requirements.txt

EXPOSE 8000

ENTRYPOINT [ "python3" ]

CMD ["manage.py","runserver"]