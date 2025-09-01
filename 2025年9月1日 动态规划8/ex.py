prices = [3,3,5,6,0,3,1,4]
l1 = prices[:-1]
l2 = prices[1:]
ll = list(zip(l1, l2))
profits = [ i - j for (j, i) in ll ]
print(profits)