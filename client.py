import logging
from emo_platform import Client, WebHook

import settings


# クライアントの設定
client = Client()
rooms_id_list = client.get_rooms_id()
room = client.create_room_client(rooms_id_list[0])

# WebHook設定
client.create_webhook_setting(WebHook(settings.WEB_HOOK_URL))
logging.info("Webhook has been set.")

@client.event('message.received')
def message_callback(data):
    logging.info("message received")
    logging.info(data)

@client.event('illuminance.changed')
def illuminance_callback(data):
    logging.info("illuminance changed")
    logging.info(data)

secret_key = client.start_webhook_event()

def send_msg(text):
    logging.info("\n" + "=" * 20 + " room send msg " + "=" * 20)
    logging.info(room.send_msg(text))
