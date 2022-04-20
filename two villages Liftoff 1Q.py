village1 = input().split(",")
village2 = input().split(",")
common_people = []
for char in village1:
    both_village_mem = char in village2
    if both_village_mem:
        common_people.append(char)
print(" ".join(common_people))