import json
import urllib2

is_empty = False
page_number = 1
total_price = 0

while not is_empty:
	url = ''.format(page_number) # insert url in quotes, for page indicator change page number to {} ie. &page=1 -> &page={} 
	json_file = urllib2.urlopen(url)
	data = json.load(json_file)
	if not data['orders']: # replace orders with proper list variable
		is_empty = True
	total_price += sum(float(item['price']) for item in data['orders']) # replace price and data with appropriate variables
	page_number += 1

print(total_price)