const fs = require('fs');
const cheerio = require('cheerio');
const ExcelJS = require('exceljs');

// فایل HTML رو بخون


// سِلکتور مورد نظر برای محصولات
const productElements = $(".css-1ro2nn");

// 🟡 لاگ برای بررسی تعداد محصولات
console.log("🔍 تعداد محصولات پیدا شده:", productElements.length);

const html = fs.readFileSync('products.html', 'utf-8');
console.log(html);  // این خط را اضافه کن تا محتوای HTML را ببینی

// اگر محصولی پیدا شده، نمایش بده
productElements.each((i, el) => {
  const title = $(el).text().trim();
  console.log(`📦 محصول ${i + 1}:`, title);
});