from os import system

system("clear")

# π¨ Don't change the code below π
row1 = ["πΎοΈ", "πΎοΈ", "πΎοΈ"]
row2 = ["πΎοΈ", "πΎοΈ", "πΎοΈ"]
row3 = ["πΎοΈ", "πΎοΈ", "πΎοΈ"]
map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")
position = input("Where do you want to put the treasure? ")
# position = "23"
# π¨ Don't change the code above π

# Write your code below this row π

vertical = int(position[0])
horizontal = int(position[1])

map[horizontal - 1][vertical - 1] = "β"


# Write your code above this row π

# π¨ Don't change the code below π
print(f"{row1}\n{row2}\n{row3}")
