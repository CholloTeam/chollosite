# Pull official base Python Docker image
FROM python:3.9.6

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Set work directory
WORKDIR /code

# Install system dependencies for psycopg2 and pillow
RUN apt-get update && \
    apt-get install -y libpq-dev libjpeg-dev zlib1g-dev

# Install dependencies
RUN pip install --upgrade pip
COPY requirements.txt /code/
RUN pip install -r requirements.txt

# Copy the Django project
COPY . /code/

# Run your Django application (replace with your actual command)
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]

