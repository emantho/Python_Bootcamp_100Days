# %%
file = open("my_file.txt")
content = file.read()
print(content)
file.close()

# %%
with open("My_file.txt") as file:
    content = file.read()
    print(content)

# %%
# mode = r: read; w: write; a: append
with open("My_file.txt", mode="w") as file:
    file.write("Hello, My name is Eder. \nI'm 12 years old, and i like chocolate")

# %%
with open("my_file.txt", mode="a") as file:
    file.write("\nNew Text.")

# %%
# A new file can be created from scratch using w mode
with open("New_file.txt", mode="w") as file:
    file.write("\nNew Text.")

# %%
# A new file can be created from scratch using w mode
with open("/home/eder/Desktop/New_file.txt", mode="w") as file:
    file.write("\nAbsolute path.")

# %%
# A new file can be created from scratch using w mode
with open("/Desktop/New_file.txt", mode="w") as file:
    file.write("\nRelative path.")
# %%
