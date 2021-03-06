import vk_api
from vk_api.bot_longpoll import VkBotLongPoll, VkBotEventType
import random
import os
print(os.path.abspath('file.txt'))

TOKEN = os.environ.get("VK_TOKEN", None)
steps = {
    0: {
        "msg": "Привет, мы хожем подобрать модель телевизора по вашим пожеланиям. Для этого напишите  ДА"
               + "\nЕсли вам нужна помощь специалиста, то оставьте сообщение. Вам ответит консультант нашего магазина",
        'ans': {
            'да': 1,
        },
        "def": 50,
    },
    1: {
        "msg": 'Вам нужен БОЛЬШОЙ или СРЕДНИЙ по-размеру телевизор?',
        'ans': {
            'большой': 2,
            'средний': 3,
            'mal': 4
        },
        "def": 1
    },
    2: {
        "msg": "Вы желаете преобрести ПРЕМИАЛЬНУЮ или БЮДЖЕТНУЮ модель?",
        'ans': {
            'бюджетную': 4,
            'премиальную': 5,
        },
        "def": 2,
    },
    3: {
        "msg": "Вы желаете преобрести ПРЕМИАЛЬНУЮ или БЮДЖЕТНУЮ модель?",
        'ans': {
            'бюджетную': 7,
            'премиальную': 6,
        },
        "def": 2,
    },
    6: {
        "msg": "Телевизор Xiaomi Mi TV 4S 43 T2 Global 42.5""" + "\n 25990 рублей"
               + "\nКомфортный в использовании LED телевизор прекрасно впишется в любой интерьер помещения. Модель "
                 "имеет диагональ 43 дюйма, поэтому отлично подойдет для любой гостиной комнаты "
               + "\nописание: https://101gadjet.ru/index.php?route=product/product&path=135&product_id=280&sort=p.price&order=DESC&limit=100"
               + "\nВсе телевизоры: https://101gadjet.ru/TvXiaomi",
        "def": 6,
    },
    7: {
        "msg": "Телевизор Xiaomi Mi TV 4A 32 T2 Global 31.5" + "\n 15200 рублей"
               + "\nПри всем изобилии умных функций, Mi TV 4A 32 прост в использовании. В комплекте к нему идет "
                 "Bluetooth-пульт управления с 12 кнопками и функцией голосового управления."
               + "\nподробное описание: https://101gadjet.ru/TvXiaomi/televizor-xiaomi-mi-tv-4a-32-t2-global-31-5-2019"
               + "\nВсе телевизоры: https://101gadjet.ru/TvXiaomi",
    },
    4: {
        "msg": "Телевизор Xiaomi Mi TV 4S 70 (Интерфейс на русском языке)" + "\n 60900 рублей"
               + "\nпрогрессивный продукт, входящий во флагманскую линейку. В технике умело реализованы новшества"
                 "искусственного интеллекта, истинное качество 4К-разрешения и технология PatchWall."
               + "\nописание: https://101gadjet.ru/TvXiaomi/televizor-xiaomi-mi-tv-4s-70-interfejs-na-russkom-jazyke"
               + "\nВсе телевизоры: https://101gadjet.ru/TvXiaomi",
    },
    5: {
        "msg": "Телевизор Xiaomi Mi TV 4S 75 (Интерфейс на русском языке)" + "\n 76900 рублей"
               + "\nТелевизор имеет стильный дизайн, выполненный в тонком, металлическом корпусе. Тонкие рамки и "
                 "LED подсветка позволяют полностью погрузиться в атмосферу мультимедиа."
               + "\nподробное описание по ссылке: https://101gadjet.ru/TvXiaomi/televizor-xiaomi-mi-tv-4s-75"
               + "\nВсе телевизоры: https://101gadjet.ru/TvXiaomi",
    },
}


def main():
    vk_session = vk_api.VkApi(token=TOKEN)
    longpoll = VkBotLongPoll(vk_session, "204074800")
    upload = vk_api.VkUpload(vk_session)
    dic = {}
    for event in longpoll.listen():
        if event.type == VkBotEventType.MESSAGE_NEW:
            print(event)
            print('Новое сообщение:')
            print('Для меня от:', event.obj['from_id'])
            print('Текст:', event.obj['text'])
            vk = vk_session.get_api()
            print(event.obj['peer_id'])

            from_id = event.obj["from_id"]
            text = event.obj['text']
            text = text.lower()

            if from_id in dic:
                stuid = dic.get(from_id, 0)  # получить текущее сост пользователя (на какой вопр ответил)
                stuid = steps[stuid]['ans'].get(text, steps[stuid]['def'])  # как ответил на вопрос
                dic[from_id] = stuid  # запоминаем состояние пользователя
                if stuid == 50:
                    continue
                elif stuid == 5:
                    response = upload.photo_messages(os.path.abspath('bp.jpg'))[0]  # картинка
                    owner_id = response['owner_id']  # картинка
                    photo_id = response['id']  # картинка
                    access_key = response['access_key']  # картинка
                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'  # картинка
                    vk.messages.send(user_id=from_id,
                                     attachment=attachment,
                                     message="Мы подобрали для вас подходящюю модель:",
                                     random_id=random.randint(0, 2 ** 64))
                elif stuid == 4:
                    response = upload.photo_messages(os.path.abspath('bb.jpg'))[0]  # картинка
                    owner_id = response['owner_id']  # картинка
                    photo_id = response['id']  # картинка
                    access_key = response['access_key']  # картинка
                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'  # картинка
                    vk.messages.send(user_id=from_id,
                                     attachment=attachment,
                                     message="Мы подобрали для вас подходящюю модель:",
                                     random_id=random.randint(0, 2 ** 64))
                elif stuid == 6:
                    response = upload.photo_messages(os.path.abspath('mp.jpg'))[0]  # картинка
                    owner_id = response['owner_id']  # картинка
                    photo_id = response['id']  # картинка
                    access_key = response['access_key']  # картинка
                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'  # картинка
                    vk.messages.send(user_id=from_id,
                                     attachment=attachment,
                                     message="Мы подобрали для вас подходящюю модель:",
                                     random_id=random.randint(0, 2 ** 64))
                elif stuid == 7:
                    response = upload.photo_messages(os.path.abspath('mb.jpg'))[0]  # картинка
                    owner_id = response['owner_id']  # картинка
                    photo_id = response['id']  # картинка
                    access_key = response['access_key']  # картинка
                    attachment = f'photo{owner_id}_{photo_id}_{access_key}'  # картинка
                    vk.messages.send(user_id=from_id,
                                     attachment=attachment,
                                     message="Мы подобрали для вас подходящюю модель:",
                                     random_id=random.randint(0, 2 ** 64))
            else:
                dic[from_id]=0
                stuid= 0
            vk.messages.send(user_id=from_id,
                             message=steps[stuid]["msg"],
                             random_id=random.randint(0, 2 ** 64))


if __name__ == '__main__':
    main()
