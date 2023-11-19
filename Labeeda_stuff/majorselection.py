from majors_data import list_of_majors, counter, ordered_questions_chars
import re

def ask_question(question, characteristics):
    # Continuously prompt the user until a valid answer is provided
    while True:
        y = input(f"{question} (yes/no/not sure): ").lower()
        if y in ("yes", "no", "not sure"):
            modifier = 1 if y == "yes" else (-1 if y == "no" else 0)
            # Update the counters based on the user's response
            for major, subjects in list_of_majors.items():
                if any(characteristic in subjects for characteristic in characteristics):
                    counter[major] += modifier
            break
        else:
            print("Invalid input. Please enter 'yes,' 'no,' or 'not sure.'")

def run_questions(question_dict):
    # Iterate through the questions and characteristics and ask the user for responses
    for question, characteristics in question_dict.items():
        ask_question(question, characteristics)

def rank_majors(majors):
    while True:
        try:
            # Get user input for rankings
            ranking_input = input(f"Enter the rankings separated by commas: ").strip()

            # Check for leading and trailing spaces or invalid input format
            if ranking_input.startswith(",") or ranking_input.endswith(","):
                raise ValueError("Please remove leading or trailing commas.")
            
            if not re.match(r'^\d+(,\d+)*$', ranking_input):
                raise ValueError("Invalid input. Please enter valid numbers separated by commas.")

            ranking_list = [int(rank) for rank in ranking_input.split(',')]

            # Check if the user missed ranking a major or provided invalid rankings
            if len(ranking_list) != len(majors) or any(rank <= 0 or rank > len(majors) for rank in ranking_list):
                raise ValueError("Invalid ranking. Please enter numbers within the range.")

            # Sort majors based on user rankings
            ranked_majors = [majors[index - 1] for index in sorted(ranking_list)]
            return ranked_majors

        except ValueError as e:
            print(f"Error: {e}")
            print("Please try again.")

def major_select():
    school_subjects = ["mathematics", "social studies", 'english', 'art',
                       "physics", "chemistry", "biology", "home economics",
                       "music", "drama", "gym"]
    print("Available school subjects:", school_subjects)
    user_input = set(input("Enter your preferred school subjects (separated by commas): ").strip().lower().split(','))
    user_subjects = [subject.strip() for subject in user_input]

    # Check if user-selected subjects match majors' characteristics and update counters
    for major, subjects in list_of_majors.items():
        if any(subject in user_subjects for subject in map(str.lower, subjects)):
            counter[major] += 1

    # Ask the user a series of questions and update counters based on responses
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
            # Ask the user to rank tied majors until valid input is provided
            while True:
                try:
                    ranked_majors.extend(rank_majors(majors))
                    break
                except ValueError:
                    print("Invalid input. Please try again.")

    print("\nRanked Majors:")
    for index, major in enumerate(ranked_majors, start=1):
        print(f"{index}. {major}")

    return ranked_majors

if __name__ == "__main__":
    major_select()
