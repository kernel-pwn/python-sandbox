# collection of {key:values} pairs
# ordered and changeable. no dupes
# print(dir(capitals)
# print(help(capitals)

capitals = {"usa": "Washington d.c",
            "india": "new Delhi",
            "china": "Beijing",
            "russia": "moscow"}

#print(capitals.get("usa"))

#if capitals.get("japan"):
#    print("that capital exists")
#else:
#    print("that capital does not exist")

#capitals.update({"Germany": "berlin"})
#capitals.update({"Germany": "Mumbai"})
#capitals.pop("usa")
#capitals.popitem
#capitals.clear()

#keys = capitals.keys()
#for key in capitals.keys():
#    print(key)

#values = capitals.values()
#for value in capitals.values():
#    print(value)

#items = capitals.items()
for key,value in capitals.items():
    print(f"{key} -> {value}")