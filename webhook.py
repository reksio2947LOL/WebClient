from discord_webhook import DiscordWebhook
import time
from pypresence import Presence

client_id = '823593956461903873'
RPC = Presence(client_id)
RPC.connect()

bruh1 = input('Podaj adres webhooka: ')

def webhook_login():
	RPC.update(state="używając WebClient", details="Piszę na webhooku", large_image="images", large_text="Piszę na webhooku",    start=time.time())

	bruh2 = input('Napisz na webhooku: ')
	webhook = DiscordWebhook(url=f'{bruh1}', content=f'{bruh2}')
	response = webhook.execute()
	webhook_login()

webhook_login()
