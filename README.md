# <img align="left" alt="Python" width="30px" style="padding:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" /> Python Self-bot

`notice! this project is against Discord's ToS and it's only a proof of concept and I cannot recommend using it. Do so at your own risk.`

---

This project is a Discord selfbot powered by [`this`](https://github.com/dolfies/discord.py-self) python selfbot library forked from the original discord.py.

## features

- Custom RPC (Rich Presence) with status
- Automatic emote managment without discord nitro and on every devide mobile/pc.
- emotes add through chat and one simple command.
- config file edit for easier use

### coming soon

- Auto-reply to messages if AFK-mode is toggled

## Available commands

This section might be outdated, so refer to the code for more up to date commands.

command Prefix: `>`
|
this can be aswell changed in code/[`config.json`](./config.json)

- ```>help``` shows a custom help message which only the sender can see.
- ```>available``` alias ```>on``` | this changes the RPC and status to idle
- ```>Work``` changes RPC and turns on "Do Not Disturb" status.
- ```>invisible``` alias ```>off``` | Switches the status to Invisible.
- ```>test``` a simple ping->pong command.
- ```>emote``` sends user defined emotes which are saved in a config file
- ```>addemote``` adds user defined emotes to mentioned before config file.
- ```>removeemote``` simply removes the entry from config.
- ```>reload``` Reloads any of the currently loaded cogs to react to code changes on runtime without having to restart the bot
- ```>load``` Loads a newly created cog on runtime without having to restart the bot

 `config manipulation features are still in progress, they will be done soon tho`

## Project Status

`all of my projects are currently under development so yea not much to say here...`

## Installation

To set up this project, clone this repository

```shell
git clone https://github.com/0MmEga/Self-bot.git
```

---

Set up & enter a virtual environment

```shell
pip install virtualenv
py -m venv .venv
```

for linux/unix:

```shell
source venv/bin/activate
```

for windows (powershell):

```shell
.\venv\Scripts\activate
```

---

Install all required libraries mentioned in the `requirements.txt` file, with this command:

```python
pip install -r requirements.txt
```

---

if you have done everything mentioned above then create a file called `.env` in src directory of the project, and paste the following:

```env
TOKEN=YOUR_DISCORD_TOKEN_HERE
```

replace `YOUR_DISCORD_TOKEN_HERE` with your actual discord token

To obtain your discord token, you can have a look [`here`](https://discordpy-self.readthedocs.io/en/latest/token.html). or just google it.

---

### Usage

To run the selfbot, execute the main.py script as follows:

```python
python3 bot.py
```
