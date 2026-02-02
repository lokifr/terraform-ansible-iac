# Control Node Setup Guide

This guide shows you how to set up an Ubuntu EC2 instance as your Terraform/Ansible control node, eliminating Windows compatibility issues.

## 🎯 Why Use a Control Node?

- ✅ No Windows compatibility issues
- ✅ Native Linux environment for DevOps tools
- ✅ Matches real-world production setups
- ✅ Can be used for multiple projects
- ✅ Easy to share with team members

---

## 📋 Step-by-Step Setup

### **Step 1: Launch Control Node EC2 Instance**

#### Option A: Using AWS Console (Easiest)

1. **Go to EC2 Dashboard** → Click "Launch Instance"

2. **Configure Instance:**
   - **Name:** `terraform-ansible-control-node`
   - **AMI:** Ubuntu Server 22.04 LTS
   - **Instance Type:** `t2.micro` (Free tier eligible)
   - **Key Pair:** Select or create `my-ec2-key`
   - **Network Settings:**
     - Allow SSH (port 22) from "My IP"
   - **Storage:** 8 GB (default is fine)

3. **Click "Launch Instance"**

4. **Wait 1-2 minutes** for instance to start

5. **Get the Public IP** from the EC2 console

#### Option B: Using AWS CLI (Faster)

```bash
# Create security group
aws ec2 create-security-group \
    --group-name control-node-sg \
    --description "Security group for control node"

# Allow SSH from your IP
aws ec2 authorize-security-group-ingress \
    --group-name control-node-sg \
    --protocol tcp \
    --port 22 \
    --cidr YOUR_IP/32

# Launch instance
aws ec2 run-instances \
    --image-id ami-0c7217cdde317cfec \
    --instance-type t2.micro \
    --key-name my-ec2-key \
    --security-groups control-node-sg \
    --tag-specifications 'ResourceType=instance,Tags=[{Key=Name,Value=control-node}]'
```

---

### **Step 2: Connect to Control Node**

```bash
# From Windows PowerShell or Command Prompt
ssh -i C:\Users\Lokesh\.ssh\my-ec2-key.pem ubuntu@<CONTROL_NODE_PUBLIC_IP>
```

---

### **Step 3: Run Setup Script**

Once connected to the control node:

```bash
# Download the setup script
curl -o setup.sh https://raw.githubusercontent.com/YOUR_REPO/control-node-setup.sh

# Or create it manually
nano setup.sh
# Paste the content from control-node-setup.sh

# Make it executable
chmod +x setup.sh

# Run it
./setup.sh
```

**Or run commands directly:**

```bash
# Update system
sudo apt update && sudo apt upgrade -y

# Install prerequisites
sudo apt install -y software-properties-common wget curl unzip git python3-pip vim

# Install Ansible
sudo add-apt-repository --yes --update ppa:ansible/ansible
sudo apt install -y ansible

# Install Terraform
wget https://releases.hashicorp.com/terraform/1.7.0/terraform_1.7.0_linux_amd64.zip
unzip terraform_1.7.0_linux_amd64.zip
sudo mv terraform /usr/local/bin/
rm terraform_1.7.0_linux_amd64.zip

# Install AWS CLI
curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
unzip awscliv2.zip
sudo ./aws/install
rm -rf aws awscliv2.zip

# Verify installations
ansible --version
terraform --version
aws --version
```

---

### **Step 4: Configure AWS Credentials**

```bash
aws configure
```

Enter your:
- AWS Access Key ID
- AWS Secret Access Key
- Default region: `us-east-1`
- Default output format: `json`

---

### **Step 5: Upload Your Project**

#### Option A: Using SCP (from Windows)

```powershell
# From Windows PowerShell
cd d:\projects\terraform_ANsible

# Upload entire project
scp -i C:\Users\Lokesh\.ssh\my-ec2-key.pem -r . ubuntu@<CONTROL_NODE_IP>:~/terraform_ANsible/
```

#### Option B: Using Git (Recommended)

```bash
# On control node
cd ~
git clone https://github.com/YOUR_USERNAME/terraform_ANsible.git
cd terraform_ANsible
```

#### Option C: Manual Upload (Small Files)

```bash
# On control node - create project structure
mkdir -p ~/terraform_ANsible/app
cd ~/terraform_ANsible

# Create files using nano/vim and paste content
nano main.tf
nano variables.tf
nano outputs.tf
nano terraform.tfvars
nano playbook.yml
nano ansible.cfg
nano app/app.py
nano app/requirements.txt
```

---

### **Step 6: Set Up SSH Key for Target Instances**

