test_str = "pythonsystem"
res = {} 
for keys in test_str:
    res[keys] = res.get(keys, 0) + 1
print ("Count of all characters in pythonsystem is -\n"
                                             +  str(res))
