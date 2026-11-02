# Ek F — Kodlar ve Kayıt Kimlikleri

Bu kitapta FG-04, KM-04 ve AS-08-01 gibi kodlar, aynı gereksinimi veya tasarım kaydını farklı bölümlerde bulabilmek için kullanılır. Bunlar ezberlenecek yeni yazılım terimleri değildir. Bir koda rastladığınızda yanındaki açıklamayı okuyabilir, ayrıntı için Ek F’deki kod dizinine dönebilirsiniz.

FG, fonksiyonel gereksinimi; IK, iş kuralını; KM, kabul ölçütünü belirtir. Örneğin FG-04 müşteriye görüşme notu ekleme ve notları görüntüleme işlevini, IK-04 notun müşteri, yazar ve eklenme zamanı ilişkisini, KM-04 ise notun doğru müşteriye bağlandığını değerlendireceğimiz koşulu gösterir. Aynı konuya ilişkin olmaları aynı belge türü oldukları anlamına gelmez.

AS-08-01 örneğinde AS kayıt türünü, 08 Bölüm 8’i, 01 ise o bölümdeki kayıt sırasını belirtir. Bu biçimdeki son 01 otomatik olarak sürüm numarası değildir. FG-04 gibi kısa kimliklerde ise 04 gereksinim sırasıdır; bölüm numarası olarak okunmaz. Kodun tamamını ve ait olduğu bağlamı birlikte okuyunuz.

Bir kimlik verilmesi, özelliğin geliştirildiğini veya testinin geçtiğini göstermez. Kodun işaret ettiği kaydın açıklaması, durumu ve kanıtı ayrıca okunur. Kitap 1’de oluşan kayıtlar, Kitap 2’de aynı kimliklerle kullanılmaya devam eder.

**Gereksinimler iş kuralları ve kabul ölçütleri**

