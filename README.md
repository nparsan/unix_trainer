# unix_trainer

A CLI interface to practice shell scripts with automatic question creation and grading.

## Table of Contents
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [UI](#ui)
- [Implementation](#implementation)
- [Contributing](#contributing)
- [License](#license)

## Features

- Interactive CLI interface
- Automatic question generation for shell script practice
- Instant grading and feedback
- Progressive difficulty levels

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/nparsan/unix_trainer.git
   cd unix_trainer
   ```

2. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Configuration

Create a `.env` file in the root directory of the project and include your Gemini API key in the following format:
```bash
GEMINI_API_KEY=your_api_key
```

## Usage

1. Run the main script:
   ```bash
   python main.py
   ```

2. Follow the on-screen prompts to select difficulty level and answer questions.

3. Receive instant feedback and grading for your responses.

## UI

![Q/A UI][https://github.com/nparsan/unix_trainer/blob/main/screenshots/Screenshot%202024-09-04%20at%2011.48.56.png]

## Implementation

The `unix_trainer` project is structured to provide an interactive CLI for practicing shell scripting. It utilizes the Gemini API for automatic question generation. 

### Key Components:

- **Main Script**: The entry point (`main.py`) manages the flow of the application, including user interactions and question handling.
- **Question Generation**: The `create_questions.py` module generates questions using the Gemini API. It constructs prompts to request questions about Linux shell navigation and scripting.
- **Question Management**: The `question_manager.py` module loads, saves, and selects questions, ensuring users receive a varied experience without repetition.
- **Response Checking**: The `response_checker.py` module evaluates user answers and provides feedback, including explanations for incorrect responses.
- **User Interface**: The`cli_interface.py` module handles the display of questions and results

### Features:

- Interactive CLI for user engagement.
- Automatic generation of questions using the Gemini API.
- Instant feedback and grading for user responses.
- Support for multiple difficulty levels.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the [MIT License](LICENSE).

