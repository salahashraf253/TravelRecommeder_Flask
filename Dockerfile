# # Base image
# FROM python:3.9-slim-buster

# # Set the working directory in the container
# WORKDIR /app

# # Set environment variables for debconf
# ENV DEBIAN_FRONTEND noninteractive
# ENV TERM linux

# # Install dependencies
# RUN apt-get update && apt-get install -y openjdk-11-jdk wget

# # Set environment variables for Spark
# ENV SPARK_VERSION=3.3.2
# ENV HADOOP_VERSION=3.2
# ENV SPARK_HOME=/spark
# ENV PATH=$PATH:$SPARK_HOME/bin

# # Download and install Spark
# RUN wget https://archive.apache.org/dist/spark/spark-3.3.2/spark-3.3.2-bin-hadoop3.2.tgz && \
#     tar -xvzf spark-3.3.2-bin-hadoop3.2.tgz && \
#     mv spark-3.3.2-bin-hadoop3.2 spark

# # Install Python dependencies
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy the application code into the container
# COPY . .

# # Expose the Flask app port
# EXPOSE 5000

# # Set the entrypoint command
# ENTRYPOINT ["python", "app.py"]

# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Set environment variables for debconf
ENV DEBIAN_FRONTEND noninteractive
ENV TERM linux

# Install dependencies
RUN apt-get update && apt-get install -y openjdk-11-jdk wget

# Set environment variables for Spark
ENV SPARK_VERSION=3.3.2
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/spark
ENV PATH=$PATH:$SPARK_HOME/bin

# Copy Spark into the container
COPY spark-3.3.2-bin-hadoop3.2.tgz .

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Extract and move Spark
RUN tar -xvzf spark-3.3.2-bin-hadoop3.2.tgz && \
    mv spark-3.3.2-bin-hadoop3.2 spark && \
    rm spark-3.3.2-bin-hadoop3.2.tgz

# Copy the application code into the container
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Set the entrypoint command
ENTRYPOINT ["python", "app.py"]

