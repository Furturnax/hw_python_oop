# Проект "Модуль фитнес-трекера"
Реализация модуля фитнес-трекера согласно методологии объектно-ориентированного программирования. 

Основные возможности:
- отправка пакета с данными с датчиков финтес-трекера;
- корректная обработка поступивших пакетов данных;
- отправка сообщения о результатах тренировки.

Проект является учебным. Основная польза в приобретении понимания реализации методологии объектно-ориентированного программирования, использования `dataclass`, аннотирования типов данных. 

<br>

## Технологический стек:
- Python 3.11.5
- Pytest 7.4.2

<br>

## Как запустить проект :shipit: :
+ Клонировать репозиторий и перейти в него в командной строке:
```bash
git clone git@github.com:Furturnax/hw_python_oop.git
```

```bash
cd hw_python_oop/
```

+ Cоздать и активировать виртуальное окружение (Windows/Bash):
```bash
python -m venv venv
```

```bash
source venv/Scripts/activate
```

+ Установить зависимости из файла requirements.txt:
```bash
python -m pip install --upgrade pip
```

```bash
pip install -r requirements.txt
```

+ Запустить проект:
```bash
python homework.py
```

<br>

## Тестирование проекта:
Тестирование реализовано с использованием библиотеки Pytest. 

+ Запустить тесты из основной директории проекта:
```bash
pytest
```

<br>

## Авторство

Автор проекта - Yandex Practicum | [GitHub](https://github.com/yandex-praktikum)

Разработчик - Andrew Fedorchenko | [GitHub](https://github.com/Furturnax) [Telegram](https://t.me/furturnax)

Ревьюер - Evgeniy Salahutdinov | [GitHub](https://github.com/EugeneSal)
