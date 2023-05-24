#FROM python:3.8.8
#
## Install Java
#RUN apt-get update && apt-get install -y default-jre-headless
#
#WORKDIR /usr/src/app
#
#COPY requirements.txt requirements.txt
#
#RUN pip install -r requirements.txt
#
#COPY . .
#
#CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]


# Base image
FROM python:3.9-slim-buster

# Set the working directory in the container
WORKDIR /app

# Install dependencies
RUN apt-get update && apt-get install -y openjdk-11-jdk

# Set environment variables for Spark
ENV SPARK_VERSION=3.3.2
ENV HADOOP_VERSION=3.2
ENV SPARK_HOME=/spark
ENV PYSPARK_PYTHON=/usr/bin/python3

# Download and install Spark
RUN wget https://archive.apache.org/dist/spark/spark-$SPARK_VERSION/spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    tar -xvzf spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION.tgz && \
    mv spark-$SPARK_VERSION-bin-hadoop$HADOOP_VERSION spark

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code into the container
COPY . .

# Expose the Flask app port
EXPOSE 5000

# Set the entrypoint command
ENTRYPOINT ["python", "app.py"]
