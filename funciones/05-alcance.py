greet = "Hey global"


def Greeting():
    global greet 
    greet = "Hello world"
    print(greet)


def GreetingPiggy():
    greet = "Hello piggy"
    print(greet)


# print(greet) #Error
print(greet)
Greeting()
GreetingPiggy()
Greeting()
print(greet)
