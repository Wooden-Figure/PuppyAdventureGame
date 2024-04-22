print("Welcome to the Puppy Text Adventure Game!\n")


def show_instructions():  # providing the instructions to the user on how to play the game
    print('\nCollect all 6 items to win the game or be stuck inside!')
    print("In order to move you must type: 'go North', 'go South', 'go East', 'go West'.")
    print("In order to collect an item you must type: 'grab Item'.")


def user_status():   # providing the current room status of the user
    print("--------------------------------------")
    print(f'You are in the {current_room}.')
    print('Inventory:', inventory)


# The dictionary created for the TextBasedGame that connects the rooms
rooms = {
    'Laundry Room': {'West': 'Hallway'},
    'Hallway': {'North': 'Living Room', 'East': 'Laundry Room', 'Item': 'Backpack'},
    'Living Room': {'North': 'Dad Bedroom', 'West': 'Kitchen', 'South': 'Hallway',
                    'East': 'Long Stairway', 'Item': 'Riley the Black Lab'},
    'Kitchen': {'East': 'Living Room', 'Item': 'Dogster Treat'},
    'Dad Bedroom': {'East': 'Bathroom', 'South': 'Living Room', 'Item': 'Homework'},
    'Bathroom': {'West': 'Dad Bedroom', 'Item': 'Fireperson Outfit'},
    'Long Stairway': {'North': 'Computer Room', 'West': 'Living Room', 'Item': 'Pair of Stinky Shoes'},
    'Computer Room': {'South': 'Long Stairway', 'Item': 'Evil Owner'}
}

# starting the user in the Laundry Room
current_room = 'Laundry Room'
items_collected = 0
inventory = []

while True:
    user_input = input("Do you want to go on a puppy adventure? (yes/no):")

    if user_input.lower() == 'yes':
        print("\nGreat! Let's go on a puppy adventure.")
        show_instructions()  # calls the instructions
        user_status()  # calls the status of the user

        while current_room != 'Computer Room':
            print("--------------------------------------")
            user_move = input("Enter your move:")

            if user_move.lower().startswith('go '):  # initiates the movement piece of the program
                movement = user_move[3:]  # sliced the word go so that I could just use the cardinal direction

                if movement in rooms[current_room]:  # validates the room
                    if movement in ["North", "South", "East", "West"]:  # sees if the user can move in the
                        # specified direction
                        current_room = rooms[current_room][movement]  # moves the user to the next room
                        user_status()  # updates the user status
                        if 'Item' in rooms[current_room]:  # if an item exists, it will be shown in the room
                            item_in_room = rooms[current_room]['Item']
                            print(f'You see a {item_in_room}.')
                        else:
                            item_in_room = None  # if there is no item, the user does not see an item
                else:  # if the user goes a way they are unable to, this prompt occurs
                    print("You must be color-blind! You can't go that way.")

            elif user_move.lower().startswith('grab ') and items_collected < 6:
                action = user_move[5:]  # creates a new variable called action that allows the item to be collected

                if 'Item' in rooms[current_room]:  # assesses if the item  is in the room
                    item_in_room = rooms[current_room]['Item']
                    if action == item_in_room:  # if there actually is an item, then the conditional goes through
                        if action not in inventory:
                            inventory.append(action)
                            items_collected += 1
                            user_status()
                            print(f'You grabbed {action}.')

                            del rooms[current_room]['Item']  # once the user grabs the item, the item is then deleted
                            # from the room so the item does not keep showing if the player reenters the room

                        else:
                            print(f'You have {action} already.')
                    else:
                        print(f'{action} is not in this room.')

            else:  # if the user inputs anything that is not a valid answer, this prompt occurs
                print("ERROR MESSAGE. Enter a correct command. Bark Bark.")

            if items_collected == 6:
                print('\nYou collected all the items!')
                break

        if items_collected == 6:  # completes the 
            print('\nYou won the  and get to go play outside!')
            break

        if current_room == 'Computer Room' and items_collected != 6:  # ends the  if the players does not follow the
            #  instructions
            print("You went into the Computer Room w/out all the items and did not distract your owner! "
                  "You are stuck inside, sad face.")
            break

    elif user_input.lower() == 'no':
        print("That is one sad puppy.")
        quit()

    else:
        print("\nERROR MESSAGE. Enter 'yes' or 'no'. Bark Bark\n")
