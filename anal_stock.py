from fin_utils import *

def display_as_percentage(val):
  return '{:.1f}%'.format(val * 100)

amazon_prices = [1699.8, 1777.44, 2012.71, 2003.0, 1598.01, 1690.17, 1501.97, 1718.73, 1639.83, 1780.75, 1926.52, 1775.07, 1893.63]
ebay_prices = [35.98, 33.2, 34.35, 32.77, 28.81, 29.62, 27.86, 33.39, 37.01, 37.0, 38.6, 35.93, 39.5]

# Write code here
def get_returns(prices):
  returns = []
  for i in range(len(prices[:-1])):
    returns.append(calculate_log_return(prices[i], prices[i + 1]))
  return returns
    #start_price = prices[i]
    #end_price = prices[i + 1]
    #returns.append(calculate_log_return(start_price, end_price))
  #return returns
amazon = get_returns(amazon_prices)
ebay = get_returns(ebay_prices)
amazon_returns = [display_as_percentage(x)for x in amazon]
ebay_returns = [display_as_percentage(x) for x in ebay]
amazon_annual = display_as_percentage(sum(amazon))
ebay_annual = display_as_percentage(sum(ebay))
#print(amazon_returns)
#print(ebay_returns)
print(amazon_annual)
print(ebay_annual)

print(display_as_percentage(calculate_stddev(amazon)))
print(display_as_percentage(calculate_stddev(ebay)))
print(calculate_correlation(amazon, ebay))