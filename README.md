# module-e7
Практическое задание от SkillFactory по Module E7 

Запуск приложения: 
- git clone https://github.com/m-v-kalashnikov/module-e7.git 
- cd module-e7 
- docker-compose up -d 

Бекенд приложения стартует на 5000 порту. Если запускаете на своей машине запросы отправлять на:
- http://127.0.0.1:5000/

Ниже список эндпоинтов:
- POST /ad (обязательный аргумент title)
- POST /ad/tag/<ad_id> (обязательный аргумент tag)
- POST /ad/comment/<ad_id> (обязательный аргумент comment)
- GET /ad/<ad_id> (возвращяет одно конкретное объявление ID которого указали)
- GET /ads (возвращяет все объявления)
- GET /ad/statistics/<ad_id> (возвращяет статистику объявления ID которого указали)
