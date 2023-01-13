friends = ['Jake Peralta', 'Luffy', 'Jesse Pinkman', 'Terry Crews']
friends[1] = "Oscar"

print(friends[0])
print(friends[-1])
print(friends[1:])
print(friends[1:3])

print('------------------')

# friends.clear()
# print(friends)

friends.append('Creed')
print(friends)

friends.insert(1, "Luffy")
print(friends)

friends.remove("Oscar")
print(friends)

friends.pop()
print(friends)

print(friends.index("Jake Peralta"))

friends.insert(1, "Luffy")
print(friends.count("Luffy"))

friends.sort()
print(friends)

friends.reverse()
print(friends)

friends2 = friends.copy()
print(friends2)

numbers = [1,2,3,4]
friends.extend(numbers) # adds an array items in this array
print(friends)
