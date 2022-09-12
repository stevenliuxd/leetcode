n = input() 

phone_book = {}

for x in range(int(n)):
    entry = input()
    split = entry.split(" ")
    phone_book[split[0]] = split[1]

while True:
    query = input()

    if query in phone_book:
        print(query + "=" + phone_book[query])
    else:
        print("Not found")
