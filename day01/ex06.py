
import requests

def get_request():
    r = requests.get('http://51.124.168.159/health.html')
    status = r.status_code
    print("Status: ", end="")
    print(status)

def main():
    get_request()

main()