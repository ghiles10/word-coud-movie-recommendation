FROM ubuntu:latest 
ADD . /app
WORKDIR /app 

RUN apt-get update
RUN apt-get -y install libpq-dev
RUN apt-get -y install python3 
RUN apt-get -y install python3-pip

RUN pip install -r requirements_dash.txt

CMD ["python3", "./dash_word_cloud.py"]
