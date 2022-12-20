from textwrap import dedent

def greeting():
    print(dedent("""
**************************************
**    Welcome to the Snakes Cafe!   **
**    Please see our menu below.    **
**
** To quit at any time, type "quit" **
**************************************
    """))

def food_order():
    print(dedent("""
    Appetizers
    ----------
    Wings
    Cookies
    Spring Rolls
    
    Entrees
    -------
    Salmon
    Steak
    Meat Tornado
    A Literal Garden
    
    Desserts
    --------
    Ice Cream
    Cake
    Pie
    
    Drinks
    ------
    Coffee
    Tea
    Unicorn Tears
    """))
    print(dedent("""
    ***********************************
    ** What would you like to order? **
    ***********************************"""))
    items_ordered= {}
    user_ordering = True
    close = "quit"

    while user_ordering:
        item_selected =input("> ")
        if item_selected != close:
            food = item_selected
            if food in items_ordered:
                items_ordered[food] +=1
            else:
                items_ordered[food] = 1
        print(f"** {items_ordered[food]} order of {food} have been added to your meal **")
        if item_selected == close:
            user_ordering = False


if __name__ == "__main__":
    greeting()
    food_order()