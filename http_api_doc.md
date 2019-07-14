# topone-api

Official Documentation for the APIs

TOP.ONE 交易接口说明

# 请求交互

## 行情API

Post /

URL: https://depth.top.one/

body:

    {"method": "depth.query", "params": ["TOP/ETH",10], "id": 0}        #查询挂单数据（10：买卖各10个报价）

Response示例：

    {
        "result": [
            {
                "bids": [["0.0000099", "126936"], ["0.00000984", "162179"]...], 
                "asks": [["0.00001088", "282265"], ["0.000011", "1561350"]...], 
                "time": 1529826401.615678
             }
        ], 
        "error": null, 
        "id": 0
     }


## 交易API

token:帐号授权字符串, 详见 token-api-doc.md

### 1)查询余额

Post /

URL: https://trade.top.one/ (中国大陆开发者：https://newtrade.topone.run/）

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
    
### 2)当前委托

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
            "status": 1,                  #订单状态   1 进行中
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

### 3)限价单

Post /

URL: https://trade.top.one/

body: 

    {
      "method":"order.limit", 
      "params":[
        "token",      #Token
        "TOP/ETH",    #市场
        2,            #买卖 1 卖  2 买 (数值，不是字符串!)
        "1000",       #数量
        "0.00001057", #价格
        0             #预留参数，无意义 (数值，不是字符串!)
      ],
      "id":0
    }

Response示例:

    {
      "error": null, 
      "result": {
        "id": 26211,                  #订单ID
        "type": 1,                    #订单类型   1 限价单  2 市价单
        "market": "TOP/ETH",          #市场
        "side": 2,                    #买卖方向   1 卖  2 买
        "ctime": 1526205633.6342139,  #下单时间
        "mtime": 1526205633.6342139,  #更新时间
        "price": "0.00001057",        #下单价格
        "deal_money": "0",            #成交额
        "status": 1,                  #订单状态   1 进行中  2 完成  3 撤单
        "amount": "10000",            #下单量
        "left": "10000",              #剩余量(未成交量)
        "deal_stock": "0"             #成交量
      }, 
      "id": 0
    }

### 4)市价单

Post /

URL: https://trade.top.one/

body: 

    {
        "method":"order.market", 
        "params":[
            "token",      #Token
            "TOP/ETH",    #市场
            2,            #买卖 1 卖  2 买   (数值，不是字符串!)
            "0.1",        #数量 买入：ETH数量  卖出：TOP数量
            0             #预留参数，无意义   (数值，不是字符串!)
        ],
        "id":0
    }

Response示例:

    {
        "error": null, 
        "result": {
            "id": 26212, 
            "ctime": 1526209901.4186571, 
            "mtime": 1526209901.418669, 
            "left": "0.004", 
            "market": "TOP/ETH", 
            "amount": "0.1", 
            "type": 2, 
            "side": 2, 
            "status": 2, 
            "price": "0", 
            "deal_stock": "16", 
            "deal_money": "0.096"
        }, 
        "id": 97
    }

### 5)撤单

Post /

URL: https://trade.top.one/

body: 

    {"method":"order.cancel", "params":["token", "TOP/ETH", 26211],"id":0}               #撤单，订单ID (数值，不是字符串!)
    {"method":"order.cancel", "params":["token", "TOP/ETH", 26211,262112,26213],"id":0}  #批量撤单

Response示例:

    {
        "result": {
            "id": 26316, 
            "type": 1, 
            "market": "TOP/ETH", 
            "side": 2, 
            "ctime": 1526209523.637193, 
            "mtime": 1526209523.637193, 
            "price": "0.0000101", 
            "deal_money": "0", 
            "status": 3, 
            "amount": "10000",
            "left": "10000", 
            "deal_stock": "0"
        }, 
        "error": null, 
        "id": 0
    }
    
### 6)历史委托

Post /history/

URL: https://trade.top.one/history/

body: 

    {
        "method":"order.history", 
        "params":[
            "token",        #Token
            "TOP/ETH",      #市场
            1526140800,     #开始时间
            1526210312,     #结束时间
            0,              #偏移
            100],           #Limit数量
        "id":0
    }

Response示例:

    {
        "result": [
            {
                "order_id": 26316,                  #订单ID
                "status": 3,                        #订单状态   2 完成  3 撤单
                "deal_money": "0",                  #成交金额
                "create_time": 1526209523.637193,   #下单时间
                "side": 2,                          #买卖 1 卖  2 买
                "finish_time": 1526209523.637193,   #订单完成时间
                "market": "TOP/ETH",                #市场
                "t": 1,                             #订单类型   1 限价单  2 市价单
                "price": "0.0000101",               #委托价格
                "amount": "10000",                  #委托数量
                "deal_stock": "0"                   #成交数量
            },{
                "order_id": 26211, 
                "status": 3, 
                "deal_money": "0", 
                "create_time": 1526205633.6342139, 
                "side": 2, 
                "finish_time": 1526205633.6342139, 
                "market": "TOP/ETH", 
                "t": 1, 
                "price": "0.00001057", 
                "amount": "10000", 
                "deal_stock": "0"
            }
        ], 
        "error": null, 
        "id": 6
    }

### 7)历史成交

Post /history/

URL: https://trade.top.one/history/

body: 

    {
        "method":"deals.history", 
        "params":[
            "token",        #Token
            "TOP/ETH",      #市场
            1526140800,     #开始时间
            1526210312,     #结束时间
            0,              #偏移
            100],           #Limit数量
        "id":0
    }

Response示例:

    {
        "result": [
            {
                "time": 1526209901.418669,      #时间
                "market": "TOP/ETH"             #市场
                "deal_id": 47521,               #成交流水ID
                "side": 2,                      #买卖 1 卖  2 买
                "price": "0.00600000",          #成交价格
                "amount": "16.00000000",        #成交数量
                "deal": "0.0960000000000000",   #成交金额
                "fee_asset": "TOP",             #手续费资产类型
                "fee": "0E-16",                 #手续费
            }
        ], 
        "id": 0, 
        "error": null
    }
