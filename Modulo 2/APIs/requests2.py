import requests 

link = requests.get ("https://www.instagram.com")


if 200 <= link.status_code <=299:
  print("deu certo", link.status_code)

elif 400 <= link.status_code <=499:
   print("deu certo", link.status_code)

else:
   print("link fora de range")
   


    
