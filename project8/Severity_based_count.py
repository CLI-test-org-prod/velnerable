import json
import requests
import sys
import smtplib
url = 'http://192.168.130.128:8080/api/v2/findings/?tags=&test__tags=BUILD_ID'
headers = {'content-type': 'application/json',
'Authorization': 'Token 2e0eb13f2aed51caf04f270f2c9b32359f321998'}
r = requests.get(url, headers=headers, verify=True) # set verify to False if ssl cert is self-signed
#print (r.json())
#y=json.loads(r.json())

test_txt = r.json()
count_high = 0

count_medium = 0
for i in range(len(test_txt['results'])):
    if (test_txt['results'][i]['found_by']) == [19]:


        if (test_txt['results'][i]['severity'])== 'High':

            count_high+=1

        elif (test_txt['results'][i]['severity'])== 'Medium':

            count_medium+=1

    else:

        # print('there are no high/medium found so pipeline continue' )

        pass

print('High Count is: ', count_high)
print('Medium Count is: ', count_medium)
#Checking

if count_high > 2:
   
    s = smtplib.SMTP('email-smtp.us-east-1.amazonaws.com', 587)
    #s.connect('email-smtp.us-east-1.amazonaws.com', 587)
    s.starttls()
    s.login('AKIAWVM3U6DD6PPTNVVU', 'BAnvfly44m17RnmWbQvT2bq0BCES+tQrjZrGf/Pz5ITI')

    msg = 'From: mukeshit100@gmail.com\nTo: mukeshkumar7@kpmg.com\nSubject:Build No- BUILD_ID\n\n Detect secrets scan tools detect High severity in report please fix as soon as possible'
    s.sendmail('mukeshit100@gmail.com','mukeshkumar7@kpmg.com', msg)

   
    print("more than 2  high severity found so terminated pipeline")
    exit(1)
elif count_medium >2:
    print("more than 2  high severity found so terminated pipeline")
    exit(1)
