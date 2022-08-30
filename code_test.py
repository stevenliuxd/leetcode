apples = ["nihao", "str"]
lst = []

for x in apples:
    if "n" in x:
        lst.append(x)

print(lst)

tst = [x for x in apples if "n" in x]