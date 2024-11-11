# Python AWS Infrastructure Automation

## Project Overview

This project leverages the AWS Cloud Development Kit (CDK) to automate the deployment and management of AWS infrastructure, following Infrastructure as Code (IaC) principles. The project name highlights the use of Python to generate AWS CloudFormation templates, offering a Python-based IaC solution for resource provisioning. The infrastructure is designed to be scalable, secure, and highly available.

## Features

"Python AWS Infrastructure Automation" project sets up a comprehensive AWS environment for hosting a Python web application. Upon user request, the application returns data from the database about the population of countries by year. The infrastructure includes:

- Custom VPC with public, private, and isolated subnets
- Amazon RDS Aurora MySQL cluster
- Two EC2 instances running Amazon Linux 2
- Application Load Balancer
- Security groups for network access control
- IAM roles for EC2 instance permissions

## Architecture diagram
![vpc-infra](https://github.com/user-attachments/assets/b07718f2-7b70-40ac-ab5d-f8f7276ac29c)

## Key Components

### VPC

A custom VPC with a CIDR block of 10.10.0.0/16, including a NAT gateway for outbound internet access from private subnets.

### Database

An Amazon Aurora MySQL cluster in the isolated subnet for enhanced security.

### Web Server

An EC2 instance running in a private subnet with egress access.

### Load Balancer

An internet-facing Application Load Balancer to handle incoming traffic.

### Security

Security groups configured to control inbound and outbound traffic for each component.

## Security Considerations

- Database in an isolated subnet, not directly accessible from the internet.
- Web server in a private subnet, accessed via the load balancer.
- Security groups configured to allow only necessary traffic between components.

## Customization

The infrastructure can be customized by modifying the CDK stack definition, including instance types, security group rules, and database configuration.

## Project Structure

- `app.py`: Entry point for the CDK application
- `cdk.json`: CDK application configuration and context
- `requirements.txt`: Python dependencies
- `/cdkapp`: Directory containing CDK stack definitions

## Configuration

The `cdk.json` file includes various configuration options and feature flags for AWS services. These can be adjusted based on specific project requirements.


## Deployment Process

The infrastructure is defined as Python code using AWS CDK, allowing for version-controlled, repeatable deployments. The Python web application will be deployed to the EC2 instances.

## Deployment Steps

To deploy the infrastructure:

```sh
cdk deploy
```

To destroy the created resources:

```sh
cdk destroy --all
```
## Results

### Resources created via VS Code

![vsc-resources-created](https://github.com/user-attachments/assets/0a70be56-b3b6-48b1-a88a-6ed0ed510d72)

### Resources created at VS AWS

![resorces-created](https://github.com/user-attachments/assets/c785f2e7-614a-474d-81c2-2dfa30fb7cd9)

### Register targets for Load Balancer

![register-targets-helthy](https://github.com/user-attachments/assets/861a4a29-3d22-4286-b586-ab154ba9868a)

### Deployed application with sample user request in Availability Zone 1

![az1](https://github.com/user-attachments/assets/beaac857-322a-43ff-a1c7-a3ab7201e237)

### The application returned data from the database. Example for Availability Zone 2.

![az2-response](https://github.com/user-attachments/assets/9cfb984e-1ee2-4ec8-ab4c-1184df72db71)


## Conclusion

This project showcases best practices for deploying AWS infrastructure using Python automation, emphasizing Infrastructure as Code (IaC) principles. It highlights security, scalability, and automation in provisioning resources for a Python web application.

