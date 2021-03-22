import time
from discord_webhook import DiscordWebhook
from pypresence import Presence

client_id = '823593956461903873'
RPC = Presence(client_id)
RPC.connect()

webhook_adress = input('Enter the webhook address: ')

def webhook_send():
	RPC.update(state="using WebClient", details="Writing in webhook", large_image="images", large_text="Writing in webhook", start=time.time())

	webhook_message = input('Write a message on the webhook: ')
	webhook = DiscordWebhook(url=webhook_adress, content=webhook_message)
	response = webhook.execute()
	webhook_send()

webhook_send()
