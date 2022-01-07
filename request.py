import requests

url = 'http://localhost:5000/results'
r = requests.post(url,json={'rate':4, 'sales_in_first_month':300, 'sales_in_second_month':500})

print(r.json())