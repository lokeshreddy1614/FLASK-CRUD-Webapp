# Deploy Flask CRUD Web Application in Docker on EC2

This guide explains how to deploy a **Flask CRUD** web application inside a **Docker container** on an **EC2 instance**.

## Prerequisites

- **Amazon EC2 instance** running **Ubuntu**.
- **Docker** installed on the EC2 instance.
- SSH access to your EC2 instance.
- Basic knowledge of Docker and Flask.

---

## Step 1: Connect to the EC2 Instance

Use SSH to connect to your EC2 instance. Open a terminal and run the following command:

```bash
ssh -i /path/to/your-key.pem ubuntu@<ec2-public-ip>
