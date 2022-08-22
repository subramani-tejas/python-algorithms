# point = {"x": 1, "y": 2}
point = dict(x=3, y=13, z="x")

for key in point:
    print("key: ", key, type(key))
    print("value: ", point[key], type(point[key]))

print("###############################")

print("get method: y =", point.get("y"))

print(point)
del point["z"]
print("deleted z")
print(point)

print("###############################")

for key, value in point.items():
    print(key, value)


print("###############################")

# # comprehension
values_old = {}

for x in range(5):
    values_old[x] = x * 2

values = {x: x*2 for x in range(5)}

print(values)
