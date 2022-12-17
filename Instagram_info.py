import os
try:
	import requests,re,time,pyfiglet,termcolor
	import webbrowser
	from sys import stdout
	from time import sleep
except ModuleNotFoundError as m:
    time.sleep(10)
    os.system("pip install requests")
    os.system("pip install re101")
    os.system("pip install jinja2-time")
    os.system("pip install pyfiglet")
    os.system("pip install termcolor2")
    os.system("pip install pycopy-webbrowser") 
    os.system("clear")
    print('Close the program and try again')
from os import system
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
print(Y+'Dev '+G+': '+R+'BlackBird')
print(Y+'Dev user '+G+': '+R+'@XM1XX')
print(Y+'Dev channel'+G+': '+R+'@UAP_TERMUX')
print((G+'-'+Y+'-')*30)
user=input(P+'Enter User Target :'+Y)
print((G+'-'+Y+'-')*30)
def check_username(username):
    datas = 0
    h = {'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.152 Safari/537.36','cookie': 'mid=YF93jgALAAE3vLXolGU8TUim3FA5; ig_did=3525CF13-8CA7-4886-8028-5FAC28C60E97; datr=U1VgYLyLNUpoQ6_ODYRFQe7n; csrftoken=llONvsDLwC82YAy8nFRJinhKvISAruxN; ds_user_id=276972397; sessionid=276972397%3AgQKkX8ikrFwQi8%3A7; shbid=14342; shbts=1623538759.6567142; rur=LDC'}
    while True:
        try:
            i = requests.get(f'https://www.instagram.com/{username}/',headers=h,timeout=5)
            break
        except:
            try:
                i = requests.get(f'https://www.instagram.com/{username}/',headers=h,timeout=5)
                break
            except:
                print('['+termcolor.colored('!','red')+'] '+'Error while logging in! Try different cookies.')
    
    word = re.findall('HttpErrorPage.css',i.text)
    if len(word) == 1:
        try:
            datas = re.findall('content=".*?Posts',i.text)[0]
            try:
                fullname = re.findall('("og:title" content=")(.*?)(\(@)',i.text)[0][1]
            except:
                fullname = None
            try:
                bio = re.findall('("description":")(.*?)(\",")',i.text)[0][1]
            except:
                bio = None
            try:
                mails = re.findall("[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*@(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?",i.text)
            except:
                mails = None
            try:
                is_private = re.findall('("is_private":)(\S{1,5})(,"is_verified":)',i.text)[0][1]
            except:
                is_private = None
        except Exception as e:
            return str(e)
    else:
        if i.status_code == 404:
            return "\033[1;31mTHE YOUSERNAME IS NOT FOUND [×] \n"
        print('Something went wrong! Try again later.')

    if datas != 0:
        head1 = {'accept': '*/*','accept-encoding': 'gzip, deflate, br','accept-language': 'en-US,en;q=0.9','content-length': '68','content-type': 'application/x-www-form-urlencoded','cookie': 'ig_cb=1; ig_did=131F2FE5-1BB1-4652-9E16-5AFF47A7CC36; mid=XzlsVQALAAFETmXB79LUzyCE348k; shbid=6664; shbts=1597861147.1435034; rur=FTW; csrftoken=Ow0d1NTJuy6sEvaH3c5irri2zk1ExJe2; urlgen="{\"185.113.96.223\": 29518}:1k8SgR:LaXQkBLADjj_JFFC4B8PkeNDmXQ"','origin': 'https://www.instagram.com','referer': 'https://www.instagram.com/accounts/password/reset/','sec-fetch-dest': 'empty','sec-fetch-mode': 'cors','sec-fetch-site': 'same-origin','user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.125 Safari/537.36','x-csrftoken': 'Ow0d1NTJuy6sEvaH3c5irri2zk1ExJe2','x-ig-app-id': '936619743392459','x-ig-www-claim': 'hmac.AR2Oj4pwhIg-NMX0JaMK9oyeAa9fEiflWvsxVaSwZhGm8l1F','x-instagram-ajax': 'f6699f3befc8','x-requested-with': 'XMLHttpRequest'}
        dat = {
        'email_or_username': f'{username}',
        'recaptcha_challenge_field':''
        }
        url = 'https://www.instagram.com/accounts/account_recovery_send_ajax/'
        try:
            res = requests.post(url,headers=head1,data=dat,timeout=5).text
            try:
                maily = re.search('[A-z0-9]{1}\*{1,}[A-z0-9]\@\S{1,}\.[A-z0-9]{1,}',res).group()
            except:
                try:
                    maily = re.search('[A-z0-9]{1}\*{1,}\@\S{1,}\.[A-z0-9]{1,}',res).group()
                except:
                    if 'Please wait a few minutes before you try again' in res:
                        maily = 'Please wait a few minutes before you try again'
                    else:
                        maily = None

            try:
                numb = re.findall('\+\d{1,3}\s{1}\*{3}\-{1}\*{4}\-{1}\*{2}\d{2}',res)[0]
            except:
                numb = None
            
            cv = datas[datas.index('"'):][1:].split(', ')
            
            if len(mails) > 1:
                for m in mails:
                    if len(m.split('@')[0]) == 1:
                        mails.pop(mails.index(m))
                mails = ' - '.join(mails)
            elif len(mails) == 1:
                mails = mails[0]
            else:
                mails = None
            date = None
            if cv[2].split(' ')[0] != 0 and is_private != 'true':
                try:
                    last_post_url = re.findall('("shortcode":")(\S{1,})(","dimensions":)',i.text)[0][1]
                    post = requests.get('https://www.instagram.com/p/'+last_post_url+'/',headers=h,timeout=5).text
                    date = re.search('( on )(.*?)(\.)(.*?)(","is_video":)',post).group(2)
                except:
                    date = 'Error'
            combo = f'''

{termcolor.colored('[♕]EMAIL ','red')}:»» {maily}
{termcolor.colored('[♕]NUMBER ','blue')}:»» {numb}
{termcolor.colored('[♕]USERNAME ','cyan')}:»» {'@'+username}
{termcolor.colored('[♕]NAME ','green')}:»» {fullname}
{termcolor.colored('[♕]PRIVATE ','yellow')}:»» {is_private}
{termcolor.colored('[♕]BIO ','white')}:»» {bio}
{termcolor.colored('[♕]OTHER MAILS IN THE PAGE ','red')}:»» {mails}
{termcolor.colored('[♕]LAST POST DATE  ','blue')}:»» {date}
{termcolor.colored('[♕]FOLLOWERS ','cyan')}:»» {cv[0].split(' ')[0]}
{termcolor.colored('[♕]FOLLOWING ','yellow')}:»» {cv[1].split(' ')[0]}
{termcolor.colored('[♕]POSTS ','white')}:»» {cv[2].split(' ')[0]}
{termcolor.colored('[♕]TIME ','green')}:»» {time.asctime()}
'''         
            return combo
            
        except Exception as ea:
            return str(ea)
    else:
        return 'no 1'
clear = lambda: system("cls")
info = check_username(user)
print (info)