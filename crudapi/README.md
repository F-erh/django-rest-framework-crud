# Pequena aplicação que possibilite a publicação de cotações de peças específicas de droids.

## Requisitos
- Python 3.6
- Django 3.1
- Django REST Framework

## Instalação
Após clonar o repositório, você deverá cirar um ambiente virtual onde rodará as aplicações python. 

```
python -m venv env
```

Após isso, será necessário ativar o ambiente virtual e instalar as dependencias rodando o comando: 

```
pip install -r requirements.txt
```

## Uso
Podemos testar a aplicação utilizando o [Postman](https://www.postman.com/)
```

Primeiramente, damos início ao Django server fazendo: 
```
python manage.py runserver
```
Apenas usuarios autenticados (adm) poderão utilizar os servicos da API
```

## Criação de Usuários e Tokens 

Primeiramente vamos criar o user para realizar o login 
```
POST http://127.0.0.1:8000/api/auth/register/ email="email@email.com" username="USERNAME" password1="PASSWORD*25" password2="PASSWORD*25"
```

Após, nós utilizamos essas credenciais para gerar um token

```
http://127.0.0.1:8000/api/v1/auth/token/ username="username" password="password"
```
Após isso, teremos nosso token
```
{
    "refresh": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA",
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA2MjIxLCJqdGkiOiJjNTNlNThmYjE4N2Q0YWY2YTE5MGNiMzhlNjU5ZmI0NSIsInVzZXJfaWQiOjN9.Csz-SgXoItUbT3RgB3zXhjA2DAv77hpYjqlgEMNAHps"
}
```
Perceba que temos dois tokens, o token de acesso será utilizado para autenticar todos os requerimentos que faremos e expirará após um certo tempo. Podemos então, utilizar o token refresh para gerar um novo: 
```
http://127.0.0.1:8000/api/v1/auth/token/refresh/ refresh="eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoicmVmcmVzaCIsImV4cCI6MTYxNjI5MjMyMSwianRpIjoiNGNkODA3YTlkMmMxNDA2NWFhMzNhYzMxOTgyMzhkZTgiLCJ1c2VyX2lkIjozfQ.hP1wPOPvaPo2DYTC9M1AuOSogdRL_mGP30CHsbpf4zA"
```
Então teremos nosso novo token: 
```
{
    "access": "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjE2MjA4Mjk1LCJqdGkiOiI4NGNhZmMzMmFiZDA0MDQ2YjZhMzFhZjJjMmRiNjUyYyIsInVzZXJfaWQiOjJ9.NJrs-sXnghAwcMsIWyCvE2RuGcQ3Hiu5p3vBmLkHSvM"
}
```


Nossa API tem as seguintes restrições, como solicitado pela Federação:
-   Os Doids sempre seão associados a um criador.
-   Apenas usuários autenticados poreão criar e ver os Droids criados. 
-   A API não permite requerimentos não autenticados. 

### Comandos 
```
Ver todos os Droids (ADM):
http://127.0.0.1:8000/api/droids/ "Autorização: Barreira {YOUR_TOKEN}" 
Ver o Droid em específico:
GET http://127.0.0.1:8000/api/droids/{droid_id}/ "Autorização: Barreira {YOUR_TOKEN}"  
Criar um novo Droid 
POST http://127.0.0.1:8000/api/droids/ "Autorização: Barreira {YOUR_TOKEN}" descricao=" C-3PO" endereco="federacao" contato=25887864 anunciante="Anakin Skywalker" status="Finalizado"
Atualizar um Droid
PUT http://127.0.0.1:8000/api/droids/{droid_id}/ "Autorização: Barreira {YOUR_TOKEN}" descricao="C-3PO" endereco="federacao" contato=25887864 anunciante="Anakin Skywalker" status="Finalizado
Atualizar algumas informações apenas 
PATCH http://127.0.0.1:8000/api/droids/{droid_id}/ "Autorização: Barreira {YOUR_TOKEN}" descricao="R2-D2" 
Apagar um Droid
DELETE http://127.0.0.1:8000/api/droids/{droid_id}/ "Autorização: Barreira {YOUR_TOKEN}"
```
## May the force be with you 