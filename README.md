 Flask CRUD Web Application Deployment on AWS EC2

This guide explains step-by-step deployment of a Flask CRUD web application on AWS EC2, including the project setup, directory structure.

---

 Project Description :-

This project is a basic CRUD web application built using {{Flask}}. It includes:
- Create : Add new records.
- Read : Display existing records.
- Update : Edit records.
- Delete : Remove records.

-----------------

 Project Setup on AWS EC2 :-

 Follow these steps to set up and run the Flask app on an EC2 instance.

 1. Launch EC2 Instance :---------
1. Log in to your AWS account and navigate to EC2 service.
2. Create an EC2 virtual machine:
   - Select an (AMI) image (e.g., Ubuntu 22.04).
   - Choose an instance type with (4GB+ storage) and sufficient CPU utilization.
3. Configure network settings:
   - Add a security group with rules to allow ports {{ SSH (22), HTTP (80), HTTPS (443), (5000) and (300001) }}.
4. Launch the instance.

-----------

 2. Connect to EC2 Instance :----
SSH into your EC2 instance:

Copy the below syntax :-
ssh -i your-key.pem ubuntu@<EC2-Public-IP>

 Update and upgrade the system :-
sudo apt update -y
sudo apt upgrade -y

 Install Python3 and pip
sudo apt install python3 python3-pip -y

******Create project directory******

 Verify Python installation :---
python3 --version
pip3 --version
 **Create a project folder and navigate into it**
mkdir project_flask_app
cd project_flask_app

 **Install Flask**
pip3 install flask

**Create project structure**

project_flask_app/

├── app.py                  [Main Flask application]
│
├── templates/             {HTML templates}
│   ├── index.html        (READ)
│   ├── add.html          (CREATE)
│   ├── edit.html         (UPDATE)
├── Dockerfile            (Dockerfile for containerization)
└── requirements.txt      (Python dependencies)


 **Create the main application file**
vim app.py  (add code)

**Create the templates folder and files**
mkdir templates
vim templates/index.html
vim templates/add.html
vim templates/edit.html

**Run the flask application**
python3 app.py

Access the application from your browser using:
  http://<EC2-Public-IP>:5000



  ******Flask CRUD Web Application Deployment with Docker on AWS EC2******

Connect to EC2 Instance :-----

**Install Docker**
Update the system:----
     sudo apt update

Install dependencies :-
A.	sudo apt install apt-transport-https ca-certificates curl software-properties-common
B.	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
C.	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

Add Docker repository :---
  A. sudo apt update
  B. apt-cache policy docker-ce
  C. sudo apt install docker-ce -y

Verify Docker is running :---
     sudo systemctl status docker

     ****Create Flask Project file for Dockers****
1. Create a Dockerfile:-
      vim Dockerfile 
 {{
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]

                 }} 
2. Add required libraries:-
       vim requirements.txt

**Build the Docker Image**

1. For to build the Docker image run the following command:
       docker build -t flask_crud_app .
2. For verfiy the image is build or not run the following command:
       docker images

**Run the Docker Container**
1. For to Start the container run following command:
       docker run -d -p 5000:5000 --name flask_crud_container flask_crud_app
2. Check the running containers by running below command:
       docker ps

**Access the Application**

1. Copy the public IP address of your instance and open new browser then paste the IP address and add port number 5000 to that IP.
2. Browse the page and then access the application.
3. http://<EC2-Public-IP>:5000

       



     






