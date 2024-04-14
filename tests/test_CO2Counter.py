import pytest 
from playwright.sync_api import Page, Route


def test_CO2Counter_22(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": -1,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/22.png")

    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_23(page: Page):
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/23.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_24(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/24.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_25(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 10,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/25.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_26(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 100,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/26.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_27(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/27.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_28(page: Page):
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/28.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_29(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1000000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/29.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_30(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1000000000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/30.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_31(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1000000000000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/31.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_32(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1000000000000000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/32.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_33(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 999,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/33.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_34(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 10000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/34.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_35(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 11111,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/35.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_36(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 125888,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/36.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_37(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 7899000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/37.png")
    
    page.wait_for_timeout(5000)
    

def test_CO2Counter_38(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 125888000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/38.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_39(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 7899000000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/39.png")
    
    page.wait_for_timeout(5000)
    

def test_CO2Counter_40(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 125888000000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/40.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_41(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1.49,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/41.png")
    
    page.wait_for_timeout(5000)
    

def test_CO2Counter_42(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 1.5,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/42.png")
    
    page.wait_for_timeout(5000)
    
    
def test_CO2Counter_43(page: Page):
    def handle(route: Route):
        json = {
	"result": {
		"blocks": {
			"personalImpact": {
				"data": {
					"co2": 2000,
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
    
    CO2Counter = None
    for elem in page.locator('div[class^="desktop-impact-item"]').all():
        if len(elem.locator('img[class^="desktop-bird"]').all()) != 0:
            CO2Counter = elem
    
    assert CO2Counter != None
    
    CO2Counter.screenshot(path="output/43.png")
    
    page.wait_for_timeout(5000)
    
