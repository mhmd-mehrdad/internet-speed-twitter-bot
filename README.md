# Internet Speed Twitter Bot

A Python browser-automation project that runs an internet speed test and posts a message about the measured speeds using a **training social-media service**.
> **Note:** This project uses the course's simulated **Y** social-media service (`app.100daysofpython.dev`), **not the real X/Twitter platform**.

## Features

- Opens Speedtest.net and starts a speed test.
- Reads the displayed download and upload speeds.
- Signs into the course's simulated Y service using credentials stored locally.
- Publishes a message comparing the measured speeds with the configured promised speeds.

## Technologies

- Python
- Selenium WebDriver
- python-dotenv
- Google Chrome

## Setup

1. Clone the repository and open the project folder.
2. Create and activate a Python virtual environment (optional but recommended):
   ```powershell
   python -m venv .venv
   .\.venv\Scripts\Activate.ps1
   ```
3. Install dependencies:
   ```powershell
   python -m pip install -r requirements.txt
   ```
4. Make a local copy of the configuration template:
   ```powershell
   Copy-Item .env.example .env
   ```
5. Open `.env` and enter your **own** credentials for the course's Y service. Change `PROMISED_DOWN` and `PROMISED_UP` if needed.
6. Make sure Google Chrome is installed, then run:
   ```powershell
   python main.py
   ```

## Project Structure

```text
internet-speed-twitter-bot/
├── main.py
├── README.md
├── requirements.txt
├── .env.example
└── .gitignore
```

Create `.env` locally; it is deliberately excluded from version control.

## Limitations

- This is a learning/demo project, not a production bot.
- The current code **posts after every test**; it does not check whether the measured speed is below the promised speed before posting.
- The browser automation uses page-specific XPath selectors and fixed delays; changes to either website can break it.
- The test can take over a minute to complete.

## Security

Never commit `.env`, passwords, API keys, or session tokens. `.env.example` contains only placeholders.
