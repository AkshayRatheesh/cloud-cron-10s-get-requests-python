# How to run cron jobs every 10 seconds with Python, Cloud Functions, & Cloud Scheduler




This project demonstrates a Cloud Function that uses a Cloud Scheduler to trigger an execution every minute. Once triggered, the Cloud Function sends GET request every 10 second








AWS, GCP, Azure, Lambda function, Cloud function, Azure function, Cloud Scheduler, EventBridge


## Note

You will need to modify the source code to specify the URL for the GET request and implement any desired processing and logging.

## Functionality
The Cloud Function performs the following actions every 10 seconds:

- Sends a GET request to a specified `URL`.
- Processes the response (optional).
- Logs the results (optional).





## Resources

 - [Cloud Functions Docs](https://cloud.google.com/functions/docs)
 - [Cloud Scheduler Docs]( https://cloud.google.com/scheduler/docs)



 

## Contributing

Contributions are always welcome!

Please feel free to fork the repository and create pull requests with your improvements.


##  parallelize the requests (python multiprocessing)

This is a Python script that runs every 10 seconds and sends HTTP requests to a list of URLs.
It uses the functions framework library to define the cloud function entry point and the requests library to send the requests.
It also uses the multiprocessing library to parallelize the requests and print the status code and the URL for each request.
The cloud function returns the output as a JSON string.


