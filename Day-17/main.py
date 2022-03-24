from os import system; system("clear")
# Class is a blueprint
class User: # All classes use Pascal Case; All words are capitalize
    
#HINT
# PascalCase -> All words init with upper case
# camelCase  -> Second and more words are upper case
# snake_case -> All words are lower case but separated by underscore

## Constructor or initialize
    # Creating atributes

    def __init__(self, user_id, username) -> None: # This method allows add and create atributes using the init function
        self.id = user_id
        self.username = username
        self.followers = 0 # This value is 0 by default and user doesn't change this when initialize
        self.following = 0

    def follow(self, user):
        user.followers += 1       
        self.following += 1


user_1 = User("001", "Eder")
user_2 = User("002", "Emilia")
print(user_1.id)


user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)