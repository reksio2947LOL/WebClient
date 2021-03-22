import time
from discord_webhook import DiscordWebhook
from pypresence import Presence

client_id = '823593956461903873'
RPC = Presence(client_id)
RPC.connect()

webhook_adress = input('Podaj adres webhooka: ')

def webhook_login():
	RPC.update(state="używając WebClient", details="Piszę na webhooku", large_image="images", large_text="Piszę na webhooku", start=time.time())

	webhook_message = input('Napisz na webhooku: ')
	webhook = DiscordWebhook(url=webhook_adress, content=webhook_message)
	response = webhook.execute()
	webhook_send()

webhook_send()
