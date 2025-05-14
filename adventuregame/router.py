town_function = None
shop_function = None
tavern_function = None

def go_to_town():
    if town_function is not None:
        town_function()
    else:
        print("Error: Town function not set")

def go_to_shop():
    if shop_function is not None:
        shop_function()
    else:
        print("Error: Shop function not set")
        
def go_to_tavern():
    if tavern_function is not None:
        tavern_function()
    else:
        print("Error: Tavern function not set") 

def register_tavern_function(func):
    global tavern_function
    tavern_function = func

def register_town_function(func):
    global town_function
    town_function = func

def register_shop_function(func):
    global shop_function
    shop_function = func