# aws-serverless-data-pipeline
# 🚀 Serverless Data Lake ETL Pipeline on AWS

This project demonstrates an end-to-end serverless data engineering pipeline built using Amazon Web Services (AWS).

---

## 🏗 Architecture

![architecture/architecture.png.png]

This architecture follows a fully serverless pattern:

Raw Data (S3) → AWS Lambda (ETL) → Processed Data (S3) → Amazon Athena (SQL Analytics)

---

## 🎥 Project Demo (60 Seconds Walkthrough)

Recruiters & reviewers:

👉 **Click below to watch the live demo of the working pipeline**

[▶ WhatsApp Video 2026-03-01 at 00.35.01.mp4]

The video shows:
- Raw data stored in S3
- Lambda transformation execution
- Processed output generation
- SQL queries in Athena

---

## ⚙️ Services Used

- Amazon S3 – Data lake storage
- AWS Lambda – Serverless ETL processing
- IAM – Secure access control
- Amazon Athena – SQL queries directly on S3
- CloudWatch – Monitoring & logs

---

## 🔄 ETL Logic

The Lambda function performs:

- Filtering high-revenue transactions
- Data type conversion
- Writing cleaned dataset to curated S3 bucket

---

## 📂 Repository Structure
aws-serverless-data-pipeline/
│
├── lambda/
├── sample_data/
├── output_sample/
├── architecture
├── WhatsApp Video 2026-03-01 at 00.35.01.mp4
└── README.md


---

## 🧠 What I Learned

- Designing a serverless data architecture
- Configuring IAM roles correctly
- Debugging Lambda with CloudWatch
- Creating external tables in Athena
- Querying S3 data using SQL without managing servers

---

## 💡 Key Takeaway

Built a cost-efficient, fully serverless data pipeline that demonstrates modern cloud-native data engineering principles.
