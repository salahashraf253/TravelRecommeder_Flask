FROM python:3.8.8

WORKDIR /usr/src/app

# Install Java
RUN apt-get update && apt-get install -y default-jre-headless


COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt

COPY . .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]