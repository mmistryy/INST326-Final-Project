# Group: Ruthenium 
# Maya Mistry, Evan Schneider
# INST326 (Spring 2024)
# Final Project: Ruthenium's Quiz Game

import json
import random

class QuizGame:
    """
    A class that represents a quiz game with multiple game modes.

    Attributes:
        quiz_data (dict): A dictionary containing quiz data loaded from the JSON file.
        cumulative_score (int): The cumulative score of the player in the current game session.
        correct_answers (int): The number of questions answered correctly.
        current_game_mode (function): The current game mode function being played.
        questions_attempted (int): The total number of questions attempted in the current session.
    """

    def __init__(self, file_name):
        """
        Brings in the quiz game with data from a JSON file.

        Args:
            file_name (str): The name of the JSON file containing quiz questions. Maya
        """
        self.quiz_data = self.load_quiz_data(file_name) 
        self.cumulative_score = 0
        self.correct_answers = 0
        self.current_game_mode = None
        self.questions_attempted = 0

    def load_quiz_data(self, file_name):
        """
        Loads quiz data from the JSON file.

        Args:
            file_name (str): The name of the JSON file containing quiz questions.

        Returns:
            dict: The data loaded from the JSON file. Maya
        """
        with open(file_name, 'r') as file:
            return json.load(file)

    def play_charades(self):
        """Plays the charades game mode.Maya"""
        self.current_game_mode = self.play_charades
        charades_questions = self.quiz_data['charades']
        question = random.choice(charades_questions)
        
        print("\n*** Charades Game Mode ***")
        print("Guess the thing or person based on the charades clues:")
        print("Question:", question['question'])
        
        print("\nClues:")
        for i, clue in enumerate(question['clues'], 1):
            print(f"{i}. {clue}")
        
        guess = input("\nYour guess: ").strip().capitalize()

        if guess == question['answer']:
            print("Nice, that's correct!")
            self.cumulative_score += 1
            self.correct_answers += 1
        else:
            print("Wrong... it's actually:", question['answer'])

        self.questions_attempted += 1
        self.continue_to_next_question()

    def play_riddles(self):
        """Plays the riddles game mode. Maya"""
        self.current_game_mode = self.play_riddles
        riddles = self.quiz_data['riddles']
        question = random.choice(riddles)
        
        print("\n*** Riddles Game Mode ***")
        print("Can you solve this riddle?")
        print("Question:", question['question'])
        
        guess = input("\nYour guess: ").strip().capitalize()

        if guess == question['answer']:
            print("Nice, that's correct!")
            self.cumulative_score += 1
            self.correct_answers += 1
        else:
            print("Wrong... it's actually:", question['answer'])

        self.questions_attempted += 1
        self.continue_to_next_question()

    def play_trivia(self):
        """Plays the trivia game mode. Maya"""
        self.current_game_mode = self.play_trivia
        trivia_questions = self.quiz_data['trivia']
        question = random.choice(trivia_questions)
        
        print("\n*** Trivia Game Mode ***")
        print("Answer the trivia question:")
        print("Question:", question['question'])
        
        guess = input("\nYour answer: ").strip().capitalize()

        if guess == question['answer']:
            print("Nice, that's correct!")
            self.cumulative_score += 1
            self.correct_answers += 1
        else:
            print("Wrong... it's actually:", question['answer'])

        self.questions_attempted += 1
        self.continue_to_next_question()

    def play_again(self):
        """
        Prompts the player to play again or quit.
        If the player chooses to continue, the game state is reset. Maya
        """
        choice = input("Thanks for playing! Would you like to play again? (yes/no): ").strip().lower()
        if choice == 'yes':
            self.reset_game()
            self.run()
        else:
            print("Ok, see you next time!")
    
    def run(self):
        """Starts the quiz game by allowing the user to choose a game mode. Evan"""
        print("Welcome to Ruthenium's Quiz Game!")
        print("What game mode would you like to play?")
        print("1. Charades")
        print("2. Riddles")
        print("3. Trivia")
        
        choice = input("\nEnter your choice: ").strip()

        if choice == '1':
            self.play_charades()
        elif choice == '2':
            self.play_riddles()
        elif choice == '3':
            self.play_trivia()
        else:
            print("Invalid choice. Please try again.")

    def continue_to_next_question(self):
        """
        Continues to the next question or ends the game if the limit of 5 questions is reached.
        Triggers the bonus round if user gets 4+ questions right. Evan
        """
        if self.questions_attempted < 5:
            input("\nPress enter to continue to the next question: ")
            self.current_game_mode()
        else:
            print(f"\nThis is your score: {self.cumulative_score}/5.")
            if self.cumulative_score >= 4:
                self.bonus_round()
            else:
                print("Better luck next time!")
                self.play_again()

    def bonus_round(self):
        """Plays a bonus round if the player scores 4 or 5 out of 5. Evan"""
        try:
            bonus_round_data = self.quiz_data['bonus_round']
            category = random.choice(['charades', 'riddles', 'trivia'])
            bonus_questions = bonus_round_data[category]
            if not bonus_questions:
                raise ValueError("No bonus questions found in the selected category.")

            question = random.choice(bonus_questions)

            print("\n*** Bonus Round ***")
            print("You've earned a bonus question! Answer this:")
            print("Question:", question['question'])

            if 'clues' in question:
                print("\nClues:")
                for i, clue in enumerate(question['clues'], 1):
                    print(f"{i}. {clue}")

            guess = input("\nYour answer: ").strip().capitalize()

            if guess == question['answer']:
                print("Excellent, you got the bonus question right!")
                self.cumulative_score += 1
            else:
                print("Not quite right... the correct answer was:", question['answer'])

            print(f"Final score: {self.cumulative_score}/5.")
        except KeyError:
            print("Error: Bonus round data is missing or improperly formatted.")
        except ValueError as e:
            print(e)

        self.play_again()

    def reset_game(self):
        """Resets the game state to start a new game session. Maya"""
        self.cumulative_score = 0
        self.correct_answers = 0
        self.current_game_mode = None
        self.questions_attempted = 0

if __name__ == "__main__":
    quiz_game = QuizGame('ruthenium_quiz_questions.json')
    quiz_game.run()
