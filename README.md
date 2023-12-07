# How to run cron jobs every 10 seconds with Python, Cloud Functions, & Cloud Scheduler
AWS, GCP, Azure, Lambda function, Cloud function, Azure function, Cloud Scheduler, EventBridge


This project demonstrates a Cloud Function that uses a Cloud Scheduler to trigger an execution every minute. Once triggered, the Cloud Function sends GET request every 10 second


Functionality
The Cloud Function performs the following actions every 10 seconds:

Sends a GET request to a specified URL.
Processes the response (optional).
Logs the results (optional).

Note: You will need to modify the source code to specify the URL for the GET request and implement any desired processing and logging.

Resources
Cloud Functions Docs: https://cloud.google.com/functions/docs
Cloud Scheduler Docs: https://cloud.google.com/scheduler/docs

Contributing
Contributions are welcome! Please feel free to fork the repository and create pull requests with your improvements.
