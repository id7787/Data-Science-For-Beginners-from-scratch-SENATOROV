"""quiz."""

# """quiz."""
#
# Список вопросов к видео https://t.me/c/1937296927/765/29780 (АЛГОРИТМ ПРИНЯТИЯ И ОТДАЧИ ДОМАШКИ):
#
# (По желанию )В ответе подробно всё опишите и обязательно нужно указывать тайм код из видео где я это сказал, по желанию, дополнительно прикладываем скриншот из видео.
# Если вы знаете ответы на вопросы из Вашего опыта, то таймкоды из видео не надо указывать и т.д.
#
# #### 1) Как понять, что домашка пришла?
#
# чат Homework --> @pythonhater Прими пулл
#
# #### 2) Как принять домашку?
#
# Git desktop --> Fetch Origin --> History --> hw --> open in VS code.
#
# #### 3) Зачем нужна кнопка history и какие функции появляются при нажатии правой кнопки мыши на коммит?
#
# history покажет историю изменений файлов; функции amend commit и тд.
#
# #### 3.1) Где брать ссылку на коммит? куда её отправлять?
#
# берем в view on github в Cursor; отправляем через github desktop кнопка commit to main.
#
# #### 4) Что такое файл лога?
#
# файл, в котором мы высылаем отчетность + конспект уроков.
#
# #### 4.1) Когда нужно его пушить?
#
# когда мы изменили данные в log.
#
# #### 5) Что такое интерпритатор?
#
# софт, который читает и запускает код.
#
# #### 6) Где можно выбрать интерпритатор?
#
# Vs code --> значок run --> python environments --> ~/anaconda3/python.exe.
#
# #### 7) Что такое модуль?
#
# файл с расширением .py.
#
# #### 8) Как создать и отправить коммит?
#
# github desktop --> commit to main --> push origin.
#
# #### 9) Как посмотреть что коммит точно отправлен и находится в github?
#
# github desktop --> history --> выбираем коммит --> view on github.
#
# #### 10) Какая команда показывает что код не прошёл проверки на ошибки?
#
# terminal cursor  --> пишем pre-commit run --all-files.
#
# #### 10.1) Напишите список линтеров которые используются для проверки кода и дайте их краткую характеристику.
#
# 1. Jupytext
# 🔹 Назначение: Конвертирует Jupyter-ноутбуки (*.ipynb) в текстовые форматы (Markdown, Python-скрипты и др.) и обратно.
# 🔹 Плюсы: Удобен для версионного контроля (Git), так как хранит ноутбуки в читаемом текстовом виде.
#
# 2. Docformatter
# 🔹 Назначение: Автоматически форматирует docstrings (строки документации) в соответствии с PEP 257.
# 🔹 Плюсы: Упрощает поддержку единого стиля документации.
#
# 3. Black
# 🔹 Назначение: "Неумолимый" форматтер кода, приводящий Python-код к единому стилю (PEP 8).
# 🔹 Плюсы: Не требует конфигурации, работает "из коробки".
#
# 4. nbQA-совместимые инструменты
# 🔹 Назначение: Адаптируют стандартные линтеры (Black, isort, flake8 и др.) для работы с Jupyter-ноутбуками.
# 🔹 Примеры:
#
# nbqa-black: применяет Black к ячейкам ноутбука.
#
# nbqa-isort: сортирует импорты в ноутбуках.
#
# nbqa-flake8: проверяет код на соответствие PEP 8.
#
# nbqa-mypy: статическая типизация в ноутбуках.
#
# #nbqa-pylint: расширенный анализ кода
#
# nbqa-pydocstyle: проверка docstrings.
#
# 5. Pyupgrade
# 🔹 Назначение: Автоматически обновляет синтаксис Python до более новых версий (например, заменяет format() на f-строки).
# 🔹 Плюсы: Помогает поддерживать современный код.
#
# 6. isort
# 🔹 Назначение: Сортирует импорты в алфавитном порядке и группирует их (стандартные, сторонние, локальные).
# 🔹 Плюсы: Чистый и читаемый код.
#
# 7. Codespell
# 🔹 Назначение: Ищет орфографические ошибки в коде и комментариях.
# 🔹 Плюсы: Полезен для поддержки качества документации.
#
# 8. Flake8
# 🔹 Назначение: Комбинированный инструмент для проверки стиля (PEP 8), сложности кода и ошибок.
# 🔹 Плюсы: Гибкость (можно настраивать через .flake8).
#
# 9. Mypy
# 🔹 Назначение: Статический анализатор типов для Python.
# 🔹 Плюсы: Помогает избежать ошибок, связанных с типами данных.
#
# 10. Pylint
# 🔹 Назначение: Мощный линтер для анализа кода на соответствие стандартам, поиска ошибок и "запахов" кода.
# 🔹 Плюсы: Поддержка кастомных правил, высокая детализация отчетов.
#
# 11. Pydocstyle
# 🔹 Назначение: Проверяет соответствие docstrings стандартам (PEP 257).
# 🔹 Плюсы: Улучшает читаемость документации.
#
#
# #### 11) Как узнать какой именно линтер не прошёл проверку?
#
# тот, на котором записано failed.
#
# #### 12) Линтер Pylint видит markdown?
#
# линтеры не видят markdown.
#
# #### 13) Номер ячейки в терминале и номер ячейки в vs code может отличаться? в каком случае?
#
# да, если в файле есть ячейки markdown.
#
# #### 14) Где посмотреть номер ячейки в vscode?
#
# vs code --> слева внизу написан cell с номером ячейки.
#
# #### 15) В каком формате ipynb отправляется в гитхаб? причём здесь JSON?
#
# в формате json.
#
# #### 16) Где посмотреть в какой ячейке ошибка?
#
# в terminal после ввода команды pre-commit run --all-files; будет написано cell, где записан номер ячейки.
#
# #### 17) Как запустить терминал?
#
# cursor -> слева вверху terminal.
#
# #### 18) Что такое линтер?
#
# софт, который проверяет корректность кода и удовлетворяет ли код станартам записи pep8.
#
# #### 19) В какой сайт нужно вставлять код ошибки если ошибка связана с pylint?
#
# https://pylint.readthedocs.io/en/stable/.
#
# #### 20) Секция pydocstyle в большинстве случае автоматический закрывается после исправления ошибок в каком линтере?
#
# pylint.
#
# #### 21) Что такое описание модуля? Оно должно отражать информацию о том что находится в модуле?
#
# описание секции, в котором записан комментарий через """, в конце ставим точку; должно отражать.
#
# #### 21) С какой  git команды начинается утро программиста?
#
# git pull
#
# #### 22) После внесения изменений в файлах, кнопка open in vs code пропадает в кошке, как по другому открыть vs code из кошки?
#
# githu  desktop --> навести курсором мыши на репозиторий и нажать пкм "open in vs code".
#
# #### 23) Что такое stash?
#
#   Общее объяснение концепции.
#   используем команду git stash, чтобы сохранить изменения в специальном хранилище (stash);  изменения не попадают в историю Git, а сохраняются в локальном stash. Вы можете вернуть их позже с помощью git stash apply или git stash pop.
#
# #### 23.1) Как сохранить стэш?
#
#     git stash save.
#
#   Кнопка в vs code:
#
# #### 23.2) Как восстановить стэш(подсказка: https://t.me/c/1937296927/3602/25747)?
# :
#       git stash apply.
#
#
# #### 23.3) Различие между стэшем и коммитом.
#
#   git commit: фиксирует изменения в истории коммитов репозитория (ветке).
#   git stash:  Временно сохраняет незакоммиченные изменения (включая неотслеживаемые файлы, если указать -u), чтобы переключиться на другую задачу.
#
# #### 23.4) Как просмотреть список сохраненных стэшей?
#
#     git stash list.
#
#
# #### 23.5) Как удалить стэш?
#
#   git stash drop.
#
#
# #### 23.6) Практические примеры использования стэша.
#
#   стэш поможет в тех ситуациях, когда нужно загрузить коммит и не потерять код, записанный на локальном репозитории.
#
# #### 24) Где посмотреть что есть конфликт в файлах?
#
# github desktop --> pull origin и вылезает error stash changed.
#
# #### 24.1) Когда он появляется?
#
# когда одновременно создается коммит кем-то другим и локальным юзером.
#
# #### 25) Как решить конфликт в файлах?
#
# github desktop --> changes --> stashed changes --> restore; changes --> жмем пкм на восклицательный знак и нажимаем open in vs code --> accept current change.
#
# #### 26) Напишиие правильное утверждение:
# -Зелёное то что пришло с гитхаба и синее локальные изменения или синее то что пришло с гитхаба и зелёное это локальные изменения
#
# Зелёное то что пришло с гитхаба и синее локальные изменения.
#
# #### 27) Если мы работаем в одном файле, можно ли принять pull после того как вы спрячете в стэш свои изменения?
#
# да.
#
# #### 27.1) Что может произойти когда stash восстановите после принятия pull?
#
# удалится stash?, если он не скопирован в буфер обмена.
#
# #### 28) Сколько способов решения конфликтов было показано в видео? Напишите ЧИСЛО и укажите их способы.
#
# 3: accept current change; accept incoming change; accept both changes.
#
# #### 29) Что делает кнопка complete merge?
#
# выполняет commit в vs code.
#
# #### 30) В какой чат нужно писать если остались вопросы?
#
#     help me.
#
# #### 31) Что такое FORK? Зачем его делают?
#
# копируем чужой репозиторий и делаем его личным.
#
# #### 32) Как скачать форкнутый репозиторий на локальный компьютер?
#
# нажимаем на кнопу fork в github.
#
# #### 33) С какой вероятностью ваши ошибки были уже решены? и кто их решил?
#
# 90%; Senatorov и участники группы.
#
# #### 34) Как создать файл в vs code?
#
# vs code-->file-->create new file.
#
# #### 35) Файл лога нужно заполнять в конце каждого урока?
#
# да.
# ==================
#
# Дополнительные вопросы:
# #### 1)Какая команда конвертирует файл в py из ipynb?
#
# ipython nbconvert --to script ваш_файл.ipynb.
#
#
# #### 2) Что такое пакетный менеджер? Вы пользуетесь пакетным менеджером conda или pip? Какой лучше использовать для дата сайнс?
#
# Пакетный менеджер — это инструмент, который автоматизирует процесс установки, обновления, удаления и управления программными пакетами (библиотеками, зависимостями) в вашей среде разработки. Он упрощает работу с внешними библиотеками, разрешает зависимости между пакетами и обеспечивает их совместимость.
# pip.
#
# #### 3) Почему расширение py лучше чем ipynb?
#
# Удобство для версионного контроля (Git).
# .py: Текстовые файлы легко отслеживать с помощью Git. Изменения в коде видны построчно, что упрощает ревью и сравнение версий.
# .ipynb: Файлы .ipynb хранятся в формате JSON, который сложно читать в Git.
#
# Простота и читаемость
#
# .py: Это обычный текстовый файл, который можно открыть в любом текстовом редакторе. Код структурирован и легко читается.
# .ipynb: Это сложный JSON-файл, который содержит не только код, но и метаданные, выводы и форматирование. Его сложнее читать вне Jupyter.
#
# #### 4) Что такое pep8?
#
# PEP 8 — это официальный стиль написания кода на Python.
# подсказка:https://peps.python.org/pep-0008/.
#
# #### 4.1) линтеры проверяют на соблюдение pep8?
#
# да.
#
# #### 4.2) Какая нотация используется для создания переменных?
#
# ответ на 85-95 страницы https://t.me/c/1937296927/1/16676.
# snake_case, PascalCase, UPPER_CASE.
#
# #### 4.3) Может ли переменная состоять из одной буквы например андерскор  "_" ?
#
# да.
#
# #### 4.4) Зачем и где мы используем андерскор _ ?
#
# Именование "неважных" переменных.
# _ используется для обозначения переменных, которые не планируется использовать в коде; использование в циклах и генераторах.
#
# #### 4.5) По PEP8 допустима переменная в одну букву?
#
# Да, по PEP 8 переменная, состоящая из одной буквы, допустима, но с оговорками.
# ответ на 85-95 страницы https://t.me/c/1937296927/1/16676.
#
#
#
#
#
#
# QUIZ 2 .
#
# #### 1. Как включить автосохранение данных в VSCODE?
#
# левый верхний угол --> навести курсор мыши на файл и нажать Автосохранение.
#
# #### 2. Как настроить перенос строки?
#
# settings vs code.
#
# #### 3. Сколько символов по pep8 разрешено на строке?
#
# 79.
#
# #### 4. Какие способы переноса строк показаны в видео:
#
# перенос, с помощью заключения в скобки; с помощью объявления двух переменных и их последующего суммирования; с помощью join; с помощью обратного слэша, с помощью тройных кавычек.
#
# #### 4.1 Строки с использованием обратного слэша (\).
#
# string_continued = "This is a long string that we want to " \
#                    "split across multiple lines."
# print(string_continued)
#
# #### 4.2 Тройные кавычки (''' или """) .
#
# multi_line_string = """This is a string that spans
# multiple lines. You can write freely
# and it will keep the line breaks."""
# print(multi_line_string)
#
# #### 4.3 Создание списка строк и объединение с помощью join.
#
# strings = [
#     "This is the first line.",
#     "This is the second line.",
#     "This is the third line."
# ]
# result = "\n".join(strings)  # Используем перенос строк '\n'
# print(result)
#
# #### 4.4 Использование круглых скобок для продолжения строки.
#
# long_string = (
#     "This is a very long string that I would like to "
#     "continue on the next line."
# )
# print(long_string)
#
# #### 4.5 Форматированные строки (f-строки) с использованием скобок.
#
# letter_a = 5
# letter_b = 6
# product_ab = letter_a * letter_b
#
# message = (
#     f"when {letter_a} is multiplied by {letter_b}, "
#     f"the result is {product_ab}"
# )
# print(message)
#
# #### 4.6 Сложение строк с помощью +.
#
# string_part1 = "This is the first part, "
# string_part2 = "and this is the second part."
# full_string = string_part1 + string_part2
# print(full_string)
#
# #### 5. Проверка на ошибки c помощью кнопки problems, где она находится?
#
# внизу посередине; там же где и вкладка terminal.
#
# #### 6. Где в vscode находится клиент гита? как в нём отправить коммит? как принять домашку?
#
# слева сбоку; иконка 3 кружочка; кнопка commit и push; принимать домашку - кнопка pull.
#
# #### 7. Что такое GIT? он локальный? В нём можно посмотреть историю изменений файлов и вернуться к любому коммиту?
#
# git - контроль версий; в нем можно посмотреть историю изменений файла; git локальный.
#
# #### 8. Как вставить картинку в маркдаун?
#
# #[image.png](attachment::image.png)
#
# #### 9. Где посмотреть длину строки в vs code?
#
# В строке состояния (внизу окна VS Code) отобразится количество символов в выделенном фрагменте после выделения кода.
#
# #### 10. Как поменять тип ячейки с питона на маркдаун?
#
# сбоку ячейки нажать на надпись python и поменять на marcdown.
#
# #### 11. Как запустить сразу все ячейки в юпитере?
#
# run all.
#
# #### 12. Как изменить размер картинки в юпитере? Нужно для этого знать HTML?
#
# нужно; #<img src="путь_к_изображению.png" width="300" height="200">.
#
# #### 13. Какой хоткей чтобы запустить ячейку с смещением на следующую?
#
# shift+enter.
#
# #### 14. Как включить отображение номеров строк в юпитере(Cell line numbers)?
#
# нажать три точки сбоку ячейки с кодом и выбрать show cell line numbers.
#
# #### 15. Что такое "Go To" чем это полезно? Как перейти сразу на ошибочную ячейку?
#
# go to расположено там же где и run all.
#
# #### 16. Как очистить вывод ячеек которые уже запущены?
#
# Наведите курсор на ячейку, вывод которой хотите очистить.
# В правом верхнем углу ячейки появится панель с иконками.
# Нажмите на иконку "Очистить вывод" (обычно это значок в виде мусорного ведра или крестика).
#
# #### 17. Как работать одновременно в нескольких файлах в VSCODE? Что такое SPLIT?
#
# с помощью split мы можем работать в нескольких файлах vscode; он разделяет окна в vs code.
#
# #### 18. Каким сочетанием убирается левый сайдбар?
#
# Ctrl + B.
#
# #### 19. Кнопка два листочка это наши локальные файлы?
#
# да.
#
# #### 20. Какая ошибка появилась в трассировке при запуске всех ячеек DICT или LIST?
#
# dict.
#
# #### 21. Вы ознакомились с https://t.me/c/1937296927/832/19307? и https://github.com/adam-p/markdown-here/wiki/Markdown-Cheatsheet?
#
# да.
#
# #### 22. Что такое валидация?
#
# Проверка корректности данных.
#
# #### 23. Что такое трассировка ошибки?
#
# отображение ошибки.
#
# #### 24. Что значит отвалился интерпритатор?
#
# интерпретатор (программа, которая выполняет код построчно) перестал работать или завершил свою работу с ошибкой.
