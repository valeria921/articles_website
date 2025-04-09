FROM python:3.13-bookworm

# Ensures Python prints output directly (useful for debugging)
ENV PYTHONUNBUFFERED=1

# Create and set working directory
RUN mkdir /code
WORKDIR /code

COPY requirements.txt .

# Install dependencies using pip (instead of Poetry)
RUN pip install --upgrade pip && pip install -r requirements.txt

# Copy all project files into the container
COPY . .

RUN chmod 755 /code/start-django.sh

# Expose port 8000 for Django
EXPOSE 8000

# Run Django development server
ENTRYPOINT ["/code/start-django.sh"]