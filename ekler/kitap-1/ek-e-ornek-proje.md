# Ek E — AI CRM Tasarım ve Devir Dosyası

Bu ek, ilk kitapta üretilen kararları ikinci kitaptaki geliştirme çalışmasına hazırlar. Amaç; gereksinimi, veri modelini, API sözleşmesini ve mimariyi aynı kapsam üzerinde okuyabilmektir. Tasarımın hazır olması çalışan uygulamanın hazır olduğu anlamına gelmez.

**E.1. İlk ürünün kapsamı**

AI-CRM, tek kurumda çalışan küçük bir ekip için tasarlanır. Müşteriler ve müşteri notları ortaktır; takip görevleri kişiseldir. Etkin bir ekip üyesi ortak iş verisine ve kendi görevlerine erişir. Hesap yönetimi rolü tek başına müşteri, not veya görevlere erişim sağlamaz. Devre dışı hesap korumalı işlemlerde kabul edilmez.

| Gereksinim | İlk ürünün davranışı |
|---|---|
| FG-01 | Etkin kullanıcının oturum açması ve oturumunu sonlandırması |
| FG-02 | Adı zorunlu, e-posta ve telefonu isteğe bağlı müşteri oluşturma |
| FG-03 | Müşterileri listeleme, adla arama ve seçilen kaydı açma |
| FG-04 | Seçilen müşteriye görüşme notu ekleme ve notlarını görüntüleme |
| FG-05 | Kişinin kendi takip görevlerini oluşturması, listelemesi ve tamamlaması |

Ödeme, dosya yükleme, çok kiracılık ve müşteri içeriğinin YZ ile işlenmesi ilk MVP’ye dahil değildir. Başlangıçtaki doğal dil örneklerinin daha geniş özellik sayması bu kapsamı kendiliğinden değiştirmez. Bağlayıcı gereksinimler [Bölüm 4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4), veri ve erişim kararları [Bölüm 7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7) ve [Bölüm 8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8) içindedir.

**E.2. Tasarım dosyalarının haritası**

| Bölüm ve kayıt | Devir dosyasında bulunacak bilgi |
|---|---|
| Bölüm 4 — FG, IK, UC ve KM | İşlevler, iş kuralları, not ekleme senaryosu, kabul ölçütleri ve açık konular |
| Bölüm 6 — TS-06-01 | Teknoloji seçimi, gerekçesi ve hedef ortam |
| Bölüm 7 — VD-07-01 | Kullanıcı, müşteri, not ve görev ilişkileri; kimlikler ve kısıtlar |
| Bölüm 8 — AS-08-01 | HTTP yolları, istek/yanıt, erişim, hata ve tekrar davranışları |
| Bölüm 9 — Kİ-09-01 ve TB-09-01 | İnceleme bulguları ve ertelenen teknik borç |
| Bölüm 10 — Tİ-10-01 | Tasarım ilkelerinin mevcut örneğe etkisi |
| Bölüm 11 — SO-11-01 | SOLID değerlendirmesi ve tercihlerin sınırları |
| Bölüm 12 — DP-12-01 | Kullanılan veya gereksiz bulunan desenlerin gerekçesi |
| Bölüm 13 — ADR-13-01 | Modüler monolit ve başlangıç mimarisinin karar kaydı |

Bu kayıtların ayrıntıları ilgili bölümün kendi metnindedir. Kodların açılımı ve tam başvuruları [Ek F](ek-f-kodlar-ve-kayit-kimlikleri.md) içindedir. Bu tablo kararların yerini buldurur; ayrıntılı API veya veri sözleşmesinin yerine geçmez.

**E.3. Tasarımı birlikte okumak**

Bir görüşme notunu uçtan uca izleyin. Önce FG-04 ile işlevi, IK-03 ve IK-04 ile boş olmayan içerik ve müşteri–yazar–zaman bağını okuyun. Ardından KM-01–KM-05 kabul ölçütlerini VD-07-01 ve AS-08-01 ile karşılaştırın.

Notun müşterisi istek yolundan, yazarı doğrulanmış aktörden, eklenme zamanı sunucudan gelir. Kayıt oluşturulmuşken yanıt kaybolabilir; bu durumda kullanıcıya kesin başarı veya başarısızlık bildirmek ve doğrulamadan otomatik yeni kayıt isteği göndermek doğru değildir. Tasarım kontrolünde hem verinin nereden geldiği hem belirsiz sonucun nasıl ele alındığı görünmelidir.

