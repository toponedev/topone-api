# -*- coding: utf-8 -*-

import httplib
import json

token = "topapi:xxxxxxxxxxxxx" 
host = 'https://trade.top.one/'

conn = httplib.HTTPSConnection(host)

url = '/'
url_history = '/history/'
headerdata = {"Content-type": "application/json"}  


#balance
print "balance:"
body = {"method":"balance.query","params":[token],"id":0}
conn.request('POST', url, json.dumps(body), headerdata)
res = conn.getresponse().read() 
print res

#current orders
print "current orders:"
body = {"method":"order.query", "params":[token, 0, 100],"id":0}
conn.request('POST', url, json.dumps(body), headerdata)
res = conn.getresponse().read() 
print res

#put limit order
print "put limit order:"
body = {"method":"order.limit", "params":[token, "TOP/ETH", 2, "100", "0.0001", 1],"id":0}
conn.request('POST', url, json.dumps(body), headerdata)
res = conn.getresponse().read() 
print res

#put market order
print "put market order:"
body = {"method":"order.market", "params":[token, "TOP/ETH", 2, "0.1", 1],"id":0}
conn.request('POST', url, json.dumps(body), headerdata)
res = conn.getresponse().read() 
print res

#cancel order  
order_id = 101  #need change!
print "cancel order:"
body = {"method":"order.cancel", "params":[token, "TOP/ETH", order_id],"id":0}
conn.request('POST', url, json.dumps(body), headerdata)
res = conn.getresponse().read() 
print res

#history orders
print "history orders:"
body = {"method":"order.history", "params":[token, "TOP/ETH", 0, 0, 0, 100],"id":0}
conn.request('POST', url_history, json.dumps(body), headerdata)
res = conn.getresponse().read() 
print res






