# Python AWS Infrastructure Automation

## Project Overview

This project demonstrates an automated infrastructure deployment for a Python web application using AWS CDK (Cloud Development Kit). The infrastructure is designed to be scalable, secure, and highly available.

## Feachures

The project sets up a comprehensive AWS environment for hosting a Python web application. It includes:

- A custom VPC with public, private, and isolated subnets
- An Amazon RDS Aurora MySQL cluster for database operations
- An EC2 instance running Amazon Linux 2 for the web server
- An Application Load Balancer for distributing incoming traffic
- Security groups to control network access
- IAM roles for EC2 instance permissions

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

Carefully configured security groups to control inbound and outbound traffic for each component.

## Deployment Process

The infrastructure is defined as code using AWS CDK, allowing for version-controlled, repeatable deployments. The Python web application will be deployed to the EC2 instance.

## Security Considerations

- The database is placed in an isolated subnet, not directly accessible from the internet.
- The web server is in a private subnet, accessed via the load balancer.
- Security groups are configured to allow only necessary traffic between components.

## Customization

The infrastructure can be easily customized by modifying the CDK stack definition. This includes changing instance types, adjusting security group rules, or modifying the database configuration.

## Conclusion

This project showcases best practices for deploying a Python web application on AWS, emphasizing security, scalability, and automation. It serves as an excellent starting point for developers looking to set up a robust AWS infrastructure for their Python applications.
