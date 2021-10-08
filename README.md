# Битли сокращает URL-адрес
При вводе полной ссылки программа выведет битлинк, а при вводе битлинка или http/https битлинк выведет кол-во кликов по этой ссылке.
# Как установить
На сайте Bitly вы можете получить свой токен-ключ. Он выглядит как набор букв и цифр. Создать файл «.env», который должен лежать рядом с main.py. В этот файл нужно положить свой ключ в переменную BITLY_API_TOKEN. 
### Пример этого файла:
``` 
BITLY_API_TOKEN="ad66ec04a762f652534670b2d404d9a7bdeec061" 
```

Python3 должен быть уже установлен. Затем используйте pip (или pip3, если есть конфликт с Python2) для установки зависимостей:
```
pip install -r requirements.txt
```

Чтобы запустить программу в терминале нужно написать 
```
python main.py
``` 
и через пробел аргумент (это может быть либо полная ссылка, либо битлинк, либо http/https битлинк).

# Цели проекта
Код написан в образовательных целях на онлайн-курсе для веб-разработчиков dvmn.org.
