"""Command Line Quiz"""
# pylint: disable=redefined-outer-name
#  pylint: disable=line-too-long

from argparse import ArgumentParser
import random
import requests
from rich.console import Console
from rich.panel import Panel
from rich.style import Style
from rich.columns import Columns

# Styles:
WARNING_STYLE = Style(color="#FF6F61", italic=True, bold=True)

# Error Classes:


class NonExistentDifficulty(Exception):
    """Error for difficulty entered not in ["easy", "medium", "hard"]"""

    def __init__(self, message="Difficulty can only be easy, medium or hard."):
        self.message = message
        super().__init__(self.message)


class InvalidNumber(Exception):
    """Error for invalid number input"""

    def __init__(self, message="Please enter a valid number."):
        self.message = message
        super().__init__(self.message)


# Functions

def get_question_data(category_id, difficulty: str = "easy", no_questions: str = "1") -> dict:
    """Load question data from API"""

    difficulty_levels = ["easy", "medium", "hard"]
    if difficulty not in difficulty_levels:
        raise NonExistentDifficulty()

    if no_questions.isalpha():
        raise InvalidNumber()

    number_questions = int(no_questions)
    if number_questions > 10 or number_questions < 1:
        raise ValueError("Quiz can only have 1 - 10 questions.")

    url = f"https://opentdb.com/api.php?amount={
        int(no_questions)}&difficulty={difficulty}&category={category_id}"
    response = requests.get(url, timeout=10)
    data = response.json()

    return data["results"]


def parse_arguments():
    """Get command line arguments"""
    parser = ArgumentParser()
    parser.add_argument("--difficulty", "-d",
                        help="Select difficulty level.", default="easy")
    parser.add_argument(
        "--amount", "-a", help="Number of questions in quiz", default="1")
    return parser.parse_args()


def pose_question(question_data: list) -> int:
    """Main game play function"""
    score = 0
    for question in question_data:
        question_posed = question["question"]
        console.print(f"\n [thistle1]{question_posed}\n")
        correct_answer = question["correct_answer"]
        answers = question["incorrect_answers"]
        answers.append(correct_answer)
        random.shuffle(answers)
        for index, answer in enumerate(answers):
            console.print(f"[bold #008080]{
                          index + 1}[/bold #008080] : {answer}")

        max_value = len(answers)
        answer = get_answer_input(max_value)
        if check_answer_correct(answer, answers, correct_answer):
            console.print(
                "\n[#98FF98]Correct! You get [bold]1[/bold] point!\n")
            score += 1
        else:
            console.print("\n[#DC143C]Nope. [bold]No[/bold] points for you.\n")
            console.print(f"[thistle1]The [bold #98FF98]correct[/bold #98FF98] answer was: {
                correct_answer}")

    percentage_score = (score / len(question_data)) * 100
    console.print(f"[thistle1]You answered [#98FF98]{score}/{len(question_data)
                                                             }[/#98FF98] ({int(percentage_score)}%) questions correct.\n")


def get_answer_input(max_value: int = 4) -> int:
    """Function gets input from user"""

    while True:
        user_answer = console.input("\n[#ffd7ff]Enter your answer here: ")
        if user_answer.isalpha():
            console.print("Please enter a valid number.", style=WARNING_STYLE)
            continue

        if not 1 <= int(user_answer) <= max_value:
            console.print("Please enter a valid number.", style=WARNING_STYLE)
            continue

        return int(user_answer)


def check_answer_correct(answer: int, possible_answers: list, correct_answer: str) -> bool:
    """function to check if answer is correct"""

    correct_index = (possible_answers.index(correct_answer))+1
    return answer == correct_index


def get_categories() -> list:
    """display categories for user to choose from."""
    url = "https://opentdb.com/api_category.php"
    response = requests.get(url, timeout=10)
    data = response.json()
    results = data["trivia_categories"]
    # want to get id and category corresponding to print and display

    category_renderables = [
        Panel(f"{category["name"]} (ID: [bold #FFFACD]{category["id"]}[/bold #FFFACD])", expand=True) for category in results]
    console.print(Columns(category_renderables,
                  width=40, equal=True, expand=True))
    print(type(results))
    return results


def pick_category(results: list):
    """Let the user choose the category to play."""
    while True:
        category_choice = console.input(
            "\n[bold #E6E6FA]Enter the category ID: ")
        for category in results:
            if int(category_choice) == category["id"]:
                console.print(f"\nYou have picked [dark_slate_gray2]{
                              category["name"]}[/dark_slate_gray2].\n")
                return category["id"]
        console.print("Please enter a valid category ID.\n",
                      style=WARNING_STYLE)


def main_game(console: Console):
    """Main game play function with console styling."""

    console.rule("[bold #E6E6FA]:classical_building: :brain:The Quiztine Chapel:brain::classical_building:",
                 style="[gray]")
    arguments = parse_arguments()
    difficulty = arguments.difficulty
    num_questions = arguments.amount

    console.print(
        "\nWelcome to the Quiz! These are the categories:", justify="center")
    results = get_categories()
    category = pick_category(results)
    questions = get_question_data(category, difficulty, num_questions)
    console.rule(
        "\n:sparkles::scroll:[bold #E6E6FA]In the name of knowledge, let us begin!:scroll::sparkles:", style="[gray]")

    pose_question(questions)
    console.rule(
        ":crystal_ball::seedling::book:[bold #E6E6FA]Your pilgrimage of knowledge ends here… until next time!:book::seedling::crystal_ball:", style="[gray]")


if __name__ == "__main__":
    console = Console()
    main_game(console)
