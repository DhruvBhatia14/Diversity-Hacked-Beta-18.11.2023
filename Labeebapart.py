# Improved version with a more interactive user experience

majors_data = {
    'Computer Science': ['programming', 'logical thinking', 'mathematics'],
    'Business Administration': ['leadership', 'communication', 'organization'],
    'Psychology': ['empathy', 'communication', 'analytical skills'],
    # Add more majors and associated characteristics as needed
}

def suggest_major(user_characteristics):
    scores = {major: len(set(user_characteristics) & set(characteristics)) for major, characteristics in majors_data.items()}
    sorted_majors = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    return sorted_majors[0][0]

def get_user_characteristics():
    characteristics = input("Enter your characteristics (separated by commas): ").split(',')
    return [characteristic.strip() for characteristic in characteristics]

def display_suggested_major(major):
    print(f"We suggest considering the major: {major}")

def main():
    print("Welcome to the College Major Suggestion Program!")
    
    while True:
        try:
            user_characteristics = get_user_characteristics()
            suggested_major = suggest_major(user_characteristics)
            display_suggested_major(suggested_major)
        except KeyboardInterrupt:
            print("\nExiting the program. Goodbye!")
            break
        except Exception as e:
            print(f"An error occurred: {e}")
        
        another_try = input("Do you want to try again? (yes/no): ").lower()
        if another_try != 'yes':
            print("Exiting the program. Goodbye!")
            break

if __name__ == "__main__":
    main()
