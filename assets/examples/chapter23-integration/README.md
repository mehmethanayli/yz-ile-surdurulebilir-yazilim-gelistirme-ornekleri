# Kitap 2 Bölüm 10 — Baştan Sona AI Destekli Bir Uygulama Geliştirmek

**Uçtan uca bütünleştirme paketi**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

**UÇ-23-01**, [Bölüm 10](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-10) için hazırlanmış öğretim paketidir. Çalışan CRM uygulaması veya ürün testi raporu değildir. Önceki kararları uygulama sırası, kabul senaryosu ve kanıt ihtiyacına bağlar.

## Dosyalar

- [integration-plan.json](integration-plan.json): beş gereksinim, beş not ölçütü, 12 açık karar grubu ve altı geliştirme paketi.
- [acceptance-cases.json](acceptance-cases.json): 16 planlı kabul senaryosu ve üç ortak kontrol alanı. Hepsi `not_run`; gerçek sonuç ve kanıt boş.
- [synthetic-data.json](synthetic-data.json): A/B ekip üyeleri, yalnız hesap yöneticisi S, devre dışı D, aynı adlı iki müşteri, bir not ve iki kişisel görev.
- [implementation-sequence.md](implementation-sequence.md): uygulama sırasında izlenecek altı paket ve kanıt beklentileri.
- [verification.json](verification.json): yerel belge/ilişki kontrolleri ve kaynak dosya özetleri.

## Nasıl okunur?

Önce FG-01–FG-05'in Kitap 1, Bölüm 4'teki anlamını ve AS-08-01'in Kitap 1, Bölüm 8'deki açık kararlarını okuyun. Pakette bu kimlikler değiştirilmez. D01–D12 bu bölümdeki takip gruplarıdır; önceki kararların yerine geçmez. D10, kullanıcı modeli ve hesap hazırlama yöntemini uygulamadan önce değerlendirmek için görünür kılınmıştır.

Paketler arasında bağımlılık vardır: P01 → P02 → P03; P03'ten P04 ve P05'e, ikisinden P06'ya geçilir. Bu, bir takvim veya tamamlanmış çalışma kaydı değildir. Yetki gibi ortak koşullar ilgili bütün dilimlerde korunur. P05'teki ortak inceleme, güvenliği ilk kez sona bırakmak anlamına gelmez.

Bir kabul senaryosunun karar bağı bulunması, bütün parçalarının anlatılamayacağı anlamına gelmez. Örneğin görev sahibinin korunması seçilmiş karardır; sayfa büyüklüğü hâlâ açıktır. Gerçek uygulama için ilgili kararlar somutlaştırılır ve hedef ortam doğrulanır. Paket, belirsizliği rastgele değerle kapatmaz.

Üç ortak kontrol X01–X03, CSRF, günlük/hata minimizasyonu ve hedef veritabanı/eşzamanlılık alanlarını ayrıca görünür tutar. Bunlar 16 senaryo sayısına ek test yöntemi gibi dahil edilmez. Aynı şekilde K23-12'nin alt koşulları çalıştırılmış test sayılmaz.

## Sentetik ilişkiler

A ve B aynı müşteriye erişebilen ekip üyeleridir. Müşteri 101 ile 102 aynı ada rağmen ayrı kimliktedir. Not 501 yalnız 102'ye bağlıdır ve yazarı A'dır. Görev 701 A'ya, 702 B'ye aittir; ortak müşteri ilişkisi görevleri ortak yapmaz. S yalnız hesap yönetimi rolündedir; D etkin değildir.

Bu ilişkileri dosyada görmek, erişim denetiminin uygulandığını kanıtlamaz. Tarihler örnek değerlerdir; sunucudan üretilmiş gerçek kayıt veya AS-08-01'in zaman dilimi kararı değildir. Gerçek kişi, müşteri, sır veya servis bağlantısı bulunmaz.

## Doğrulama ve sınırı

Yerel kontrol; kimlik benzersizliği, paket bağımlılıklarının döngüsüzlüğü, gereksinim/ölçüt kapsamı, açık karar referansları, sentetik ilişkiler ve çalıştırılmamış durumların korunmasını inceler. Dosya özetleri UTF-8 metin okunup satır sonları LF'ye normalleştirilerek hesaplanır. Kullanılan yerel Python sürümü verification.json'dadır.

Hedef Python 3.14, Django 5.2, PostgreSQL 18 ve Psycopg 3 kurulmamıştır. Gerçek HTTP, oturum, parola, CSRF, tarayıcı, veritabanı, eşzamanlılık, CI/CD, yayın ve restore denenmemiştir. Yeni uygulama deposu veya commit oluşturulmamış, uzak depoya gönderim yapılmamıştır. Uygulama tamamlanması için bu paketin ötesinde gerçek geliştirme ve kabul kanıtı gerekir.
