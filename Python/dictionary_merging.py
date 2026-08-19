'''
Practice Problem: Write a function that merges two dictionaries. If a key exists in both dictionaries, sum their values. If a key exists in only one, include it as is.
'''


def merge_dicts(d1, d2):
    # Start with a copy of d1 to avoid modifying the original
    result = d1.copy()
    
    for key, value in d2.items():
        # .get(key, 0) returns 0 if the key doesn't exist yet
        result[key] = result.get(key, 0) + value
    
    return result

dict_a = {'a': 10, 'b': 20}
dict_b = {'b': 5, 'c': 15}

merged = merge_dicts(dict_a, dict_b)
print(f"Merged Dictionary: {merged}")