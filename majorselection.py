

list_of_majors = {
    'Administration Studies': ['social studies', 'organizational skills', 'time management', 'leadership', 'problem-solving'],
    'Art Studies': ['art', 'creativity', 'attention to detail', 'adaptability', 'patience'],
    'Aviation': ['mathematics', 'physics', 'creativity', 'attention to detail', 'adaptability', 'patience'],
    'Business Studies': ['economics', 'mathematics', 'attention to detail', 'problem-solving', 'decision-making', 'adaptability'],
    'Construction': ['mathematics', "teamwork", "problem-solving", "adaptability", "attention to detail"],
    'Design Studies': ['art', "creativity", "attention to detail", "adaptability", "time management"],
    'Economic Studies': ['economics', "analytical skills", "critical thinking", "research", "problem-solving"],
    'Education': ['psychology', "patience", "empathy", "adaptability", "organization"],
    'Energy Studies': ['physics', 'environmental science', "analytical skills", "problem-solving", "attention to detail", "adaptability"],
    'Engineering Studies': ['physics', 'mathematics', "analytical skills", "problem-solving", "attention to detail", "teamwork"],
    'Environmental Studies': ['biology', 'environmental science', "critical thinking", "problem-solving", "attention to detail", "adaptability"],
    'Fashion': ['art', 'home economics', "creativity", "attention to detail", "adaptability", "time management"],
    'Food and Beverage Studies': ['home economics', "attention to detail", "teamwork", "adaptability", "time management"],
    'General Studies': ['general studies', "critical thinking", "adaptability", "problem-solving", "time management"],
    'Health Care': ['biology', 'chemistry', "empathy", "teamwork", "adaptability", "attention to detail"],
    'Humanities Studies': ['english', 'social studies', "critical thinking", "analytical skills", "research", "adaptability"],
    'Journalism and Mass Communication': ['english', 'media studies', "writing", "adaptability", "time management", "research"],
    'Languages': ['english', 'language courses', "multilingualism", "cultural proficiency", "adaptability", "writing"],
    'Law Studies': ['social studies', 'law', "analytical skills", "critical thinking", "research", "problem-solving"],
    'Life Sciences': ['biology', "analytical skills", "attention to detail", "problem-solving", "research"],
    'Management Studies': ['business studies', "leadership", "analytical skills", "problem-solving", "adaptability"],
    'Marketing Studies': ['business studies', "creativity", "analytical skills", "adaptability", "time management"],
    'Natural Sciences': ['physics', 'chemistry', 'biology', "analytical skills", "problem-solving", "attention to detail", "research"],
    'Performing Arts': ['art', 'music', 'drama', "creativity", "adaptability", "teamwork", "discipline"],
    'Social Sciences': ['social studies', 'psychology', "analytical skills", "critical thinking", "empathy", "research"],
    'Sport': ['gym', "teamwork", "adaptability", "discipline", "leadership"],
    'Sustainability Studies': ['biology', 'environmental science', "critical thinking", "problem-solving", "attention to detail", "adaptability"],
    'Technology Studies': ['physics', 'mathematics', "analytical skills", "problem-solving", "teamwork", "adaptability"],
    'Tourism and Hospitality': ['business studies', 'geography', "customer service", "adaptability", "teamwork", "time management"],
    'Transportation and Logistics': ['physics', 'mathematics', 'technology studies', "analytical skills", "problem-solving", "attention to detail", "adaptability"]
}

counter = {
    'Administration Studies': 0,
    'Art Studies': 0,
    'Aviation': 0,
    'Business Studies': 0,
    'Construction': 0,
    'Design Studies': 0,
    'Economic Studies': 0,
    'Education': 0,
    'Energy Studies': 0,
    'Engineering Studies': 0,
    'Environmental Studies': 0,
    'Fashion': 0,
    'Food and Beverage Studies': 0,
    'General Studies': 0,
    'Health Care': 0,
    'Humanities Studies': 0,
    'Journalism and Mass Communication': 0,
    'Languages': 0,
    'Law Studies': 0,
    'Life Sciences': 0,
    'Management Studies': 0,
    'Marketing Studies': 0,
    'Natural Sciences': 0,
    'Performing Arts': 0,
    'Social Sciences': 0,
    'Sport': 0,
    'Sustainability Studies': 0,
    'Technology Studies': 0,
    'Tourism and Hospitality': 0,
    'Transportation and Logistics': 0
}


ordered_questions_chars ={
    "Do you enjoy teamwork? (yes/no/not sure): ": ["teamwork"],
    "Do you enjoy holding leadership roles and leading people? (yes/no/not sure): ": ["leadership"],
    "Would you consider yourself to be a creative and artistic person? (yes/no/not sure): ": ["creativity", "artistic"]
    }

def ask_question(question, characteristics):
    y = input(f"{question} (yes/no/not sure): ").lower()
    modifier = 1 if y == "yes" else (-1 if y == "no" else 0)

    for major, subjects in list_of_majors.items():
        if any(characteristic in subjects for characteristic in characteristics):
            counter[major] += modifier

def run_questions(question_dict):
    for question, characteristics in question_dict.items():
        ask_question(question, characteristics)

def major_select():
    school_subjects = ["mathematics", "social studies", 'english', 'art', 
                       "physics", "chemistry", "biology", "home economics", 
                       "music", "drama", "gym"]
    print(school_subjects)
    user_input = set(input("Enter your preferred school subjects (separated by commas): ").strip().lower().split(','))
    
    for major, subjects in list_of_majors.items():
        if any(subject in user_input for subject in map(str.lower, subjects)):
            print(f"Your selected subjects match the characteristics of {major}.")
            counter[major] += 1
    
    run_questions(ordered_questions_chars)

    for major, total_count in counter.items():
        print(f"Total count for {major}: {total_count}")
    

if __name__ == "__main__":
    major_select()