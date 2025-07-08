from playwright.sync_api import sync_playwright

def get_price_from_liateam(url):
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=True)
        page = browser.new_page()
        page.goto(url, timeout=60000)
        page.wait_for_selector("div.product-price", timeout=10000)
        price = page.inner_text("div.product-price")
        browser.close()
        return price.strip()

url = "https://liateam.ir/products/399"
print(get_price_from_liateam(url))