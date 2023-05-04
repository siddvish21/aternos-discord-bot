from python_aternos import Client,Status
import os
import interactions

#In the Discord developer portal remember to surely enable messages in privileged intents else it won't work

bot = interactions.Client(os.getenv("TOKEN"))



help_message = "```Available commands:\n" \
               "/startserver - Start the Aternos server.\n" \
               "/serverstatus - Check the status of the Aternos server.\n" \
               "/playercount - Check the number of players on the Aternos server.\n" \
               "/playerlist - Check the list of players on the Aternos server.\n" \
               "/serveraddress - Check the address of the Aternos server.```"


api = Client.from_credentials(os.getenv('ATERNOS_USERNAME'), os.getenv('ATERNOS_PASSWORD'))
servers = api.list_servers()
server = servers[2] #To select a server from a list of servers

@bot.event
async def on_ready():
    print('Bot is ready.')


@bot.command(name="startserver",description="Starts Minecraft Server")
async def startserver(ctx: interactions.CommandContext):
    if server.status_num == Status.on:
        await ctx.send('Server is already **online**!')
    else:
        await ctx.send('Starting Aternos server. Please wait patiently...')
        server.start()
    

@bot.command(name="serverstatus",description="Status of Minecraft Server")
async def serverstatus(ctx: interactions.CommandContext):
    
    status_msg = {
            Status.on: 'Server is online!',
            Status.off: 'Server is offline!',
            Status.starting: 'Server is starting!',
            Status.loading:'Server is Loading',
            Status.preparing:'Server is Preparing'
        }
    await ctx.send(f'```{status_msg[server.status_num]}```')


@bot.command(name="playercount",description="Number of players playing in Minecraft Server")
async def playercount(ctx: interactions.CommandContext):
    await ctx.send(server.players_count)


@bot.command(name="playerlist",description="List of players playing in minecraft server")
async def playerlist(ctx: interactions.CommandContext):
    if server.status_num == Status.off:
        await ctx.send('```The server is currently offline```')
    else:
        if server.players_count == 0:
            await ctx.send('No one is playing right now')
        else:
            list = ''
            for i in range(len(server.players_list)):
                list += str(i + 1) + ") " + str(server.players_list[i]) + '\n'
            await ctx.send(f'```{list}```')


@bot.command(name="serveraddress",description="Address of minecraft Server")
async def serveraddress(ctx: interactions.CommandContext):
    api = Client.from_credentials(os.getenv('ATERNOS_USERNAME'), os.getenv('ATERNOS_PASSWORD'))
    servers = api.list_servers()
    server = servers[2]
    
    await ctx.send(server.address)


@bot.command(name="help",description="Help for all commands")
async def help(ctx: interactions.CommandContext):
    await ctx.send(help_message)


bot.start()
