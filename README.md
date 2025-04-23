# DevOps Pipeline Project

This project implements a simplified DevOps pipeline using local resources. It includes a Flask-based task management web application with automated testing, CI/CD, and Infrastructure as Code components.

## Project Structure

```
devops-midterm/
├── app/
│   └── app.py          # Flask application
├── tests/
│   └── test_app.py     # Unit tests
├── scripts/            # Deployment and monitoring scripts
├── infrastructure/     # IaC configurations
└── requirements.txt    # Python dependencies
```

## Tools and Technologies

- **Web Application**: Flask
- **Testing**: pytest
- **Version Control**: Git
- **CI/CD**: GitHub Actions
- **Infrastructure as Code**: Ansible
- **Programming Language**: Python 3.x

## Local Development Setup

1. Clone the repository
2. Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. Install dependencies:
   ```powershell
   pip install -r requirements.txt
   ```
4. Run the application:
   ```powershell
   python app/app.py
   ```
5. Run tests:
   ```powershell
   pytest
   ```

## Features

- Task management web application
- RESTful API endpoints
- Unit tests
- Automated CI/CD pipeline
- Infrastructure as Code
- Health monitoring

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

## Monitoring

Basic health monitoring is implemented through:
- Endpoint health checks
- Application logs
- Status monitoring script

## Documentation

Detailed documentation for each component will be maintained in their respective directories:
- `/app` - Application documentation
- `/infrastructure` - IaC documentation
- `/scripts` - Script documentation 