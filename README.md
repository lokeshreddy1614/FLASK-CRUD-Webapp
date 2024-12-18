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
├── kubernetes
     ├──config.yaml
     ├──deployment.yaml
     ├──service.yaml

 **Create the main application file**
1. vim app.py  (add code)
     **code**
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
        name = request.form['name']
        description = request.form['description']
        new_item = Item(name=name, description=description)
        db.session.add(new_item)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('add.html')

@app.route('/update/<int:id>', methods=['GET', 'POST'])
def update(id):
    item = Item.query.get_or_404(id)
    if request.method == 'POST':
        item.name = request.form['name']
        item.description = request.form['description']
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('update.html', item=item)

@app.route('/delete/<int:id>')
def delete(id):
    item = Item.query.get_or_404(id)
    db.session.delete(item)
    db.session.commit()
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
    
2. **Create the templates folder and files**
     A. mkdir templates
      1. vim templates/index.html
**code**
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>CRUD Application</title>
</head>
<body>
    <h1>Items List</h1>
    <a href="{{ url_for('add') }}">Add New Item</a>
    <ul>
        {% for item in items %}
        <li>
            {{ item.name }} - {{ item.description }}
            <a href="{{ url_for('update', id=item.id) }}">Update</a>
            <a href="{{ url_for('delete', id=item.id) }}">Delete</a>
        </li>
        {% endfor %}
    </ul>
</body>
</html>

    2. vim templates/add.html
**code**
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Add Item</title>
</head>
<body>
    <h1>Add New Item</h1>
    <form method="POST">
        <label>Name:</label>
        <input type="text" name="name" required>
        <br>
        <label>Description:</label>
        <input type="text" name="description" required>
        <br>
        <button type="submit">Add Item</button>
    </form>
    <a href="{{ url_for('index') }}">Back</a>
</body>
</html>


    3. vim templates/edit.html
**code**
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <title>Update Item</title>
</head>
<body>
    <h1>Update Item</h1>
    <form method="POST">
        <label>Name:</label>
        <input type="text" name="name" value="{{ item.name }}" required>
        <br>
        <label>Description:</label>
        <input type="text" name="description" value="{{ item.description }}" required>
        <br>
        <button type="submit">Update Item</button>
    </form>
    <a href="{{ url_for('index') }}">Back</a>
</body>
</html>



**Run the flask application**
python3 app.py

Access the application from your browser using:
  http://<EC2-Public-IP>:5000



  ******Flask CRUD Web Application Deployment with Docker on AWS EC2******

Connect to EC2 Instance :-----

1. **Install Docker**
   Update the system:----
     sudo apt update

   Install dependencies :-
   A.	sudo apt install apt-transport-https ca-certificates curl software-properties-common
   B.	curl -fsSL https://download.docker.com/linux/ubuntu/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg
   C.	echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/ubuntu $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null

2. Add Docker repository :---
   A. sudo apt update
   B. apt-cache policy docker-ce
   C. sudo apt install docker-ce -y

3. Verify Docker is running :---
     sudo systemctl status docker

   ****Create Flask Project file for Dockers****
      1. Create a Dockerfile:-
      vim Dockerfile 
 **code**
FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install -r requirements.txt

EXPOSE 5000

CMD ["python3", "app.py"]

                 }} 
   2. Add required libraries:-
      vim requirements.txt

1. **Build the Docker Image**

   1. For to build the Docker image run the following command:
      docker build -t flask_crud_app .
   2. For verfiy the image is build or not run the following command:
      docker images

2. **Run the Docker Container**
   1. For to Start the container run following command:
       docker run -d -p 5000:5000 --name flask_crud_container flask_crud_app
   2. Check the running containers by running below command:
       docker ps

3. **Access the Application**

   1. Copy the public IP address of your instance and open new browser then paste the IP address and add port number 5000 to that IP.
   2. Browse the page and then access the application.
   3. http://<EC2-Public-IP>:5000


 **Flask CRUD Application Deployment on Kubernetes Cluster**
   1. Access the EC2 Instance.
   2. Navigate to the project directory.
   3. Ensure the Dockerfile is present in the project root.
   4. Install kubectl to interact with the Kubernetes cluster:
     **Download the latest kubectl version**
     curl -LO https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl

     **Install kubectl**
     sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl

     **Verify installation**
     kubectl version --client

   5. Install Kind (Kubernetes-in-Docker) helps create local Kubernetes clusters.
      Download Kind binary:
      curl -Lo ./kind https://kind.sigs.k8s.io/dl/v0.25.0/kind-linux-amd64

      Make it executable:
      chmod +x ./kind

      Move to system path:
      sudo mv ./kind /usr/local/bin/kind

      Verify Kind installation:
      kind --version
  6. Create Kubernetes Cluster with Kind
       Create a config.yaml file:
       vim config.yaml

   kind: Cluster
apiVersion: kind.x-k8s.io/v1alpha4
nodes:
- role: control-plane
  extraPortMappings:
  - containerPort: 30001
    hostPort: 30001
    protocol: TCP

  7.Create a Kind cluster using the configuration:
   kind create cluster --config config.yaml

  8. Create Kubernetes Manifests( deployment.yaml) & (service.yaml)
  9. Create deployment.yaml:
      vim deployment.yaml
**code**
apiVersion: apps/v1
kind: Deployment
metadata:
  name: flask-web-app
  labels:
    app: flask-web-app
spec:
  replicas: 1
  selector:
    matchLabels:
      app: flask-web-app
  template:
    metadata:
      labels:
        app: flask-web-app
    spec:
      containers:
      - name: flask-container
        image: flask-crud-app:latest
        imagePullPolicy: IfNotPresent
        ports:
        - containerPort: 5000


  10. Create service.yaml:
      vim service.yaml
**code**
apiVersion: v1
kind: Service
metadata:
  name: flask-web-service
  labels:
    app: flask-web-app
spec:
  type: NodePort
  selector:
    app: flask-web-app
  ports:
  - protocol: TCP
    port: 5000
    targetPort: 5000
    nodePort: 30001


  11. Build and Load Docker Image into Kind Cluster.
  12. Build the Docker image:
      docker build -t flask-crud-app:latest
      
  13.Load the image into the Kind cluster:
     kind load docker-image flask-crud-app:latest

  14. Deploy to Kubernetes.
  15. Apply the deployment:
      kubectl apply -f deployment.yaml

  16. Apply the service:
      kubectl apply -f service.yaml

  17. Verify the pods and services:
      kubectl get pods
      kubectl get services     (or)
      kubectl get all

  18. Use telnet to check if the service is accessible:
      telnet localhost 30001

 19. Open inbound port 30001 in the EC2 security group:

     Go to EC2 Console > Instance Details > Security Group > Inbound Rules.
     Add a rule:
     Type: Custom TCP
     Port: 30001
     Source: Anywhere (0.0.0.0/0)

20. Copy the EC2 public IP and access the app in your browser.
21. http://<public-ip>:30001







   



     