| Kod veya aralık | Açıklama | Başvuru |
|---|---|---|
| FG-01 | Fonksiyonel gereksinim: etkin kullanıcının oturum açması ve oturumunu sonlandırması. | [Bölüm 4.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| FG-02 | Fonksiyonel gereksinim: adı zorunlu, e-posta ve telefonu isteğe bağlı müşteri kaydı oluşturma. | [Bölüm 4.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| FG-03 | Fonksiyonel gereksinim: müşterileri listeleme, adla arama ve seçilen kaydı açma. | [Bölüm 4.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| FG-04 | Fonksiyonel gereksinim: müşteriye görüşme notu ekleme ve o müşterinin notlarını görüntüleme. | [Bölüm 4.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| FG-05 | Fonksiyonel gereksinim: kişinin kendi takip görevlerini oluşturması, listelemesi ve tamamlaması. | [Bölüm 4.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| IK-01 | İş kuralı: müşteri adı zorunludur. Kodda Türkçe İ yerine I kullanımı korunur. | [Bölüm 4.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| IK-02 | İş kuralı: müşteri e-postası ve telefonu isteğe bağlıdır. | [Bölüm 4.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| IK-03 | İş kuralı: görüşme notu boş veya yalnızca boşluklardan oluşamaz. | [Bölüm 4.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| IK-04 | İş kuralı: not seçilen müşteriye bağlanır; ekleyen kullanıcı ve sistemin kaydettiği eklenme zamanı tutulur. | [Bölüm 4.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| UC-01 | Use case, kullanım senaryosu: görüşme notu ekleme akışı. | [Bölüm 4.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| KM-01 | Kabul ölçütü: geçerli not, doğru müşteri, yazar ve eklenme zamanı ile saklanıp yeniden görüntülenir. | [Bölüm 4.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| KM-02 | Kabul ölçütü: boş veya yalnızca boşluk içeren not reddedilir; yeni not oluşmaz. | [Bölüm 4.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| KM-03 | Kabul ölçütü: oturumsuz not ekleme isteği reddedilir; müşteri bilgisi açığa çıkarılmaz. | [Bölüm 4.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| KM-04 | Kabul ölçütü: not yalnız seçilen müşteriye bağlanır ve onun geçmişinde görünür. | [Bölüm 4.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| KM-05 | Kabul ölçütü: yanıt alınamadığında kesin başarı veya başarısızlık bildirilmez; sonuç doğrulanmadan otomatik yeni kayıt isteği başlatılmaz. | [Bölüm 4.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| AÇ-01 | Açık konu kaydı örneği: müşteri adı aramasında Türkçe büyük ve küçük harflerin nasıl eşleştirileceği. | [Bölüm 4.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |
| V-01 | Varsayım kaydı örneği: hedef günün gelecekte olması önerisinin mevcut kapsamla karşılaştırılıp reddedilmesi. | [Bölüm 4.16](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4) |

**Tasarım ve karar kayıtları**

| Kod veya aralık | Açıklama | Başvuru |
|---|---|---|
| TS-06-01 | Teknoloji seçimi kaydı: AI-CRM için başlangıç teknoloji kararı. | [Bölüm 6.22](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-6) |
| VD-07-01 | Veri tasarımı kaydı: AI-CRM başlangıç veri tasarımı ve ilişkileri. | [Bölüm 7.25](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7) |
| AS-08-01 | API sözleşmesi kaydı: AI-CRM başlangıç API taslağı; istek, yanıt, erişim ve tekrar kararları. | [Bölüm 8.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8) |
| Kİ-09-01 | Kod İnceleme ve İyileştirme Kaydı. | [Bölüm 9.18](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9) |
| TB-09-01 | Teknik borç kaydı örneği: yinelenen görev erişim kuralının bakım yükü. | [Bölüm 9.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9) |
| Tİ-10-01 | Tasarım İlkeleri Değerlendirmesi. | [Bölüm 10.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10) |
| SO-11-01 | SOLID Değerlendirmesi. | [Bölüm 11.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11) |
| DP-12-01 | Desen Değerlendirmesi. | [Bölüm 12.15](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12) |
| ADR-13-01 | Architecture Decision Record, mimari karar kaydı: AI-CRM’in Başlangıç Mimarisi. | [Bölüm 13.20](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13) |

**Yerel öğretim etiketleri**

| Kod veya aralık | Açıklama | Başvuru |
|---|---|---|
| P17 ve P18 | Örnek uygulama paketinin iki farklı içeriğini ayırt eden etiketler. Kitap 2, Bölüm 10’teki P01–P06 çalışma paketleriyle aynı dizi değildir. | [Bölüm 3.18](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3) |
| T-01 ve T-02 | Bir talimatın ilk ve düzeltilmiş sürümüne verilen örnek etiketler; iki ayrı ürün gereksinimi değildir. | [Bölüm 5.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5) |

**Bu kitabın eklerinde kullanılan kodlar**

**Ek B:** B01, B02, B03, B04, B05, B10. Her listede on iki kontrol maddesi bulunur. B02-04, ikinci listenin dördüncü maddesidir; bir bölüm numarası veya ürün sürümü değildir.

**Ek C:** T-C01, T-C02, T-C03, T-C05. T-C, yapılandırılmış talimat ailesini belirtir.

**Ek D:** K-D01, K-D02, K-D03, K-D04, K-D05, K-D06, K-D07, K-D08, K-D09, K-D10, K-D17, K-D21. K-D, kaynak rehberinin kimliğidir.

B, T-C ve K-D dizileri iki kitap boyunca sabittir. Kitapta bulunmayan numaralar diğer kitabın seçkisinde olabilir; bunlar eksik sayfa veya yeniden numaralandırma hatası değildir. Kod açıklamasına ihtiyaç duyduğunuzda önce bu ekteki kayıt türünü, sonra ilgili bölümün ayrıntısını okuyun.

**Benzer görünen kodları ayırt etme**

Bu dizin, kitap metinlerindeki kayıtlarla bunlara eşlik eden öğretim paketlerini birlikte kapsar. Aynı ailedeki benzer kayıtlar aralıkla gösterilir; örneğin FG-01–FG-05, FG-01’den FG-05’e kadar beş kaydın tümünü belirtir. Her kod ailesinin anlamı kendi bölümünden gelir; harflere her yerde geçerli tek bir açılım yüklenmez.

A ve B gibi kişi etiketleri, K-A ve K-B gibi kurum etiketleri, T1 gibi görev etiketleri ve 101/701 gibi sayısal kimlikler sentetik veriyi izlemek için kullanılır. Bunlar gereksinim veya onay kodu değildir. Kitap 2, Bölüm 7, 23 ve 24’ün örnek veri açıklamalarında ilgili kişi, kurum ve kayıt ilişkileri gösterilir.

API, HTTP, CI/CD ve SOLID gibi genel kısaltmalar Ek A’nın Kısaltmalar ve arama adları bölümündedir. OWASP risk sınıfları A01–A10, HTTP-01/DNS-01 doğrulama adları, UTF-8 ve SHA-256 gibi teknik adlar bu kitabın proje kayıt kimlikleriyle aynı adlandırma dizisine ait değildir. Bunlar kullanıldıkları bölümde açıklanır.
