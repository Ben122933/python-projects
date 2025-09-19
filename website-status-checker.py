import requests
from requests import Response, RequestException
from requests.structures import CaseInsensitiveDict
#Get url
url_to_check = 'https://' + input('Enter a url to check: https:// ')

def check_status(url: str) -> None:

    try:

        response: Response = requests.get(url)

        #Information
        status_code: int = response.status_code
        headers: CaseInsensitiveDict[str] = response.headers
        content_type: str = headers.get('Content-Type', 'Unknown')
        server: str = headers.get('Server', 'Unknown')
        response_time: float = response.elapsed.total_seconds()

        print(f'URL: {url}')
        print(f'Status Code: {status_code}')
        print(f'Content-Type: {content_type}')
        print(f'Server: {server}')
        print(f'Response Time: {response_time}')

    except RequestException as e:
        print(f'Error: {e}')


def main() -> None:
    check_status(url = url_to_check)

if __name__ == '__main__':
    main()
