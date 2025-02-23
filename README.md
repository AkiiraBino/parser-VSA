# Сервис сбора фреймов с видеопотока
Сервис предназначен для сбора фреймов с видеопотоков (rtsp, mp4 и др.), для задач по разработке видеоаналитической системы streamio.

## Инструкция по применению
Установить зависимости
```bash
poetry install --with dev
 ```

### Создать конфиг
Прописать в конфиге требуемые подмножества датасета, пример в `dataset_config.example.yaml`.
Обязательно требуется прописать *root* и хотя бы одно подмножество, например *train*.
Значения *imgs* и *labels* также являются обязательными.
Подможества обязательно должны иметь директорию и количество фреймов для сохранения (*dir* и *number* соответственно)

### Задать переменные окружения
Задать переменные окружения в файле `.env`, пример в `.env.example`.
Обязательными являются хотя бы один источник (*RTSP_URI* или *VIDEO_PATH*) и название файла с конфигом (*CONFIG_NAME*)

### Запустить парсинг
```bash
python main.py
```

## Локальная разработка
Установить зависимости
```bash
poetry install --with dev
 ```

Установить git хуки
```bash
poetry run pre-commit install
poetry run pre-commit install --hook-type commit-msg
poetry run pre-commit install --hook-type pre-push
```