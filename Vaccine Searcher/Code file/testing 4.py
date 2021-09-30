# import hashlib
# str = "216367"
# result = hashlib.sha256(str.encode())
# print("The hexadecimal equivalent of SHA256 is : ")
# print(result.hexdigest())
#

import requests
dist=375
date='29-09-2021'
URL = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/findByDistrict?district_id={}&date={}'.format(
    dist, date)
response = requests.get(URL)
print(response)

response_json = response.json()
print(response_json)

data = response_json["sessions"]
print(data)

for each in data:
  print(each)

# response = {"sessions":[{"center_id":101010,"name":"solapur"},{"center_id":1701010,"name":"solapur1"}]}
#
# response_json=response.json()
#
# data = response_json["sessions"]
#
# for each in data:
#    print(each)