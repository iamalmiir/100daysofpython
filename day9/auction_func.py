def auction():
    dictionary = {
        "name": 0
    }
    q = "yes"
    name = ""
    while q == "yes":
        n = str(input("What is your name?: "))
        p = int(input("What's your bid?: $"))
        if p > dictionary["name"]:
            dictionary["name"] = p
            name = n
            w = (input("Are there any other bidders? Type 'yes' or 'no'. \n")).lower()
            q = w
            # clear()
        if p < dictionary["name"]:
            w = (input("Are there any other bidders? Type 'yes' or 'no'. \n")).lower()
            q = w
            # clear()
    if q == "no":
        newOne = {}
        newOne[name] = dictionary["name"]
        dictionary = newOne
        print(f"The winner is {name} with a bid of ${dictionary[name]}")