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

    charity_links = {
    "Education Charity": "https://www.unicef.org/education",
    "Environmental Charity": "https://www.wwf.org.uk/",
    "Health Charity": "https://www.who.int/",
    "Animal Welfare Charity": "https://www.rspca.org.uk/",
    "Food Bank Charity": "https://www.trusselltrust.org/",
    "Water Conservation Charity": "https://www.wateraid.org/uk",
    "Children's Charity": "https://www.savethechildren.org.uk/",
    "Women's Empowerment Charity": "https://www.womensaid.org.uk/",
    "Mental Health Charity": "https://www.mind.org.uk/",
    "Disaster Relief Charity": "https://www.redcross.org.uk/",
    "Homeless Support Charity": "https://www.crisis.org.uk/",
    "Art and Culture Charity": "https://www.artscouncil.org.uk/"
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
            print("Too many letters!\n")
            return self.user_guess(word,attempts)
        elif len(word) > len(guess):
            print("Not enogh letters\n")
            return self.user_guess(word,attempts)
        else:
            return guess
        

    def colorize_letter(self,letter, color_code):
        return f"\033[{color_code}m{letter}\033[0m"

    

    #grades the user's guess based by color
    def grade_guess(self, guess, word, attempts):
        guess, word = guess.upper(), word.upper()  # Ensure case insensitivity
        answer = list(word)
        guess = list(guess)

        # Initialize output as an empty list for storing the final result
        output = [""] * len(answer)

        # Track unmatched letters in the answer
        remaining_letters = answer[:]

        # Step 1: Handle green letters (correct position)
        for i in range(len(guess)):
            if guess[i] == answer[i]:
                output[i] = self.colorize_letter(guess[i], 32)  # Green
                remaining_letters[i] = None  # Mark as matched

        # Step 2: Handle yellow letters (wrong position)
        for i in range(len(guess)):
            if guess[i] != answer[i]:  # Skip green letters
                if guess[i] in remaining_letters:
                    output[i] = self.colorize_letter(guess[i], 33)  # Yellow
                    remaining_letters[remaining_letters.index(guess[i])] = None  # Mark as matched
                else:
                    output[i] = guess[i]  # Normal color (not in the word or no unmatched occurrences left)

        # Convert the output list to a string
        output_str = "".join(output)

        # Display results
        print(f"Attempt: {attempts}")
        print(output_str + "\n")





    # Import ANSI escape codes for colors (optional)
    def colorize_string(self,string, color_code):
        reset_code = "\033[0m"
        return f"{color_code}{string}{reset_code}"






    


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
        charity_link = self.charity_links[charity]
        
        Pillar_interface.clear_terminal()

        Pillar_interface.display_logo(name)



        while not Game_finished:
            user_guess = self.user_guess(word,attempts)
            attempts += 1


            self.grade_guess(user_guess,word,attempts)

            Game_finished = self.Game_over(word,user_guess,attempts)
        

        Pillar_interface.clear_terminal()
        Pillar_interface.display_logo(name)

        yellow = "\033[33m"
        green = "\033[32m"
        red = "\033[31m"
        cyan = "\033[36m"

# Failure case
        if attempts == 6:
            print(self.colorize_string(f"Come on {name}! Too many guesses, the word was {word}.\n", red))
            print(self.colorize_string(f"Today's Charity is: {charity}", yellow))
            print(self.colorize_string(f"Learn more and support them here: {charity_link}\n", cyan))

    # Success case
        else:
            print(self.colorize_string("WOOOOOO! We knew you would get it!\n", green))
            print(self.colorize_string(f"Today's Charity is: {charity}", yellow))
            print(self.colorize_string(f"Learn more and support them here: {charity_link}\n", cyan))
            
        



                  

        
               
        









    






            



