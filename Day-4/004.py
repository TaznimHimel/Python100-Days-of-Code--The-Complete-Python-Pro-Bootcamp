# states_of_america = ["Delaware", "Pennsylvania", "New Jersey", "Georgia", "Connecticut", "Massachusetts", "Maryland", "South Carolina", "New Hampshire", "Virginia", "New York", "North Carolina", "Rhode Island", "Vermont", "Kentucky", "Tennessee", "Ohio", "Louisiana", "Indiana", "Mississippi", "Illinois", "Alabama", "Maine", "Missouri", "Arkansas", "Michigan", "Florida", "Texas", "Iowa", "Wisconsin", "California", "Minnesota", "Oregon", "Kansas", "West Virginia", "Nevada", "Nebraska", "Colorado", "North Dakota", "South Dakota", "Montana", "Washington", "Idaho", "Wyoming", "Utah", "Oklahoma", "New Mexico", "Arizona", "Alaska", "Hawaii"]

# # states_of_america.append("Bangladesh") 
# # states_of_america[-1] = "Himel" #Altering the list item
# print(states_of_america)
# # print(states_of_america[-4]) #It starts counting the list from the end. 




# dirty_dozen = ["Strawberries", "Spinach", "Kale", "Nectarines", "Apples", "Grapes", "Peaches", "Cherries", "Pears", "Tomatoes", "Celery", "Potatoes"]

# print(dirty_dozen[2])
# # print(dirty_dozen[5])
# # print("Minhuz Taznim Himel");

#Option number 1
import random
friends = ["Alice", "Bob", "Charli", "David", "Emanuel"]
print(random.choice(friends))

#Option number 2
random_index = random.randint(0, 4)
print(friends[random_index])