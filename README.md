# Aternos Discord Bot

You can use this bot to start your server, get the server status, get the number of players online, and more.

## Getting Started

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Create a Discord bot and get the bot token from the Discord Developer Portal.
4. Enable messages in privileged intents for your bot.
5. Fill in your Aternos credentials in the `on_message` function of the `bot.py` file.
6. Start the bot using `python bot.py`.

## Usage

### Commands

- `!startserver`: Starts the Aternos server.
- `!serverstatus`: Gets the status of the Aternos server (online, offline, starting).
- `!playercount`: Gets the number of players online on the Aternos server.
- `!playerlist`: Gets the list of players online on the Aternos server.
- `!serveraddress`: Gets the address of the Aternos server.

### Notes

- If the server is already online and you try to start it, the bot will report that the server is already online.
- If the server is offline and you try to get the number or list of players online, the bot will report that the server is currently offline.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Acknowledgments

This project was inspired by the Python Aternos API Wrapper by Marceau Cuvelier.
