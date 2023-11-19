import re
from majors_data import list_of_majors, counter, ordered_questions_chars, school_subjects

class MajorSelector:
    def __init__(self):
        self.list_of_majors = list_of_majors
        self.counter = counter
        self.ordered_questions_chars = ordered_questions_chars
        self.school_subjects = school_subjects

    def ask_question(self, question, characteristics):
        while True:
            y = input(f"{question} (yes/no/not sure): ").lower()
            if y in ("yes", "no", "not sure"):
                modifier = 1 if y == "yes" else (-1 if y == "no" else 0)
                for major, subjects in self.list_of_majors.items():
                    if any(characteristic in subjects for characteristic in characteristics):
                        self.counter[major] += modifier
                break
            else:
                print("Invalid input. Please enter 'yes,' 'no,' or 'not sure.'")

    def run_questions(self):
        for question, characteristics in self.ordered_questions_chars.items():
            self.ask_question(question, characteristics)

    def rank_majors(self, majors):
        # This method is used for ranking majors when there is a tie based on user preferences.
        while True:
            try:
                # Prompting the user to enter their rankings, separated by commas.
                ranking_input = input("Enter the rankings separated by commas (most preferred to least preferred): ").strip()

                # Validate the input to ensure no leading or trailing commas and the format is correct.
                if ranking_input.startswith(",") or ranking_input.endswith(","):
                    raise ValueError("Please remove leading or trailing commas.")
                if not re.match(r'^\d+(,\d+)*$', ranking_input):
                    raise ValueError("Invalid input. Please enter valid numbers separated by commas.")

                # Converting the string input into a list of integers.
                ranking_list = [int(rank) for rank in ranking_input.split(',')]

                # Checking if the length of the ranking list matches the number of majors.
                if len(ranking_list) != len(majors):
                    raise ValueError("The number of rankings does not match the number of majors.")

                # Checking for duplicate rankings.
                if len(set(ranking_list)) != len(ranking_list):
                    raise ValueError("Duplicate rankings detected. Each rank must be unique.")

                # Ensuring that the rankings are within the valid range.
                if any(rank <= 0 or rank > len(majors) for rank in ranking_list):
                    raise ValueError("Invalid ranking. Please enter numbers within the range.")

                # Creating a dictionary to map the rankings to their respective majors.
                ranked_dict = {index: majors[index - 1] for index in ranking_list}

                # Compiling the final ranked list of majors based on user input.
                majors_ranked = [ranked_dict[index] for index in range(1, len(majors) + 1)]

                return majors_ranked

            except ValueError as e:
                # Handling any value errors in user input.
                print(f"Error: {e}")
                print("Please try again.")


    def major_select(self):
        print("Available school subjects:", self.school_subjects)
        while True:
            user_input = set(input("Enter your preferred school subjects (separated by commas): ").strip().lower().split(','))
            user_subjects = [subject.strip() for subject in user_input]
            if all(subject in self.school_subjects for subject in user_subjects):
                break
            else:
                invalid_subjects = [subject for subject in user_subjects if subject not in self.school_subjects]
                print(f"Invalid subjects: {', '.join(invalid_subjects)}. Please enter valid subjects such as:", self.school_subjects)
        
        for major, subjects in self.list_of_majors.items():
            if any(subject in user_subjects for subject in map(str.lower, subjects)):
                self.counter[major] += 1
        
        self.run_questions()
        
#        for major, total_count in self.counter.items():
#            print(f"Total count for {major}: {total_count}")

        sorted_majors = sorted(self.counter.items(), key=lambda x: x[1], reverse=True)
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
                print("\nList of majors to rank:")
                for index, major in enumerate(majors, start=1):
                    print(f"{index}. {major}")
                while True:
                    try:
                        ranked_majors.extend(self.rank_majors(majors))
                        break
                    except ValueError:
                        print("Invalid input. Please try again.")

        print("\nRanked Majors:")
        for index, major in enumerate(ranked_majors, start=1):
            print(f"{index}. {major}")

        return ranked_majors

if __name__ == "__main__":
    major_selector = MajorSelector()
    major_selector.major_select()