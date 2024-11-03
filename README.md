# Work Shift Management Telegram Bot

A Telegram bot for managing work shifts, breaks, and administrative oversight.

## Features

- Start/end work shifts
- Manage breaks (lunch, smoke, restroom)
- Break time limits and warnings
- Admin notifications for violations
- Automatic shift end at 2 AM

## Setup

1. Create a `.env` file from `.env.example`:
   ```bash
   cp .env.example .env
   ```

2. Update `.env` with your:
   - Telegram Bot Token (from @BotFather)
   - Admin user IDs (comma-separated)

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

4. Run the bot:
   ```bash
   python main.py
   ```

## Commands

- `/start` - Show help message
- `/start_shift` - Start work shift
- `/end_shift` - End work shift
- `/break <type>` - Start break (lunch/smoke/restroom)
- `/end_break` - End current break

## Break Time Limits

- Lunch: 30 minutes
- Smoke: 10 minutes
- Restroom: 5 minutes

Exceeding these limits triggers admin notifications.