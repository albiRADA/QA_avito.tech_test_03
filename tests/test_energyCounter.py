import pytest
from playwright.sync_api import Page, Route


def test_energyCounter_44(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": -1,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/44.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_45(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 0,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/45.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_46(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/46.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_47(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 10,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/47.png")

    page.wait_for_timeout(5000)
    

def test_energyCounter_48(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 100,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/48.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_49(page: Page):
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/49.png")

    page.wait_for_timeout(5000)
    

def test_energyCounter_50(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 100000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/50.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_51(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 1000000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/51.png")

    page.wait_for_timeout(5000)
    

def test_energyCounter_52(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 1000000000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/52.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_53(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 1000000000000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/53.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_54(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 1000000000000000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/54.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_55(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 999,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/55.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_56(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 10000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/56.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_57(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 11111,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/57.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_58(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 125888,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/58.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_59(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 7899000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/59.png")

    page.wait_for_timeout(5000)
    

def test_energyCounter_60(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 125888000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/60.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_61(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 7899000000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/61.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_62(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 125888000000,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/62.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_63(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 1.49,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/63.png")

    page.wait_for_timeout(5000)
    
    
def test_energyCounter_64(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 0,
					"energy": 1.5,
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

    page.wait_for_selector('div[class^="desktop-impact-items"]')
    
    energyCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-sun"]').all()) != 0:
            energyCounter = elem
    
    assert energyCounter != None
    
    energyCounter.screenshot(path="output/64.png")

    page.wait_for_timeout(5000)
    
    