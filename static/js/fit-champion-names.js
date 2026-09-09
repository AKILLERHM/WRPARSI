// fit-champion-names.js
// اگه اسم چمپیون توی یک خط جا نشه (مثل "MORDEKAISER")، فونتش رو
// کم‌کم کوچیک‌تر می‌کنیم تا کامل و بدون شکستن خط نمایش داده بشه.

(function () {
  var MIN_SCALE = 0.6; // حداکثر تا ۶۰٪ سایز اصلی کوچیک می‌شه، نه کمتر
  var STEP_PX = 0.5;

  function fitNames() {
    var names = document.querySelectorAll('.champion-info-bar__name');

    names.forEach(function (el) {
      // اول فونت رو به حالت پیش‌فرض CSS برگردون تا اندازه‌گیری درست انجام بشه
      el.style.fontSize = '';

      var baseFontSize = parseFloat(window.getComputedStyle(el).fontSize);
      var minFontSize = baseFontSize * MIN_SCALE;
      var currentFontSize = baseFontSize;

      while (el.scrollWidth > el.clientWidth && currentFontSize > minFontSize) {
        currentFontSize -= STEP_PX;
        el.style.fontSize = currentFontSize + 'px';
      }
    });
  }

  // بعد از لود کامل صفحه (فونت‌ها هم لود شده باشن) اجرا کن
  window.addEventListener('load', fitNames);

  // موقع تغییر سایز صفحه (مثلاً چرخش گوشی یا تغییر تعداد ستون‌ها) دوباره حساب کن
  var resizeTimer;
  window.addEventListener('resize', function () {
    clearTimeout(resizeTimer);
    resizeTimer = setTimeout(fitNames, 150);
  });
})();