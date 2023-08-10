# Pull official base Python Docker image

FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1

ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install dependencies
RUN pip3 install --upgrade pip

COPY requirements.txt /code/
RUN pip3 install -r requirements.txt

# Copy the Django project
COPY . /code/





