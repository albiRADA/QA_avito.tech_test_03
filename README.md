*Инструкция по воспроизведению автотестов*: 
(P.S. Для каждого счетчика я создавала отдельную группу тестов)

1. Для написания тестов нам понадобится утилиты python, pytest, playwright:

   
   1.1. python: можно уставновить с официального сайта : <https://www.python.org/downloads/>

   1.2. Установка pytest: <https://docs.pytest.org/en/latest/getting-started.html#install-pytest>

   1.3. Далее так же устанавливаем playwright: <https://playwright.dev/python/docs/intro>

   
3. Создаем файл в локальной дириктории формата test_*.py (для pytest это файлы с тестами) 
4. Тесты для всех тест кейсов создаем аналогично:

``````puthon
import pytest 
import re 

from playwright.sync_api import Page, expect, Route

def test_waterCounter_1(page: Page): # Названия функций и переменный были в соответстии с счетчиком
    def handle(route: Route): # В данных тестах нам необходимо подставлять значения счетчиков 
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 0,
					"materials": 0,
					"pineYears": 0,
					"water": -1 # Тут указывается значение в соответствие с тестовым значением из тест-кейса
				}
			}
		},
		"isAuthorized": False # НА сайт входит как неавторизованный пользователь
	},
	"status": "ok"
}
        route.fulfill(json=json)
        
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", handle) # Указываем ресурс, где будут подставляться данные
        
    page.goto("https://www.avito.ru/avito-care/eco-impact") # Указываем путь до Экосчетчика
    
    waterCounter = None
#Далее мы обозначем отличительные особенности каждого счетчика
    for elem in page.locator('div[class^="desktop-impact-item"]').all(): # Мы находим через DevTools, где то что нам необходимо(это изображение определенного счетчика)
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0: #Например, счетчик воды отличителен капельками воды, их мы и указываем
            waterCounter = elem
    # Проверяем что там у нас не пусто
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/1.png") #Делаем скриншот и сохраняем например в папку output (в нужное нам место)

``````

5. Для запуска теста, сохраняем файл и в терминале vs code пишем: pytest test_*.py (название файла)
6. Cкриншот будет в папке output!

Удачи )
