from menu_manager import MenuManager
from menu_item import MenuItem


def show_user_menu():
    print()
    print("Menu Options:")
    print("- View an Item (press V)")
    print("- Add an Item (press A)")
    print("- Delete an Item (press D)")
    print("- Update an Item (press U)")
    print("- Show the Menu (press S)")
    print("- Exit (press X)")
    choice = input("Your option?: ").upper()
    return choice

def add_item_to_menu():
    
    name = input("Enter item name: ")
    price = int(input("Enter item price: "))
    # print(name, " ", price)
    item = MenuItem(name, price)
    item.save()

    print(f"{name} was added successfully")



def remove_item_from_menu():
    name = input("Enter the name of the item to remove: ")
    item = MenuManager.get_by_name(name)
    # print(item)
    if item:
        item.delete()
        print(f"{name} was deleted")
    else:
        print("Item not found")

def update_item_from_menu():
    name = input("Enter the current name of the item: ")
    item = MenuManager.get_by_name(name)
    #print(item)
    if item:
        new_name = input("Enter the new name of the item: ")
        new_price = int(input("Enter the new price of the item: "))
        item.update(new_name, new_price)
        print(f"{name} was updated successfully")
    else:
        print("Item not found")



def show_restaurant_menu():
    items = MenuManager.all_items()
    print()
    print("Restaurant Menu:")
    for x in items:
        print(f"{x.name} - ${x.price}")




def main():
    
    while True:
        s = show_user_menu()
        if s == 'V':
            name = input("Enter the name of the item to view: ")
            item = MenuManager.get_by_name(name)
            if item:
                print(f"{item.name} - ${item.price}")
            else:
                print("Item not found.")
        elif s == 'A':
            add_item_to_menu()
        elif s == 'D':
            remove_item_from_menu()
        elif s == 'U':
            update_item_from_menu()
        elif s == 'S':
            show_restaurant_menu()
        elif s == 'X':
            print("Gameover")
            break
        else:
            print("Please try again")

if __name__ == "__main__":
    main()