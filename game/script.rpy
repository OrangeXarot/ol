# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define e = Character("Halo")
define me = Character("Me")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show halo happy

    # These display lines of dialogue.

    e "Here's my cock."

    e "You like it?"

    menu choice:
        "You like it?"
        "Yes":
            jump yessed
        "No":
            jump noed
        
label yessed:
    me "Yes, I love it!"
    jump after

label noed: 
    me "I Hate it!"
    "But I was lying"
    jump after

label after:

    hide halo
    with fade

    me "Wait what?"

    # This ends the game.

    return
