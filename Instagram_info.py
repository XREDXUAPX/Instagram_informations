try:
	import requests ,re,os
except:
	import os
	os.system('pip install requests')
	os.system('pip install re')
os.system('clear')
B="\033[1;30m" # Black
R="\033[1;31m" # Red
G="\033[1;32m" # Green
Y="\033[1;33m" # Yellow
Bl="\033[1;34m" # Blue
P="\033[1;35m" # Purple
C="\033[1;36m" # Cyan
W="\033[1;37m" # White
print(R+''' ###                                                        
  #  #    #  ####  #####   ##    ####  #####    ##   #    # 
  #  ##   # #        #    #  #  #    # #    #  #  #  ##  ## 
  #  # #  #  ####    #   #    # #      #    # #    # # ## # 
  #  #  # #      #   #   ###### #  ### #####  ###### #    # 
  #  #   ## #    #   #   #    # #    # #   #  #    # #    # 
 ### #    #  ####    #   #    #  ####  #    # #    # #    # 
                                                            ''')
print((G+'-'+Y+'-')*30)
print(Y+'Dev '+G+':'+Y+'BlackBird')
print(Y+'Dev user '+G+':'+Y+'@XM1XX')
print(Y+'Dev channel'+G+':'+Y+'@UAP_TERMUX')
print((G+'-'+Y+'-')*30)
user=input(P+'Enter User Target :'+Y)
print((G+'-'+Y+'-')*30)
data = { "key": "bb81a522abdbd718eb24921719ae0946c8340058", "username": f"{user}" }
headers = { "user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/108.0.0.0 Safari/537.36" } 
r = requests.post("https://givt.pw/API/v1/instagram-info", data=data, headers=headers)
us=re.findall('("username":")(.*?)(\",")',r.text)[0][1] 
id=re.findall('("user_id":")(.*?)(\",")',r.text)[0][1]
try:
	dat=re.findall('("create_time":")(.*?)(\",")',r.text)[0][1]
	prv=re.findall('("is_private":")(.*?)(\",")',r.text)[0][1]
	vre=re.findall('("is_verified":")(.*?)(\",")',r.text)[0][1]
except:
	dat='null'
	prv='null'
	vre='null'
print(W+f'''
"username": "{us}",
"user_id": "{id}",
"is_verified": "{vre}",
"is_private": "{prv}",
"create_time": "{dat}"''')
