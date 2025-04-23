
# DevOps Pipeline Midterm Project
Project Description
This project implements a simplified DevOps pipeline for a Task Manager web application. The system demonstrates core DevOps principles including version control, automated testing, CI/CD, and Infrastructure as Code (IaC), all operating in a local environment without Docker or cloud platforms.
The Task Manager application allows users to add, view, and manage tasks through a simple web interface. The project focuses on building a complete pipeline from development to deployment with proper testing and monitoring.

# Application

Backend: Python with Flask framework
Frontend: HTML/CSS with simple form handling
Database: Local file storage for tasks

# DevOps Tools

Version Control: Git with GitHub
CI/CD: GitHub Actions
Testing: Pytest for unit and route testing
Infrastructure as Code: Ansible for configuration management
Deployment: Custom blue/green deployment scripts
Monitoring: Health check script with logging

- **Web Application**: Flask
- **Testing**: pytest
- **Version Control**: Git
- **CI/CD**: GitHub Actions
- **Infrastructure as Code**: Ansible
- **Programming Language**: Python 


# Application Architecture:
/devops-midterm/
├── .github/
│   └── workflows/
│       └── ci.yml          # CI pipeline configuration
├── app/
│   ├── __init__.py         # Flask application initialization
│   └── app.py              # Main application logic
├── deploy/
│   ├── blue/               # Blue deployment environment
│   ├── current/            # Symlink to active environment
│   ├── green/              # Green deployment environment
│   └── deployment_log.txt  # Deployment history log
├── infrastructure/
│   └── playbook.yml        # Ansible playbook for environment setup
├── prod-green/             # Production-ready green environment
│   ├── __init__.py
│   └── app.py
├── project/
│   └── app/                # Development version of application
│       ├── __pycache__/
│       ├── __init__.py
│       └── app.py
├── screenshots/            # Project screenshots for documentation
├── scripts/
│   ├── deploy.py           # Deployment automation script
│   └── health_check.py     # Application monitoring script
├── tests/
│   ├── __init__.py
│   └── test_app.py         # Test cases for application
├── .gitignore              # Git ignore configuration
├── conftest.py             # Pytest configuration
├── health_log.txt          # Health check history
├── README.md               # Project documentation
└── requirements.txt        # Python dependencies

# Workflow Diagram
┌─────────────┐    ┌────────────┐    ┌───────────────┐
│  Developer  │───>│   Git/SCM  │───>│ GitHub Actions│
└─────────────┘    └────────────┘    └───────────────┘
                                            │
                                            │
┌─────────────┐    ┌────────────┐    ┌──────▼──────┐
│   Monitor   │<───│Blue/Green  │<───│   Ansible   │
│Health Checks│    │ Deployment │    │Configuration│
└─────────────┘    └────────────┘    └─────────────┘

## Features

- Task management web application
- RESTful API endpoints
- Unit tests
- Automated CI/CD pipeline
- Infrastructure as Code
- Health monitoring

# CI/CD and IaC Explanation

# Continuous Integration (CI)
The CI pipeline is configured in GitHub Actions and triggers automatically on pushes to both main and dev branches. The pipeline performs the following steps:

Checkout code from repository
Set up Python environment
Install dependencies
Run unit tests with pytest
Generate test reports
Report build status back to GitHub

Tests verify the core functionality including:

Index route access
Task addition functionality
Task listing functionality
Individual task retrieval

# Infrastructure as Code (IaC)
Ansible is used to manage the configuration of the local development and deployment environments. Key aspects include:

Installation of required Python packages
Setting up virtual environments
Configuring application directories
Managing application deployment to different environments

# Continuous Deployment (CD)
The deployment strategy implements a blue/green approach:

Two identical environments are maintained (blue and green)
New deployments target the inactive environment
Health checks verify the deployed application
Traffic is switched to the new environment if health checks pass
The previous environment becomes inactive and is ready for the next deployment

## Monitoring

Basic health monitoring is implemented through:
- Endpoint health checks
- Application logs
- Status monitoring script
## CI/CD Pipeline

The CI/CD pipeline includes:
1. Automated testing on push
2. Code quality checks
3. Local deployment
4. Health monitoring

## Infrastructure as Code

The infrastructure configuration includes:
- Environment setup
- Application deployment
- Configuration management


## Status Display
- A `/status` route displays the latest health check result from `health_log.txt`.

# Setup and Usage Instructions

# Prerequisites

Python 3.11+
Git
Ansible

# Local Development Setup

# Clone the repository:
git clone https://github.com/niinora/Devops-midterm

# Create and activate virtual environment:
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies:
pip install -r requirements.txt

# Run the application locally:
python app/app.py

Access the application at http://127.0.0.1:5000

# Running Tests
pytest tests/
Deployment

# Configure environments:
ansible-playbook ansible/playbooks/setup.yml

# Deploy to target environment:
python scripts/deploy.py

# Switch active environment if health checks pass:
python scripts/switch.py

## Screenshots

- **Screenshot 1** [Task Manager web interface showing task list and input form.](screenshots/picture1.png)
- **Screenshot 2** [Task Manager after adding a new task ("gym").](screenshots/picture2.png)
- **Screenshot 3** [Server logs showing GET and POST requests to the application.](screenshots/picture3.png)
- **Screenshot 4** [Task Manager web interface showing task list and input form.](screenshots/picture4.png)
- **Screenshot 5** [JSON representation of a single task/0 accessed via API.](screenshots/picture5.png)
- **Screenshot 6** [JSON representation of a single task/1 accessed via API.](screenshots/picture6.png)
- **Screenshot 7** [JSON representation of a single task/2 accessed via API.](screenshots/picture7.png)
- **Screenshot 8** [ All tests passing in the pytest suite.](screenshots/picture8.png)
- **Screenshot 9** [Git branch structure showing dev as the active branch](screenshots/picture9.png)
- **Screenshot 10** [Successful CI pipeline run on the dev branch.](screenshots/picture10.png)
- **Screenshot 11** [Blue/green deployment switch log showing successful change.](screenshots/picture11.png)
- **Screenshot 12** [Deployment history showing timestamps for green and blue environment deployments.](screenshots/picture12.png)
- **Screenshot 13** [Health check logs showing application status history, including an unhealthy state detection.](screenshots/picture13.png)
- **Screenshot 14** [Custom status page showing real-time application health information.](screenshots/picture14.png)
- **Screenshot 15** [Infrastructure as Code execution showing successful configuration tasks including Python installation, directory creation, and file copying.](screenshots/picture15.png)


