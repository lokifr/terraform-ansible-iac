# Infrastructure as Code Web Application

## 🎯 Project Overview

A complete Infrastructure as Code (IaC) demonstration project that uses **Terraform** for infrastructure provisioning and **Ansible** for configuration management to deploy a Flask web application on AWS.

---

## 🏗️ Architecture

```
┌─────────────────────────────────────────────────────────┐
│                      AWS Cloud (Ohio)                    │
│                                                          │
│  ┌────────────────────────────────────────────────┐    │
│  │         Custom VPC (10.0.0.0/16)               │    │
│  │                                                 │    │
│  │  ┌──────────────────────────────────────┐     │    │
│  │  │   Public Subnet (10.0.1.0/24)        │     │    │
│  │  │                                       │     │    │
│  │  │   ┌─────────────────────────┐        │     │    │
│  │  │   │   EC2 Instance          │        │     │    │
│  │  │   │   (Ubuntu 22.04)        │        │     │    │
│  │  │   │                         │        │     │    │
│  │  │   │  ┌──────────────────┐  │        │     │    │
│  │  │   │  │  Nginx (Port 80) │  │        │     │    │
│  │  │   │  └────────┬─────────┘  │        │     │    │
│  │  │   │           │             │        │     │    │
│  │  │   │  ┌────────▼─────────┐  │        │     │    │
│  │  │   │  │ Flask + Gunicorn │  │        │     │    │
│  │  │   │  │   (Port 5000)    │  │        │     │    │
│  │  │   │  └──────────────────┘  │        │     │    │
│  │  │   └─────────────────────────┘        │     │    │
│  │  │                                       │     │    │
│  │  └──────────────────────────────────────┘     │    │
│  │                                                 │    │
│  │  Security Group:                               │    │
│  │  • SSH (22) - Controlled Access                │    │
│  │  • HTTP (80) - Public Access                   │    │
│  │  • HTTPS (443) - Public Access                 │    │
│  │                                                 │    │
│  └────────────────────────────────────────────────┘    │
│                                                          │
└─────────────────────────────────────────────────────────┘
```

---

## 🚀 Technologies Used

### **Infrastructure & DevOps**
- **Terraform** (v1.7.0) - Infrastructure provisioning
- **Ansible** (v2.x) - Configuration management
- **AWS EC2** - Compute instances
- **AWS VPC** - Network isolation

### **Application Stack**
- **Python Flask** - Web framework
- **Gunicorn** - WSGI HTTP server
- **Nginx** - Reverse proxy and web server
- **Ubuntu 22.04 LTS** - Operating system

---

## 📋 What This Project Demonstrates

### **1. Infrastructure as Code (IaC)**
- Declarative infrastructure definition using Terraform
- Version-controlled infrastructure
- Reproducible deployments
- Automated resource provisioning

### **2. Configuration Management**
- Automated server configuration with Ansible
- Idempotent playbooks
- Service orchestration
- Application deployment automation

### **3. Cloud Computing**
- AWS VPC networking
- EC2 instance management
- Security group configuration
- Internet gateway setup

### **4. Web Application Architecture**
- Reverse proxy pattern (Nginx → Gunicorn)
- WSGI application server
- RESTful API endpoints
- Systemd service management

---

## 🎯 Key Features

✅ **Fully Automated Deployment** - Single command infrastructure creation  
✅ **Custom VPC** - Isolated network with public subnet  
✅ **Security Groups** - Properly configured firewall rules  
✅ **Web Application** - Flask app with health check endpoints  
✅ **Production-Ready** - Nginx reverse proxy with Gunicorn  
✅ **Auto-Start Services** - Systemd integration for reliability  
✅ **Clean Teardown** - Complete infrastructure destruction with one command  

---

## 📁 Project Structure

```
terraform_ANsible/
├── main.tf                 # Terraform main configuration
├── variables.tf            # Variable definitions
├── outputs.tf              # Output definitions
├── terraform.tfvars        # Variable values
├── ansible.cfg             # Ansible configuration
├── playbook.yml            # Ansible playbook
├── app/
│   ├── app.py             # Flask application
│   └── requirements.txt   # Python dependencies
├── README.md              # Setup and usage guide
└── PROJECT_SUMMARY.md     # This file
```

---

## 🔧 Infrastructure Components

### **Terraform Resources Created**
1. **VPC** - Custom virtual private cloud (10.0.0.0/16)
2. **Subnet** - Public subnet (10.0.1.0/24)
3. **Internet Gateway** - Internet connectivity
4. **Route Table** - Network routing configuration
5. **Security Group** - Firewall rules (SSH, HTTP, HTTPS)
6. **EC2 Instance** - Ubuntu 22.04 t2.micro instance
7. **Inventory File** - Auto-generated for Ansible

### **Ansible Tasks Executed**
1. System package updates
2. Python, pip, and Nginx installation
3. Application directory creation
4. Flask app deployment
5. Gunicorn systemd service configuration
6. Nginx reverse proxy setup
7. Service startup and enablement

---

## 🌐 Application Endpoints

### **Home Page**
- **URL:** `http://<instance-ip>/`
- **Description:** Landing page with project information
- **Features:** Gradient UI, tech stack display

