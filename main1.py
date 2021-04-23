import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os

import requests
from vk_api import VkUpload
import datetime

TOKEN = os.environ.get("VK_TOKEN", None)

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
    attachments = []
    upload = VkUpload(vk_session)
    image_url = 'https://avatars.mds.yandex.net/get-zen_doc/96780/pub_5cbd534a5d653c00b37f7171_5cbd540d569af600b33b2d8b/scale_1200'
    session = requests.Session()
    image = session.get(image_url, stream=True)
    photo = upload.photo_messages(photos=image.raw)[0]
    attachments.append(
        'photo{}_{}'.format(photo['owner_id'], photo['id'])
    )
    vk = vk_session.get_api()
    vk.messages.send(
        user_id=event.user_id,
        attachment=','.join(attachments),
        message='Ваш текст'
    )


if __name__ == '__main__':
    main()
