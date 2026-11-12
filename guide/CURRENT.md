# Актуальность и обязательные поправки

Сверено 12.11.2026. Это адресная проверка перечисленных страниц, а не обновление
всего архива. Факты и оговорки машинно читаются в [sources.json](sources.json).

Исходный snapshot: 17.09.2025, 261 страница плюс README/SITEMAP. В 25 страницах
оказалась капча, ещё у одной некорректный исходный URL. Они помечены `challenge`
и `invalid_source` в [каталоге](catalog.json) и исключены из поиска по умолчанию.
Остальные 235 — `historical_unverified`: проверка на капчу не подтверждает свежесть,
полноту или техническую правильность. Кандидат URL в каталоге не считается
проверенной ссылкой. Исходные байты сохранены для происхождения и upstream merge.

## Что проверять до реализации

| Область | Текущая поправка | Первоисточник |
|---|---|---|
| Версия | Для ЕПК используется UnifiedCampaign и v501. Reports также описывает v501. Конкретный endpoint берётся из своего сервиса; массовая замена v5 не применяется. | [Кампания](https://yandex.ru/dev/direct/doc/ru/objects/campaign), [Reports](https://yandex.ru/dev/direct/doc/ru/reports), [спецификация](https://yandex.ru/dev/direct/doc/ru/spec) |
| Песочница | С 15.07.2026 больше недоступна. Офлайн-fixture проверяет код, реальную интеграцию принимают отдельно. | [История изменений](https://yandex.ru/dev/direct/doc/ru/changelog) |
| Форматы | Для новой ЕПК проверять актуальную совместимость типов объявлений. Старый TextAd и архивный пример создания нельзя автоматически переносить в новый запуск. | [Объявление](https://yandex.ru/dev/direct/doc/ru/objects/ad), [обновление комбинаторных](https://yandex.ru/dev/direct/doc/ru/update-tga) |
| Reports | 200 — готовый отчёт, 201 — поставлен в очередь, 202 — формируется. Опрос сохраняет параметры и ReportName; ожидание учитывает retryIn и конечный deadline проекта. | [Коды](https://yandex.ru/dev/direct/doc/ru/codes), [режимы](https://yandex.ru/dev/direct/doc/ru/mode), [заголовки](https://yandex.ru/dev/direct/doc/ru/headers) |
| Деньги | Reports по умолчанию использует микросуммы; returnMoneyInMicros:false меняет представление результата. Единицы фильтров проверяются отдельно. Currency, IncludeVAT и период сохраняются в паспорте отчёта. | [Деньги](https://yandex.ru/dev/direct/doc/ru/money), [спецификация](https://yandex.ru/dev/direct/doc/ru/spec) |
| Баллы | Units описывает нагрузку API. Баллы не равны рекламному расходу или балансу. У Reports собственные лимиты. | [Units](https://yandex.ru/dev/direct/doc/ru/concepts/units), [Reports limits](https://yandex.ru/dev/direct/doc/ru/restrictions) |
| Состояния | State, Status и moderation различаются. OFF и SUSPENDED имеют разные значения. Add не гарантирует универсальный SUSPENDED; в схеме Campaigns.add нельзя задавать произвольное State. | [Кампания](https://yandex.ru/dev/direct/doc/ru/objects/campaign), [add](https://yandex.ru/dev/direct/doc/ru/campaigns/add) |
| Чтение | get запрашивает поля явно. Несуществующие/недоступные ID могут отсутствовать без отдельной ошибки. Выборку нужно проверять на полноту. | [Получение данных](https://yandex.ru/dev/direct/doc/ru/best-practice/get) |
| Пагинация | В общем get продолжение задаётся LimitedBy → Page.Offset при том же отборе. Reports имеет свой Page-контракт; не смешивать протоколы. | [get](https://yandex.ru/dev/direct/doc/ru/best-practice/get), [Reports spec](https://yandex.ru/dev/direct/doc/ru/spec) |
| Пакетные результаты | Успех/ошибки/предупреждения разбираются по каждому входному объекту. Один успешный HTTP-ответ не принимает весь batch. | [Изменение данных](https://yandex.ru/dev/direct/doc/ru/best-practice/modify) |
| Свежесть | Статистика может пересчитываться; предусмотрены Changes.check/BorderDate и AUTO. Готовый файл не означает зрелость всех оплат в CRM. | [Актуальность](https://yandex.ru/dev/direct/doc/ru/actual) |
| Атрибуция | В актуальной спецификации есть FCCD, LC, LSCCD, AUTO; старые модели имеют правила преобразования/предупреждения. Сохранять выбранную модель и предупреждения, не смешивать срезы. | [Спецификация Reports](https://yandex.ru/dev/direct/doc/ru/spec) |

## Что является нашей политикой

Раздельные права, журнал намерений, резерв расходов, UNKNOWN/reconcile,
независимый судья, границы повторов и квитанция — контракты рабочего проекта.
Они не объявляются встроенными возможностями API. Серверная идемпотентность add,
транзакционная фотография кабинета и мгновенная сходимость readback не считаются
гарантированными без подтверждения выбранного метода.

При расхождении снимка с текущим первоисточником агент фиксирует расхождение,
обновляет затронутую карточку и её доказательства. До выяснения критического поля
или lifecycle зависимое внешнее действие остаётся заблокированным.

Вернуться: [START](START.md), [маршруты](ROUTES.md).
