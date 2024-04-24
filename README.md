# Project-Web ❤️

<h2 align="center">
Общая Пояснительная записка:
</h2>


<h2 align="center">
Пояснительная записка для каждой игры в этом проекте:
</h2>




<h2 align="center">
Пояснительная записка Дэвида: Кроссворд осетинских слов <img src="https://github.com/marathedziov/Project-Web/assets/134272993/51d1350b-1434-4294-a3b4-f39dc9a3796b" height="25"/>

<h4 align="center"> 
Аннотация
</h4>

<p align="center">
Проект направлен на популяризацию осетинского языка. Изучение и сохранение осетинского языка очень важная сейчас задача, когда на носителей языка влияет не только русский, но и английский язык. Для изучения языка очень важно наличие игр на этом языке. Существует много различных игр на английском языке, и практически нет игр на осетинском языке. Я написал программу, в процессе которой идет повторение, усвоение слов на осетинском языке. Используется текстовое, звуковое и графическое представление языка. Эта игра может быть использована как преподавателями осетинского языка в рамках учебного процесса, так и широким кругом пользователей просто для развлечения.
</p>

<h4 align="center">
Техническое задание:
</h4>

<h4 align="center"> 
Процесс игры:
</h4>

<p align="center">
На верхней части страницы находиться кроссворд, который образован из множества вертикальных линий из квадратов, создающие в центре другую линию из квадратов. Каждая из колонок кроссворда помечена цифрой
Под кроссвордом находятся вопросы на русском языке, где ответом является слово на осетинском. Это слово необходимо ввести в соответствующий номеру вопроса столбец.
После ответа на все вопросы в центре кроссворда на выделенной строке составляется слово на русском языке. В ответ нужно ввести это слово, но на осетинском языке.
</p>
 
<h4 align="center"> 
Пример кроссворда:
</h4>

<p align="center">
<img src=https://github.com/marathedziov/Project-Web/assets/134272993/1181491a-dcc0-4b77-be5b-086d26f557e7 width="500">
</p>

<h4 align="center">
Для проекта используются следующие модули:
</h4>

<ol>
    <li>
        <p>Навбар</p>
        <ul>
            <li>
                <p>имя и ава человека</p>
            </li>
            <li>
                <p>меню</p>
            </li>
             <li>
                <p>настройки</p>
            </li>
             <li>
                <p>о нас</p>
            </li>
        </ul>
    </li>
    <li>
      <p>Страничка кроссворда, в котором: </p>
        <ul>
            <li>
                <p>Сам кроссворд</p>
            </li>
            <li>
               <p>Ссылки для ввода отывета на каждый вопрос</p>
            </li>
            <li>
                <p>Поле для ввода ответа на главный вопрос</p>
            </li>
        </ul>
    </li>
</ol>


<h4 align="center">Руководство администратора</h4>
<p align="center">Для запуска сервера необходимо запустить файл server.py и перейти по адресу 127.0.0.1:5000. Кроссворды хранятся в базе данных crosswords.db. Она необходима для корректной работы программы. Для навбара используются иконка которая находится на пути static/img/ava.png, а также файл стиля crossword.css в static/css и шрифты в папке static/fonts</p>

<h4 align="center">Руководство пользователя</h4>
<h4 align="center">Игра будет состоять из нескольких страниц:</h4>
<ol>
    <li>
        <p>Страница выбора категории</p>
        <img src=https://github.com/marathedziov/Project-Web/assets/134272993/515cea18-9b6f-4ad6-abf6-f5b74d920af6 width=300>
    </li>
    <li>
        <p>Страница выбора кроссворда (позже будет переработан дизайн)</p>
        <img src=https://github.com/marathedziov/Project-Web/assets/134272993/01f1c369-5bbd-41a9-88e8-7da89442c9d6 width=300>
    </li>
    <li>
        <p>Страница для каждого отдельного кроссворда</p>
        <img src=https://github.com/marathedziov/Project-Web/assets/134272993/eb47a8b3-f240-4a52-b1e7-c5664793f004 width=300>
        <p>Для ввода слов в таблицу необходимо нажать на цифру рядом со строкой таблицы и ввести слово на осетинском языке</p>
    </li>
    <li>
        <p>Страница ввода ответа слов на осетинском языке</p>
        <img src=https://github.com/marathedziov/Project-Web/assets/134272993/862adc4e-060e-4dd6-a291-2569950eb864 width=300>
    </li>
    <li>
        <p>Страница победы</p>
        <img src=https://github.com/marathedziov/Project-Web/assets/134272993/ae634830-7f06-43b0-a190-f7951b757e4f width=300>
    </li>
