<?php
/*
Plugin Name: WooCommerce Product Discount with Countdown
Description: تخفیف زمانی برای هر محصول با شمارش معکوس و برچسب تخفیف
Version: 1.2
Author: شما
*/

if (!defined('ABSPATH')) exit;

// 1. افزودن فیلدهای تخفیف به صفحه محصول
add_action('woocommerce_product_options_general_product_data', function () {
    echo '<div class="options_group">';

    woocommerce_wp_checkbox([
        'id' => '_ppd_enable_discount',
        'label' => 'فعال‌سازی تخفیف زمان‌دار؟'
    ]);

    woocommerce_wp_select([
        'id' => '_ppd_discount_type',
        'label' => 'نوع تخفیف',
        'options' => [
            'percent' => 'درصدی',
            'fixed' => 'مقدار ثابت'
        ]
    ]);

    woocommerce_wp_text_input([
        'id' => '_ppd_discount_value',
        'label' => 'مقدار تخفیف',
        'type' => 'number',
        'description' => 'درصد یا مبلغ ثابت'
    ]);

    woocommerce_wp_text_input([
        'id' => '_ppd_start_date',
        'label' => 'تاریخ شروع',
        'type' => 'date'
    ]);

    woocommerce_wp_text_input([
        'id' => '_ppd_end_date',
        'label' => 'تاریخ پایان',
        'type' => 'date'
    ]);

    echo '</div>';
});

// 2. ذخیره فیلدها
add_action('woocommerce_process_product_meta', function ($post_id) {
    $fields = ['_ppd_enable_discount', '_ppd_discount_type', '_ppd_discount_value', '_ppd_start_date', '_ppd_end_date'];
    foreach ($fields as $field) {
        if (isset($_POST[$field])) {
            update_post_meta($post_id, $field, sanitize_text_field($_POST[$field]));
        } else {
            delete_post_meta($post_id, $field);
        }
    }
});

// 3. اعمال تخفیف به قیمت محصول
add_filter('woocommerce_product_get_price', 'ppd_apply_discount', 10, 2);
add_filter('woocommerce_product_get_regular_price', 'ppd_apply_discount', 10, 2);

function ppd_apply_discount($price, $product) {
    if (get_post_meta($product->get_id(), '_ppd_enable_discount', true) !== 'yes') return $price;

    $start = get_post_meta($product->get_id(), '_ppd_start_date', true);
    $end = get_post_meta($product->get_id(), '_ppd_end_date', true);
    $today = date('Y-m-d');

    if (($start && $today < $start) || ($end && $today > $end)) return $price;

    $type = get_post_meta($product->get_id(), '_ppd_discount_type', true);
    $value = floatval(get_post_meta($product->get_id(), '_ppd_discount_value', true));

    if ($type === 'percent') {
        return $price * (1 - $value / 100);
    } elseif ($type === 'fixed') {
        return max(0, $price - $value);
    }

    return $price;
}

// 4. نمایش قیمت تخفیف‌خورده در صفحه محصول
add_filter('woocommerce_get_price_html', function ($price_html, $product) {
    $reg = $product->get_regular_price();
    $sale = $product->get_price();

    if ($sale < $reg) {
        return '<span class="onsale">تخفیف ویژه!</span><br><del>' . wc_price($reg) . '</del> <ins>' . wc_price($sale) . '</ins>';
    }

    return $price_html;
}, 20, 2);

// 5. شمارش معکوس در صفحه محصول
add_action('woocommerce_single_product_summary', 'ppd_countdown_timer', 25);
function ppd_countdown_timer() {
    global $product;
    if (get_post_meta($product->get_id(), '_ppd_enable_discount', true) !== 'yes') return;

    $end = get_post_meta($product->get_id(), '_ppd_end_date', true);
    if (!$end) return;

    echo '<div id="ppd-countdown" data-end="' . esc_attr($end) . '" style="margin-top:15px;font-size:18px;color:#d00;"></div>';
    ?>
    <script>
    document.addEventListener("DOMContentLoaded", function () {
        let end = document.getElementById('ppd-countdown').dataset.end;
        let countdownEl = document.getElementById('ppd-countdown');

        function updateCountdown() {
            let endDate = new Date(end + 'T23:59:59');
            let now = new Date();
            let diff = endDate - now;

            if (diff <= 0) {
                countdownEl.innerText = "مهلت تخفیف به پایان رسیده است.";
                return;
            }

            let days = Math.floor(diff / (1000 * 60 * 60 * 24));
            let hours = Math.floor((diff / (1000 * 60 * 60)) % 24);
            let minutes = Math.floor((diff / (1000 * 60)) % 60);
            let seconds = Math.floor((diff / 1000) % 60);

            countdownEl.innerText = `پایان تخفیف: ${days} روز ${hours} ساعت ${minutes} دقیقه ${seconds} ثانیه`;
        }

        updateCountdown();
        setInterval(updateCountdown, 1000);
    });
    </script>
    <?php
}
