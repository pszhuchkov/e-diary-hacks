
## Скрипт для редактирования данных в электронном дневнике школы
### О скрипте
Скрипт предназначен для исправления "плохих" оценок (2 и 3) на 5, удаления замечаний и добавления похвалы от учителей.
Исходный код дневника: https://github.com/pszhuchkov/e-diary
### Использование
1. При локальном использовании скачать [код электронного дневника](https://github.com/pszhuchkov/e-diary) и запустить сайт.
2. Разместить файл `hacks.py` в корневой директории (в одной директории с файлом `manage.py`).
3. Запустить интерактивную консоль Python для взаимодействия с базой данных с помощью команды:
	```console
	python manage.py shell
	```
4. Выполнить импорт скрипта `hacks.py`:
	```python
	import hacks
	```
	
5. Редактирование данных:
	* Для исправления "плохих" оценок запустить команду:
	```python
	hacks.fix_marks(<ФИО ученика>)
	```
	* Для удаления всех замечений запустить команду:
	```python
	hacks.remove_chastisements(<ФИО ученика>)
	```
	* Для добавления похвалы запустить команду:
	```python
	hacks.create_commendation(<ФИО ученика>, <Предмет>)
	```
	Похвала будет добавлена к последнему уроку по указанному предмету.

	#### Параметры
	При использовании параметров [регистр букв](https://bit.ly/3nBaLsk) имеет значение.
	`<ФИО ученика>`
	Ожидаемый формат: *Иванов Иван Иванович* | *Иванов Иван*
	В первом случае вероятность однозначно определить ученика выше.
	`<Предмет>`
	Ожидаемый формат: *Математика* | *Музыка* | *Русский язык*
	```python
	>>> import hacks
	>>> hacks.fix_marks('Громов Зосима')
	Исправлено плохих оценок: 262
	>>> hacks.remove_chastisements('Громов Зосима')
	Удалено замечаний: 10
	>>> hacks.create_commendation('Громов Зосима', 'Математика')
	Добавлена похвала: "Ты многое сделал, я это вижу!"
	```
6. Ошибки:
	* Требуется уточнить ФИО или предмет
	```python
	>>> hacks.fix_marks('Авдей')
	Найдены несколько записей, соответствующих указанному имени. Требуется более точное указание имени.
	>>> hacks.create_commendation('Громов Зосима', 'язык')
	Найдены несколько записей, соответствующих указанному 	предмету. Требуется более точное указание предмета.
	```
	* Проверить правильность введенных данных
	```python
	>>> hacks.fix_marks('Громов Засима')
	Ученик с указанным именем не найден. Проверьте правильность 	введенных данных.
	>>> hacks.create_commendation('Громов Зосима', 'Матиматика')
	Указанный предмет не найден. Проверьте правильность введенных 	данных.
	```

### Цель проекта

Код написан в образовательных целях на онлайн-курсе для веб-разработчиков [dvmn.org](https://dvmn.org/).