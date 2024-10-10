
names = [
    ['Alice', 'Bob', 'Charlie'],
    ['David', 'Eve', 'Frank'],
    ['Grace', 'Heidi', 'Ivan'],
    ['Judy', 'Ken', 'Laura'] 
]

#if Alice exist
for sublist in names:
    if 'Alice' in sublist:
        sublist.remove('Alice')
        alice_found = True


#if not found:
    new_name = input("Alice does not exist. Please enter a new name to add: ")
    names[0].append(new_name)


print(names)