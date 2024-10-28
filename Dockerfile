# First we import the python image from DockerHub (https://hub.docker.com/_/python)

FROM python:3.12

# Standard environment variables when creating a python based dockerfile
# First env tells python not to write .pyc files. These files are unnecessary for a container.
# Second env tells python to output directly into the console without buffering

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1 

# Make a directory called app to store your django project, update any packages, and update pip

RUN mkdir /app && \ 
    apt update && \
    pip install --upgrade pip

# Set the new directory as the working directory    

WORKDIR /app

# Copy all the files in your current directory on your host to the current directory of the container

COPY . .

# Run commands to install the requirements from your requirements.txt

RUN pip install -r requirements.txt

# Expose port 8000

EXPOSE 8000

# Commands to run when container is finished. Seperate each string with a comma.

CMD ["gunicorn", "-b", "0.0.0.0:8000", "mysite.wsgi:application"]