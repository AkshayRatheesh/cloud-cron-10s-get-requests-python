'''
This is a Python script that runs every 10 seconds and sends HTTP requests to a list of URLs.
It uses the functions framework library to define the cloud function entry point and the requests library to send the requests.
It also uses the multiprocessing library to parallelize the requests and print the status code and the URL for each request.
The cloud function returns the output as a JSON string.

'''



import functions_framework
import multiprocessing
import requests 
import time


@functions_framework.http
def square_sum(x):
    #print(x.get("url"))
    #print(x.get("wait"))      
    
    counter = 0
    while counter < x.get("iterations"):
        response = requests.get(x.get("url"))
        status = f"Status code: {response.status_code}"
        print(status) 
        print(counter,x.get("url"))
        counter += 1
        time.sleep(x.get("wait"))
        
    return "success"

# Define the cloud function entry point
def run_every_10_seconds(request):


    url1 = [
        {
        "url" : "http://0.0.0.0/one",
        "wait":10,
        "iterations": 2
        },
        {
        "url" : "http://1.1.1.1/two",
        "wait":10,
        "iterations" : 4
        }
        ]
    
    pool = multiprocessing.Pool()

    # Map the input list to the function
    results = pool.map(square_sum, url1)

    pool.close()
    pool.join()
    
    print(results)
    # time.sleep(10)

    # Return the output as JSON
    return "output"

