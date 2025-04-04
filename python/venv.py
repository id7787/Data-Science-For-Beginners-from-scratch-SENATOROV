"""Урок по виртуальному окружению."""

#
# ## Что делает команда python -m venv venv?
#
# Команда python -m venv venv используется для создания виртуального окружения в Python. Виртуальное окружение — это изолированная среда, которая позволяет управлять зависимостями проекта отдельно от глобальной установки Python. Это особенно полезно, когда разные проекты требуют разных версий одних и тех же библиотек.
#
# Разберем команду по частям:
# python — вызывает интерпретатор Python.
# -m venv — указывает Python запустить модуль venv, который отвечает за создание виртуальных окружений.
# venv — это имя папки, в которой будет создано виртуальное окружение. Вы можете указать любое другое имя вместо venv.
#
# ## Что такое pip:
# pip — это стандартный менеджер пакетов для Python, который используется для установки, обновления и управления библиотеками (пакетами) и их зависимостями. Название pip расшифровывается как "Pip Installs Packages" (или "Pip Installs Python")
#
#
#
# ## 1.1 Что делает каждая команда в списке ниже?
# Команда pip list используется для вывода списка всех пакетов (библиотек), установленных в текущем окружении Python. Это полезно для проверки, какие пакеты уже установлены и их версий.
#
# Команда pip freeze > requirements.txt используется для создания файла requirements.txt, который содержит список всех установленных пакетов и их версий в текущем окружении Python. Этот файл часто используется для управления зависимостями проекта.
#
# Команда pip install -r requirements.txt используется для установки всех пакетов, перечисленных в файле requirements.txt. Этот файл обычно содержит список зависимостей проекта в формате package==version, который был создан с помощью команды pip freeze > requirements.txt.
#
#
#
# ## 1.2 Что делает каждая команда в списке ниже?
#
# Команда conda env list используется в среде управления пакетами и окружениями Conda для отображения списка всех созданных виртуальных окружений, доступных на вашем компьютере.
#
# Что делает команда:
# Выводит список всех виртуальных окружений, которые были созданы с помощью Conda.
# Для каждого окружения указывает его имя и путь к каталогу, где оно расположено.
# Текущее активное окружение будет помечено символом * (звездочка).
#
# Команда вводится в терминале (или Anaconda Prompt, если вы используете Windows).
#
#
#
#
# Команда conda create -n env_name python=3.5 создает новое виртуальное окружение с именем env_name и устанавливает в него Python версии 3.5.
#
# Разбор команды:
#
# conda create:
# Это основная команда для создания нового виртуального окружения в Conda.
#
# -n env_name:
# Опция -n (или --name) указывает имя нового окружения. В данном случае окружение будет называться env_name.
#
# python=3.5:
# Указывает версию Python, которую нужно установить в это окружение. В данном случае это Python 3.5.
#
#
# Что происходит при выполнении команды:
#
# Conda создает новое изолированное окружение с именем env_name.
# В это окружение устанавливается Python версии 3.5.
# Также устанавливаются базовые пакеты, необходимые для работы Python.
#
# Пример использования:
# conda create -n myenv python=3.5
# Создается окружение с именем myenv.
# В нем будет установлен Python 3.5.
#
# Что дальше?
# После создания окружения:
#
# Активируйте его:
# conda activate myenv
#
# Проверьте версию Python:
# python --version
# Вывод должен быть:
# Python 3.5.x
#
# Установите дополнительные пакеты, если нужно:
# conda install numpy pandas
#
#
#
#
#
#
# Команда conda env update -n env_name -f file.yml используется для обновления существующего виртуального окружения Conda (env_name) на основе конфигурации, описанной в YAML-файле (file.yml). Давайте разберем эту команду подробнее:
#
# Что делает команда?
# Читает YAML-файл:
# Команда использует файл file.yml, который содержит описание окружения (например, список пакетов и их версий).
#
# Обновляет окружение:
# Если пакеты, указанные в YAML-файле, уже установлены в окружении, они будут обновлены до версий, указанных в файле.
# Если пакеты отсутствуют в окружении, они будут установлены.
#
# Сохраняет существующие пакеты:
# Пакеты, которые уже установлены в окружении, но не указаны в YAML-файле, останутся без изменений.
#
# Синтаксис команды
# conda env update -n env_name -f file.yml
#
# -n env_name:
# Указывает имя окружения (env_name), которое нужно обновить.
#
# -f file.yml:
# Указывает путь к YAML-файлу (file.yml), который содержит описание окружения.
#
# Пример YAML-файла
# Файл environment.yml может выглядеть так:
#
# name: myenv  # Имя окружения (не обязательно, если используется -n)
# channels:
#   - defaults
# dependencies:
#   - python=3.8
#   - numpy=1.21
#   - pandas=1.3
#   - pip:
#     - flask==2.0.1
#
# name: Имя окружения (опционально, если используется -n).
# channels: Каналы, из которых будут устанавливаться пакеты (например, defaults, conda-forge).
# dependencies: Список пакетов и их версий.
# pip: Пакеты, которые нужно установить через pip.
#
#
#
#
#
# Команда source activate env_name используется для активации виртуального окружения Conda с именем env_name (переключает текущую сессию терминала на использование виртуального окружения env_name). После активации все команды Python, pip и других инструментов будут выполняться в контексте этого окружения. Команда сработает на linux/Mac os
#
#
# Команда source deactivate используется для деактивации (выхода) из текущего активного виртуального окружения Conda. После выполнения этой команды терминал возвращается к использованию глобальной среды Python (или базового окружения Conda).
#
#
#
#
#
# ## вставьте скрин вашего терминала, где вы активировали сначала venv, потом conda, назовите окружение "SENATOROV"
#
#
#
#
#
# ## Как установить необходимые пакеты внутрь виртуального окружения для conda/venv?
#
# venv:
#
# Используйте команду pip install, чтобы установить пакеты. Например:
#
# pip install numpy pandas flask
#
#
# Установка из файла requirements.txt
# Если у вас есть файл requirements.txt, содержащий список пакетов, установите их все одной командой:
#
# pip install -r requirements.txt
#
#
#
# Пример файла requirements.txt:
#
# numpy==1.21.0
# pandas==1.3.0
# flask==2.0.1
#
#
# conda:
#
# conda install numpy pandas flask
#
# Установка из файла environment.yml
# Если у вас есть файл environment.yml, содержащий описание окружения, создайте или обновите окружение:
#
# conda env update -n myenv -f environment.yml
#
# Пример файла environment.yml:
#
# name: myenv
# channels:
#   - defaults
# dependencies:
#   - python=3.9
#   - numpy=1.21
#   - pandas=1.3
#   - pip:
#     - flask==2.0.1
#
#
#
# ## Что делают эти команды?
# pip freeze > requirements.txt
# conda env export > environment.yml
#
# Эти команды используются для экспорта списка установленных пакетов из виртуального окружения в файл. Это полезно для создания конфигурационных файлов, которые можно использовать для восстановления окружения на другом компьютере или для совместной работы над проектом.
#
#
#
#
#
# ## 5.1 вставьте скрин, где будет видна папка VENV в вашем репозитории а также файлы зависимостей requirements.txt и environment.yml, файлы должны содержать зависимости
#
#
#
#
#
# ## Что делают эти команды?
# pip install -r requirements.txt
# conda env create -f environment.yml.
#
# Эти команды используются для восстановления виртуального окружения на основе ранее экспортированных конфигурационных файлов (requirements.txt для pip и environment.yml для conda).
#
#
#
#
# ## Что делают эти команды?
# pip list
# pip show,
# conda list
#
#
# Команда pip list выводит список всех пакетов, установленных в текущем виртуальном окружении (или глобальной среде Python, если окружение не активировано).
#
# pip list
#
# Пример вывода
#
# Package    Version
# ---------- -------
# numpy      1.21.0
# pandas     1.3.0
# pip        21.1.2
# setuptools 57.0.0
#
#
#
# pip show:
#
# Команда pip show выводит подробную информацию о конкретном установленном пакете, включая версию, расположение, зависимости и другую информацию.
#
# pip show numpy
# Пример вывода
#
# Name: numpy
# Version: 1.21.0
# Summary: NumPy is the fundamental package for array computing with Python.
# Home-page: https://www.numpy.org
# Author: Travis E. Oliphant et al.
# Author-email: None
# License: BSD
# Location: /path/to/venv/lib/python3.9/site-packages
# Requires:
# Required-by: pandas
#
#
# conda list:
# Команда conda list выводит список всех пакетов, установленных в текущем окружении Conda. Она аналогична pip list, но также показывает пакеты, установленные через conda.
#
# conda list
#
# Пример вывода
# Name                    Version                   Build  Channel
# numpy                     1.21.0           py39h7a8b1e3_0
# pandas                    1.3.0            py39h7a8b1e3_0
# pip                       21.1.2             pyhd8ed1ab_0    conda-forge
# python                    3.9.0                h7579374_2
#
#
# ## Где по умолчанию больше пакетов venv/pip или conda? и почему дата сайнинисты используют conda?
# больше пакетов в venv/pip чем в conda
#
# дата сайнинисты используют conda так как там содержатся необходимые им библиотеки например(numpy, scipy, matplotlib, pandas и другие)
#
# ## вставьте скрин где будет видно, Выбор интерпретатора Python (conda) в VS Code/cursor
# добавьте в .gitignore папку SENATOROV
#
# ## Зачем нужно виртуально окружение?
# С этого момента надо работать в виртуальном окружении conda, ты научился(-ась) выгружать зависимости и работать с окружением?
#
# Виртуальное окружение (virtual environment) в Python — это изолированная среда, которая позволяет управлять зависимостями проекта и избегать конфликтов между версиями пакетов.
#
# Удалите папку VENV, она больше не нужна, мы же не разрабы, нам нужна только conda