</ol>

<h4 align="center">Руководство программиста</h4>
<h4 align="center"> 
База данных:
</h4>

<p align="center">
В проекте будет база данных слов.
</p>
  <p>Она включает следующие таблицы:</p>
  <ol>
       <li>
        <p>categories</p>
        <ul>
            <li>
                <p>id категории (id)</p>
            </li>
            <li>
                <p>Категория на осетинском языке (category_iron)</p>
            </li>
            <li>
                <p>Категория на русском языке (category_rus)</p>
            </li>
        </ul>
       </li>
       <li>
        <p>crosswords</p>
        <ul>
            <li>
                <p>id кроссворда (id)</p>
            </li>
            <li>
                <p>Слово-ответ на осетинском языке (word_ans_iron)</p>
            </li>
            <li>
                <p>Слово-ответ на русском языке (word_ans_rus)</p>
            </li>
            <li>
                <p>id категории (id_category)</p>
            </li>
        </ul>
       </li>
       <li>
        <p>words</p>
        <ul>
            <li>
                <p>id слова (id)</p>
            </li>
            <li>
                <p>Слово на осетинском языке (word_iron)</p>
            </li>
            <li>
                <p>Описание слова на русском языке (description)</p>
            </li>
            <li>
                <p>Слово на русском языке (word_rus)</p>
            </li>
            <li>
                <p>Индекс буквы составляющей ответ (place)</p>
            </li>
            <li>
                <p>Координаты первой буквы слова в таблице (coords)</p>
            </li>
            <li>
                <p>id кроссворда (id_cross)</p>
            </li>
        </ul>
       </li>
  </ol>

  <h4>Структура БД</h4>
   <img src=https://github.com/marathedziov/Project-Web/assets/134272993/d4711e05-f772-473c-91cf-09c8e8475c29>
  
<h4 align="center">Используемая литература</h4>

<ul>
	<li>
		<p>Учебные материалы Яндекс лицея.</p>
	</li>
	<li>
		<p>ChatGPT</p>
	</li>
	<li>
		<p>Stack Overflow</p>
	</li>
</ul>







<h2 align="center">
Пояснительная записка Марата: <br> Собери Животное
</h2>

<h4 align="center">
Аннотация:
</h4>

<p align="center">
Проект направлен на популяризацию осетинского языка. Изучение и сохранение осетинского языка очень важная сейчас задача, когда на носителей языка влияет не только русский, но и английский язык. Для изучения языка очень важно наличие игр на этом языке. Существует много различных игр на английском языке, и практически нет игр на осетинском языке. Я написал программу, в процессе которой идет повторение, усвоение слов на осетинском языке. Используется текстовое, звуковое и графическое представление языка. Эта игра может быть использована как преподавателями осетинского языка в рамках учебного процесса, так и широким кругом пользователей просто для развлечения.
</p>

<h4 align="center">
Руководство пользователя:
</h4>

<p align="center">
Игра состоит из двух уровней никак не связанных друг с другом. После открытия сайта пользователь попадает на главное окно. Там он может ознакомится с правилами игры, а также просмотреть список лидеров и увидеть свой уровень достижений И зарегистрироваться/войти в аккаунт.
    
