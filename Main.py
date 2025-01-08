import Pillar_interface
from WordGame import WordGame
from user_module import User


Pillar_interface.display_pillar3_intro()


first_name = input("\n         Please enter your First Name: ") 
last_name = input("\n         Please enter your Last Name: ")

data_base = {}

name = first_name + " " + last_name

if name not in data_base:
    print("\n         It seems you have not created and account yet!")
    password = input("\n         Please enter your password: ")
    user = User(first_name,last_name,password)
    user.hash_password










user_choice = input("\n         Would you like to try and guess today's word?")


Game = WordGame()

if user_choice == "Y":
    Game.play_game()
else:
    Pillar_interface.clear_terminal()
    print("No worries sometimes we like to just get into it as well!")
    charity, word = Game.get_charity_and_word_of_the_day()
    print(Game.colorize_string(f"Today's Charity is: {charity}", "\033[33m"))
    print(Game.colorize_string(f"Learn more and support them here: {Game.charity_links[charity]}\n", "\033[36m"))







