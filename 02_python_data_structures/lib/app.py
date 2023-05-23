# Sequence Types
#Note: use print() to execute the examples. Comment out examples after they've been demoed.

# Creating Lists
#1. ✅ Create a list of 10 pet names
pet_names = ['Rose', 'Meow Meow Beans', 'Mr.Legumes', 'Luke', 'Lea', 'Princess Grace', 'Spot', 'Tom', 'Mini', 'Paul']

# Reading Information From Lists
#2. ✅ Return the first pet name 
# print(pet_names[0])

#3. ✅ Return all pet names beginning from the 3rd index
# print(pet_names[3:])

#4. ✅ Return all pet names before the 3rd index
# print(pet_names[:3])

#5. ✅  Return all pet names beginning from the 3rd index and up to the 7th
# print(pet_names[3:7])

#6. ✅ Find the index of a given element
# print(pet_names.index('Lea'))

#7. ✅ Reverse the original list
# pet_names.reverse()
# print(pet_names)

#8. ✅ Return the frequency of a given element 
# print(pet_names.count("Lea"))

# Updating Lists
#9. ✅ Change the first element to all uppercase 

# didnt work becasue i didnt reassign 
# pet_names[0] = pet_names[0].upper()
# print(pet_names)

#10. ✅ Append a new name to the list
# pet_names.append('Darth Vader')
# print(pet_names)

#11. ✅ Add a new name at a specific index
# pet_names.insert(8, 'Luke SkyWalker')
# print(pet_names)

#12. ✅ Add two lists together 
# list1 = [ 1,2,3,4 ]
# list2 = [5,6,7,8]
# # didnt work 
# list1.extend(list2)
# # or 
# new_list = list1 + list2 
# print(new_list)

#13. ✅ Remove the final element from the list
# pet_names.pop()
# print(pet_names)

#14. ✅ Remove element by specific index
# pet_names.pop(7)
# print(pet_names)

#15. ✅ Remove a specific element 
# pet_names.remove('Luke SkyWalker')
# print(pet_names)

#16. ✅ Remove all pet names from the list
# pet_names.clear()
# print(pet_names)

#Tuple 
# 📚 Review With Students:
    # Mutable, Immutable, Changeable, Unchangeable

# Tuple not Immutable
#17. ✅ Create a Tuple of pet 10 ages 
# first_Tuple = [('Cleo', 4), ('Aslma', 6),('Nero', 2), ('Dante', 10), ('Incel', 1), ('Byron', 3), ('Ash', 7), ('Saxsa', 8), ('Peach', 9), ('Claire', 5)]
# pet_age = (1,2,3,4,5,6,7,8,9,10)

#18. ✅ Print the first pet age
# print(first_Tuple[0])
# print(first_Tuple)
# # sorting using the second key
# def sorted_tuple(first_Tuple):
#     # returning the key you want to sort by???
#     return first_Tuple[1]
# first_Tuple.sort(key = sorted_tuple)
# print(first_Tuple)
# print(pet_age[0]) 

# Testing Changeability 
#19. ✅ Attempt to remove an element with ".pop" (should error)
# pet_age.pop()

#20. ✅ Attempt to change the first element (should error)
# pet_age[0] = "Peony"

# Tuple Methods
#21. ✅ Return the frequency of a given element
# print(pet_age.count(3))

#22. ✅ Return the index of a given element 
# print(pet_age.index(4))

#23. ✅ Create a Range 
#Note:  Ranges are primarily used in loops
# range_to_10 = range(0,10,3) #start, set, stop 
# for n in range_to_10:
#     print(n)

# Demo Sets (Stretch Goal)
#24. ✅ Create a set of 3 pet foods
# pet_foods = {'tuna' , 'carrot' , 'catnip'}
# print(pet_foods)

# Demo Dictionaries 
# Creating 
#25. ✅  Create a dictionary of pet information with the keys "name", "age" and "breed"
# pet_info_rose = {'name':'rose','age':11,'breed':'domestic long '}


#26. ✅  Use dict to create a dictionary of pet information with the keys "name", "age" and "breed"
# pet_info_spot = dict(name='Spot', age=25, breed='boxer')


