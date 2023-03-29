# TinderBot

## Overview
TinderBot is an automation script that logs into your Tinder account using your Facebook credentials, automates swiping right, closes match pop-ups, and sends custom, AI-generated messages to your matches. This script is written in Python and uses Selenium WebDriver, OpenAI GPT-3 (text-davinci-002), and Tinder's web platform.

## Dependencies
To use TinderBot, you'll need to have the following dependencies installed:

- Python 3.x
- Selenium WebDriver
- OpenAI Python library
You can install the Selenium WebDriver and OpenAI Python library using pip:

```
pip install selenium openai
```

Also, make sure to have the appropriate WebDriver for your browser installed. This example uses Chrome WebDriver. You can download it from the following link and add it to your system's PATH:

https://sites.google.com/a/chromium.org/chromedriver/downloads

## Configuration
In the config.py file, add your Facebook email, password, and OpenAI API key. This information is necessary for the bot to log into your Tinder account and to generate AI-generated text.

Example `config.py`:

```
email = "your_facebook_email@example.com"
password = "your_facebook_password"
api_key = "your_openai_api_key"
```

## How to Use TinderBot
1. Ensure all dependencies are installed and your config.py file contains the necessary information.
2. Run the TinderBot script using the following command:

```
python tinderbot.py
```

3. The script will launch a Chrome browser and navigate to Tinder's web platform. It will then log in using your provided Facebook credentials.

By default, the bot will not perform any action after logging in. Uncomment one of the following lines in the script to either auto-swipe or send messages to your matches:

```
# bot.auto_swipe()
# bot.send_messages_to_matches()
```

For auto-swiping, the bot will continuously swipe right on profiles. If a match occurs, the bot will automatically close the match pop-up and continue swiping.

For sending messages, the bot will send custom, AI-generated messages to your matches based on their names. The message prompts are randomly chosen from a list of pre-defined options.

## Note
Use TinderBot at your own risk. Automating actions on Tinder might violate their terms of service, which could lead to account suspension or termination. This script is intended for educational purposes and should not be used to harass or spam other users.
