print("Введите ID человека, анализ друзей которого вы хотите провести:")
def col(a):
    b={}
    for i in range(0,len(a)):
        if a[i] in b:
            b[a[i]]=b[a[i]]+1
        else:
            b.update({a[i]:1})
    return b
import requests
name=input()
bdate=[]
voz=[]
value=[]
url='https://api.vk.com/method/users.get?user_ids='+name+'&access_token=853d54b0853d54b0853d54b053854d98c68853d853d54b0dbb75cf7e1f6b6eb49524719&v=5.103' 
a=requests.get(url)
idd=a.json()['response'][0]['id']
url='https://api.vk.com/method/friends.get?user_id=' + str(idd) + '&fields=bdate&access_token=853d54b0853d54b0853d54b053854d98c68853d853d54b0dbb75cf7e1f6b6eb49524719&v=5.103'
b=requests.get(url)
dr=b.json()['response']['items']
for i in range(0,len(dr)):
    if 'bdate' in dr[i]:  
        bdate=bdate+[dr[i]['bdate'].split('.')]
for i in range(0,len(bdate)):
    if len(bdate[i])==3:
        voz=voz+[2020-int(bdate[i][2])]
coll=col(voz)
coll2= sorted(coll.items(), key=lambda kv: kv[1])[::-1]
print("Формат вывода: (кол-во лет : кол-во друзей)")
for i in range(0,len(coll2)):
    print(coll2[i],end=' ')


