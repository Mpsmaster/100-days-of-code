import random
friends = ["Alice", "Bob", "Charlie", "David", "Emanuel"]
payer = random.randint(0, 4)
# 1 option
print(friends[payer])
# 2 option
print(random.choice(friends))