practice2024-file-creator

Опис:
Цей репозиторій містить простий додаток на Python для створення, перегляду та читання файлів. Додаток контейнеризований за допомогою Docker і опублікований на Docker Hub.

Посилання:
- Docker Hub: https://hub.docker.com/r/maestrodaniel/practice2024-file-creator

Інструкція для перевірки:

1. Завантаження образу з Docker Hub:
   Виконайте наступну команду для завантаження образу з Docker Hub:
   
   docker pull maestrodaniel/practice2024-file-creator

2. Запуск контейнера для створення нового файлу:
   Виконайте наступну команду для запуску контейнера і створення нового файлу:

   docker run -v ${PWD}:/app maestrodaniel/practice2024-file-creator python app.py test_1.txt

   Ця команда створить файл test_1.txt у поточній директорії.

3. Перевірка списку файлів:
   Виконайте наступну команду для перегляду списку файлів у директорії:

   docker run -v ${PWD}:/app maestrodaniel/practice2024-file-creator python app.py

   Ця команда виведе список файлів у директорії.

4. Читання вмісту файлу:
   Виконайте наступну команду для читання вмісту файлу:

   echo "Hello, world!" > test_1.txt
   docker run -v ${PWD}:/app maestrodaniel/practice2024-file-creator python app.py read test_1.txt

   Ця команда виведе вміст файлу test_1.txt.