# Reading
#27. ✅ Print the pet attribute of "name" using bracket notation 
# print(pet_info_rose['name'])

#28. ✅ Print the pet attribute of "age" using ".get"
#Note: ".get" is preferred over bracket notation in most cases because it will return "None" instead of an error
# print(pet_info_spot.get("age"))

# Updating 
#29. ✅ Update the pets age to 12
# newAge = pet_info_spot["age"] = 12
# print(newAge)
# print(pet_info_spot)

#30. ✅ Update the other pets age to 26
# newAger = pet_info_rose["age"] = 26
# print(newAger)
# pet_info_spot.update({'age' : 26})
# print(pet_info_rose)

# Deleting
#30. ✅ Delete a pets age using the "del" keyword 
# del(pet_info_rose["age"])
# print(pet_info_rose)


#31. ✅ Delete the other pets age using ".pop"
# pet_info_spot.pop('age')
# print(pet_info_spot)


#32. ✅ Delete the last item in the pet dictionary using "popitem()"
# pet_info_spot.popitem()
# print(pet_info_spot)

# Demo Loops 
pet_info = [
    {
        'name':'rose',
        'age':11,
        'breed': 'domestic long-haired',
    }, 
    {
        'name':'spot',
        'age':25,
        'breed': 'boxer',
    },
    {
        'name':'Meow Meow Beans',
        'age':2,
        'breed': 'domestic long-haired',
    }
    ]

#33. ✅ Loop through a range of 10 and print every number within the range
# for num in range(0, 10):
#     print(num)

#34. ✅ Loop through a range between 50 and 60 that iterates by 2 and print every number
for i in range(50, 60):
    print(i)

#35. ✅ Loop through the "pet_info" list and print every dictionary 
# for each_pet in pet_info:
#     print(each_pet)

#36. ✅ Create a function that takes a list as an argument 
    # The function should use a "for" loop to loop through the list and print every item 
    # Invoke the function and pass it "pet_names" as an argument
# def print_pet(list):
#     for i in list:
#         print(i)

# print_pet(pet_info)

#37. ✅ Create a function that takes a list as an argument. (simple example) 
    # The function should define a counter and set it to 0
    # Create a "while" loop 
        # The loop will continue as long as the counter is less than the length of the list
        # Every loop should increase the count by 1
    # Return the counter 
# def increase_one(list):
#     i = 0
#     while( i < len(list)-1):
#         i += 1
#         return i
#     print(increase_one(pet_info))

#38. ✅ Create a function that updates the age of a given pet
        # The function should take a list of "dict"s, "name" and "age" as parameters 
        # Create am index variable and set it to 0
        # Create a while loop 
            # The loop will continue so long as the list does not contain a name matching the "name" param and the index is less then the length of the list
            # Every list will increase the index by 1
        # If the dict containing a matching name is found, update the item's age with the new age 
            # Otherwise, return 'pet not found'
# def update_age(lst, name, age):
#     idx = 0

#     while(lst[idx].get('name') != name) and idx < len(lst)-1:
#                 idx += 1
#     if lst[idx].get('name') == name: 
#           print(lst[idx])
#           lst[idx]['age'] = age
#           print(lst[idx])
#           return(lst[idx])
#     else : 
#           return 'pet not found'
# print(update_age(pet_info, 'rose', 2))

# map like 
#39. ✅ Use list comprehension to return a list containing every pet name from "pet_info" changed to uppercase
# pet_uppercase = [pet["name"].upper() for pet in pet_info] 
# print([pet_uppercase])
        
# find like
#40. ✅ Use list comprehension to find a pet named spot
# pet_find = [pet["name"] for pet in pet_info if pet["name"] == "spot"]
# print(pet_find)

# filter like
#41. ✅ Use list comprehension to find all of the pets under 3 years old
# pet_filter = [pet for pet in pet_info if pet["age"] < 3]
# print(pet_filter)

#43. ✅ Create a generator expression matching the filter above. Compare and contrast the generator to the list comprehension. 
generator = [pet for pet in pet_info if pet["age"] < 3]
for pet in generator:
    print(pet)