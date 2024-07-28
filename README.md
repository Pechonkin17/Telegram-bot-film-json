Створено телеграм бота з цілю запису фільмуів, які я переглянув. Тому, що з часом забуваю які фільми я дивився (якщо це не цікаві фільми), після перегляду можна добавити фільм в телеграм бота додавши коментар і свою оцінку.
реалізовано такі функції:
створення фільмів, 
виведення інформації про конкретний фільм,
видалення фільму,
оновлення фільму, 
показ усіх фільмів,
показ усіх команд,
кнопка назад,
кнопка перейти за посиланням,
меню:

![image](https://github.com/user-attachments/assets/7b58a24d-380e-47e4-8c16-460100481c3c)
![image](https://github.com/user-attachments/assets/8ef3a62f-2b0e-471e-829d-77b4d8e45434)

![image](https://github.com/user-attachments/assets/b1448cd7-6013-4a2d-95a6-c9e424bd7793)

Усі команди є опрацьовані, тобто, всі помилки і команди обробленні.

Переглянути бота:
https://t.me/Film_Python_Bot_Json_bot

  Опис команд бота:
1. Команда отримати всі фільми:
![image](https://github.com/user-attachments/assets/2cedf989-cde0-40bc-a657-376bd2ae1eef)
Якщо немає фільмів у списку:
![image](https://github.com/user-attachments/assets/e87b954a-c522-4e07-a806-5ff7c0135a05)

2. Команда отримати детальну інформацію про фільм:
![image](https://github.com/user-attachments/assets/df00a49b-9c2b-4dce-a14a-ecd92789fc98)

3. Команда створення бота:
![image](https://github.com/user-attachments/assets/af5bf07e-1100-436f-9011-b416a4db70fd)
![image](https://github.com/user-attachments/assets/3b086902-cb44-4e52-87df-45b11a2cbec2)
Після створення фільму виводиться інформація про фільм
Якщо ввести команду (/films, /start, /help, ... etc) - буде припинено форму для створення фільму і бот не буде очікувати наступні поля для вводу
![image](https://github.com/user-attachments/assets/25bc298e-735a-4647-9992-89d316855f38)
Є автоматична перевірка посилання, за допомогою validators. Посилання буде записане - яке відкривається
![image](https://github.com/user-attachments/assets/14c42189-98b3-4b01-86a9-964a00c60b24)

4. Функція оновлення інформації про фільм:
![image](https://github.com/user-attachments/assets/1f25d43e-80c8-4eea-86aa-55bf8b965623)
![image](https://github.com/user-attachments/assets/f030c5d9-e1d5-4dd0-a842-06d4f6a63c88)
Якщо фільму з такою назвою немає:
![image](https://github.com/user-attachments/assets/9c1dbf75-8d4b-41c1-8013-79df8718042e)
Перервання команди /update_film:
![image](https://github.com/user-attachments/assets/93beb8ff-323c-4a08-9e78-454aa9712794)

5. Видалення фільму:
![image](https://github.com/user-attachments/assets/1c33a8a6-b208-41ac-9fa9-8eb0b44cdc47)
Якщо назва фільму не існує або немає в json:
![image](https://github.com/user-attachments/assets/914b2a18-6dd7-4794-835c-71533e1ed12a)

6. Пошук фільму за назвою. Якщо знайдено 1 фільм - повернення детальної інформації про цей фільм. В іншому випадку - повернення списку фільмів з цією назвою.
![image](https://github.com/user-attachments/assets/799690f1-b58d-42df-92f8-59fbcf119142)
![image](https://github.com/user-attachments/assets/9edd36dd-ff5e-4234-8975-242692d7302d)
Якщо фільму в json немає:
![image](https://github.com/user-attachments/assets/b46f4134-22b5-4700-aad2-f00f4756d733)

7. Початок роботи бота:
![image](https://github.com/user-attachments/assets/7f9f8033-b8b5-4f15-83a9-e0119ed70c23)

8. Інструкція з командами:
![image](https://github.com/user-attachments/assets/8e64c393-2c4b-490f-9016-47c421e24057)

Також команди працюють з і без `/`:
![image](https://github.com/user-attachments/assets/04839765-1b9b-4ad6-9170-592d40e7eeb7)





