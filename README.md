# Discord Selfbot

A Discord.py Selfbot

## Description

This project is a Discord selfbot powered by [this](https://github.com/dolfies/discord.py-self) python selfbot library forked from the original discord.py library. The bot is built using Python 3.10.11 and is compatible with Python 3.8 and higher.

Its primary features include:

- Rich presence statuses for being available, school/work, sleeping & doing homework
- Automatic emote management which doesn't require discord nitro, no matter what client you're on (mobile/PC)

## Available commands

This section might be outdated at times, so check the code for more up to date information if you care about it.

Command prefix: >>>

- test (see if the bot is active)
- help (shows a custom help message)
- available (custom RPC saying 'Watching \<user> being lazy')
- sleep (custom RPC saying 'Watching \<user> sleep')
- school (custom RPC saying 'Watching \<user> suffer at school')
- homework (custom RPC saying 'Watching \<user> doing homework')
- emote (command to use any of the following emotes: `troll`, `trolla`, `crackcat`, `zzzcat`, `zzzcatconfused`, `zzzcathappy`, `5head`, `kekwdisco`, `sadangry`, `edits`, `fastsmh`, `catjamfast`, `bruh`, `sus`)

## Project Status

This project is currently under development. New features could be added at any time.

## Prerequisites

To run this project, you need Python 3.8 or higher.

## Installation

To set up this project, clone this repository with the following command:
```shell
git clone https://gitlab.com/TherioJunior/discord-selfbot
```
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
Afterwards, create a file called `.env`, having the following text:
```
TOKEN=YOUR_DISCORD_TOKEN_HERE
```
To obtain your discord token, you can have a look [here](https://discordpy-self.readthedocs.io/en/latest/token.html).

## Usage
To run the selfbot, execute the main.py script as follows:
```python
python3 bot.py
```
