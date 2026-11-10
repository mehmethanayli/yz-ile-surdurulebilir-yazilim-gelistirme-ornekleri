# UÇ-23-01 — Uygulama sırası

Bu belge uygulanacak adımları tanımlar. [Paket özeti](README.md), [plan](integration-plan.json) ve [kabul senaryoları](acceptance-cases.json) birlikte okunur. Komut veya ürün testi çalıştırma kaydı değildir.

## P01 — Karar ve ortam hazırlığı

GO-14-01'in hedef ortamını gerçekten kurup sürüm, bağımlılık ve bağlantı kanıtını toplayın. AS-08-01'in uygulamayı etkileyen açık kararlarını somutlaştırın. Kullanıcı modelini ilk migration öncesinde değerlendirin. Ürün kararı beklerken yapılabilen belge ve senaryo hazırlığını sürdürebilirsiniz; bu hazırlığı şema veya ürün onayı saymayın.

## P02 — Oturum ve hesap sınırı

Aynı kökenli sunucu oturumunu, etkin hesap ve ekip rolünü uygulayın. K23-01–K23-04 ile giriş, çıkış, eski oturum ve yalnız hesap yöneticisi durumunu inceleyin. X01 ve X02 kapsamındaki CSRF/günlük koşullarını başlangıçtan itibaren koruyun. Gerçek sonucu aday ve ortam bilgisiyle kaydedin.

## P03 — Müşteri akışı

K23-05–K23-07 üzerinden oluşturma, yeniden okuma, aynı adla ayrı kimlik, arama ve sayfalama yolunu geliştirin. Gerekli alan, iletişim ve tekrar kararları çözülmeden tam kabul iddiasında bulunmayın. X03 ile gerçek PostgreSQL ilişkilerini ve oluşturma tekrarlarını değerlendirin.

## P04 — Not akışı

K23-08–K23-12'yi KM-01–KM-05 ile birlikte uygulayın. Müşteri yoldan, yazar oturumdan ve zaman sunucudan gelsin. İş kaydı ile tekrar bilgisinin tutarlılığını ve eşzamanlı durumu sınayın. Yanıt kaybında arayüzün otomatik yeni kayıt göndermediğini gerçek etkileşimle kontrol edin. CSRF ve veri minimizasyonunu koruyun.

## P05 — Kişisel görev ve ortak güvenlik incelemesi

K23-13–K23-15 ile oluşturma, A/B sınırı ve tekrarlanan tamamlama davranışını geliştirin. Liste, tekil okuma, yazma, yönetim ve varsa önbellek yollarını birlikte inceleyin. X01–X03 ortak kontrollerinin ilgili kapsamını tamamlayın. Code review, gerekli refactoring ve teknik borç değerlendirmesini adayla ilişkilendirin.

## P06 — Yayın ve bakım hazırlığı

P04 ve P05'in kabul kanıtları olmadan kullanıcıya hazır sürüm sonucu vermeyin. YK-21-01 yayın koşulları ile İB-22-01 işletim ve kurtarma ihtiyaçlarını gerçek ortama bağlayın. K23-16, dar yayın sonrası akışı değerlendirsin. Gözlem, restore ve kullanıcı öğrenmesi için ayrı kanıt toplayın; kısa smoke sonucunu bütün hizmetin garantisi saymayın.

## Kapanış kaydı

Kaynak commit'i, artifact, gerçek ortam, yürütülen kontrol ve gözlenen sonuç birlikte kaydedilir. Gerçek geliştirme başlamadığından mevcut pakette bu alanlar boştur. Öğretim dosyalarının yerel bütünlük kontrolü bu boşlukları tamamlamaz. Gerçek çalışma sırasında karar değişirse ilgili senaryolar, veri/API sözleşmesi ve metin birlikte güncellenir.
