# DeepRenalFlow: Kidney Disease Classification

**DeepRenalFlow** is a deep learning application designed for kidney disease classification. This project is built with a robust, modular architecture and leverages a modern MLOps stack for seamless experiment tracking, data versioning, and automated CI/CD deployment to the cloud.

The core of this project is its automated pipeline. From data ingestion and versioning with **DVC** to experiment tracking with **MLflow** and automated deployment using **Docker**, **GitHub Actions**, and **AWS**, every step is designed for reproducibility, scalability, and ease of use.


## Real-World Use Case

A medical technology startup could use this exact framework to deploy and manage a diagnostic AI tool for hospitals. When their data scientists develop an improved version of the kidney classification model, they simply push their code to a Git repository. This single action automatically triggers the GitHub Actions workflow, which packages the new model into a container and deploys it to an AWS server. The hospital's application can then immediately and securely access the updated model. This automated, version-controlled process is crucial for maintaining regulatory compliance (e.g., with HIPAA or FDA standards) as every model deployed can be traced back to the exact code, data, and performance metrics that produced it.

## 🛠️ Technology Stack

This project is built using a suite of powerful tools to ensure a robust and efficient workflow:

* **Model Development**: Python, TensorFlow, Keras

* **Experiment Tracking**: [MLflow](https://mlflow.org/)

* **Data Version Control**: [DVC](https://dvc.org/)

* **Containerization**: [Docker](https://www.docker.com/)

* **CI/CD Automation**: [GitHub Actions](https://github.com/features/actions)

* **Cloud Deployment**: Amazon Web Services (AWS)

  * **ECR (Elastic Container Registry)**: For storing Docker images.

  * **EC2 (Elastic Compute Cloud)**: For hosting the application.

## 🚀 Getting Started (Local Setup)

Follow these steps to set up and run the project on your local machine.

### **STEP 1: Clone the Repository**

``` bash
git clone https://github.com/Mohit-Bansal-31/DeepRenalFlow_AI
cd DeepRenalFlow_AI
```

### **STEP 2: Create and Activate a Virtual Environment**

It's recommended to use a virtual environment to manage project dependencies.

``` bash
Create the environment
python -m venv myenv

Activate the environment
On Windows
myenv\Scripts\activate.bat

On macOS/Linux
source myenv/bin/activate
```

### **STEP 3: Install Dependencies**

Install all the required Python packages from the `requirements.txt` file.

``` bash
pip install -r requirements.txt
```

### **STEP 4: Run the Application**

Start the Flask web application.

``` bash
python app.py
```

Once running, open your web browser and navigate to `http://127.0.0.1:8080` (or the address shown in your terminal) to use the app.

## 🔬 MLOps Tools

### **MLflow: Experiment Tracking**

To track experiments, you need to configure your MLflow tracking server URI and credentials. Set the following environment variables:

``` bash
export MLFLOW_TRACKING_URI=<your_dagshub_repo_uri>.mlflow
export MLFLOW_TRACKING_USERNAME=<your_dagshub_username>
export MLFLOW_TRACKING_PASSWORD=<your_dagshub_password_or_token>
```

### **DVC: Data & Pipeline Version Control**

DVC is used to manage large data files and define the ML pipeline.

* `dvc init`: Initialize DVC in the repository (if not already done).

* `dvc repro`: Reproduce the entire pipeline (from data ingestion to model training).

* `dvc dag`: Visualize the Directed Acyclic Graph (DAG) of the pipeline.

## ☁️ Automated CI/CD Deployment to AWS

This project is configured for continuous integration and deployment to AWS using GitHub Actions. Here is a high-level overview of the setup process.

### **Deployment Workflow Overview**

1. Code is pushed to the GitHub repository.

2. A **GitHub Actions** workflow is triggered.

3. The workflow builds a **Docker image** of the application.

4. The image is pushed to the **AWS ECR** repository.

5. The workflow connects to an **AWS EC2** instance (configured as a self-hosted runner).

6. The EC2 instance pulls the new Docker image from ECR and runs it, deploying the updated application.

### **Part 1: AWS Initial Setup**

#### **1. Create an IAM User**

Create an IAM user in your AWS console with programmatic access. Attach the following policies to grant the necessary permissions:

* `AmazonEC2ContainerRegistryFullAccess`

* `AmazonEC2FullAccess`

Save the generated **Access Key ID** and **Secret Access Key**.

#### **2. Create an ECR Repository**

In the AWS ECR service, create a new private repository to store your Docker images. Note the repository **URI**.

#### **3. Launch an EC2 Instance**

Launch a new EC2 instance (e.g., using an Ubuntu Server AMI). This machine will host your application.

### **Part 2: Configure the EC2 Instance**

#### **1. Install Docker**

Connect to your EC2 instance via SSH and install Docker.

``` bash
#Update package lists
sudo apt-get update -y

Install Docker
curl -fsSL https://get.docker.com -o get-docker.sh
sudo sh get-docker.sh

Add the 'ubuntu' user to the 'docker' group to run docker commands without sudo
sudo usermod -aG docker ubuntu
newgrp docker
```

#### **2. Configure EC2 as a GitHub Self-Hosted Runner**

In your GitHub repository, go to `Settings > Actions > Runners`.

* Click `New self-hosted runner`.

* Select `Linux` as the operating system.

* Follow the on-screen commands to download, configure, and run the actions runner on your EC2 instance.

### **Part 3: GitHub Repository Configuration**

#### **Set up GitHub Secrets**

In your GitHub repository, go to `Settings > Secrets and variables > Actions` and add the following repository secrets. These will be used by the GitHub Actions workflow to authenticate with AWS.

* `AWS_ACCESS_KEY_ID`: Your IAM user's access key.

* `AWS_SECRET_ACCESS_KEY`: Your IAM user's secret key.

* `AWS_REGION`: The AWS region where your services are located (e.g., `us-east-1`).

* `AWS_ECR_LOGIN_URI`: The URI of your ECR repository (e.g., `123456789012.dkr.ecr.us-east-1.amazonaws.com`).

* `ECR_REPOSITORY_NAME`: The name of your ECR repository.
