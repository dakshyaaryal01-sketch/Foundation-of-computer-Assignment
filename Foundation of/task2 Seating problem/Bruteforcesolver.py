import itertools

students = ["A", "B", "C", "D"]

friends = {("A", "B"), ("C", "D")}
same_city = {("A", "C")}

def is_valid(arrangement):
    for i in range(len(arrangement)-1):
        pair = (arrangement[i], arrangement[i+1])
        reverse = (arrangement[i+1], arrangement[i])
        
        if pair in friends or reverse in friends:
            return False
        if pair in same_city or reverse in same_city:
            return False
    return True

for perm in itertools.permutations(students):
    if is_valid(perm):
        print("Valid arrangement:", perm)