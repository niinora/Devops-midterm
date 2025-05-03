import os
import shutil
import subprocess
import sys
from datetime import datetime

def get_current_deployment():
    if os.path.exists("deploy/current"):
        return os.path.realpath("deploy/current")
    return None

def get_next_environment():
    current = get_current_deployment()
    if current is None or "blue" in current:
        return "green"
    return "blue"

def deploy(environment):
    deploy_path = f"deploy/{environment}"
    
    # Create deployment directory if it doesn't exist
    os.makedirs(deploy_path, exist_ok=True)
    raise Exception("Simulated error to test rollback")
    
    # Copy application files
    print(f"Copying files to {environment} environment...")
    shutil.copytree("app", f"{deploy_path}/app", dirs_exist_ok=True)
    shutil.copy("requirements.txt", deploy_path)
    
    # Create virtual environment if it doesn't exist
    if not os.path.exists(f"{deploy_path}/venv"):
        print("Creating virtual environment...")
        subprocess.run([sys.executable, "-m", "venv", f"{deploy_path}/venv"], check=True)
    
    # Install dependencies
    print("Installing dependencies...")
    if os.name == 'nt':  # Windows
        pip_path = f"{deploy_path}/venv/Scripts/python"
        pip_exe = f"{deploy_path}/venv/Scripts/pip"
    else:  # Unix
        pip_path = f"{deploy_path}/venv/bin/python"
        pip_exe = f"{deploy_path}/venv/bin/pip"
    
    # Update pip first
    print("Updating pip...")
    subprocess.run([pip_path, "-m", "pip", "install", "--upgrade", "pip"], check=True)
    
    # Then install requirements
    print("Installing project dependencies...")
    subprocess.run([pip_exe, "install", "-r", "requirements.txt"], check=True)
    
    return deploy_path

def switch_environment(new_env_path):
    current_path = "deploy/current"
    if os.path.exists(current_path):
        shutil.rmtree(current_path)
    shutil.copytree(new_env_path, current_path)
    print(f"Switched deployment to: {new_env_path}")

def rollback():
    current = get_current_deployment()
    if current is None:
        print("No current deployment to rollback to!")
        return False
    
    if "blue" in current:
        alternate = "deploy/green"
    else:
        alternate = "deploy/blue"
    
    if os.path.exists(alternate):
        switch_environment(alternate)
        print(f"Rolled back to {alternate}")
        return True
    
    print("No alternate environment to rollback to!")
    return False

def main():
    # Get next environment to deploy to
    next_env = get_next_environment()
    print(f"Deploying to {next_env} environment...")
    
    try:
        # Deploy to new environment
        deploy_path = deploy(next_env)
        
        # Switch to new environment
        switch_environment(deploy_path)
        print(f"Successfully switched to {next_env} environment")
        
        # Log deployment
        with open("deploy/deployment_log.txt", "a") as f:
            timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            f.write(f"[{timestamp}] Deployed to {next_env} environment\n")
        
    except Exception as e:
        print(f"Deployment failed: {str(e)}")
        print("Attempting rollback...")
        if rollback():
            print("Rollback successful")
        else:
            print("Rollback failed")
        sys.exit(1)

if __name__ == "__main__":
    main() 
    