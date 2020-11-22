# megapolis-test-task

## API
### Авторизация

Для авторизации необходимо получить токен. Воспользуемся утилитой <code>curl</code>

<code>curl -X POST -d "username=username&password=userpassword" http://localhost:8000/api/auth/</code>

На что получим соответствующий ответ (в качестве примера)

<code>{"token":"eba95a16c5aa7c8e7a8175352d7aec31d00d148d"}</code>

Попытаемся получить информацию используя наш токен:

<code>curl -X GET http://localhost:8000/api/subcontractor/ -H 'Authorization: Token eba95a16c5aa7c8e7a8175352d7aec31d00d148d'</code>

Результат:

<code>[{"id":1,"user":2,"position":{"id":1,"name":"position_name_1","contracts":[{"id":1,"name":"contract-01"},{"id":2,"name":"contract-02"}]}}]</code>

## Точки входа API
### /api/auth/
Получение токена

### /api/contract/
Просмотр и редактирование модели "Договоры"

### /api/position/
Просмотр и редактирование модели "Должностей"

### /api/permissioncontract/
Просмотр и редактирование промежуточной модели "Разрешения на договоры"

### /api/subsidiary/
Просмотр и редактирование модели "Персонала дочерних организаций"

### /api/subcontractor/
Просмотр и редактирование модели "Персонала субподрядных организаций"
