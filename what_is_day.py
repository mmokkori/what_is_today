from sys import api_version
import requests
from bs4 import BeautifulSoup
import datetime

def time():
    t_delta = datetime.timedelta(hours=9)
    JST = datetime.timezone(t_delta, 'JST')
    now = datetime.datetime.now(JST)
    m = now.strftime('%m')
    day = now.strftime('%d')
    d = [m,day]
    return d 

date = time()
url = "https://www.nnh.to/{}/{}.html".format(date[0],date[1])

r = requests.get(url)

soup = BeautifulSoup(r.content,features="html.parser")

h4_tags = soup.find("h4")



title = []

title = h4_tags.get_text("h4")

print(title)

#LINEに送る。

api_url = 'https://notify-api.line.me/api/notify'

#内容
send_message = "\n\n{}".format(title)

token_dic = {'Authorization': 'Bearer' + ' ' + "JJFq9BxLrmCZNnVicPeWqV47u3pxe0Jb6JNFxIzK4oW"}
send_dic = {"message": send_message}

requests.post(api_url,headers=token_dic,data=send_dic)