![image](https://github.com/marathedziov/Project-Web/assets/151550733/3310dbbf-8a7c-4869-a640-d951cf660d58)
    
В окне зарегистрироваться/авторизации пользователь пишет имя и пароль, после этого он добавляется в базу данных, где будет собираться его рейтинг. После того как он вошел в аккаунт, он выбирает уровень.
    
![image](https://github.com/marathedziov/Project-Web/assets/151550733/43299d21-af37-4b90-b9d3-3d3c6aa111e8)
</p>


<h4 align="center">
Первый уровень. Части тела.
</h4>

<p align="center">
    Первый уровень игры представляет собой собирание животного по частям тела. Выбирая этот уровень, пользователю отрывается следующее окно, в котором есть вопрос: на осетинском языке, например, уши это… и даны разные варианты ответов в виде написанных слов. Пользователь должен нажать верное название того слова, которое требуется в вопросе. Если пользователь отвечает неправильно, у него отнимается 5 очков, а если он даст неправильный 2 раза подрят, то игра начинается сначала. При верном ответе отрисовывается та часть животного, которая была в вопросе (уши, тело, ноги, голова и т.д.). В этом же окне есть кнопка возврата на окно выбора уровня (В верхней части экрана, в навбаре). Т.е. игрок в любое время может прервать игру и выбрать другой уровень.

![image](https://github.com/marathedziov/Project-Web/assets/151550733/4f316652-d8cc-46ef-8103-32df155b5f0c)

![image](https://github.com/marathedziov/Project-Web/assets/151550733/3dab6bb7-f5f9-49f4-8f42-f0f446f9f8fa)

</p>

<h4 align="center">
Второй уровень. Геометрические фигуры
</h4>



<p align="center">
Второй уровень представляет собой собирание животного из геометрических фигур. На данном уровне идет восприятие на слух осетинских слов. В этом уровне нужно нажать кнопку «Послушай диктора». Игрок услышит слово на осетинском языке обозначающее геометрическую фигуру. Он должен нажать на соответствующую картинку геометрической фигуры и появится часть картинки животного. У игрока есть 3 попытки на правильный ответ. Когда ответ дан верно, отрисовывается та фигура, которая была в вопросе. По мере предоставления правильных ответов будет собираться животное из геометрических фигур.     

![image](https://github.com/marathedziov/Project-Web/assets/151550733/3dd5c447-3c10-4ac0-a3d0-86ef45dbc21e)
														  
			                                                    
После полной отрисовки появляется поле ввода, в котором надо написать: кто на картинке.

![image](https://github.com/marathedziov/Project-Web/assets/151550733/2c8d4e3d-0723-4709-8040-db1e1704e3cf)

</p>

<h4 align="center">
Подсчет очков
</h4>

<p align="center">
    За уровень можно набрать максимум 100 баллов. За каждый неверный ответ отнимается 5 баллов. Если дважды ответил неверно, еще минус 5 баллов.
</p>

<h4 align="center">
Руководство администратора
</h4>

<p align="center">
   В папке игры находятся файлы и папки. Файл server,py главный файл, который запускает игру или через ссылку https://piece-by-piece.glitch.me/ . В папке Piece-by-piece находятся папка(static/img/mode1) с файлами картинок для первого уровня, в этой же папке находятся файлы звуковые(static/sound) для второго уровня. Рейтинг пользователей храниться в файле BaseDate.sqlite. Все эти файлы нужны для успешного запуска игры.
</p>


<h4 align="center">
Руководство программиста
</h4>

<p align="center">
Для проекта использовалась библиотека Flask, позволяющая создавать web-приложения. Приложение состоит из 8 окон, код которых находится в файлах:
    
  ![image](https://github.com/marathedziov/Project-Web/assets/151550733/66ad449a-8954-4e60-bd09-8f8bd3eacab8)

</p>


<h4 align="center">
Список литературы
</h4>

«Лабиринт». Картинка 
https://www.labirint.ru/screenshot/goods/431441/10/


Учебные материалы Яндекс лицея.  Введение в БД, работа с SQL-таблицами и отображение данных в PyQT. 
https://lms.yandex.ru/courses/1054/groups/8525/lessons/5944/materials/17786


Учебник | PyQT. Диалоги, работа с изображениями. 
https://lms.yandex.ru/courses/1054/groups/8525/lessons/5942/materials/17547


Stack Overflow на русском. 
https://ru.stackoverflow.com/


chat gpt     https://chat.openai.com/







