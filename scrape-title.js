const puppeteer = require('puppeteer');

(async () => {
  const url = 'https://liateam.ir/products/399';

  const browser = await puppeteer.launch({
    headless: 'new',
    args: ['--no-sandbox', '--disable-setuid-sandbox'],
  });

  const page = await browser.newPage();

  try {
    await page.goto(url, { waitUntil: 'networkidle2', timeout: 0 });

    // اینجا سلکتور واقعی و تست‌شده را می‌گذاریم
    await page.waitForSelector('h1.chakra-heading.css-12gbwdp', { timeout: 15000 });
    const title = await page.$eval('h1.chakra-heading.css-12gbwdp', el => el.innerText.trim());

    console.log('✅ عنوان محصول:', title);
  } catch (err) {
    console.error('❌ خطا در پیدا کردن عنوان:', err);
  } finally {
    await browser.close();
  }
})();