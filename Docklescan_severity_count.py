import json
import requests
import sys
url = 'http://192.168.130.128:8080/api/v2/findings/?tags=&test__tags=BUILD_ID'
headers = {'content-type': 'application/json',
'Authorization': 'Token 2e0eb13f2aed51caf04f270f2c9b32359f321998'}
r = requests.get(url, headers=headers, verify=True) # set verify to False if ssl cert is self-signed
#print (r.json())
#y=json.loads(r.json())

test_txt = r.json()
count_high = 0
count_low = 0
count_medium = 0

for i in range(len(test_txt['results'])):
    if (test_txt['results'][i]['found_by']) == [73]:


        if (test_txt['results'][i]['severity'])== 'High':

            count_high+=1

        elif (test_txt['results'][i]['severity'])== 'Medium':

            count_medium+=1
        elif (test_txt['results'][i]['severity'])== 'Low':
            count_low+=1        
    else:

        # print('there are no high/medium found so pipeline continue' )

        pass

print('High Count is: ', count_high)
print('Medium Count is: ', count_medium)
print('Low Count is: ', count_low)

if count_high > 2:
    
    print("more than 2  high severity found so terminated pipeline")
    #exit(1)
elif count_medium > 1:
    print("more than 1  medium severity found so terminated pipeline")
    exit(1)
elif count_low > 3:
    print("more than 3  Low severity found so terminated pipeline")
    exit(1)
