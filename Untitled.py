import console
#list
console.clear()
list = ["first", "second", "third"]
tuple = (1,3,4,4,5)
set = {5,4,35,5,5}
dictionary = {"key": 3, "identifier": 7, "key2": 45}

for l in list:
	print(l)
	
for t in tuple:
	print(t)
	
for s in set:
	print(s)
	
for d in dictionary:
	print(f"{d} {dictionary[d]}")
