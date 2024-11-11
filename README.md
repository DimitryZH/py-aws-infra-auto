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

## Key Components:

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

## Configuration

The `cdk.json` file includes various configuration options and feature flags for AWS services. These can be adjusted based on specific project requirements.

## Conclusion

This project showcases best practices for deploying a Python web application on AWS, emphasizing security, scalability, and automation.