```bash
# On control node
mkdir -p ~/.ssh
chmod 700 ~/.ssh

# Upload your EC2 key from Windows
# From Windows PowerShell:
scp -i C:\Users\Lokesh\.ssh\my-ec2-key.pem C:\Users\Lokesh\.ssh\my-ec2-key.pem ubuntu@<CONTROL_NODE_IP>:~/.ssh/

# On control node - set permissions
chmod 400 ~/.ssh/my-ec2-key.pem
```

---

### **Step 7: Update Configuration**

```bash
# On control node
cd ~/terraform_ANsible

# Edit terraform.tfvars
nano terraform.tfvars
# Update key_name and my_ip as needed

# Edit ansible.cfg
nano ansible.cfg
# Ensure private_key_file = ~/.ssh/my-ec2-key.pem
```

---

### **Step 8: Deploy Your Infrastructure**

```bash
# Initialize Terraform
terraform init

# Preview changes
terraform plan

# Apply infrastructure
terraform apply
# Type 'yes' when prompted

# Note the outputs (instance IP, etc.)

# Wait 60 seconds for instance to boot
sleep 60

# Deploy application with Ansible
ansible-playbook playbook.yml
```

---

### **Step 9: Access Your Application**

From your Windows browser:
```
http://<TARGET_INSTANCE_PUBLIC_IP>
```

---

## 🧹 Cleanup

### Destroy Target Infrastructure (Keep Control Node)

```bash
# On control node
cd ~/terraform_ANsible
terraform destroy
```

### Destroy Everything (Including Control Node)

```bash
# From Windows or AWS Console
aws ec2 terminate-instances --instance-ids <CONTROL_NODE_INSTANCE_ID>

# Or from AWS Console: EC2 → Instances → Select control node → Instance State → Terminate
```

---

## 💡 Tips & Best Practices

### Keep Control Node Running
- **Cost:** ~$3-4/month for t2.micro
- **Benefit:** Always ready to use, no setup time
- **Alternative:** Stop when not in use (no charges when stopped)

### Stop/Start Control Node

```bash
# Stop (from Windows)
aws ec2 stop-instances --instance-ids <CONTROL_NODE_INSTANCE_ID>

# Start (from Windows)
aws ec2 start-instances --instance-ids <CONTROL_NODE_INSTANCE_ID>

# Note: Public IP will change when restarted
# Use Elastic IP if you want a permanent IP
```

### Use VS Code Remote SSH

1. Install "Remote - SSH" extension in VS Code
2. Connect to control node
3. Edit files directly on the EC2 instance

### Create a Snapshot

```bash
# Create AMI of your configured control node
aws ec2 create-image \
    --instance-id <CONTROL_NODE_INSTANCE_ID> \
    --name "terraform-ansible-control-node-configured" \
    --description "Pre-configured control node with Terraform and Ansible"
```

---

## 🐛 Troubleshooting

**Problem:** Can't SSH to control node
- **Solution:** Check security group allows SSH from your IP

**Problem:** AWS credentials not working
- **Solution:** Run `aws configure` again, verify keys are correct

**Problem:** Terraform/Ansible not found
- **Solution:** Run setup script again, or install manually

**Problem:** Permission denied on SSH key
- **Solution:** `chmod 400 ~/.ssh/my-ec2-key.pem`

---

## 📊 Architecture

```
┌─────────────────────────────────────────────┐
│          Your Windows Machine               │
│                                             │
│  ┌─────────────────────────────────┐       │
│  │  VS Code / Terminal             │       │
│  │  SSH Connection                 │       │
│  └──────────────┬──────────────────┘       │
└─────────────────┼───────────────────────────┘
                  │ SSH
                  ▼
┌─────────────────────────────────────────────┐
│         AWS Cloud                           │
│                                             │
│  ┌──────────────────────────────────────┐  │
│  │  Control Node (Ubuntu EC2)           │  │
│  │  • Terraform                         │  │
│  │  • Ansible                           │  │
│  │  • AWS CLI                           │  │
│  └──────────────┬───────────────────────┘  │
│                 │                           │
│                 │ Terraform Provision       │
│                 │ Ansible Configure         │
│                 ▼                           │
│  ┌──────────────────────────────────────┐  │
│  │  Target Instance (Ubuntu EC2)        │  │
│  │  • Nginx                             │  │
│  │  • Flask App                         │  │
│  │  • Gunicorn                          │  │
│  └──────────────────────────────────────┘  │
│                                             │
└─────────────────────────────────────────────┘
```

---

## ✅ Advantages of This Approach

1. **No Windows Issues** - Everything runs on Linux
2. **Faster Execution** - Better network connectivity within AWS
3. **Real-world Practice** - This is how it's done in production
4. **Portable** - Can be accessed from any device
5. **Team Collaboration** - Multiple people can use the same control node
6. **Cost Effective** - t2.micro is free tier eligible

---

**Ready to start?** Follow Step 1 to launch your control node! 🚀
