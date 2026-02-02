#!/bin/bash
# Control Node Setup Script
# This script sets up an Ubuntu EC2 instance as a Terraform/Ansible control node

set -e

echo "=================================="
echo "Control Node Setup Starting..."
echo "=================================="

# Update system
echo "[1/6] Updating system packages..."
sudo apt update && sudo apt upgrade -y

# Install prerequisites
echo "[2/6] Installing prerequisites..."
sudo apt install -y \
    software-properties-common \
    wget \
    curl \
    unzip \
    git \
    python3-pip \
    vim

# Install Ansible
echo "[3/6] Installing Ansible..."
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible

# Install Terraform
echo "[4/6] Installing Terraform..."
TERRAFORM_VERSION="1.7.0"
wget https://releases.hashicorp.com/terraform/${TERRAFORM_VERSION}/terraform_${TERRAFORM_VERSION}_linux_amd64.zip
unzip terraform_${TERRAFORM_VERSION}_linux_amd64.zip
sudo mv terraform /usr/local/bin/
rm terraform_${TERRAFORM_VERSION}_linux_amd64.zip

# Install AWS CLI
echo "[5/6] Installing AWS CLI..."
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip

# Verify installations
echo "[6/6] Verifying installations..."
echo ""
echo "✅ Ansible version:"
ansible --version | head -n 1
echo ""
echo "✅ Terraform version:"
terraform --version | head -n 1
echo ""
echo "✅ AWS CLI version:"
aws --version
echo ""

echo "=================================="
echo "✅ Control Node Setup Complete!"
echo "=================================="
echo ""
echo "Next steps:"
echo "1. Configure AWS credentials: aws configure"
echo "2. Upload your SSH key to ~/.ssh/"
echo "3. Clone or upload your project"
echo "4. Run: terraform init && terraform apply"
echo ""
