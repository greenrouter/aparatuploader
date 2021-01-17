import hashlib 
import requests
import codecs
import json
import filetype



print("Enter your aparat username:")

usernameaparat=input()


print("Enter your password:")

passwordaparat=input()


print("Enter your video path:")

fileadd=input()


print("Enter Title for video:")

titlevideo=input()


print("Enter description for video:")

description=input()

print("Enter category ID video: like this link https://www.aparat.com/etc/api/categories")

cat=input()

print("Enter tag for video:")

taged=input()



mdf5 = hashlib.md5()
sha1 = hashlib.sha1()
mdf5.update(passwordaparat.encode('utf-8'))
sha1.update(mdf5.hexdigest().encode('utf-8'))
hashedValue = sha1.hexdigest()


req="https://www.aparat.com/etc/api/login/luser/"+usernameaparat+"/lpass/"+hashedValue


x = requests.get(req)


jss=json.loads(x.content)
print(jss)
token=jss['login']['ltoken']


reqtoken="https://www.aparat.com/etc/api/upload​form/luser/"+usernameaparat+"/ltoken/"+token

reqtokenrespo = requests.get(reqtoken)

jssreqtokenrespo=json.loads(reqtokenrespo.content)
print(jssreqtokenrespo)



addvideo = open(fileadd, "rb")

kind = filetype.guess(fileadd)

filesvid = {'video': ('video.mp4', addvideo, kind.mime)}

print(kind.mime)


values = {'frm-id':jssreqtokenrespo['uploadform']['frm-id'] , 'data[title]': titlevideo,'data[category]':cat,'data[tags]':taged,'data[descr]':description}

uploadurl = requests.post(jssreqtokenrespo['uploadform']['formAction'], files=filesvid, data=values)

jsourl=json.loads(uploadurl.content)
print(jsourl)

