import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os

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
                             message="Спасибо, что написали нам. Мы скоро ответим ))",
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
