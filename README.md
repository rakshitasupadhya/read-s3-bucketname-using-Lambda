# read-s3-bucketname-using-Lambda
Simple demonstratiion on reading the s3 buckets using Lambda function.

# Requirements 
This sample project depends on boto3, the AWS SDK for Python, and requires Python 2.6.5+, 2.7, 3.3, 3.4, or 3.5. You can install boto3 using pip:

pip install boto3

# Project highlights

1. Create s3 buckets
2. Create a lambda function
3. Add Role to lambda to allow read the buckets
•	Go to Configurations --> Permissions --> click on Role name 
•	Click on add permissions , search for s3ReadOnlyAccess and select & Save it
4. Write python code in Lambda to read the bucket
•	Click on deploy , add configuration test event and click on test


