#8kyu
#Cat years, Dog years
def human_years_cat_years_dog_years(human_years):
    human_dog_cat = []
    dog_year = 0
    cat_year = 0
    if human_years == 1:
        dog_year += 15
        cat_year += 15
    elif human_years == 2:
        dog_year += 24
        cat_year += 24
    elif human_years > 2:
        dog_year += 5 * (human_years - 2) + 24
        cat_year += 4 * (human_years - 2) + 24
    human_dog_cat.append(human_years)
    human_dog_cat.append(cat_year)
    human_dog_cat.append(dog_year)
    return human_dog_cat


#Find Nearest square number

def nearest_sq(n):
    root = n ** 0.5
    nearest_int = round(root)
    nearest_square = nearest_int ** 2
    return nearest_square



#7kyu
#Sum of array singles
def repeats(arr):
    new_arr = []
    sum = 0
    for i in arr:
        if arr.count(i) == 1:
            new_arr.append(i)
    for i in new_arr:
        sum += i
    return sum


#Triangular Treasure
def triangular(n):
    if n <= 0:
        return 0
    else:
        return (n * (n + 1)) // 2
    


#6kyu
#Find the Mine!
def mine_location(field):
    answer = []
    for i in range(len(field)):
        for j in range(len(field[i])):
            if field[i][j] == 1:
                answer.append(i)
                answer.append(j)
                return answer



#5kyu
#The Hashtag Generator
def generate_hashtag(s):
    answer = "#"
    arr = s.split(" ")
    for i in arr:
        answer += i.capitalize()
    if s == "":
        return False
    elif len(answer) > 140:
        return False
    else:
        return answer



#Calculate Variance
def variance(numbers): 
    sum = 0
    for i in numbers:
        sum += i
    mean = sum / len(numbers)
    variance = 0
    for i in numbers:
        variance += (i - mean) ** 2
    return variance / len(numbers)