FROM python:3.7

WORKDIR /app
EXPOSE 8000

COPY ./app/ /app/
RUN pip install pipenv
RUN pipenv install --system --deploy

CMD ["python", "app.py"]
