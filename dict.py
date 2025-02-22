a={"id":1,"name":"abc"}
print(a)

a={"id":1,"name":"abc"}
print(a["id"])


a={"id":1,"name":"abc"}
a["place"]="cbe"
print(a)

a={"id":1,"name":"abc"}
for i in a:
    print(i)

a={"id":1,"name":"abc"}
for i in a.values():
    print(i)

a={"id":1,"name":"abc"}
for i,j in a.items():
    print(i,j)

a={"id":1,"name":"abc"}
a.pop("id")
print(a)

a={"id":1,"name":"abc"}
a.popitem()
print(a)