## Лабораторная работа No 7. Задачи.

**Задание выполнил:** Лебедев Дмитрий

Комплект 1: Создание микросервиса в Django REST Framework
1.1: Для улучшения функциональности приложения для создания голосо­ ваний (polls) из предыдущих лаюлтаторных работ, создайте микро­ сервис (или несколько микросервисов), написанный с использовани­ ем Django Rest Framework (DRF), который предоставляет возможность анализа результатов голосований и предоставления статистики по го­ лосованиям. Этот микросервис (poll analytics) будет вторым приложе­ нием в вашем Django­проекте. Реализуйте в данном микросервисе(­ ах) по крайней мере 2 элемента из перечисленных ниже.
• Статистика по голосованиям: микросервис может агрегировать данные о голосах, проведенных в приложении для создания го­ лосований. Это включает в себя общее количество голосований, количество голосов на каждый вариант ответа, а также процент­ ное соотношение голосов.
• Сортировка и фильтрация данных: пользователи могут сортиро­ вать голосования по различным параметрам, таким как дата про­ ведения, популярность, или количество голосов.
• Графики и диаграммы: микросервис может предоставлять гра­ фики и диаграммы, которые визуализируют результаты голосо­ вания, что делает аналитику более понятной и наглядной.
• Экспортданных:микросервисможетпредоставлятьвозможность экспорта данных в различных форматах, таких как CSV или JSON, для дальнейшего анализа внешними инструментами.

Создайте страницу в основном приложении polls, где можно искать голосования по датам и/или другим критериям, используя созданный микросервис(­ы). Найденные голосования отображаются на странице
1
динамически в виде списка. При нажатии на элемент списка (на заго­ ловок найденного голосования) справа от списка динамически отоб­ ражается вся необходимая статистика по данному голосованию, по­ лученная после запроса к реализованному микросервису(­ам).
Все голосования являются анонимными, поэтому авторизации на про­ смотр статистики и вызов микросервиса(­ов) не требуется.
Способ реализации кода ­ полностью свободный

