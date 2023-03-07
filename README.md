# test_backend
Backend для тестового задания \
Реализовано с fastapi, подключение к бд postgres.  
база данных создана в pgadmin4.   

Запуск: python -m uvicorn app.main:app --host localhost --port 8000 --reload  

Фронтенд: https://github.com/vergeeva/test_task 

Запросы http://localhost:8000/ 
## GET: 
api/users/all_users - получить список всех пользователей из бд \
Пример запроса из postman: \
![image](https://user-images.githubusercontent.com/61785118/223023035-8d7198bd-034b-4fc2-a66c-640f38f49763.png)

## POST: 
/api/users/user_clicked - создает пользователя, если такового нет, или обновляет количество кликов, если этот пользователь уже есть\
Пример отправки запроса: \
{ \
  "name": "string", \
  "email": "user@example.com", \
  "click_count": 0 \
} \
Пример запроса из postman: \
![image](https://user-images.githubusercontent.com/61785118/223023259-a15d94cb-05d6-43d2-ab23-cabc5034704d.png)
