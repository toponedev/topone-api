# -*- coding: utf-8 -*-

import time
import json
import random
import hashlib
import requests

headerdata = {"Content-type": "application/json"}

#get depth(orders)
body = {"method":"depth.query","params":["TOP/ETH",10],"id":0}
res=requests.post("https://depth.top.one/",data=json.dumps(body),headers=headerdata)
print res.text

appid  = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'
appkey = 'xxxxxxxxxxxxxxxxxxxxxxxxxx'

#get token
num = random.randint(100000,999999)
curtime = int(time.time())
data = 'appkey='+appkey+'&random='+str(num)+'&time='+str(curtime)
sha256 = hashlib.sha256()
sha256.update(data.encode('utf-8'))
signature = sha256.hexdigest()
params = {'appid': appid, 'time': str(curtime), 'random': num, 'sig': signature}
res=requests.get("https://server.top.one/api/apiToken",params=params)
print res.text

token = json.loads(res.text)['data']['apitoken']

#balance
body = {"method":"balance.query","params":[token],"id":0}
res=requests.post("https://trade.top.one/",data=json.dumps(body),headers=headerdata)
print res.text

#current orders
body = {"method":"order.query", "params":[token, 0, 100],"id":0}
res=requests.post("https://trade.top.one/",data=json.dumps(body),headers=headerdata)
print res.text

#put limit order
body = {"method":"order.limit", "params":[token, "TOP/ETH", 2, "100", "0.0001", 1],"id":0}
res=requests.post("https://trade.top.one/",data=json.dumps(body),headers=headerdata)
print res.text

#put market order
body = {"method":"order.market", "params":[token, "TOP/ETH", 2, "0.1", 1],"id":0}
res=requests.post("https://trade.top.one/",data=json.dumps(body),headers=headerdata)
print res.text

#cancel order  
order_id = 101  #your order id , need change!
body = {"method":"order.cancel", "params":[token, "TOP/ETH", order_id],"id":0}
res=requests.post("https://trade.top.one/",data=json.dumps(body),headers=headerdata)
print res.text

#history orders
body = {"method":"order.history", "params":[token, "TOP/ETH", 0, 0, 0, 100],"id":0}
res=requests.post("https://trade.top.one/history/",data=json.dumps(body),headers=headerdata)
print res.text
