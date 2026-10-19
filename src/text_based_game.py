"""Project Two starter for the student's text-based adventure game."""

Escape the Cursed Jungle


def show_instructions():
    print("Welcome to Escape the Cursed Jungle!")
    print("Collect all 6 items to defeat the Jungle Guardian.")
    print("Move commands: go North, go South, go East, go West")
    print("To collect an item, type: get Item Name")
    print("Type exit to quit the game.")
    print("-------------------------------------")

def show_status(current room, inventory, rooms):
    print("\nYou are in the", current_room)
    print("Inventory:", inventory)

    if 'item' in rooms[current_room]:
        print("You see a", rooms[current_room]['item'])

    print("-----------------------------------')

def main():
    rooms = {
        'Jungle Entrance': {
            'West': 'Bamboo Forest',
            'East': 'Monkey Grove'
        },
        'Bamboo Forest': {
             'East': 'Jungle Entrance',
             'North': 'Hidden Waterfall',
             'South': 'Ancient Ruins',
             'item': 'Machete'

        },
        'Hidden Waterfall': {
             'South': 'Bamboo Forest',
             'item': 'Water Flask'

        }.
        'Monkey Grove": {
             'West': 'Jungle Entrance',
             'item';: 'Rope'

        },
        'Ancient Ruins': {
            'North': 'Bamboo Forest',
            'South': 'Crocodile Swamp',
            'item': 'Keychain'

        },
        'Crocodile Swamp': {
             'North': 'Ancient Ruins'
             'South': 'Jacguar Cave'
             'item": Hibiscus Flower

        },
        "Guardian's Temple": {
             'North': 'Jaquar Cave'

        } 

 }

 current_room = 'Jungle Entrance'
 inventory = []

 show_instructions()

 whilw True:
 show_status(current_room, inventory, rooms)

 command = input("Enter your command: ").strip()
 parts = command.split(maxsplit=1)

 if not parts:
     print("Please enter a command: ")
     continue  

  action = parts[0].lower()

  if action == 'exit':
      print("Thanks for playing!")
      break

  elif action == 'go':
      if len(parts) < 2:
          print("Please enter a direction.")
          continue

       direction = parts[1].title()

       if direction in rooms[current_room]:
           current_room = rooms[current_room][direction]
           print("You traveled", direction)

        else:
            print("You cannot go that way!")

    elif action == 'get':
        if len(parts) < 2:
             print("Please enter an item name.")
             continue

        else:
            print("That item is not in this room!")

    else:
        print("Invalid command. Please try again.")

    if current_room == "Guardian's Temple":
        if len(inventory) == 6:
            print("\nCongratulations!")
            print("You collected all 6 items!")
            print("You defeated the Jungle Guardian!")
            print("You escaped the cursed jungle!")
            print("You WIN!)
        else:
            print('\nThe Jungle Guardian has found you!")
            print("You did not collect all 6 items.')
            print("Game OVER! YOU LOSE!")
        break

if __name__ == "__main__":
    main()
