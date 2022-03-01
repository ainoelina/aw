
import requests

def get_request():
    r = requests.get('http://51.124.168.159/health.html')
    print("Status: ", end="")
    print(r.status_code)

def main():
    get_request()

main()