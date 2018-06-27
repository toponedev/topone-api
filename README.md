# Trade APIs

# APIs Documents

Name | Description
------------ | ------------ 
token-api-doc.md | Details on the api key and token
http-api-doc.md | Details on market data,balance and order APIs
websocket-api-doc.md | Details on the market data websocket APIs
error_code.md | Trade error codes

# Interface frequency

get token Interface limit is 1 minute 1 translation.（获取token接口频率限制为1分钟1次。请勿频繁请求，否则将被屏蔽一小时。）

order(put order,cancel order) Interface limit is 1 minute 10 translation.（下单撤单接口频率限制为1秒5次。请勿频繁请求，否则将被屏蔽一小时。）

