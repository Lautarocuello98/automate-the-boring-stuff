
# 2048 Bot
# Automates the 2048 web game by sending arrow key inputs
# using Selenium.


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time


def main():
    # Start the Chrome browser
    driver = webdriver.Chrome()

    # Open the 2048 game website
    driver.get("https://gabrielecirulli.github.io/2048/")

    # Wait a few seconds to allow the page to load completely
    time.sleep(3)

    # Find the body element of the page
    # We send key presses to this element
    body = driver.find_element(By.TAG_NAME, "body")

    try:
        # Main loop: keep sending moves to the game
        while True:
            body.send_keys(Keys.UP)
            body.send_keys(Keys.RIGHT)
            body.send_keys(Keys.DOWN)
            body.send_keys(Keys.LEFT)

            # Small delay to avoid sending keys too fast
            time.sleep(0.1)

    except KeyboardInterrupt:
        # Allows the user to stop the script with Ctrl+C
        print("Bot stopped by user.")

    finally:
        # Close the browser when finished
        driver.quit()


if __name__ == "__main__":
    main()