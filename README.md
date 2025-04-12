# Secure Serverless Message Board

This project demonstrates a secure, serverless web app on AWS with layered security.

## Overview

- **Frontend/API:** API Gateway + Lambda
- **Database:** DynamoDB
- **Security Layers:** WAF, IAM, GuardDuty, CloudTrail, Secrets Manager
- **Logging & Monitoring:** CloudWatch

## Features

- Submit and retrieve messages via REST API
- AWS WAF blocks common threats (XSS, SQLi)
- Fine-grained IAM permissions
- All activity logged via CloudTrail
- Threat detection via GuardDuty

## Technologies

| Layer           | Service Used                         |
|----------------|---------------------------------------|
| API            | API Gateway                          |
| Backend        | AWS Lambda (Node.js)                 |
| Database       | DynamoDB                             |
| Security       | WAF, IAM, GuardDuty, Secrets Manager |
| Monitoring     | CloudWatch, CloudTrail               |

## Architecture

![Architecture](architecture/architecture-diagram.png)

## 📂 Folder Structure

| Folder        | Description                            |
|---------------|----------------------------------------|
| `lambda/`     | Lambda function code                   |
| `iam/`        | IAM policy for Lambda                  |
| `waf/`        | WAF WebACL setup                       |
| `images/`     | Screenshots of demo, WAF logs          |
| `cloudtrail/` | (Optional) Sample logs                 |
| `guardduty/`  | (Optional) Simulated findings          |

## Screenshots

### ✅ Clean request (stored):
![Secure POST](images/test_POST.png)

### ❌ XSS attack (blocked):
![Blocked XSS](images/Simulate_XSS.png)

### 🔒 WAF Log:
![WAF Log](images/XSS_waflog.png)
