import discord
from pycoingecko import CoinGeckoAPI
import asyncio

token = 'TOKEN_ID'
guildName = "SERVER_NAME"
botToken = 'YOUR_TOKEN'


async def update(price, change):
    print('activity')
    try:
        if (float(change) > 0):
            stt = discord.Status.online
            change = "+" + change
        else:
            stt = discord.Status.dnd
        await client.change_presence(
            status=stt,
            activity=discord.Activity(type=discord.ActivityType.watching,
                                      name=change + "%" +
                                      " | BTC/USD Coingecko"))
        guild = [guild for guild in client.guilds if guild.name == guildName]
        await guild[0].me.edit(nick="BTC $" + price)
        print('name')

    except Exception as e:
        print(e)
    print('updated')


async def main():
    while True:
        try:
            coin = cg.get_price(include_24hr_change='true',
                                ids=token,
                                vs_currencies='usd')
            print(coin[token]['usd'])
            price = str("{:.2f}".format(coin[token]['usd']))
            change = str(coin[token]['usd_24h_change'])
            change = "{:.2f}".format(float(change))
            print("price is : " + price + " change : " + change)
        except:
            continue
            await asyncio.sleep(10)
        await update(price, change)
        await asyncio.sleep(5)


old_price = 0.0
client = discord.Client()
cg = CoinGeckoAPI()


@client.event
async def on_ready():
    print('logged in as {0.user}'.format(client))
    await main()


client.run(botToken, reconnect=True)
