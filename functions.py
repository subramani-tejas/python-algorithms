##### function param & return types #####
def increment(number: int, by: int = 1) -> tuple:
    return (number, number + by)


print(increment(2, by=3))
########################################


##### function xxargs-numtiple keyword args #####
def save_user(**user):
    print(type(user), user)


save_user(name='admin')
########################################
