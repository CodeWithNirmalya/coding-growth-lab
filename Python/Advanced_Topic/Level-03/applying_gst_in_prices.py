# QUESTION :- Given prices [100, 250, 499, 999], apply 18% GST using map().
prices = [100,250,499,999]

gst_prices = map(lambda x:(x*18/100),prices)
print(f'The 18 % gst for your {prices} is: {list(gst_prices)}')