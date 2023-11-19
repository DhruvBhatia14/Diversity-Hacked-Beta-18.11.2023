

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
    "Do you enjoy holding leadership roles and leading people?": ["leadership"],
    "Would you consider yourself to be a creative and artistic person?": ["creativity", "artistic"],
    "Do you enjoy problem-solving?": ["problem-solving"],
    "Are you adaptable to new situations?": ["adaptability"],
    "Do you have a keen attention to detail?": ["attention to detail"],
    "Do you possess strong analytical skills?": ["analytical skills"],
    "Are you disciplined and well-organized?": ["discipline"],
    "Do you enjoy conducting research?": ["research"],
    "Do you have good customer service skills?": ["customer service"],
    "Are you multilingual or interested in language courses?": ["multilingualism"],
    "Are you environmentally aware?": ["environmental science", "adaptability"],
    "Do you enjoy collaborating in a team?": ["teamwork"],
    "Are you good at making decisions?": ["decision-making"],
    "Do you manage your time effectively?": ["time management"],
    "Are you patient and empathetic?": ["empathy", "patience"],
    "Do you have a creative mindset?": ["creativity"],
    "Are you interested in legal studies or law-related topics?": ["law"],
    "Do you enjoy physical activities and sports?": ["sport"],
    "Are you interested in arts and culture?": ["arts", "culture"],
    "Do you have a strong interest in technology and innovation?": ["technology"],
    "Are you interested in healthcare and well-being?": ["healthcare"],
    "Do you enjoy writing and communication?": ["writing"],
    "Are you interested in fashion and design?": ["fashion"],
    "Do you enjoy music, drama, or the performing arts?": ["music", "drama"],
    "Are you interested in geography and tourism?": ["geography", "tourism"],
    "Do you have an interest in energy and the environment?": ["energy", "environmental science"],
    "Do you have a general interest in various subjects?": ["general studies"],
    "Are you interested in studying and understanding economic principles?": ["economics", "business studies"],
    "Do you have a knack for understanding and interpreting laws and regulations?": ["law", "analytical skills"],
    "Do you enjoy exploring and experimenting with scientific concepts?": ["physics", "chemistry", "biology", "analytical skills"],
    "Are you passionate about promoting environmental sustainability?": ["environmental science", "sustainability"],
    "Would you like to work on projects that involve creative expression and artistic skills?": ["art", "creativity"],
    "Do you find joy in coordinating and managing various aspects of projects?": ["organization", "time management"],
    "Are you interested in exploring and understanding different cultures and societies?": ["social studies", "multiculturalism"],
    "Do you see yourself excelling in roles that involve leadership and decision-making?": ["leadership", "decision-making"],
    "Would you enjoy working on projects related to technology and innovation?": ["technology", "innovation"],
    "Are you passionate about health and well-being, with an interest in biology and chemistry?": ["healthcare", "biology", "chemistry"],
    "Do you find satisfaction in problem-solving and attention to detail?": ["problem-solving", "attention to detail"],
    "Are you interested in the world of business and its various aspects?": ["business studies", "management"],
    "Do you enjoy creative pursuits in the realm of arts and design?": ["art", "design", "creativity"],
    "Are you fascinated by the natural world and interested in environmental issues?": ["environmental science", "biology"],
    "Do you have a strong interest in the performing arts, including music, drama, and theater?": ["arts", "performing arts"],
    "Are you interested in languages, linguistics, or cultural proficiency?": ["languages", "cultural proficiency"],
    "Do you enjoy teamwork and collaboration in various projects?": ["teamwork", "collaboration"],
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
    user_subjects = [subject.strip() for subject in user_input]
    
    for major, subjects in list_of_majors.items():
        if any(subject in user_subjects for subject in map(str.lower, subjects)):
            print(f"Your selected subjects match the characteristics of {major}.")
            counter[major] += 1
    
    run_questions(ordered_questions_chars)

    for major, total_count in counter.items():
        print(f"Total count for {major}: {total_count}")
    
        # Sort majors based on counts in descending order
    sorted_majors = sorted(counter.items(), key=lambda x: x[1], reverse=True)

    # Group majors with the same count
    grouped_majors = {}
    for major, count in sorted_majors:
        if count not in grouped_majors:
            grouped_majors[count] = []
        grouped_majors[count].append(major)

    ranked_majors = []
    for count, majors in grouped_majors.items():
        if len(majors) == 1:
            ranked_majors.append(majors[0])
        else:
            # Ask the user to rank tied majors
            print(f"\nRank the following majors based on your preference (1 = most preferred):")
            for index, major in enumerate(majors, start=1):
                print(f"{index}. {major}")
            
            # Get user input for rankings
            ranking_input = input(f"Enter the rankings separated by commas: ")
            ranking_list = [int(rank) for rank in ranking_input.split(',').strip()]

            # Sort majors based on user rankings
            ranked_majors.extend([majors[index - 1] for index in sorted(ranking_list)])

    print("\nRanked Majors:")
    for index, major in enumerate(ranked_majors, start=1):
        print(f"{index}. {major}")
    
    return ranked_majors
    

if __name__ == "__main__":
    major_select()