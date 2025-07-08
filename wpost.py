import requests

# اطلاعات کاربر
WP_USER = 'naderiforphone@gmail.com'
WP_PASSWORD = 'khnvd1400@'
WP_SITE = 'https://zibatrust.com'

# آدرس API
api_url = f"{WP_SITE}/wp-json/wp/v2/posts"

# احراز هویت - روش Basic Auth
from requests.auth import HTTPBasicAuth
auth = HTTPBasicAuth(WP_USER, WP_PASSWORD)

# داده‌های پست
post_data = {
    'title': 'عنوان تستی از پایتون',
    'content': 'این پست از طریق برنامه پایتون ساخته شده است.',
    'status': 'publish',  # یا draft یا private
    'categories': [1],  # شناسه دسته‌بندی (از پیش باید ساخته شده باشد)
    'tags': [3, 4],      # شناسه برچسب‌ها (در صورت نیاز)
}

# ارسال پست
response = requests.post(api_url, json=post_data, auth=auth)

if response.status_code == 201:
    print("✅ پست با موفقیت منتشر شد!")
    print("لینک:", response.json()['link'])
else:
    print("❌ خطا در ارسال پست:", response.status_code)
    print(response.text)