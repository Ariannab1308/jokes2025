# ARIANNA BARRERA, CHLOE DOUGHERTY :)
jokes = {
    "robbers": ["Knock knock", "Calder", "Calder police — I've been robbed!"],
    "tanks": ["Knock knock", "Tank", "You're welcome!"],
    "pencils": ["Knock knock", "Broken pencil", "Nevermind — it's pointless!"]
}
# This shows a list abstraction, as the jokes are stored in a dictionary with keys 
# representing the joke types and values being lists of strings that make up the jokes.
def tell_joke(joke_key):
    for line in jokes[joke_key]:
        input(line)  # user presses enter to continue 
# this shows the use of abstraction, 
# as the jokes are stored in a dictionary and accessed through a function
# for a cleaner and more organized code structure.
# The tell_joke function abstracts away the details of how the jokes are stored and presented
# allowing the main function to focus on the flow of the game.
def get_joke_choice():
     while True:
        choice = input("Choose a joke: robbers, tanks, or pencils: ").lower()
        if choice in jokes:
            return choice
        print("Invalid choice. Try again.")
# this shows the use of sequencing, 
# as the steps are executed in a specific order to achieve the desired outcome.
# The user is first asked if they want to hear a joke, 
# then they are prompted to choose a joke, and finally, 
# they are asked if they want to hear another joke or if they are finished.
def main():
    start = input("Do you want to hear a joke? (yes/no): ").lower()

    if start == "no":
        print("Okay, maybe next time!")
        return
# The while loop allows the user to continue 
# hearing jokes until they choose to finish.
# it is an example of iteration, as it allows the user to 
# repeat the joke-telling process multiple times based on their input.
    while start == "yes":
        print("Great! Let's play.")
        joke_choice = get_joke_choice()
        tell_joke(joke_choice)

        start = input("Do you want to hear another joke or are you finished? ").lower()
# After the user finishes hearing jokes, 
# they are prompted to rate the game 
# and provide feedback on if they would recommend it to others.
    if start == "finished":
        rating = int(input("Please rate our game 1–10: "))
        score = rating * 10
        print(str(score) + "% satisfaction rate")

        recommend = input("Would you recommend this game to a friend? ").lower()
        if recommend in ["yes", "maybe"]:
            print("Thanks, we appreciate it!")
        else:
            print("Sorry you didn’t enjoy it.")
# The program ends with a thank you message for the user’s time and feedback.
    print("Thank you for playing our joke game!")
main()
# runs the program by calling the main function, 
# which is the entry point of the application.