import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os

TOKEN = os.environ.get("VK_TOKEN", None)

from vk_api import VkApi
from vk_api.upload import VkUpload
from vk_api.utils import get_random_id


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, "204074800")
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj['from_id'])
            print('Текст:', event.obj['text'])
            vk = vk_session.get_api()
            vk.messages.send(user_id=event.obj['from_id'],
                             message="Спасибо, что написали нам. Мы скоро ответим ))" + "\nНовое сообщение",
                             random_id=random.randint(0, 2 ** 64))
    vk_session = VkApi(token=TOKEN)
    vk = vk_session.get_api()
    upload = VkUpload(vk)

    send_photo(vk, PEER_ID, *upload_photo(upload, 'photo.jpg'))


def upload_photo(upload, photo):
    response = upload.photo_messages(photo)[0]

    owner_id = response['204074800']
    photo_id = response['https://vplate.ru/images/article/orig/2019/03/kak-opredelit-pol-morskoj-svinki.jpg']
    access_key = response['access_key']

    return owner_id, photo_id, access_key

def send_photo(vk, peer_id, owner_id, photo_id, access_key):
    attachment = f'photo{owner_id}_{photo_id}_{access_key}'  #attachment = f'photo{owner_id}_{photo_id}_{access_key}'
    vk.messages.send(
        random_id=get_random_id(),
        peer_id=peer_id,
        attachment=attachment
    )
PEER_ID = '204074800'


if __name__ == '__main1__':
    main()
