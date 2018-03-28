import time, json, requests
import matplotlib.pyplot as plt
import matplotlib.animation as animation
import matplotlib as style

#Fill In Portfolio Holdings Here
supplyDict = {'ETH' : 10, 'BTC' : 1, 'ETHOS' : 1000}
priceDict = {'ETH' : 0, 'BTC' : 0, 'ETHOS' : 0}
valueDict = {'ETH' : 0, 'BTC' : 0, 'ETHOS' : 0}




def main():
	#Period defines the frequency of portfolio updates (in Seconds)
	period = 4

	while True:
		total = 0
		updatePrice(priceDict)
		print(priceDict)
		for key, value  in supplyDict.items():
			valueDict[key] = value * priceDict[key]
			total += valueDict[key]
			print(key, "Value($): " , valueDict[key])
		print("Total Value($): ", total)
		

		# Uncomment to view Pie Plot of Holdings
		# plotpie(total)

		print("=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=-=")
		time.sleep(period) 

#Function that updates priceDict
def updatePrice(priceDict):
	capTick = requests.get('https://api.coinmarketcap.com/v1/ticker/')
	if (capTick.status_code == 200):
		theJSON = capTick.json()
		for i in theJSON:
			if i["symbol"] in priceDict:
				priceDict[i["symbol"]] = float(i["price_usd"])

#Function that graphs holdings
def plotpie(total): 
	labels = []
	sizes = []

	for k, v in valueDict.items():
		labels.append(k)
		sizes.append(v)

	colors = ['gold', 'yellowgreen', 'lightcoral', 'lightskyblue', 'orange']

	# Plot
	plt.pie(sizes,
	 labels=labels,
	 colors=colors,
	 autopct='%1.1f%%',
	 shadow=True, 
	 startangle=140)
 
	plt.title('Portfolio Value($): ' + str(total))
	plt.axis('equal')
	plt.show()

if __name__ == "__main__":
	main()