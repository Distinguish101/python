friends = ["kevin", "karen", "jim"]
print(friends)

friends = ["kevin", "karen", "jim"]
print(friends[0])

friends = ["kevin", "karen", "jim"]
print(friends[-1])

friends = ["kevin", "karen", "jim", "oscar"]
print(friends[1:3])# grabs just 1 and 2 not 3

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends.extend(lucky_numbers)
print(friends)

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends.append("creed")
print(friends)

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends.insert(1, "creed")
print(friends)

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends.remove("jim")
print(friends)

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends.clear()
print(friends)

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends.pop()# takes off last element
print(friends)

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
print (friends.index("kevin"))

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar", "jim"]
print(friends.count("jim"))

lucky_numbers = [401, 823, 112, 123, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends.sort()
lucky_numbers.sort()
print(friends)
print(lucky_numbers)

lucky_numbers = [40, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
lucky_numbers.reverse()
print(lucky_numbers)

lucky_numbers = [4, 8, 12, 23, 55]
friends = ["kevin", "karen", "jim", "oscar"]
friends2 = friends.copy()
print(friends2)
