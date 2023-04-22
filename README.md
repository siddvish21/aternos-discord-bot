# Aternos (Minecraft servers) Discord Bot

You can use this bot to start your minecraft server, get the server status, get the number of players online, and more.
More Details : https://aternos.org/:en/

## Getting Started

1. Clone this repository to your local machine.
2. Install the required libraries using `pip install -r requirements.txt`.
3. Create a Discord bot and get the bot token from the Discord Developer Portal.
4. Enable messages in privileged intents for your bot.
5. Fill in your Aternos credentials in the env file in the ATERNOS_USERNAME and ATERNOS_PASSWORD fields
6. Start the bot using `python bot.py`.

First Start by creating an aternos account or login to an existing one

![](https://github.com/siddvish21/assets/blob/main/login_aternos.gif)

Then create a minecraft server for you

![](https://github.com/siddvish21/assets/blob/main/How_to_create_server.gif)

Next login to discord developer portal and then go to this link https://discord.com/developers/applications

Create a new application like this:

![](https://github.com/siddvish21/assets/blob/main/create_application_discord.gif)


After that go and get the bot token as follows and **paste it in the env file in the TOKEN variable**

![](https://github.com/siddvish21/assets/blob/main/bot_token_reset.gif)


To invite the bot to your discord server you need to generate a url as follows in the gif

![](https://github.com/siddvish21/assets/blob/main/url_generate_discord-bot.gif)

Paste the url in the webbrowser and select the discord server you want it to join and authorise it 

![](https://github.com/siddvish21/assets/blob/main/authorisation_from_link.gif)

After Authorisation it will look like this
![](https://github.com/siddvish21/assets/blob/main/authorised.PNG)

After completing this setup u can use the discord bot by running the python file

This is the Demonstration of the bot starting the server
![](https://github.com/siddvish21/assets/blob/main/server_start_demonstration.gif)

## Usage

### Commands

- `!startserver`: Starts the Aternos server.
- `!serverstatus`: Gets the status of the Aternos server (online, offline, starting).
- `!playercount`: Gets the number of players online on the Aternos server.
- `!playerlist`: Gets the list of players online on the Aternos server.
- `!serveraddress`: Gets the address of the Aternos server.
- `!help`:Shows list of all available commands

### Notes

- If the server is already online and you try to start it, the bot will report that the server is already online.
- If the server is offline and you try to get the number or list of players online, the bot will report that the server is currently offline.

## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.

Please make sure to update tests as appropriate.


## Acknowledgments

This project was inspired by the Python Aternos API Wrapper by Marceau Cuvelier.
