# module-e7
Практическое задание от SkillFactory по Module E7 

Запуск приложения: 
- https://github.com/m-v-kalashnikov/module-e7.git 
- cd module-e7 
- docker-compose up -d 

Бекенд приложения стартует на 5000 порту. Если запускаете на своей машине запросы отправлять на:
- http://127.0.0.1:5000/

Или на мой
- 


- POST message?text=text для создания нового сообщения с текстом text
- POST /tag/<message_id> добавление тега к существующему сообщению с id message_id. У тега есть обязательный аргумент text
- POST /comment/<message_id> добавление комментария к существующему сообщению с id message_id. У комментария есть обязательный аргумент text
- GET /message/message_id получение полного сообщения с тегами и комментариями по id
- GET /stats/message_id получение статистики по сообщению (количество тегов и комментариев) id
