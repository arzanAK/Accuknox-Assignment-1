import requests
import logging

logging.basicConfig(filename='application_health.log', level=logging.INFO,format='%(asctime)s - %(levelname)s - %(message)s')

APP_URL = "http://example.com"

def check_application_health(url):
    try:
        response = requests.get(url)
        if response.status_code == 200:
            logging.info(f"Application is UP. Status code:{response.status_code}")
        else:
            logging.error(f"Application is DOWN. Status code:{response.status_code}")
    except requests.exceptions.RequestException as e:
            logging.error(f"Application is DOWN. Error:{e}")
if __name__ == "__main__":
    check_application_health(APP_URL)