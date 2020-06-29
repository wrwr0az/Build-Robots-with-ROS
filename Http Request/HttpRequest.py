import requests 
import webbrowser


url = 'https://s-m.com.sa/tr/login.html' 
response = requests.get(url)        # To execute get request 
#print(response.status_code)     # To print http response code  

print(response.text)            # To print formatted JSON response 

