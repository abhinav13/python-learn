list=[15,16,14,17,13,11,19]

pos_buy_price = list[0]
neg_buy_price = list[0]
neg_sell_price = -1
pos_sell_price = -1
temp_buy_price = pos_buy_price
temp_sell_price = -1
max_loss=0
max_profit=0
temp_max_profit=0

for val in list[1:]:
	#Check if the price is falling down
	if(val <= neg_buy_price):
		if(neg_sell_price == -1):
			neg_sell_price=val
			max_loss = neg_buy_price-neg_sell_price
		elif(val-neg_buy_price > max_loss):
			neg_sell_price = val
			max_loss = neg_buy_price-neg_sell_price
	if(val < temp_buy_price):
		temp_buy_price = val

	if(val > temp_buy_price):
		if(pos_sell_price == -1):
			pos_sell_price = val
			pos_buy_price = temp_buy_price
			temp_sell_price=pos_sell_price
			max_profit=pos_sell_price-pos_buy_price
			temp_max_profit=max_profit
		elif(val-temp_buy_price > max_profit):				
			pos_sell_price = val
			temp_sell_price=pos_sell_price
			pos_buy_price = temp_buy_price
			max_profit=pos_sell_price-pos_buy_price

if(max_profit > 0 ):
	print "Buy price ", pos_buy_price
	print "Sell price",pos_sell_price
else:
	print "Buy price", neg_buy_price
	print "Sell price", neg_sell_price

