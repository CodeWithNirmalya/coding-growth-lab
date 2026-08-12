# QUESTION --Find second largest number in a list

# A sample list for test case
listn = [52,41,36,52,5,24,5,465,51,65,135,4685,5,65,498,513,5146,8,316,8496,8,3516,84,8]

#sorting the list using python built_in function
unique_list = sorted(set(listn))
#show the output to the user
print(unique_list[-2])


