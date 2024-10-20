
import pyautogui
import time
import logging
import random
import os
import psutil

# Written by Idlan bin Hafiz

# Configure logging for automated testing
logging.basicConfig(filename="game_automation.log", level=logging.INFO, format="%(asctime)s - %(message)s")

# Simulate player actions using pyautogui
def simulate_player_movement():
    try:
        logging.info("Starting player movement simulation.")
        
        # Simulate walking forward (e.g., pressing the 'W' key)
        pyautogui.keyDown('w')
        time.sleep(random.uniform(2, 5))  # Walk forward for a random duration
        pyautogui.keyUp('w')
        logging.info("Player walked forward.")
        
        # Simulate jumping (pressing the spacebar)
        pyautogui.press('space')
        logging.info("Player jumped.")
        time.sleep(1)
        
        # Simulate interacting with an object (pressing 'E')
        pyautogui.press('e')
        logging.info("Player interacted with an object.")
        time.sleep(1)

    except Exception as e:
        logging.error(f"Error during movement simulation: {str(e)}")
        capture_screenshot()

# Capture screenshot of the game if an error occurs
def capture_screenshot():
    screenshot = pyautogui.screenshot()
    screenshot.save("error_screenshot.png")
    logging.info("Screenshot saved due to an error.")

# Log performance data (FPS and memory usage)
def log_performance_data():
    fps = random.uniform(40, 60)  # Mock FPS data (replace with actual FPS reading)
    memory_usage = psutil.virtual_memory().percent  # Memory usage in percentage
    
    logging.info(f"FPS: {fps}, Memory Usage: {memory_usage}%")
    return fps, memory_usage

# Main test loop with performance logging
def run_automation_test_with_performance():
    for i in range(5):  # Run the test multiple times
        logging.info(f"Starting test iteration {i + 1}.")
        simulate_player_movement()
        
        # Log performance data after each action
        fps, memory_usage = log_performance_data()
        
        # Check for performance issues
        if fps < 30 or memory_usage > 80:
            logging.warning(f"Performance issue detected: FPS {fps}, Memory Usage {memory_usage}%")
        
        time.sleep(2)  # Pause between actions

if __name__ == "__main__":
    run_automation_test_with_performance()
