import requests
from requests.exceptions import HTTPError

def get_response(url, parameters=None):
    response = requests.get(url, params=parameters)
    status_code = response.status_code
    print(response)
    print(status_code)
    if response:
        print("success!")
    else:
        print("An error occurred")
    
    try:
        response.raise_for_status
    except HTTPError as http_error:
        print(f"HTTP error occurred:{http_error}")
    except Exception as err:
        print(f"Other error occurred: {err}")
    else:
        return response

def get_content(url, parameters=None, limit=None):
    response = requests.get(url, params=parameters)
    #content = response.content
    #text = response.text
    # hedaer = response.header
    json_result = response.json()
    i=0
    for key, value in json_result.items():
        print(f"{key} : {value}")
        i+=1
        if limit and i==limit:
            break
    return json_result




if __name__ == "__main__":
    url = 'https://api.github.com'
    url_invalid = "https://api.github.com/invalid"
    get_response(url)
    get_response(url_invalid)
    #get content
    get_content(url, None, 1)
    # parameters
    json = get_content("https://api.github.com/search/repositories",
                    {"q":"requests+language:python"},1)
    repo = json['items'][0]
    print(f"repo name: {repo['name']}")
    print(f"repo description: {repo['description']}")



