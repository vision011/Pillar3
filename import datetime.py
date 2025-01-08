import datetime




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


def get_charity_and_word_of_the_day():
    today = datetime.datetime.now()
    day_of_year = today.timetuple().tm_yday
    
    # Get the charity of the day
    charity_list = list(charity_words.keys())
    charity_index = (day_of_year - 1) % len(charity_list)
    selected_charity = charity_list[charity_index]
    
    # Get the word of the day for the selected charity
    words = charity_words[selected_charity]
    word_of_the_day = words[(day_of_year - 1) % len(words)]
    
    return selected_charity, word_of_the_day

# Example usage
charity, word = get_charity_and_word_of_the_day()
print(f"Today's Charity of the Day is: {charity}")
print(f"Word of the Day: ?????")
