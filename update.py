import json
import requests, urllib, time, random
import subprocess
 
# the following 4 are the actual values that pertain to your account and this specific metric
api_key = subprocess.check_output(['pass', 'statuspage/mmoda']).decode().strip()
page_id = '8jwgp02737qw'
metric_id = 'k16sfpwgd9ks'
api_base = 'api.statuspage.io'
 
# need 1 data point every 5 minutes
# submit random data for the whole day

while True:
  ts = time.time()
  requests.get('https://www.astro.unige.ch/mmoda')
  value = time.time() - ts

  params = {'timestamp': ts, 'value': value}
  headers = {"Content-Type": "application/json", "Authorization": "OAuth " + api_key}
 
  response = requests.post("https://" + api_base + "/v1/pages/" + page_id + "/metrics/" + metric_id + "/data.json", 
                           data=json.dumps({'data': params}), headers=headers)
 
  if (response.status_code >= 500):
    genericError = "Error encountered. Please ensure that your page code and authorization key are correct."
    print(genericError)
    break
  else:
    print("Submitted point")
    print(response.text)
    time.sleep(1)
  
