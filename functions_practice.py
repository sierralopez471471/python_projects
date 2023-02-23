def hello() :
    print("Greetings, user!")

def pack(thing1, thing2, thing3):
    return [thing1, thing2, thing3]

def eat_lunch(any_list):
    if len(any_list) == 0 :
        print("My lunchbox is empty")
    else :
        for i in range(len(any_list)):
            if i == 0 :
                print(f"First I eat {any_list[0]}")
            else :
                print(f"Next I eat {any_list[i]}")


hello()
print(pack("toothbrush", "clothes", "Nintendo Switch"))
eat_lunch([])
eat_lunch(["taquitos", "avacodos", "bacon cheeseburger", "protein shake"])