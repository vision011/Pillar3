import Pillar_interface
from WordGame import WordGame
from user_module import User


Pillar_interface.display_pillar3_intro()


first_name = input("\n         Please enter your First Name: ") 
last_name = input("\n          Please enter your Last Name: ")

data_base = {}

name = first_name + " " + last_name

if name not in data_base:
    print("It seems you have not created and account yet!")
    password = input("Please enter your password: ")
    user = User(first_name,last_name,password)
    user.hash_password













Game = WordGame() 








Game.play_game(name)