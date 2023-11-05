# Use the official Python image as the base image
FROM python:3

# Set the working directory inside the container
WORKDIR /app

# Copy the local Python script into the container
COPY app.py /app/app.py

# Run the Python script when the container starts
CMD ["python", "app.py"]
