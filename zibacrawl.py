import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
import pytz

# فقط دسته‌ی عطر
my_site_categories = {
    'https://www.zibatrust.com/product/%d8%b5%d8%a7%d8%a8%d9%88%d9%86-%d8%a8%d8%b1%d9%87-%d9%85%d9%88%d9%85-%d8%b9%d8%b3%d9%84-%d9%83%d9%86%d8%aa%d8%b1%d9%84-%d9%88-%d9%83%d8%a7%d9%87%d8%b4-%da%86%d8%b1%d8%a8%d9%8a-%d9%be%d9%88%d8%b3/': 'عطر و ادکلن',
}

def fetch_product_links(category_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        response = requests.get(category_url, headers=headers, timeout=10)
        if response.status_code != 200:
            print(f"❌ خطا در دریافت لینک‌ها از: {category_url} - Status code: {response.status_code}")
            return []
        soup = BeautifulSoup(response.text, 'html.parser')
        product_links = [a['href'] for a in soup.select('a.woocommerce-LoopProduct-link') if a.get('href')]
        return product_links
    except Exception as e:
        print(f"❌ خطای دریافت لینک محصول: {e}")
        return []

def fetch_product_data(product_url):
    headers = {
        'User-Agent': 'Mozilla/5.0'
    }
    try:
        response = requests.get(product_url, headers=headers, timeout=10)
        if response.status_code != 200:
            return None
        soup = BeautifulSoup(response.text, 'html.parser')
        
        # عنوان
        title = soup.find('h1', class_='product_title entry-title elementor-heading-title elementor-size-default')

        # قیمت از meta tag
        price_meta = soup.find('meta', property='product:price:amount')
        price = price_meta['content'] + ' تومان' if price_meta and price_meta.get('content') else None

        if title and price:
            return {
                'محصول': title.get_text(strip=True),
                'قیمت': price
            }
        else:
            print(f"⚠️ عنوان یا قیمت پیدا نشد برای: {product_url}")
        return None
    except Exception as e:
        print(f"❌ خطا در محصول: {product_url} - {e}")
        return None

all_dataframes = []

for category_url, title in my_site_categories.items():
    product_links = fetch_product_links(category_url)
    if not product_links:
        continue

    rows = []
    for link in product_links:
        data = fetch_product_data(link)
        if data:
            data['زمان ثبت'] = datetime.now(pytz.timezone('Asia/Tehran')).strftime('%Y-%m-%d %H:%M:%S')
            rows.append(data)

    if rows:
        all_dataframes.append(pd.DataFrame([{
            'محصول': f'📂 {title}', 'قیمت': '', 'زمان ثبت': ''
        }]))
        all_dataframes.append(pd.DataFrame(rows))
        all_dataframes.append(pd.DataFrame([{}]))  # خط جداکننده

if all_dataframes:
    final_df = pd.concat(all_dataframes, ignore_index=True)
    final_df.to_excel('my_site_output.xlsx', index=False)
    print("✅ فایل my_site_output.xlsx با موفقیت ساخته شد.")
else:
    print("⚠️ هیچ داده‌ای دریافت نشد، فایل اکسل ساخته نشد.")