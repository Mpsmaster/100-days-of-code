def calculate_love_score(name1, name2):
    combine = (name1 + name2).lower()
    true = 0
    for letter in "true":
        true += combine.count(letter)
    love = 0
    for letter in "love":
        love += combine.count(letter)
    score = str(true) + str(love)
    print(score)      

calculate_love_score("kanye West", "Kim Kardashian")