### **Health Check**
- **URL:** `http://<instance-ip>/health`
- **Response:** JSON with status, timestamp, service name
- **Use Case:** Monitoring and load balancer health checks

### **System Info**
- **URL:** `http://<instance-ip>/info`
- **Response:** JSON with hostname, platform, Python version
- **Use Case:** Debugging and system verification

---

## 📊 Deployment Workflow

### **Phase 1: Infrastructure Provisioning (Terraform)**
```bash
terraform init      # Initialize Terraform
terraform plan      # Preview changes
terraform apply     # Create infrastructure
```

**Output:** VPC, subnet, security group, EC2 instance, inventory file

### **Phase 2: Application Deployment (Ansible)**
```bash
ansible-playbook playbook.yml
```

**Output:** Configured server with running Flask application

### **Phase 3: Verification**
- Access web application via public IP
- Test health check endpoint
- Verify system info endpoint

### **Phase 4: Cleanup**
```bash
terraform destroy   # Remove all infrastructure
```

---

## 🎓 Learning Outcomes

### **Skills Demonstrated**
- ✅ Infrastructure as Code principles
- ✅ Cloud resource provisioning
- ✅ Configuration management automation
- ✅ Network architecture design
- ✅ Security best practices
- ✅ Web application deployment
- ✅ Linux system administration
- ✅ DevOps tooling integration

### **AWS Services Used**
- EC2 (Elastic Compute Cloud)
- VPC (Virtual Private Cloud)
- Security Groups
- Internet Gateway
- Route Tables

### **DevOps Practices**
- Infrastructure as Code
- Configuration Management
- Automation
- Version Control
- Declarative Configuration

---

## 🔒 Security Considerations

### **Implemented**
- ✅ Custom VPC for network isolation
- ✅ Security groups with minimal required ports
- ✅ SSH key-based authentication
- ✅ No hardcoded credentials
- ✅ Separate control and target instances

### **Production Recommendations**
- Use AWS Secrets Manager for credentials
- Implement HTTPS with SSL/TLS certificates
- Enable CloudWatch monitoring
- Set up Auto Scaling groups
- Use Application Load Balancer
- Implement backup strategies
- Enable VPC Flow Logs

---

## 💰 Cost Optimization

### **Free Tier Eligible**
- t2.micro instances (750 hours/month)
- VPC and networking (no charge)
- Data transfer (within limits)

### **Cost Saving Tips**
- Stop instances when not in use
- Use `terraform destroy` after testing
- Monitor AWS billing dashboard
- Set up billing alerts

---

## 🐛 Troubleshooting Guide

### **Common Issues**

**Issue:** Terraform can't find AMI  
**Solution:** Ensure IAM user has `ec2:DescribeImages` permission

**Issue:** Ansible connection timeout  
**Solution:** Wait 60 seconds for instance to fully boot

**Issue:** Website not accessible  
**Solution:** Check security group allows HTTP (port 80)

**Issue:** Key pair not found  
**Solution:** Ensure key pair exists in the correct AWS region

---

## 📈 Future Enhancements

### **Potential Improvements**
- [ ] Add HTTPS support with Let's Encrypt
- [ ] Implement CI/CD pipeline
- [ ] Add database tier (RDS)
- [ ] Set up CloudWatch monitoring
- [ ] Implement Auto Scaling
- [ ] Add Application Load Balancer
- [ ] Use Terraform modules for reusability
- [ ] Add automated testing
- [ ] Implement blue-green deployment
- [ ] Add container support (Docker)

---

## 📝 Project Timeline

1. **Planning** - Architecture design and tool selection
2. **Terraform Development** - Infrastructure code creation
3. **Ansible Development** - Playbook and configuration
4. **Application Development** - Flask web app
5. **Testing** - Deployment and verification
6. **Documentation** - README and guides
7. **Cleanup** - Resource teardown

---

## 🏆 Project Highlights

### **Why This Project Stands Out**
- ✅ **End-to-End Automation** - Complete infrastructure and application deployment
- ✅ **Production Patterns** - Uses industry-standard tools and practices
- ✅ **Well Documented** - Comprehensive README and comments
- ✅ **Reproducible** - Can be deployed in any AWS region
- ✅ **Clean Code** - Organized structure and best practices
- ✅ **Real-World Application** - Demonstrates practical DevOps skills

---

## 📚 Resources & References

### **Official Documentation**
- [Terraform AWS Provider](https://registry.terraform.io/providers/hashicorp/aws/latest/docs)
- [Ansible Documentation](https://docs.ansible.com/)
- [Flask Documentation](https://flask.palletsprojects.com/)
- [AWS VPC Guide](https://docs.aws.amazon.com/vpc/)

### **Related Technologies**
- Gunicorn WSGI Server
- Nginx Web Server
- Ubuntu Server
- Python 3

---

## 👤 Author

**Project Type:** Learning & Portfolio Project  
**Purpose:** Demonstrate Infrastructure as Code and DevOps skills  
**Technologies:** Terraform, Ansible, AWS, Python, Flask, Nginx  

---

## 📄 License

This project is open source and available for educational purposes.

---

**Built with ❤️ using Infrastructure as Code principles**

*Last Updated: February 2026*
