"""Module Six Milestone starter for the simplified movement prototype."""


rooms = {
    'Jungle Entrance': {'North': 'Bamboo Forest'},
    'Bamboo Forest': {
        'South': 'Jungle Entrance',
        'East': 'Hidden Waterfall',
        'North': 'Monkey Grove'
        
},
'Hidden Waterfall': {
    'West': 'Bamboo Forest',
    'North': 'Monkey Grove'
},
'Monkey Grove': {
    'South': Bamboo Forest',
    'East': Ancient Ruins'

},
'Ancient Ruins': {
    'West': 'Monkey Grove',
    'South': Hidden Waterfall',
    'East': 'Crocodile Swamp'

},
'Crocodile Swamp' {
    'West': 'Ancient Ruins',
    'North': 'Jacguar Cave'

},
'Jacguar Cave' {
    'South': 'Crocodile Swamp'
    "East": "Guardian's Temple"

},
"Guardian's Temple': {
    'West': 'Jacguar Cave'
}

}

current_room = 'Jungle Entrance'

while True:
    print('\nYou are in the', current_room)
    print('Enter go North, go South, go East, or go West.')
    print("Type 'exit' to quit the game.)

    command = input('Enter your move: ').strip()

    if command.lower() == 'exit':
         print('Thanks for playing Escape the Cursed Jungle!')
         break

    if command.lower().startswith('go '):
        direction = command[3:].strip().capitalize()

        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
            print('You moved to the', current_room)
        else:
            print('You cannot go that way!')
        else:
           print('Invalid command. Try go North or exit.')



# TODO: Run and debug all milestone cases in prototype/README.md.
