import os
import smtplib
from dotenv import load_dotenv

load_dotenv()
password = os.getenv("YANDEX_PASSWORD")
username = os.getenv("YANDEX_LOGIN")

sender = "adoratorres@yandex.ru"
recipient = "adoratorres@yandex.ru"

sender_address = "adoratorres@yandex.ru"
recipient_address = "adoratorres@yandex.ru"
title = "Приглашение!"
type_content = 'text/plain; charset="UTF-8";'

old_name_friend = "%friend_name%!"
new_name_friend = "Lisa!"

old_my_name = "%my_name%"
new_my_name = "Polina"

old_name_site = "%website%"
new_name_site = "https://dvmn.org/profession-ref-program/"

template = """From: {0}
To: {1}
Subject: {2}
Content-Type: {3}

Привет, %friend_name%! %my_name% приглашает тебя на сайт %website%!                                                                                                                                             

%website% — это новая версия онлайн-курса по программированию. 
Изучаем Python и не только. Решаем задачи. Получаем ревью от преподавателя. 

Как будет проходить ваше обучение на %website%? 

→ Попрактикуешься на реальных кейсах. 
Задачи от тимлидов со стажем от 10 лет в программировании.
→ Будешь учиться без стресса и бессонных ночей. 
Задачи не «сгорят» и не уйдут к другому. Занимайся в удобное время и ровно столько, сколько можешь.
→ Подготовишь крепкое резюме.
Все проекты — они же решение наших задачек — можно разместить на твоём GitHub. Работодатели такое оценят. 

Регистрируйся → %website%  
На курсы, которые еще не вышли, можно подписаться и получить уведомление о релизе сразу на имейл."""

letter = template.format(sender_address, recipient_address, title, type_content)
letter = letter.replace(old_name_friend, new_name_friend).replace(old_my_name, new_my_name).replace(old_name_site, new_name_site)

server = smtplib.SMTP_SSL('smtp.yandex.ru', 465) 
server.login(username, password)
server.sendmail(sender, recipient, letter.encode("UTF-8"))
server.quit()
