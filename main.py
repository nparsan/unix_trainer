import cli_interface
import question_manager
import response_checker
import config
import utils
import asyncio

async def main():
    cli_interface.display_welcome()
    difficulty = await cli_interface.get_difficulty()
    used_questions = []
    total_questions = 0
    total_score = 0
    
    while total_questions < config.QUESTIONS_PER_GAME:
        remaining_questions = config.QUESTIONS_PER_GAME - total_questions
        questions = question_manager.select_questions(difficulty, remaining_questions, used_questions)
        
        if not questions:
            break
        
        for question in questions:
            remaining_time, user_response = await cli_interface.display_question_and_timer(question, total_questions + 1, config.QUESTIONS_PER_GAME, config.TIME_LIMIT)
            
            sanitized_response = utils.sanitize_input(user_response)
            is_correct, explanation = response_checker.check_response(question, sanitized_response)
            
            cli_interface.display_result(is_correct, explanation, remaining_time)
            
            if is_correct:
                total_score += config.CORRECT_ANSWER_POINTS
                if remaining_time > config.TIME_BONUS_THRESHOLD:
                    total_score += config.TIME_BONUS_POINTS
            
            question_manager.mark_question_as_used(question, used_questions)
            total_questions += 1
    
    # Ensure total_questions does not exceed the maximum allowed
    total_questions = min(total_questions, config.QUESTIONS_PER_GAME)
    cli_interface.display_final_score(total_score, total_questions)

if __name__ == "__main__":
    asyncio.run(main())