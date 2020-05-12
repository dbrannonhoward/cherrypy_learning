import requests

request_session = requests.Session()
local_url = 'http://127.0.0.1:8080/'


def print_send_status_of(http_type):
    print(" > > Sending " + str(http_type) + " request to " + str(local_url))


def print_return_code_and_text_if_200(session_return):
    print(" < < The return code is " + str(session_return.status_code))
    if session_return.status_code == 200:
        print(" < < The return text is " + str(session_return.text))


print_send_status_of("GET")
http_return = request_session.get(local_url)
print_return_code_and_text_if_200(http_return)
print("This code is returned because we haven't generated a string through POST")

# POST
print_send_status_of("POST")
http_return = request_session.post(local_url)
print_return_code_and_text_if_200(http_return)

# GET
http_return = request_session.get(local_url)
print_send_status_of("GET")
print_return_code_and_text_if_200(http_return)

# GET with headers
print_send_status_of("GET")
http_return = request_session.get(local_url, headers={'Accept': 'application/json'})
print_return_code_and_text_if_200(http_return)

# PUT with headers
print_send_status_of("PUT")
http_return = request_session.put(local_url, params={'another_string': 'hello'})
http_return = request_session.get(local_url)
print_return_code_and_text_if_200(http_return)

# POP
print_send_status_of("DELETE")
http_return = request_session.delete(local_url)
http_return = request_session.get(local_url)
print_return_code_and_text_if_200(http_return)
