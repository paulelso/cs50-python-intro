import datetime
import inflect

def main():
    # Prompt the user for their date of birth and convert the input to a datetime object
    dob = input("Date of birth: ")
    print(convert_minutes_to_words(convert_date_to_minutes(dob)))

def convert_date_to_minutes(date):
    # Get today's date
    current_date = datetime.date.today()
    try:
        # Convert the input to a datetime object
        date_object = datetime.datetime.strptime(date, "%Y-%m-%d").date()
    except ValueError:
        print("Invalid date")
        exit(1)
    # Calculate the age in minutes
    age_in_minutes = (current_date - date_object).days * 24 * 60   
    return age_in_minutes

def convert_minutes_to_words(minutes):    
    # Create an instance of the inflect engine
    p = inflect.engine()    
    # Convert minutes to English words
    minutes_in_words = p.number_to_words(minutes)    
    # Capitalize the words
    capitalized_minutes_in_words = minutes_in_words.capitalize().replace(" and ", " ") + " minutes"
    return capitalized_minutes_in_words

if __name__ == "__main__":
    main()