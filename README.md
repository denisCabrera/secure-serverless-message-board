# 🛡️ Secure Serverless Message Board (AWS)

This is a secure, serverless message board built using AWS Lambda, API Gateway, DynamoDB, WAF, GuardDuty, CloudTrail, and other AWS services. The project follows security best practices and is designed as a portfolio project to demonstrate cloud architecture, infrastructure security, and monitoring.

---

## 🚀 Project Features

- 🔐 **IAM least privilege** roles for Lambda functions
- 🧾 **Secrets Manager** for securely handling sensitive data
- 🌐 **API Gateway** endpoints secured with **WAF**
- 🛡️ **GuardDuty** enabled for threat detection
- 🕵️ **CloudTrail** logging for all API and resource events
- 📊 **CloudWatch** monitoring and alarms for function errors

---

## 📸 Screenshots

| Feature | Screenshot |
|--------|------------|
| DynamoDB Table | ![](screenshots/dynamodb-table.png) |
| IAM Role for Lambda | ![](screenshots/iam-role.png) |
| Lambda Function | ![](screenshots/lambda-function.png) |
| API Gateway Setup | ![](screenshots/api-gateway.png) |
| AWS WAF Rules | ![](screenshots/waf-rules.png) |
| GuardDuty Finding | ![](screenshots/guardduty-finding.png) |
| CloudWatch Alarm | ![](screenshots/cloudwatch-alarm.png) |

---

## 🧱 Architecture

![Architecture Diagram](architecture/diagram.png)

---

## 🛠️ Stack

| Service | Purpose |
|--------|---------|
| Lambda | Serverless backend (create/read messages) |
| DynamoDB | NoSQL database for messages |
| API Gateway | REST endpoints for Lambda integration |
| IAM | Role-based access and least privilege policies |
| WAF | Protects against XSS, SQLi, bad inputs |
| CloudWatch | Logging and alarms |
| CloudTrail | Audit logging |
| GuardDuty | Threat detection |
| Secrets Manager | Securing mock secrets (passwords) |

---

## 🧪 How to Test

### Submit a Message

```bash
curl -X POST https://<api-id>.execute-api.<region>.amazonaws.com/prod/messages \
-H "Content-Type: application/json" \
-d '{"message": "Hello secure world!"}'
