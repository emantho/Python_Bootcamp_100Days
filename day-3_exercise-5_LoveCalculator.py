from os import system
system('clear')

# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
t,r,u,e = 0, 0, 0, 0 
l,o,v,e = 0, 0, 0, 0

print(name1)
print(name2)

if 't' in name1 or 'r' in name1 or 'u' in name1 or 'e' in name1 or 't' in name2 or 'r' in name2 or 'u' in name2 or 'e' in name2:
    if 't' in name1 or 't' in name2:
        t += 1
        print(f'T={t}')
    elif 'r' in name1 or 'r' in name2:
        r += 1
        print(f'R={r}')
    elif 'u' in name1 or 'u' in name2:
        u += 1
        print(f'U={u}')
    elif 'e' in name1 or 'e' in name2:
        e += 1
        print(f'E={e}')

elif 'l' in name1 or 'o' in name1 or 'v' in name1 or 'e' in name1 or 'l' in name2 or 'o' in name2 or 'v' in name2 or 'e' in name2:
    if 'l' in name1 or 'l' in name2:
        l += 1
        print(f'L={l}')
    elif 'o' in name1 or 'o' in name2:
        o += 1
        print(f'O={o}')
    elif 'v' in name1 or 'v' in name2:
        v += 1
        print(f'V={v}')
    elif 'e' in name1 or 'e' in name2:
        e += 1
        print(f'E={e}')

score = t+r+u+e+l+o+v+e
print(score)
