# QUESTION - Remove all negative numbers from a list using filter().
num = [10,24,-14,45,-32,45,-78,10,-68,-98,-74,66]
remove_neg = filter(lambda x:x>0,num)
print(f"All positive number in the list is : {list(remove_neg)}")