FROM python:3.10-alpine as builder

RUN mkdir /app

COPY requirements.txt /app/

# Set Env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN python -m pip install --trusted-host pypi.python.org --trusted-host files.pythonhosted.org --trusted-host pypi.org -r /app/requirements.txt

COPY . /app/
WORKDIR /app
CMD ["python", "manage.py", "runserver", "127.0.0.1:8000"]
