import pytest
from playwright.sync_api import Page, Route


def test_counters_65(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 100000,
					"energy": 0,
					"materials": 0,
					"pineYears": 0,
					"water": 1000
				}
			}
		},
		"isAuthorized": False
	},
	"status": "ok"
}
        route.fulfill(json=json)
        
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", handle)
        
    page.goto("https://www.avito.ru/avito-care/eco-impact")
    
    page.wait_for_selector(".desktop-impact-items-F7T6E")

    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/65.png")

    page.wait_for_timeout(5000)
    
    
def test_counters_66(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 1000,
					"materials": 0,
					"pineYears": 0,
					"water": 1000000
				}
			}
		},
		"isAuthorized": False
	},
	"status": "ok"
}
        route.fulfill(json=json)
        
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", handle)
        
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    page.wait_for_selector(".desktop-impact-items-F7T6E")
    
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/66.png")

    page.wait_for_timeout(5000)
    
    
def test_counters_67(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1000000,
					"energy": 1,
					"materials": 0,
					"pineYears": 0,
					"water": 0
				}
			}
		},
		"isAuthorized": False
	},
	"status": "ok"
}
        route.fulfill(json=json)
        
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", handle)
        
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    page.wait_for_selector(".desktop-impact-items-F7T6E")
    
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/67.png")

    page.wait_for_timeout(5000)


def test_counters_68(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1000000,
					"energy": 1,
					"materials": 0,
					"pineYears": 0,
					"water": 1000
				}
			}
		},
		"isAuthorized": False
	},
	"status": "ok"
}
        route.fulfill(json=json)
        
    page.route("https://www.avito.ru/web/1/charity/ecoImpact/init", handle)
        
    page.goto("https://www.avito.ru/avito-care/eco-impact")

    page.wait_for_selector(".desktop-impact-items-F7T6E")
    
    page.locator(".desktop-impact-items-F7T6E").screenshot(path="output/68.png")

    page.wait_for_timeout(5000)
    