# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Set the entrypoint command
ENTRYPOINT ["python", "app.py"]
