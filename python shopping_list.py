# python shopping_list.py
# make a list to hold items
shopping_list = []
def show_help ():
#print out instructions
    print("what should we pick up at the store?")
    print("""
Enter 'Done' to stop adding items.
Enter 'Help' for this help.
Enter 'Show' to see your current list.
""")
def show_list():
    # print out the list
    print("Here's your list:")
    
    for item in shopping_list:
    
        # print out the list
        print(item)
        
def add_to_list(new_item):
    shopping_list.append(new_item)
    print ("added {}. list now has {} items.".format(new_item, len(shopping_list)))
    
show_help()
while True:
    # ask for new items

    new_item = input("> ")
      #be able to quit the app
    if new_item == 'Done':
        break
    elif new_item == 'Help':
        show_help()
        continue
    elif new_item == 'Show':
        show_list()
        continue
    add_to_list(new_item)
    # add new items
    
    show_list()
    

