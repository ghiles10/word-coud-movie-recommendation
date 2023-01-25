FROM ubuntu:latest 
ADD . /app
WORKDIR /app 

RUN apt-get update
RUN apt-get -y install libpq-dev
RUN apt-get -y install wget
RUN apt-get -y install openjdk-8-jdk-headless 
RUN wget https://dlcdn.apache.org/spark/spark-3.3.1/spark-3.3.1-bin-hadoop3.tgz

RUN tar -xzf spark-3.3.1-bin-hadoop3.tgz
RUN mv spark-3.3.1-bin-hadoop3 spark

RUN apt-get -y install python3 
RUN apt-get -y install python3-pip



RUN pip install -r requirements.txt

CMD ["python3", "./write_to_sql.py"]