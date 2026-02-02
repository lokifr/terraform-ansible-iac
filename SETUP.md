# Quick Setup Guide

## 🚀 Getting Started

### Prerequisites
- AWS Account with appropriate permissions
- Terraform (>= 1.0)
- Ansible (>= 2.9)
- AWS CLI configured
- SSH key pair in AWS

### Setup Steps

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd terraform_ANsible
   ```

2. **Configure variables**
   ```bash
   cp terraform.tfvars.example terraform.tfvars
   nano terraform.tfvars
   ```
   
   Update:
   - `key_name` - Your AWS EC2 key pair name
   - `my_ip` - Your public IP (optional, for better security)
   - `aws_region` - Your preferred AWS region

3. **Update Ansible config**
   ```bash
   nano ansible.cfg
   ```
   
   Update `private_key_file` path to your SSH key location.

4. **Deploy infrastructure**
   ```bash
   terraform init
   terraform apply
   ```

5. **Wait for instance to boot** (60 seconds)
   ```bash
   sleep 60
   ```

6. **Deploy application**
   ```bash
   ansible-playbook playbook.yml
   ```

7. **Access your application**
   ```
   http://<instance_public_ip>
   ```
   
   Get the IP from: `terraform output instance_public_ip`

### Cleanup

```bash
terraform destroy
```

---

For detailed instructions, see [README.md](README.md)
