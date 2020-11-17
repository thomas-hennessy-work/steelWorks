#Python base image
FROM python:3.7

#create and set a working directory
WORKDIR /steelworks

#install dependancies
RUN apt update
RUN apt install python3-pip -y

COPY ./requierments.txt .

#installing the rest of the dependancies
RUN pip install -r requierments.txt

#copy all files in to the image
COPY . .

#Give the app a port it is listening to
EXPOSE 5000

#Import environemnt variables
ARG SECRET_KEY=$SECRET_KEY
ARG DB_URI=$DB_URI

#Run the create comand
RUN python create.py

#The comands that will be run on start up
ENTRYPOINT ["python", "app.py"]

#Start comand:
#docker build --build-arg SECRET_KEY --build-arg DB_URI -t myapp .
#docker run -d -p 5000:5000 --name myapp -e DB_URI myapp
