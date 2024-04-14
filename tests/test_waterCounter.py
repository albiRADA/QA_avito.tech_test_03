import pytest 
from playwright.sync_api import Page, Route


def test_waterCounter_1(page: Page):
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/1.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_2(page: Page):
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/2.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_3(page: Page):
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
					"water": 1
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/3.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_4(page: Page):
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
					"water": 10
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/4.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_5(page: Page):
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
					"water": 100
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/5.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_6(page: Page):
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
    
    page.wait_for_selector('div[class^="desktop-impact-items"]')
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/6.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_7(page: Page):
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
					"water": 100000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/7.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_8(page: Page):
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
    
    page.wait_for_selector('div[class^="desktop-impact-items"]')
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/8.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_9(page: Page):
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
					"water": 1000000000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/9.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_10(page: Page):
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
					"water": 1000000000000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/10.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_11(page: Page):
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
					"water": 1000000000000000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/11.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_12(page: Page):
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
					"water": 999
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/12.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_13(page: Page):
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
					"water": 10000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/13.png")

    page.wait_for_timeout(5000)
    

def test_waterCounter_14(page: Page):
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
					"water": 11111
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/14.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_15(page: Page):
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
					"water": 125888
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/15.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_16(page: Page):
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
					"water": 7899000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/16.png")

    page.wait_for_timeout(5000)


def test_waterCounter_17(page: Page):
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
					"water":125888000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/17.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_18(page: Page):
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
					"water":7899000000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/18.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_19(page: Page):
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
					"water":125888000000
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/19.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_20(page: Page):
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
					"water":1.49
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/20.png")

    page.wait_for_timeout(5000)
    
    
def test_waterCounter_21(page: Page):
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
					"water":1.5
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
        
    waterCounter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-water"]').all()) != 0:
            waterCounter = elem
    
    assert waterCounter != None
    
    waterCounter.screenshot(path="output/21.png")

    page.wait_for_timeout(5000)
