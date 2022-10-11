import os
import requests

#url = "http://127.0.0.1:8000/process-video"
url = "http://10.5.20.179:8000/health"
#videopath = os.getcwd() + '\\..\\TestVid\\testvid.mp4'

#files=[('file',('testvid.mp4',open(videopath,'rb'),'application/octet-stream'))]

# response = requests.request("POST", url, headers={}, data={}, files=files)
response = requests.request("GET", url, headers={}, data={})

print(response.text)

#file1 = open("object.csv","w")
#res = response.text.split('\r')
#for temp in res:
#    file1.writelines(temp)
#file1.close()