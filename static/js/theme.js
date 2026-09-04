// theme.js
// مدیریت حالت دارک/لایت:
// ۱. اگه کاربر قبلاً دستی انتخاب کرده بود (تو localStorage ذخیره شده)، همون رو اعمال کن.
// ۲. اگه انتخابی نشده، هیچ data-theme ای ست نمی‌کنیم؛ CSS خودش با
//    @media (prefers-color-scheme: dark) بر اساس تنظیمات سیستم رنگ می‌ده.
// ۳. با کلیک روی دکمه toggle، کاربر می‌تونه بین لایت/دارک دستی جابه‌جا کنه.

(function () {
  const STORAGE_KEY = 'wrparsi-theme'; // مقادیر ممکن: 'light' | 'dark'
  const root = document.documentElement;

  function applyStoredTheme() {
    const stored = localStorage.getItem(STORAGE_KEY);
    if (stored === 'light' || stored === 'dark') {
      root.setAttribute('data-theme', stored);
    }
    // اگه چیزی ذخیره نشده، data-theme رو دست نمی‌زنیم تا حالت "خودکار" (سیستم) فعال بمونه
  }

  // این تابع رو بلافاصله در <head> صدا می‌زنیم (نه بعد از لود کامل صفحه)
  // تا رنگ درست از همون اول render بشه و صفحه چشمک نزنه
  applyStoredTheme();

  // بعد از لود شدن DOM، دکمه toggle رو پیدا کن و رویداد کلیک رو وصل کن
  document.addEventListener('DOMContentLoaded', function () {
    const toggleBtn = document.querySelector('[data-theme-toggle]');
    if (!toggleBtn) return;

    toggleBtn.addEventListener('click', function () {
      const current = root.getAttribute('data-theme');

      // اگه فعلاً حالت خودکاره (data-theme ست نشده)، بر اساس سیستم تصمیم بگیر
      const systemPrefersDark = window.matchMedia('(prefers-color-scheme: dark)').matches;
      const effectiveCurrent = current || (systemPrefersDark ? 'dark' : 'light');

      const next = effectiveCurrent === 'dark' ? 'light' : 'dark';
      root.setAttribute('data-theme', next);
      localStorage.setItem(STORAGE_KEY, next);
    });
  });
})();