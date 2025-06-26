<h1 align="center">☁️AWS-serverless-webapp ☁️</h1>

<p align="center">
  <b>A modern, minimal, 100% serverless web app</b><br>
  Powered by <code>AWS Lambda</code>, <code>API Gateway</code>, and <code>DynamoDB</code>
</p>

<p align="center">
  🚀 Fast • 💡 Scalable • ⚡ Event-driven • 🎯 Zero server maintenance
</p>

---

## ✨ Overview

This project is a cloud-native, serverless web application built to handle real-time form submissions and post operations with the power of AWS.  
It combines frontend form interactions with backend logic and storage — **entirely serverless, infinitely scalable.**

---

## 🗂 Project Structure

<pre>
  trivickram-aws-serverless-webapp/
├── Amazon API Gateway/
│ ├── GetMethod
│ └── PostMethod
├── DynamoDB/
│ └── results.csv
└── Lambda/
├── DELETE-post
├── GET-post
├── submitpost
└── Form-Submission/
├── Contact.html
├── lambga_function.py
└── success.html
</pre>


### 📦 Modules Explained

| Module | Description |
|--------|-------------|
| `Amazon API Gateway/` | Defines GET and POST methods, acting as the REST API layer for Lambda. |
| `Lambda/` | Contains serverless functions for submitting, retrieving, and deleting data. |
| `Form-Submission/` | Frontend HTML form and Lambda function that handles submissions. |
| `DynamoDB/results.csv` | Local backup/export of stored entries from DynamoDB. |

---

## 🔄 Workflow

1. **User submits the form** (`Contact.html`)
2. **API Gateway POST method** triggers `submitpost` Lambda
3. **Lambda function** writes the data into `DynamoDB`
4. **GET/DELETE methods** allow data retrieval and deletion via API endpoints
5. **Success page** is shown after a successful form submission

---

## 🛡️ AWS Services Used

- **Amazon API Gateway** – For routing HTTP requests to Lambda
- **AWS Lambda** – For running code without provisioning servers
- **Amazon DynamoDB** – NoSQL database for storing form data
- **Amazon IAM** – To manage permissions securely

---

## 📷 Screenshots 


---

## 📌 Deployment Notes

This project is deployed using the AWS Console. To deploy manually:

1. Upload the Lambda zip packages or use the inline editor
2. Set up API Gateway methods (GET, POST, DELETE)
3. Link each method to corresponding Lambda function
4. Enable CORS if integrating with a frontend
5. Create a DynamoDB table (e.g., `Posts`) with appropriate keys

---

## 🧠 Future Enhancements

- Add **authentication** using Cognito
- Automate deployment with **AWS SAM** or **CDK**
- Connect to **SES** for email notifications
- Use **S3** to host frontend pages

---

## 🙋‍♂️ Author

**Trivickram Baratam**  
_ML Enthusiast | Web Developer | Cloud Advocate_  
[GitHub](https://github.com/trivickram) • [LinkedIn](https://linkedin.com/in/trivickram)

---


