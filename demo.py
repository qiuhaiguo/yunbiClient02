import time
import urllib2
import sys
import json

from lib.client import Client, get_api_path

client = Client(access_key='ZURvhizTAkcw2aYcnYQ9Jn3CYKNREeDcNdl1HXlp', secret_key='TYJeyNkXH1y7CD3xW64u6NbNsfgdIwJmlPfzsx58')
#client = Client(access_key='E4xWabtFKMWrj2YAwIyg3LHIml0ACLP2Cr1', secret_key='3p33k2yF22lE0nHJxwr5lN8R1gu44cBC6JV')

#####################
#get member info
#########################
member= (client.get(get_api_path('members')))
print "Name:", member['name']
print "memo:", member['memo']
print "sn:",member['sn']
print "email:",member['email']
print "active:",member['activated']
print "Account:"
for i in range(0,len(member['accounts'])):
    print "       ", member['accounts'][i]['currency'],"Balance: ",member['accounts'][i]['balance'],"Locked: ",member['accounts'][i]['locked']


print
print

#####################
#get markets
######################
markets =  client.get(get_api_path('markets'))
#for i in range(0,len(markets)):
    #print markets[i]
#print "markets:", markets

##########################
#delete an order
##############################
#params = {"id": 418306528}
#res = client.post(get_api_path('delete_order'), params)
#print
#print res

#########################
#sell XXX  at price XXX
##########################
#params = {'market': 'zeccny', 'side': 'sell', 'volume': 9.99, 'price':300 }
#res = client.post(get_api_path('orders'), params)
#print
#print res

#########################
#buy XXXX at price XXXX
##########################
#params = {'market': 'qtumcny', 'side': 'buy', 'volume': 1, 'price': 10}
#res = client.post(get_api_path('orders'), params)
#print
#print res

###########################################
#get orders of each market
#market should be specified in params
###########################################
print
print "orders in markets"
for market in markets:
    order = client.get(get_api_path('orders'), {'market': market['id']})
    for i in range(0,len(order)):
        #print order[i]
        print "Market: ",order[i]['market'],"side: ", order[i]['side'],"price: ", order[i]['price'],"volume: ", order[i]['volume'],"state: ", order[i]['state'],"trade id: ", order[i]['id']


####################################
#get tickers of each market
#market should be specified in url
#####################################
#print
#print "tickers in markets"
#for market in markets:
    #print client.get(get_api_path('tickers') % market['id'])

###########################################
#get my trades for special crypto currency
###########################################
#print
#print "trades order"
#myTrades = client.get(get_api_path('trades'), params={'market': 'zeccny'})
#for i in range(0,len(myTrades)):
    #print "time:",myTrades[i]['created_at'],"   market:",myTrades[i]['market'], "   price:",myTrades[i]['price'] ,"   Volumen:",myTrades[i]['volume']



####################################
#clear all orders in all markets
#res = client.post(get_api_path('clear'))
#print
#print res

####################
#get order book
#####################
#orderBook = client.get(get_api_path('order_book'), params={'market': 'zeccny'})
#print orderBook
#for i in range(0,len(orderBook['bids'])):
    #print "Time: ", orderBook['bids'][i]['created_at'],"  market: ", orderBook['bids'][i]['market'],"  price: ", orderBook['bids'][i]['price'],"  remaining_volume: ", orderBook['bids'][i]['remaining_volume']

"""
#get order book
#print client.get(get_api_path('order_book'), params={'market': 'btccny'})

#get tardes
#print client.get(get_api_path('trades'), params={'market': 'btccny'})

#get my trades
#print client.get(get_api_path('my_trades'), params={'market': 'btccny'})

#get k line
#print client.get(get_api_path('k'), params={'market': 'btccny'})

#buy 10 dogecoins at price 0.001
#params = {'market': 'dgdcny', 'side': 'buy', 'volume': 10, 'price': 96}
#res = client.post(get_api_path('orders'), params)
#print res

#demo of POST APIs
#DANGROUS, you better use test account to debug POST APIs

#params = {"id": 416528242}
#res = client.post(get_api_path('delete_order'), params)
#print res


markets =  client.get(get_api_path('markets'))
print markets

#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 10, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res

#buy 10 dogecoins at price 0.001
params = {'market': 'dogcny', 'side': 'buy', 'volume': 10, 'price': 0.001}
res = client.post(get_api_path('orders'), params)
print res

#clear all orders in all markets
res = client.post(get_api_path('clear'))
print res
#delete a specific order by order_id

#first, let's create an sell order
#sell 10 dogecoins at price 0.01
params = {'market': 'dogcny', 'side': 'sell', 'volume': 12, 'price': 0.01}
res = client.post(get_api_path('orders'), params)
print res
order_id = res['id']

#delete this order
params = {"id": order_id}
res = client.post(get_api_path('delete_order'), params)
print res

#create multi orders
params = {'market': 'dogcny', 'orders': [{'side': 'buy', 'volume': 12, 'price': 0.0002}, {'side': 'sell', 'volume': 11, 'price': 0.01}]}
res = client.post(get_api_path('multi_orders'), params)
print res
"""
