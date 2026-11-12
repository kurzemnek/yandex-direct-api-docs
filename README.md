# API Яндекс Директа для агентной работы · kurzemnek

Русская адаптация: подключение → данные → анализ → обоснованная спецификация →
проверенное разрешённое действие. Подходит для сборки своего агента и обучения.

**Начать:** [guide/START.md](guide/START.md). **Выбрать задачу:**
[guide/ROUTES.md](guide/ROUTES.md). **Перед кодом:**
[guide/CURRENT.md](guide/CURRENT.md). Правила агента: [AGENTS.md](AGENTS.md).

## Наши сценарии

1. Проверить приложение, OAuth, рекламодателя и доступы.
2. Получить полный инвентарь кампаний, групп, объявлений и настроек.
3. Правильно выгрузить Reports: ожидание, деньги, НДС, атрибуция и пересчёты.
4. Связать рекламу с CRM: заказы, оплаты, возвраты и время до денег.
5. Подготовить аргументированную спецификацию первой кампании и независимую проверку.
6. Выполнить разрешённое изменение с чтением результата и восстановлением после сбоя.

Полный паспорт кампании включает бюджет, тип, географию, корректировки, применимые
ключи/интересы/автотаргетинг/ретаргетинг, форматы, баннеры, заголовки, тексты,
посадочные URL и UTM. Агент сначала изучает проект и задаёт до трёх вопросов
текущего шага. Обязательное неизвестное блокирует зависимую работу.

## Что действительно есть в этом форке

- 6 русских практических карточек, маршрутизация и правила работы с LLM Wiki.
- 13 адресно проверенных фактов по первичной документации Яндекса на 12.11.2026.
- Офлайн-поиск и проверка целостности на Python 3.10+, без внешних зависимостей.
- Сохранённый английский snapshot upstream от 17.09.2025: 261 страница.
  25 файлов содержат капчу, у одного некорректный URL; поиск скрывает их.
  Остальные 235 помечены историческими непроверенными снимками.

```bash
python3 tools/docs.py find "Reports"
python3 tools/docs.py find "создать кампанию" --route
python3 tools/docs.py check
python3 -m unittest discover -s tools -p 'test_*.py'
```

Проверка целостности подтверждает ссылки и происхождение файлов, не работоспособность
рекламной интеграции. Исполняемый движок, ключи, CRM, личные данные и боевые
полномочия находятся в отдельном рабочем проекте. Реальных API-вызовов в приёмке
этой адаптации нет. Публикация справочника не даёт разрешение запускать рекламу.

## Источники и обновления

Fork: [DragonSigh/yandex-direct-api-docs](https://github.com/DragonSigh/yandex-direct-api-docs).
Первоисточник: [официальная документация API](https://yandex.ru/dev/direct/doc/ru/).
Общая рекламная справка: [VKirill/yandex-direct-docs](https://github.com/VKirill/yandex-direct-docs).
Для правил рекламы она дополняет API-справочник; точные поля методов проверяются отдельно.

[Как обновлять upstream](guide/UPDATING.md) · [реестр проверенных источников](guide/sources.json) ·
[индекс снимка](guide/catalog.json) · [исходный SITEMAP](SITEMAP.md).
Исходный корпус и условия его использования не переобъявляются нашей лицензией.
[Оригинальный README](guide/upstream/README.md) сохранён без изменений.

<details>
<summary>README исходного репозитория, September 2025</summary>

# Yandex Direct API Documentation

A comprehensive collection of Yandex Direct API documentation in Markdown format for offline access and integration with AI tools.

## Overview

This repository contains the complete English documentation for the Yandex Direct API, automatically extracted and converted to Markdown format. The documentation covers all aspects of the API including authentication, campaign management, ad groups, keywords, bidding strategies, and reporting.

## Contents

The documentation is organized into the following main sections:

- **Concepts** - Core concepts, authentication, error handling
- **Campaigns** - Campaign management and strategies
- **AdGroups** - Ad group operations
- **Ads** - Text, image, and video ad management
- **Keywords** - Keyword management and bidding
- **Audiences** - Audience targeting
- **Reports** - Statistics and reporting
- **Best Practices** - Implementation guides and examples

## Usage

Navigate through the documentation using the [SITEMAP.md](SITEMAP.md) file which provides a complete index of all available pages.

## Source

Documentation extracted from: https://yandex.com/dev/direct/doc/en/

## License

This documentation is provided for educational and development purposes. Please refer to Yandex's official terms of service for usage rights.

## Updates

Last updated: September 2025

For the latest official documentation, visit: https://yandex.com/dev/direct/

</details>
