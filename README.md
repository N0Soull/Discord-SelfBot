# Discord Selfbot

made just for fun but maybe i will realse it in feature

## Description

This project is a Discord selfbot powered by [this](https://github.com/dolfies/discord.py-self) python selfbot library forked from the original discord.py The bot is built using Python 3.11.2 and is compatible with Python 3.8 and higher.

Its primary features include:

- Rich presence statuses for being available and actualy everything that discord allows you to do.
- Automatic emote management which doesn't require discord nitro, no matter what client you're on (mobile/PC), this feature is still under developments tho.

## Available commands

This section might be outdated at times, so check the code for more up to date information if you care about it.

Command prefix: ">"

- help (shows a custom help message)
- available/ON (custom RPC saying 'playing with the shotgun trigger')
- Work (custom RPC saying 'playing with my sanity')
- invisible
- test (see if the bot is active)

## Project Status

all of my projects are currently under development...

## Installation

To set up this project, clone this repository or download the source code

Set up & enter a virtual environment

```shell
pip install virtualenv
virtualenv venv
source venv/bin/activate
```

Install all required libraries mentioned in the `requirements.txt` file, with this command:

```python
pip install -r requirements.txt
```

if you have done everything mentioned above then create a file called `.env` in src, having the following text:

```env
TOKEN=YOUR_DISCORD_TOKEN_HERE
```

To obtain your discord token, you can have a look [here](https://discordpy-self.readthedocs.io/en/latest/token.html). or just google it.

### Usage

To run the selfbot, execute the main.py script as follows:

```python
python3 bot.py
```
