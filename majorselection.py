

list_of_majors = {
    'Administration Studies': ['social studies'],
    'Art Studies': ['art'],
    'Aviation': ['mathematics', 'physics'],
    'Business Studies': ['economics', 'mathematics'],
    'Construction': ['mathematics'],
    'Design Studies': ['art'],
    'Economic Studies': ['economics'],
    'Education': ['psychology'],
    'Energy Studies': ['physics', 'environmental science'],
    'Engineering Studies': ['physics', 'mathematics'],
    'Environmental Studies': ['biology', 'environmental science'],
    'Fashion': ['art', 'home economics'],
    'Food and Beverage Studies': ['home economics'],
    'General Studies': ['general studies'],
    'Health Care': ['biology', 'chemistry'],
    'Humanities Studies': ['english', 'social studies'],
    'Journalism and Mass Communication': ['english', 'media studies'],
    'Languages': ['english', 'language courses'],
    'Law Studies': ['social studies', 'law'],
    'Life Sciences': ['biology'],
    'Management Studies': ['business studies'],
    'Marketing Studies': ['business studies'],
    'Natural Sciences': ['physics', 'chemistry', 'biology'],
    'Performing Arts': ['art', 'music', 'drama'],
    'Social Sciences': ['social studies', 'psychology'],
    'Sport': ['gym'],
    'Sustainability Studies': ['biology', 'environmental science'],
    'Technology Studies': ['physics', 'mathematics'],
    'Tourism and Hospitality': ['business studies', 'geography'],
    'Transportation and Logistics': ['physics', 'mathematics', 'technology studies']
}

def main():
    school_subjects = ["mathematics", "social studies", 'english', 'art', 
                       "physics", "chemistry", "biology", "home economics", 
                       "music", "drama", "gym"]
    print(school_subjects)
    x = input("Enter which school subjects you prefer from the list above (separated by commas): ").split(',')
    chosen_subjects = [subject.strip() for subject in x]
    
    compatible_majors = [major for major, subjects in list_of_majors.items() if any(subject in subjects for subject in chosen_subjects)]
    
    if compatible_majors:
        print("Possible majors:", ", ".join(compatible_majors))
    else:
        print("No majors found for the given preferences.")

if __name__ == "__main__":
    main()