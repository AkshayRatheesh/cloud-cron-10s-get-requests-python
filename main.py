import functions_framework
import requests #requests==2.30.0
import time

url1 = "http://0.0.0.0:7001/check"
iterations = 6
# 6*10 = 1 minutes

@functions_framework.http
def http_request():
    response = requests.get(url1)
    status1 = f"Status code: {response.status_code}"
    return status1#'  {}!'.format(status1 , status2)


def run_every_10_seconds(request):
    count = 0
    while count < iterations:
        status1 = http_request()
        count += 1
        time.sleep(30)
        print(status1)
    return '  {}!'.format(status1)
