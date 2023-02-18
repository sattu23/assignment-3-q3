def letters(x):
    d={"UPPER":0, "LOWER":0}
    for c in x:
        if c.isupper():
           d["UPPER"]+=1
        elif c.islower():
           d["LOWER"]+=1
    print ("No. of Upper case characters : ", d["UPPER"])
    print ("No. of Lower case Characters : ", d["LOWER"])
letters('The quick Brow Fox')
