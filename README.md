# <img align="left" alt="Python" width="30px" style="padding:5px;" src="https://cdn.jsdelivr.net/gh/devicons/devicon/icons/python/python-plain.svg" /> Python Self-bot

`notice! This project violates Discord's ToS and it's only a proof of concept and I cannot recommend using it. Do so at your own risk.`

---

This project is a Discord selfbot powered by [`this`](https://github.com/dolfies/discord.py-self) python selfbot library forked from the original discord.py.

## features

- Custom RPC (Rich Presence) with status change
- Automatic emote managment without discord nitro and on every device mobile/pc.
- emotes add through chat and one simple command
- config file edit for easier use
- automatic embed replacement
- info logging

### coming soon

(Section outdated, no plans at the moment)

## Available commands

This list might be outdated, consult the code for updated commands.

command Prefix: `>`
|
this can be aswell changed in code/[`config.json`](./config.json)

- ```>help``` custom help message visible only to the sender.
- ```>available``` alias ```>on``` | this changes the RPC and status to idle
- ```>Work``` changes RPC and turns on "Do Not Disturb" status.
- ```>invisible``` alias ```>off``` | Switches the status to Invisible.
- ```>test``` a simple ping->pong command.
- ```>emote``` sends user defined emotes which are saved in a config file
- ```>addemote``` adds user defined emotes to mentioned before config file.
- ```>removeemote``` simply removes the entry from config.
- ```>reload``` Reloads any of the currently loaded cogs to react to code changes on runtime without having to restart the bot
- ```>load``` Loads a newly created cog on runtime without having to restart the bot
- ```>debug``` switches the debug mode ON/OFF
- ```>logout``` simply logs out the bot
- ```>restart``` restarts bot.py
- ```>rpc```accepts all availiable presence parameters and a custom message
- ```>status``` simply changes the status

## Project Status

`Project finished and ready for use. Feel free to report issues or errors.`

## Installation

To set up this project, clone this repository

```shell
git clone https://github.com/N0Soull/Discord-SelfBot.git
```

---

### Set up & enter a virtual environment

`for linux/unix:`

install and create the virtual enviroment

```bash
pip install virtualenv
virtualenv .venv
```

then activate it

```shell
source .venv/bin/activate
```

`for windows (powershell):`

install and create install and create the virtual environment

```shell
pip install virtualenv
python -m venv .venv
```

then activate it

```shell
.venv\Scripts\activate
```

---

Install necessary dependencies listed in `requirements.txt`:

```python
pip install -r requirements.txt
```

---

if you have done everything mentioned above then create a file called `.env` in the directory of the project and paste the following into the new `.env` file:

```env
TOKEN=YOUR_DISCORD_TOKEN_HERE
```

replace `YOUR_DISCORD_TOKEN_HERE` with your actual discord token

To obtain your discord token, you can have a look [`here`](https://discordpy-self.readthedocs.io/en/latest/token.html), or search online.

---

### Usage

To run the selfbot, execute the python script as follows:

```python
python3 bot.py
```
