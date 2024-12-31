import datetime
import Pillar_interface
class WordGame:



    charity_words = {
    "Education Charity": ["learn", "school", "teacher", "books", "classroom", "study", "knowledge"],
    "Environmental Charity": ["earth", "tree", "ocean", "recycle", "green", "nature", "climate"],
    "Health Charity": ["doctor", "nurse", "hospital", "medicine", "care", "wellness", "healing"],
    "Animal Welfare Charity": ["rescue", "shelter", "adopt", "wildlife", "habitat", "protection", "species"],
    "Food Bank Charity": ["hunger", "donate", "meals", "nutrition", "food", "support", "relief"],
    "Water Conservation Charity": ["river", "clean", "hydration", "ocean", "conserve", "sustainable", "aqua"],
    "Children's Charity": ["child", "future", "care", "play", "grow", "smile", "protection"],
    "Women's Empowerment Charity": ["strength", "rights", "equality", "empower", "leadership", "change", "support"],
    "Mental Health Charity": ["mind", "therapy", "stress", "calm", "balance", "resilience", "well-being"],
    "Disaster Relief Charity": ["aid", "recovery", "emergency", "help", "support", "rescue", "relief"],
    "Homeless Support Charity": ["shelter", "home", "support", "care", "warmth", "donate", "rebuild"],
    "Art and Culture Charity": ["painting", "music", "dance", "theater", "history", "expression", "creativity"]
    }





    def __init__(self):
        pass


    
    #chooses a charity based on the month and the day
    def get_charity_and_word_of_the_day(self):
        today = datetime.datetime.now()
        day_of_year = today.timetuple().tm_yday
        
        # Get the charity of the day
        charity_list = list(self.charity_words.keys())
        charity_index = (day_of_year - 1) % len(charity_list)
        selected_charity = charity_list[charity_index]
        
        # Get the word of the day for the selected charity
        words = self.charity_words[selected_charity]
        word_of_the_day = words[(day_of_year - 1) % len(words)]
        
        return selected_charity, word_of_the_day
    


    # return's the user's guess
    def user_guess(self,word,attempts):
        if attempts == 0:
            word_lenght = len(word)
            print(f"today's word is {word_lenght} letter's long\n")
        guess = input("Guess the word of the day!: ")

        if len(word) < len(guess):
            print("Too many words!")
            Pillar_interface.clear_terminal()
            self.user_guess(word,attempts)
        elif len(word) > len(guess):
            print("Not enough Character's")
            Pillar_interface.clear_terminal()
            self.user_guess(word,attempts)
        else:
            return guess
        

    def colorize_letter(self,letter, color_code):
        return f"\033[{color_code}m{letter}\033[0m"

    

    #grades the user's guess based by color
    def grade_guess(self,guess,word,attempts):
        guess, word = guess.upper(), word.upper()
        
        answer = list(word)
        guess = list(guess)

        output = ""

        for i in range(len(guess)):
            if guess[i] in answer:
                if guess[i] == answer[i]:
                    output += self.colorize_letter(guess[i],32)
                else:
                    output += self.colorize_letter(guess[i],33)
            else:
                output += guess[i]
        print(f"current attempts {attempts}")
        print(output)
    


    def Game_over(self,word,guess,attempts):
        if word.lower() == guess.lower():
            return True
        elif attempts == 6:
            return True
        return False

        


    def play_game(self,name):

        charity,word = self.get_charity_and_word_of_the_day()
        Game_finished = False
        attempts = 0
        
        Pillar_interface.clear_terminal()

        Pillar_interface.display_logo(name)



        while not Game_finished:
            user_guess = self.user_guess(word,attempts)
            attempts += 1


            self.grade_guess(user_guess,word,attempts)

            Game_finished = self.Game_over(word,user_guess,attempts)
        

        Pillar_interface.clear_terminal()
        Pillar_interface.display_logo(name)

        if attempts == 6:
            print(f"Come on {name}! Too many guesses, the word was {word}\n")
            print(f"Today's Charity is {charity}")
        else:
            print(f"WOOOOOOO We knew you would get it!")
            print(f"Today's charity is {charity}")

    
        



                  

        
               
        









    






            



