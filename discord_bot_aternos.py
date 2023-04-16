
import discord
from python_aternos import Client
from python_aternos import Status
import os
from dotenv import load_dotenv
load_dotenv()

# Set up Discord client with message PRIVILEGED intents enabled in DEVELOPER PORTAL
intents = discord.Intents(messages=True)
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
  print('Bot is ready.')


@client.event
async def on_message(message):
  
  # Fill in your ATERNOS CREDENTIALS in env file
  api = Client.from_credentials(os.getenv('USERNAME'), os.getenv('PASSWORD'))

  # Get list of Aternos servers and select the first one
  servers = api.list_servers()
  server = servers[1]

  # If command is !startserver,then start the Aternos server
  if message.content == '!startserver':
    if server.status_num == Status.on:
      await message.channel.send('Server is already online!')
    else:
      await message.channel.send(
        'Starting Aternos server. Please wait patiently...')
      try:
        server.start()
      except:
        await message.channel.send('The server is already Online.')

  # If command is !serverstatus, send the status of the Aternos server in the discord channel
  elif message.content == '!serverstatus':
    if server.status_num == Status.on:
      await message.channel.send('Server is online!')
    if server.status_num == Status.off:
      await message.channel.send('Server is offline!')
    if server.status_num == Status.starting:
      await message.channel.send('Server is Starting!')

  # If command is !playercount, send the number of players on the Aternos server in the Discord channel
  elif message.content == "!playercount":
    await message.channel.send(server.players_count)

  # If command is !playerlist, send the list of players on the Aternos server in  the Discord channel
  elif message.content == "!playerlist":
     if server.status_num == Status.off:
       await message.channel.send("The server is currently offline")
     else:       
      if server.players_count==0:  
        await message.channel.send("No one is playing right now")
      else:
        await message.channel.send(server.players_list)

  # If command is !serveraddress,send the address of the Aternos server  to the Discord channel
  elif message.content == "!serveraddress":
    await message.channel.send(server.address)

#Enter the discord token below.
client.run(os.getenv('TOKEN'))
