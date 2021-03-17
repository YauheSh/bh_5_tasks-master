# Урок 5. Функции

Задания разбиты на 3 уровня сложности:

- easy - легкие задания, требующие базовых знаний
- medium - задания средней сложности, которые приближены к production задачам, требующие комбинировать знания из разных тем
- hard - сложные задания

**Задания рекомендуется выполнять по мере возрастания сложности!**

## Работа в классе

**Кто работает онлайн — отправляют задачи по мере выполнения**

**Кто работает в классе — подзываем и показываем**

Задания, которые не успели сделать в классе — выполняем дома.

## Домашние задания

Обязательно необходимо выполнить задания уровня:

- easy
- medium

Домашнее задание следует отправить личным сообщением с указанием ФИО:

- В Telegram
- В Viber

Результат выполненного домашнего задания - 2 файла:

- Архив .zip, который содержит все выполненные задания
- Скриншот консоли (терминала) с пройденными тестами pytest

*Если есть навыки работы с git и github, то домашнее задание можно предоставить в виде:*

- Ссылка на репозиторий или fork в github (pull-request делать **не надо**)
- Screenshot консоли (терминала) с пройденными тестами pytest 

## Как работать с Pytest

Для того, чтобы тестировать свой код по мере выполнения заданий, необходимо установить модуль pytest, 
который выполняет unit-тесты.

Тесты именуются следующим образом:

    [уровень сложности][/тема (может не быть)]/test_[название задания].py

Если тест для задания пройден успешно, то он отображается с одним или несколькими символами ".":

    tests\test_t1.py .....

Если какой-то тест выполняется с ошибкой, то он помечается символом "F":

    tests\test_t1.py ..F..

Для работы необходимо установить Pytest с помощью pip. Для этого в командной строке или терминале необходимо выполнить команду:

    pip install pytest

Если вы находитесь в директории проекта, то можно установить также с помощью команды:

    pip install -r requirements.txt

Для прогона всех тестов, выполняем команду (нужно находиться в папке проекта):

    pytest

Для прогона теста до первой ошибки, выполняем команду:

    pytest -x

Для прогона теста к конкретному заданию, выполняем команду:

    pytest tests/[уровень сложности][/тема (может не быть)]/test_[название задания].py

Пример успешно пройденных тестов:

![Pytest прошел](pictures/pytest-ok.jpg)

Пример прогона, когда некоторые тесты завершились с ошибкой:

![Pytest не прошел](pictures/pytest-fail.jpg)