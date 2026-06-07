# Infrastructure as Code Web Application
![Terraform](https://img.shields.io/badge/terraform-%235835CC.svg?style=for-the-badge&logo=terraform&logoColor=white)
![Ansible](https://img.shields.io/badge/ansible-%231A1918.svg?style=for-the-badge&logo=ansible&logoColor=white)
![AWS](https://img.shields.io/badge/AWS-%23FF9900.svg?style=for-the-badge&logo=amazon-aws&logoColor=white)
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Flask](https://img.shields.io/badge/flask-%23000.svg?style=for-the-badge&logo=flask&logoColor=white)
![Nginx](https://img.shields.io/badge/nginx-%23009639.svg?style=for-the-badge&logo=nginx&logoColor=white)
![Gunicorn](https://img.shields.io/badge/gunicorn-%298729.svg?style=for-the-badge&logo=gunicorn&logoColor=white)
![Ubuntu](https://img.shields.io/badge/Ubuntu-E95420?style=for-the-badge&logo=ubuntu&logoColor=white)

A clean demonstration of Infrastructure as Code (IaC) principles using **Terraform** to provision AWS infrastructure and **Ansible** to automate application deployment. This project creates a complete web application stack with a single command.

## 🏗️ Architecture
<img width="1346" height="686" alt="Screenshot 2026-02-15 104028" src="https://github.com/user-attachments/assets/084239ee-69a6-4462-b56f-223460e27961" />




## 🚀 What This Project Does

1. **Terraform** provisions:
   - VPC with public subnet
   - Internet Gateway and routing
   - Security groups (SSH, HTTP, HTTPS)
   - EC2 instance (Ubuntu 22.04)
   - Automatically generates Ansible inventory

2. **Ansible** configures:
   - System packages and dependencies
   - Nginx web server
   - Python Flask application
   - Gunicorn WSGI server
   - Systemd service for auto-start

3. **Result**: A fully functional web application accessible via HTTP

## 📋 Prerequisites

Before you begin, ensure you have:

- **AWS Account** with appropriate permissions
- **AWS CLI** installed and configured (`aws configure`)
- **Terraform** (>= 1.0) - [Install Guide](https://developer.hashicorp.com/terraform/downloads)
- **Ansible** (>= 2.9) - [Install Guide](https://docs.ansible.com/ansible/latest/installation_guide/intro_installation.html)
- **SSH Key Pair** for EC2 access

### Creating an SSH Key Pair

You need an EC2 key pair in your AWS region:

**Option 1: AWS Console**
1. Go to EC2 Dashboard → Key Pairs
2. Click "Create Key Pair"
3. Name: `my-ec2-key` (or your preferred name)
4. Type: RSA
5. Format: `.pem`
6. Download and save to `~/.ssh/my-ec2-key.pem`
7. Set permissions: `chmod 400 ~/.ssh/my-ec2-key.pem` (Linux/Mac)

**Option 2: AWS CLI**
```bash
aws ec2 create-key-pair --key-name my-ec2-key --query 'KeyMaterial' --output text > ~/.ssh/my-ec2-key.pem
chmod 400 ~/.ssh/my-ec2-key.pem  # Linux/Mac only
```

## 🛠️ Configuration

1. **Edit `terraform.tfvars`** with your settings:

```hcl
# Replace with your EC2 key pair name
key_name = "my-ec2-key"

# (Optional) Restrict SSH access to your IP for better security
# Find your IP: curl ifconfig.me
my_ip = "YOUR_IP/32"  # e.g., "203.0.113.45/32"
```

2. **Update `ansible.cfg`** if your key is in a different location:

```ini
private_key_file = ~/.ssh/my-ec2-key.pem
```

## 🚀 Deployment

### Step 1: Provision Infrastructure with Terraform

```bash
# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Create infrastructure
terraform apply
```

**Note the outputs:**
- `instance_public_ip` - You'll need this to access the app
- `web_url` - Direct link to your application
- `ssh_command` - Command to SSH into the instance

### Step 2: Configure Server with Ansible

Wait 30-60 seconds for the EC2 instance to fully boot, then:

```bash
# Run the Ansible playbook
ansible-playbook playbook.yml
```

This will:
- Install all dependencies
- Deploy the Flask application
- Configure Nginx as a reverse proxy
- Start all services

### Step 3: Access Your Application

Open your browser and navigate to:
```
http://<instance_public_ip>
```

**Available Endpoints:**
- `/` - Home page with project information
- `/health` - Health check endpoint (JSON)
- `/info` - System information (JSON)

## 🧪 Testing

### Test Terraform Configuration
```bash
terraform validate
terraform fmt -check
```

### Test Ansible Playbook
```bash
ansible-playbook playbook.yml --syntax-check
ansible-playbook playbook.yml --check  # Dry run
```

### Test Application
```bash
# Health check
curl http://<instance_public_ip>/health

# System info
curl http://<instance_public_ip>/info
```

## 🧹 Cleanup

To destroy all resources and avoid AWS charges:

```bash
terraform destroy
```

Type `yes` when prompted. This will remove:
- EC2 instance
- Security groups
- Subnets
- VPC
- Internet Gateway

## 📁 Project Structure

```
terraform_ANsible/
├── main.tf              # Main Terraform configuration
├── variables.tf         # Variable definitions
├── outputs.tf           # Output definitions
├── terraform.tfvars     # Variable values (customize this)
├── ansible.cfg          # Ansible configuration
├── playbook.yml         # Ansible playbook
├── inventory            # Auto-generated by Terraform
├── app/
│   ├── app.py          # Flask application
│   └── requirements.txt # Python dependencies
└── README.md           # This file
```

## 🔧 Customization

### Change Instance Type
Edit `terraform.tfvars`:
```hcl
instance_type = "t2.small"  # or t2.medium, etc.
```

### Change AWS Region
Edit `terraform.tfvars`:
```hcl
aws_region = "us-west-2"
```

### Modify the Application
Edit `app/app.py` to customize the Flask application, then re-run:
```bash
ansible-playbook playbook.yml
```

## 🐛 Troubleshooting

### Terraform Issues

**Problem:** `Error: No valid credential sources found`
- **Solution:** Run `aws configure` and enter your AWS credentials

**Problem:** `Error: InvalidKeyPair.NotFound`
- **Solution:** Ensure the key pair exists in your AWS region and `terraform.tfvars` has the correct name

### Ansible Issues

**Problem:** `Permission denied (publickey)`
- **Solution:** Check that your SSH key has correct permissions: `chmod 400 ~/.ssh/my-ec2-key.pem`

**Problem:** `Host key verification failed`
- **Solution:** This is handled by `ansible.cfg`, but you can manually add: `ssh-keyscan <instance_ip> >> ~/.ssh/known_hosts`

### Application Issues

**Problem:** Can't access the web application
- **Solution:** 
  1. Check security group allows HTTP (port 80)
  2. Verify services are running: `ssh -i ~/.ssh/my-ec2-key.pem ubuntu@<instance_ip>` then `sudo systemctl status flask-app nginx`
  3. Check application logs: `sudo journalctl -u flask-app -f`

## 📚 Technologies Used

- **Terraform** - Infrastructure provisioning
- **Ansible** - Configuration management
- **AWS** - Cloud provider
- **Python Flask** - Web framework
- **Gunicorn** - WSGI HTTP server
- **Nginx** - Reverse proxy and web server

## Documentation formatting and structure assisted by AI tools