Kişisel görevde ortak müşteriye bağlanmak ortak sahiplik oluşturmaz. Görev yalnız sahibine açıktır; durum açık veya tamamlanmıştır. Gecikmişlik, açık görevin hedef gününün değerlendirme gününden önce olmasından türetilir. Geçmiş bir hedef günü seçilebilmesi mevcut kapsamla uyumludur.

**E.4. Açık kararlar ve değişiklik kaydı**

Alan uzunlukları, iletişim alanlarının dolu değer doğrulaması, zaman dilimi, oturum süresi veya tekrar isteği anahtarı gibi tamamlanmamış konular YZ tahminiyle kesinleştirilmez. Bir öneriyi önce açık karar olarak kaydedin; etkilenen gereksinim, veri ve API maddelerini birlikte değerlendirin.

| Alan | Yazılacak bilgi |
|---|---|
| Konu ve durum | Karar bekliyor, kabul edildi veya değiştirildi |
| Dayanak | İlgili FG, IK, KM, VD, AS veya ADR kaydı |
| Gerekçe ve seçenekler | Çözülen sorun, alternatifler ve sonuçlar |
| Etkilenen çıktılar | Veri, API, arayüz, test ve devir dosyası |
| Sorumlu ve tarih | Kararı veren kişi ve değerlendirme tarihi |
| Gerekli kanıt | Belge incelemesi veya uygulamada yürütülecek kontrol |

Çalışma kaydı kimliği ürün sürüm numarası değildir. Kabul edilen karar değişirse önceki gerekçe ve değişiklik ilişkisi korunur. Git kullanımı ve gerçek commit kaydı Kitap 2’de Bölüm 2’de ele alınır.

**E.5. Tasarımı sınamak için sentetik örnek**

Aşağıdaki senaryo [ortak sentetik veri dosyasıyla](../../assets/examples/chapter23-integration/synthetic-data.json) uyumludur. Gerçek müşteri verisi içermez; bir kurulum veya veritabanına yükleme dosyası değildir.

| Aktör veya kayıt | Tasarımda incelenecek durum |
|---|---|
| A ve B | Etkin ekip üyeleri; ortak müşteri ve notlara, kendi kişisel görevlerine erişirler |
| S | Etkin, yalnız hesap yönetimi rolü; bu rol iş verisine erişim sağlamaz |
| D | Devre dışı ekip üyesi; eski oturum korumalı işleme yeterli değildir |
| Müşteri 101 ve 102 | İkisinin de görünen adı Deniz Kaya’dır; kimlikleri farklıdır |
| Not 501 | Müşteri 102’ye aittir; yazarı A’dır |
| Görev 701 ve 702 | İkisi de müşteri 102 ile ilişkilidir; 701 A’nın, 702 B’nindir |

Okuma soruları: Not 501 aynı adlı müşteri 101’in ayrıntısında görünürse hangi ölçüt bozulur? B, 701’i tamamlayabilir mi? S yalnız hesap yönetimi rolüyle müşteri notlarını açabilir mi? D’nin eski oturumu hangi koşulu karşılamaz? Yanıtları sırasıyla doğru müşteri ilişkisi, kişisel sahiplik, ekip erişimi ve etkin hesap koşuluyla açıklayın. Bu değerlendirme belge üzerindeki senaryo incelemesidir.

**E.6. İkinci kitaba devir**

Geliştirmeye geçmeden önce [Ek B’deki](ek-b-kontrol-listeleri.md) gereksinim, mimari ve veritabanı listelerini kullanın. Eksikleri [Ek C’deki](ek-c-yapilandirilmis-ai-talimatlari.md) gereksinim, mimari veya veri modeli talimatıyla inceleyebilirsiniz.

| Devir bileşeni | Tamamlanma ölçütü |
|---|---|
| Kapsam | FG-01–FG-05 ve kapsam dışı işler görünür |
| İş kuralları ve kabul | IK ve KM kayıtları gereksinimle tutarlı |
| Veri ve API | VD-07-01 ile AS-08-01 aynı kimlik, değer kaynağı ve yetkiyi anlatıyor |
| Tasarım ve mimari | TS-06-01, değerlendirme kayıtları ve ADR-13-01 erişilebilir |
| Açık işler | Karar bekleyen konular ve etkilenen geliştirme işleri belirtilmiş |
| Kanıt durumu | Belge üzerinde incelenenlerle henüz uygulanmayan ve sınanmayanlar ayrılmış |

Bu paketle Kitap 2’nin Bölüm 1’ündeki ortam hazırlığına geçilir. Kitap 2, Bölüm 10’teki bütünleştirme paketi aynı tasarımı uygulama sırasına bağlar. İlk kitabı okumak için uygulama veya veritabanı kurulması gerekmez.
