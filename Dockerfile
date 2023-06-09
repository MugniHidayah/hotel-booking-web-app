# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.10.2

#Expose port 8080
EXPOSE 8080

#upgrade pip
RUN python -m pip install --upgrade pip

#Copy Requirements.txt file into app directory
COPY requirements.txt app/requirements.txt

#install all requirements in requirements.txt
RUN pip install -r app/requirements.txt

#Copy all files in current directory into app directory
COPY . /app

#Change Working Directory to app directory
WORKDIR /app

#Run the application on port 8080
# ENTRYPOINT ["python", "index.py", "--server.port=8080", "--server.address=0.0.0.0"]
CMD python index.py