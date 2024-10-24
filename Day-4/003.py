# import random

# random_side = random.randint(0, 1)

# if random_side == 1:
#     print("Head!")
# else:
#     print("Tail!") 


import random

number_of_flips = 10
heads_count = 0
tails_count = 0

for _ in range(number_of_flips):
    random_side = random.randint(0, 1)
    if random_side == 1:
        heads_count += 1
        print("Head!")
    else:
        tails_count += 1
        print("Tail!")

print(f"\nTotal Heads: {heads_count}")
print(f"Total Tails: {tails_count}")