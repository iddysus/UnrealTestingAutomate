
# Game Automation Testing Tool

This tool automates basic game testing tasks by simulating player actions such as movement, jumping, and interacting with objects. It also logs performance data such as FPS and memory usage, and captures screenshots in case of errors.

## Features
- **Simulates Player Actions**: Simulates keyboard inputs like walking, jumping, and interacting with objects.
- **Logs Performance**: Tracks FPS and memory usage after each action.
- **Captures Errors**: Takes a screenshot if an error occurs during the test.

## Setup
1. Install Python 3.x if you don't have it.
2. Install the necessary libraries:
   ```bash
   pip install pyautogui psutil
   ```

## Usage
1. Run the automation tool:
   ```bash
   python game_automation_tool.py
   ```

2. The tool will simulate player actions and log performance data in `game_automation.log`. If any issues occur, a screenshot will be saved as `error_screenshot.png`.
