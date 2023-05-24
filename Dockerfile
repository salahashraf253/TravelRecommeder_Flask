# our base image
FROM python:3.8.8

## Install python and pip
#RUN apk add --update py2-pip
#
## upgrade pip
#RUN pip install --upgrade pip

WORKDIR /app

COPY . .

# install Python modules needed by the Python app
RUN pip install  -r requirements.txt

# tell the port number the container should expose
EXPOSE 5000

# run the application
CMD ["python", "app.py"]