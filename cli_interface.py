from prompt_toolkit import PromptSession, print_formatted_text
from prompt_toolkit.formatted_text import HTML
from prompt_toolkit.patch_stdout import patch_stdout
from datetime import datetime, timedelta
import asyncio

prompt_session = PromptSession()

# ANSI color codes
class Colors:
    GREEN = "\033[92m"  # Bright Green
    YELLOW = "\033[93m"  # Bright Yellow
    BLUE = "\033[94m"    # Bright Blue
    RED = "\033[91m"     # Bright Red
    RESET = "\033[0m"    # Reset to default color

def display_welcome():
    print("=" * 40)
    print(f"{Colors.GREEN}Welcome to the Shell Skills Tester!{Colors.RESET}")
    print("=" * 40)

async def get_difficulty():
    difficulty = await prompt_session.prompt_async(HTML("<ansiyellow>Choose difficulty (easy/medium/hard): </ansiyellow>"))
    return difficulty.lower()

def display_question(question, current_num, total):
    print_formatted_text(HTML(f"\n<ansiblue>Question {current_num}/{total}</ansiblue>\n" + "=" * 40 + f"\n<ansiblue>Task: {question['task']}</ansiblue>\n"))

async def display_question_and_timer(question, current_num, total, time_limit):
    end_time = datetime.now() + timedelta(seconds=time_limit)
    user_input = ""

    def get_remaining_time():
        return max((end_time - datetime.now()).total_seconds(), 0)

    display_question(question, current_num, total)

    async def update_timer():
        while get_remaining_time() > 0:
            print(f"\rTime remaining: {get_remaining_time():.1f}s", end="", flush=True)
            await asyncio.sleep(0.1)
        print()  # Move to the next line after timer expires

    async def get_input():
        nonlocal user_input
        with patch_stdout():
            while get_remaining_time() > 0:
                user_input = await prompt_session.prompt_async(
                    HTML("\n<ansiyellow>Enter your command: </ansiyellow>")
                )
                break  # Exit after first input
            print(f"\nYou entered: {user_input}")

    timer_task = asyncio.create_task(update_timer())
    input_task = asyncio.create_task(get_input())

    done, pending = await asyncio.wait(
        [timer_task, input_task],
        return_when=asyncio.FIRST_COMPLETED
    )

    for task in pending:
        task.cancel()

    return get_remaining_time(), user_input

def display_result(is_correct, explanation, remaining_time):
    print("\n" + "=" * 40)
    if is_correct:
        print(f"{Colors.GREEN}Correct!{Colors.RESET}")
    else:
        print(f"{Colors.RED}Incorrect.{Colors.RESET}")
    print(f"Time remaining: {remaining_time:.1f}s")
    print("=" * 40)
    print("Explanation:")
    print(explanation)
    print("=" * 40 + "\n")

def display_final_score(score, total):
    percentage = (score / total) * 100
    print("\n" + "=" * 40)
    print(f"Final Score: {score}/{total} ({percentage:.1f}%)")
    if percentage >= 90:
        print(f"{Colors.GREEN}Excellent job! You're a shell master!{Colors.RESET}")
    elif percentage >= 70:
        print(f"{Colors.YELLOW}Good work! Keep practicing to improve.{Colors.RESET}")
    else:
        print(f"{Colors.RED}You might want to study more. Don't give up!{Colors.RESET}")
    print("=" * 40 + "\n")