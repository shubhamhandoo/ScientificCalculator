
# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY calculator.py .
COPY test.py .

# Command to run your application
CMD ["python", "calculator.py"]
