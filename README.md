# topone-api

Official Documentation for the APIs

TOP.ONE 交易接口说明

请求交互

REST访问的根URL：https://trade.top.one/

API参考

1)查询余额

Post /

URL: https://trade.top.one/

body: 

    {"method":"balance.query","params":["token"],"id":0}                #查询所有资产余额
    {"method":"balance.query","params":["token", “ETH”, “TOP”],"id":0}  #查询指定资产余额

Response示例：

    {
      "result": [
        {
          "freeze": "0.6",            #下单冻结
          "asset": "ETH",             #资产名称
          "available": "999.2036012", #可用余额
          "total": "999.8036012",     #总余额
          "btcvalue": "0",            #BTC估值
          "ethvalue": "999.8036012"   #ETH估值
        }, 
        {
          "freeze": "0", 
          "asset": "TOP", 
          "available": "0", 
          "total": "0", 
          "btcvalue": "0", 
          "ethvalue": "0e-8"
        }
      ], 
      "error": null, 
      "id": 0
    }
    
2)当前委托

Post /

URL: https://trade.top.one/

body: 

    {"method":"order.query", "params":["token", 0, 100],"id":0}     #查询前100个委托
    {"method":"order.query", "params":["token", 100, 100],"id":0}   #查询第100至200个委托

Response示例：

    {
      "result": {
        "limit": 99, 
        "records": [
          {
            "id": 26211,                  #订单ID
            "type": 1,                    #订单类型   1 限价单  2 市价单
            "market": "TOP/ETH",          #市场
            "side": 2,                    #买卖方向   1 卖  2 买
            "ctime": 1526205633.6342139,  #下单时间
            "mtime": 1526205633.6342139,  #更新时间
            "price": "0.00001057",        #下单价格
            "deal_money": "0",            #成交额
            "status": 1,                  #订单状态   0 进行中  1 完成  2 撤单
            "amount": "10000",            #下单量
            "left": "10000",              #剩余量
            "deal_stock": "0"             #成交量
          }
        ], 
        "total": 1, 
        "offset": 0
      }, 
      "error": null, 
      "id": 0
    }

3)限价单

Post /

URL: https://trade.top.one/

body: 

    {
      "method":"order.limit", 
      "params":[
        "token",      #Token
        "BTC/USDT",   #市场
        1,            #买卖 1 卖  2 买
        "3",          #数量
        "8001",       #价格
        1             #是否使用top抵扣手续费 1是 0 否
      ],
      "id":0
    }

Response示例:

    {
      "result": {
        "id": 26211,                  #订单ID
        "type": 1,                    #订单类型   1 限价单  2 市价单
        "market": "TOP/ETH",          #市场
        "side": 2,                    #买卖方向   1 卖  2 买
        "ctime": 1526205633.6342139,  #下单时间
        "mtime": 1526205633.6342139,  #更新时间
        "price": "0.00001057",        #下单价格
        "deal_money": "0",            #成交额
        "status": 1,                  #订单状态   0 进行中  1 完成  2 撤单
        "amount": "10000",            #下单量
        "left": "10000",              #剩余量
        "deal_stock": "0"             #成交量
      }, 
      "error": null, 
      "id": 0
    }
