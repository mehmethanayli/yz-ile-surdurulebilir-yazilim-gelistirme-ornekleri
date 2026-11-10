# Ek B — AI ile Yazılım Geliştirme Kontrol Listeleri

Bu ek, iki kitap boyunca verilen kararları çalışma sırasında kullanılabilen kontrollere dönüştürür. Bir kontrol listesi, işi otomatik olarak doğru veya güvenli yapmaz; unutulabilecek soruları, beklenen kanıtı ve eksik bulunduğunda izlenecek yolu görünür kılar. Maddeler kitabın AI-CRM örneğiyle somutlaştırılmıştır. Başka projeye uyarlarken örneğin iş kuralını evrensel yazılım kuralı olarak taşımayın.

**Serinin bütünü:** Ortak Ek B kaynağında B.1–B.10 altında 120 madde bulunur; bu kitap için aşağıda bir seçki verilmiştir. Her maddeye kalıcı kimlik verilmiştir; örneğin `B06-04`, güvenlik listesindeki dördüncü kontroldür. Bu kimlikler FG, KM, AS, GO veya diğer bölüm kayıtlarının yerine geçmez. Ayrıntılı terimler için [Ek A — Terimler Sözlüğü](ek-a-terimler-sozlugu.md) kullanılabilir.

Listeler farklı anlarda yeniden kullanılabilir. Proje başlangıcında B.1–B.4 ağırlık kazanır; değişikliklerde B.5–B.7 ve B.10 kullanılır; yayın öncesi B.8, hizmet sürerken B.9 uygulanır. Güvenlik ve doğrulama yalnız bu sıralamada ilk kez yapılacak işler değildir. Küçük bir değişiklikte etkilenen maddeler seçilir; uygulanmayan maddenin neden kapsam dışında olduğu açıklanır.

**Nasıl kullanılmalı?**

Önce incelenen işi, kaynak sürümünü, ortamı ve beklenen davranışı yazın. Her maddenin yanındaki **Kanıt** alanı ne aranacağını, **Eksikse** alanı açığın nasıl ele alınacağını belirtir. Kanıt türü kontrolün iddiasına uygun olmalıdır: gereksinim kararı için belge incelemesi yeterli olabilir; gerçek ürün davranışı için o davranışı gösteren yürütme gerekir. Belgeye bakarak ürün testini geçmiş saymayın.

| Durum | Anlamı | Kayıtta bulunması gereken |
|---|---|---|
| Bekliyor | Kontrol henüz değerlendirilmedi. | Beklenen kanıt ve sonraki iş |
| Doğrulandı | Belirtilen kapsamda yeterli kanıt bulundu. | Kanıt türü, kaynak/ortam, sonuç ve tarih |
| Uygunsuz | İncelenen kanıt bir koşulun sağlanmadığını gösterdi. | Beklenen–gözlenen farkı ve düzeltme işi |
| Çalıştırılamadı | Gerekli kontrol ortam veya erişim gibi engelle yürütülemedi. | Engel, etkilediği iddia ve giderme adımı |
| Kapsam dışı | Madde incelenen iş için geçerli değil. | Gerekçe ve hangi değişiklikte yeniden ele alınacağı |

Kutuyu yalnız **Doğrulandı** durumunda işaretleyin. Diğer durumları inceleme kaydına yazın; kapsam dışı maddeyi başarı sayısına katmayın. Bu dosyadaki bütün kutular başlangıçta boştur. Dosyanın hazırlanması, gerçek AI-CRM kontrollerinin yapıldığı anlamına gelmez. Doğrulanmış bir tasarım maddesi de kendi başına yayın onayı vermez. Kaynak sürümü, gereksinim veya yapılandırma değiştiğinde etkilenen kanıt yeniden değerlendirilir; eski işaret yeni çalışma kaydına otomatik aktarılmaz.

Eksik maddeyi ilgili karar veya düzeltme işine bağlayın. Her eksik bütün projeyi durdurmaz: hangi bağımlı işin ilerleyemeyeceği açıklanır, etkilenmeyen işler sürdürülebilir. Veri veya yetki sınırını bozan bilinen kusur, test engeliyle veya başka bir başarılı ölçütle gizlenmez. İşin kabulünü etkileyen açık konular karar kaydında görünür tutulur.

**Bu kitaptaki seçim:** 6 liste, 72 kontrol maddesi. Liste ve madde numaraları seri boyunca korunur; atlayan numaralar bu kitaba alınmayan listelerdir. B01–B05 planlama, tasarım ve kod okuma; B10 YZ çıktısını inceleme için kullanılır. Henüz kurulmamış ortam veya çalıştırılmamış test isteyen bir madde, hazırlık işi olarak kaydedilir. Tasarım incelemesi gerçek ürün testi yerine yazılmaz.

**İçindekiler**

- [B.1. Yeni Proje Kontrol Listesi](#ek-b-1)
- [B.2. Gereksinim Analizi Kontrol Listesi](#ek-b-2)
- [B.3. Mimari Kontrol Listesi](#ek-b-3)
- [B.4. Veritabanı Tasarım Kontrol Listesi](#ek-b-4)
- [B.5. Kod Review Kontrol Listesi](#ek-b-5)
- [B.10. AI Çıktısı Doğrulama Kontrol Listesi](#ek-b-10)
- [İnceleme kaydı şablonu](#ek-b-kayit)
- [Öğretim örneği Bir gereksinim önerisini incelemek](#ek-b-ornek)
- [Kaynakça](#ek-b-kaynakca)

<a id="ek-b-1"></a>

**B.1. Yeni Proje Kontrol Listesi**

Bu liste, işe başlanacak bağlamı görünür kılar. Kullanıcının problemiyle teknoloji tercihinin karıştırılmasını ve mevcut bir depoda yanlış hedef üzerinde çalışılmasını önlemeye yardım eder. Tasarım aşamasında karar belgesi kanıt olabilir; kurulmuş ortam veya çalışan ürün iddiası için gerçek yürütme gerekir. Güvenli geliştirme uygulamalarını yaşam döngüsüne yerleştirme yaklaşımı, NIST SSDF'nin temel çerçevesidir (Souppaya vd., 2022).

AI-CRM için kitap deposu, bağımsız öğretim laboratuvarı ve gelecekteki uygulama deposu ayrı tutulur. Hedef teknolojilerin adlarının bulunması bunların birlikte kurulduğunu göstermez. Başlangıç incelemesi neyin kararlaştırıldığını ve hangi kararın açık olduğunu belirlemelidir.

Dayanak: [Gereksinim ve MVP](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4), [GO-14-01](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1), [UÇ-23-01](../../assets/examples/book-2-chapter-10-integration/README.md).

- [ ] **B01-01 — Çözülecek problem ve hedef kullanıcı açık mı?** **Kanıt:** Kimin hangi işini iyileştireceğini açıklayan problem kaydı. **Eksikse:** Teknoloji seçmeden önce ihtiyaç ifadesini düzeltin.

- [ ] **B01-02 — Başlangıç başarısı nasıl anlaşılacak?** **Kanıt:** Gözlenebilir sonuç ve değerlendirme koşulu. **Eksikse:** Belirsiz “başarılı” ifadesini değerlendirilebilir beklentiye çevirin.

- [ ] **B01-03 — İlk kapsam ve kapsam dışı işler yazılı mı?** **Kanıt:** MVP işlevleri ve ertelenen özellikler. **Eksikse:** Yeni isteğin veri, yetki ve süre etkisini değerlendirin.

- [ ] **B01-04 — Doğru depo, dal ve çalışma dizini belirlendi mi?** **Kanıt:** Yerel yol, depo amacı, dal ve mevcut değişiklik özeti. **Eksikse:** Yanlış hedefte değişiklik yapmadan çalışma bağlamını düzeltin.

- [ ] **B01-05 — Mevcut kullanıcı değişiklikleri görüldü mü?** **Kanıt:** Başlangıç farkı ve korunacak dosyaların kaydı. **Eksikse:** Değişiklikleri ayırın; bilinmeyen içeriği silmeyin.

- [ ] **B01-06 — Hedef ortam ile kurulu ortam ayrıldı mı?** **Kanıt:** Araç sürümleri ve çalıştırılmış kurulum kontrolleri. **Eksikse:** Hedef sürüm listesini başarılı kurulum sonucu diye sunmayın.

- [ ] **B01-07 — Bağımlılıklar için gerekçe var mı?** **Kanıt:** Temel paketlerin amacı ve mevcut çözümle ilişkisi. **Eksikse:** Gereksiz öneriyi çıkarın; gerekeni uyumlulukla değerlendirin.

- [ ] **B01-08 — Veri ve sırların yeri belirlendi mi?** **Kanıt:** Sentetik örnek, yapılandırma ve gizli bilgi ayrımı. **Eksikse:** Gerçek müşteri veya erişim bilgisini genel bağlamdan çıkarın.

- [ ] **B01-09 — YZ görevi ve araç yetkisi sınırlı mı?** **Kanıt:** İlgili kaynak, değiştirilecek alan ve izinli eylem. **Eksikse:** Belirsiz görevi dar çalışma birimlerine ayırın.

- [ ] **B01-10 — Geliştirme sırası bağımlılıkları gösteriyor mu?** **Kanıt:** Birbirini bekleyen karar ve işlerin planı. **Eksikse:** Açık sözleşme kararını varsayan işi yeniden sıraya koyun.

- [ ] **B01-11 — İlk doğrulama yolu uygulanabilir mi?** **Kanıt:** Kontrolün ortamı, yöntemi ve beklentisi. **Eksikse:** Çalıştırılamayan kontrolün engelini kaydedin.

- [ ] **B01-12 — İş ve karar sorumluları belli mi?** **Kanıt:** Karar sahibi, uygulayan ve inceleyen roller. **Eksikse:** Tek kişi çalışsa da sorumlulukları belirtin.

Bu liste kapanınca elde edilen şey başlangıç bağlamıdır. Ürün kabulü ve yayın kanıtı sonraki çalışmalarla tamamlanır; ilk planın düzgün olması uygulamanın tamamlandığı anlamına gelmez.

<a id="ek-b-2"></a>

**B.2. Gereksinim Analizi Kontrol Listesi**

Bu liste kullanıcı isteğini uygulanabilir davranışa dönüştürürken kullanılır. YZ önerisi, örnek verideki rastlantı ve kararlaştırılmış gereksinim aynı kaynak değildir. Bilinmeyen uzunluk, süre veya kota değerleri sessizce tamamlanmamalıdır. Her kararın kaynağı ve değiştiğinde etkilediği alanlar izlenebilmelidir.

AI-CRM'de ortak müşteri portföyü ve notlarla kişisel görevler arasındaki ayrım temel örnektir. Bir müşteri üzerinde ortak çalışmak, o müşteriye bağlı bütün görevleri ortak yapmaz. Gereksinim incelemesi bu ayrımı ekran, veri ve API kararlarına aynı anlamla taşır.

Dayanak: [MVP kapsamı](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4), [API sözleşmesi](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8), [Bütünleştirme planı](../../assets/examples/book-2-chapter-10-integration/integration-plan.json).

- [ ] **B02-01 — Gereksinimler kimlik ve kaynakla izleniyor mu?** **Kanıt:** FG-01–FG-05 ve ilgili ihtiyaç açıklamaları. **Eksikse:** Aynı işe çelişkili tanımlar eklemek yerine kaynak kaydı bağlayın.

- [ ] **B02-02 — Aktör ve rol anlamları açık mı?** **Kanıt:** Ekip üyesi, hesap yöneticisi ve etkinlik durumu. **Eksikse:** Rol adına dayanarak iş verisi yetkisi eklemeyin.

- [ ] **B02-03 — Ortak ve kişisel kapsam ayrıldı mı?** **Kanıt:** Ortak müşteri/not ve yalnız sahibine açık görev. **Eksikse:** Liste, ayrıntı ve tamamlama yollarını aynı sınırla eşleştirin.

- [ ] **B02-04 — Kabul ölçütleri davranışı gösteriyor mu?** **Kanıt:** Not akışında KM-01–KM-05; diğer işlevlerin ayrı koşulları. **Eksikse:** Not ölçütlerini bütün uygulamanın kabul kapsamı saymayın.

- [ ] **B02-05 — Ön koşul ve alternatif yollar yazılı mı?** **Kanıt:** Oturum, etkin hesap, boş sonuç ve ret yolları. **Eksikse:** Yalnız mutlu yolu anlatan senaryoyu tamamlayın.

- [ ] **B02-06 — Girdi ile sunucunun değerleri ayrıldı mı?** **Kanıt:** Not müşterisi yoldan, yazarı aktörden, zamanı sunucudan. **Eksikse:** İstemcinin kendine yazar veya sahip seçtiği varsayımı kaldırın.

- [ ] **B02-07 — Görev yaşam döngüsü tutarlı mı?** **Kanıt:** Açık/tamamlanmış durumları ve türetilen gecikmişlik. **Eksikse:** Yeni durum, atama veya hatırlatmayı kapsam kararı olmadan eklemeyin.

- [ ] **B02-08 — Sınır değerler ve açık kararlar ayrıldı mı?** **Kanıt:** Uzunluk, biçim, boşluk, takvim günü ve arama kararları. **Eksikse:** Açık alanı rastgele değerle kapatmayın.

- [ ] **B02-09 — Tekrar ve belirsiz yanıt tanımlı mı?** **Kanıt:** Yanıt kaybı, aynı eylemin tekrarı ve çatışma koşulları. **Eksikse:** Yanıt yokluğunu otomatik başarısız kayıt saymayın.

- [ ] **B02-10 — Kalite beklentileri ölçüm bağlamı taşıyor mu?** **Kanıt:** Ortam, yük, ölçü ve kabul sınırı. **Eksikse:** Bağlamsız yüzdeyi veya süreyi kesin gereksinim saymayın.

- [ ] **B02-11 — Kapsam dışı işlerle çelişki var mı?** **Kanıt:** Ödeme, dosya yükleme, çok kiracılık ve YZ içerik işlemenin durumu. **Eksikse:** Gelecek özellikleri ilk MVP'ye sessizce taşımayın.

- [ ] **B02-12 — Gereksinim değişiminin etkisi izlendi mi?** **Kanıt:** Veri, API, test, belge ve kabul kaydı değişiklikleri. **Eksikse:** Yalnız ekran metnini değiştirerek incelemeyi kapatmayın.

Çıktı, kararlaştırılan davranışları açık sorulardan ayıran gereksinim kaydıdır. Belge incelenmiş olsa bile gerçek kabul senaryoları henüz yürütülmemiş olabilir; iki durumu ayrı raporlayın.

<a id="ek-b-3"></a>

**B.3. Mimari Kontrol Listesi**

Mimari inceleme diyagramdaki kutu sayısını değil, kararın ihtiyaca uygunluğunu değerlendirir. Her sınırın sorumluluğu, veri hareketi ve değişiklik maliyeti bulunmalıdır. Popülerlik tek başına gerekçe değildir; alternatifin yararı ekip ve işletim koşullarıyla ilişkilendirilir.

AI-CRM'in modüler monolit yaklaşımı müşteri, not ve görev sorumluluklarını tek dağıtım biriminde düzenler. Gelecekteki SaaS taslağı bugünkü tek kurumlu MVP'nin içine kendiliğinden taşınmaz. Mimari karar kaydı, seçimin gerekçesini ve yeniden değerlendirme koşulunu saklar.

Dayanak: [Mimari](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13), [Tasarım ilkeleri](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10), [Gelecek SaaS kapsamı](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

- [ ] **B03-01 — Kararın çözdüğü sorun açık mı?** **Kanıt:** İş ihtiyacı, kısıt ve karar gerekçesi. **Eksikse:** Mimari etiket yerine karşılanan ihtiyacı yazın.

- [ ] **B03-02 — Daha basit seçenek karşılaştırıldı mı?** **Kanıt:** Alternatiflerin yarar ve bakım maliyetleri. **Eksikse:** Gerekçesiz servis veya katmanı çıkarın.

- [ ] **B03-03 — Modül sorumlulukları anlamlı mı?** **Kanıt:** Müşteri, not ve görev işlerinin sınırları. **Eksikse:** Dosya sayısı yerine değişiklik etkisini inceleyin.

- [ ] **B03-04 — Bağımlılık yönleri görünür mü?** **Kanıt:** Bileşenlerin arayüz ve veri ilişkileri. **Eksikse:** Gizli ortak durum ve döngüleri somutlaştırın.

- [ ] **B03-05 — Güven sınırları çizildi mi?** **Kanıt:** İstemci, uygulama, veritabanı ve varsa dış hizmet akışı. **Eksikse:** Girdinin nerede güvenilir kabul edildiğini sorgulayın.

- [ ] **B03-06 — Yetki doğru yerde uygulanıyor mu?** **Kanıt:** Sunucuda hesap, rol ve kaynak kapsamı. **Eksikse:** Ekran gizlemeyi yetki kanıtı saymayın.

- [ ] **B03-07 — Ortak hata noktaları belirlendi mi?** **Kanıt:** Bağımlılık arızasının kullanıcı yoluna etkisi. **Eksikse:** Sunucu sayısından hizmet garantisi çıkarmayın.

- [ ] **B03-08 — İşlem ve dış yan etkiler ayrıldı mı?** **Kanıt:** Kalıcı veri, yanıt ve varsa olayın sırası. **Eksikse:** Yerel transaction'ı tüm dış sistem için atomiklik saymayın.

- [ ] **B03-09 — Ölçek önerisi ölçüme bağlı mı?** **Kanıt:** Tanımlı yükte darboğaz veya sınanacak hipotez. **Eksikse:** Ölçülmemiş kapasiteyi gerçekleşmiş kazanç diye yazmayın.

- [ ] **B03-10 — Gözlem ve teşhis tasarlandı mı?** **Kanıt:** Gerekli olay, metrik ve ilişkilendirme bilgisi. **Eksikse:** Gereksiz hassas içerik toplamadan teşhis yolunu belirleyin.

- [ ] **B03-11 — Yayın ve şema geçişi birlikte düşünüldü mü?** **Kanıt:** Eski/yeni kodun veri uyumu ve dönüş seçeneği. **Eksikse:** Uyumsuz migration'ı yalnız kod rollback'iyle çözülebilir saymayın.

- [ ] **B03-12 — Karar kaydı güncel mi?** **Kanıt:** ADR'de bağlam, seçenek, karar ve açık konular. **Eksikse:** Değişen varsayımı kayda işleyin.

Liste ayrı servis veya desen kullanmayı zorunlu tutmaz. Kapsama girmeyen dış hizmet kontrolleri gerekçesiyle ayrılabilir; mevcut veri ve yetki sınırları mimari tercihle kaldırılmaz.

<a id="ek-b-4"></a>

**B.4. Veritabanı Tasarım Kontrol Listesi**

Kavramsal model, saklama yapısı ve uygulama erişimi birlikte incelenir. Yabancı anahtar ilişkiyi kısıtlayabilir; kullanıcının erişimini tek başına belirlemez. PostgreSQL belgeleri NOT NULL, benzersizlik ve referans bütünlüğü gibi kısıtları ayrı işlevlerle açıklar (PostgreSQL Global Development Group, t.y.). Kuralların uygulandığı katman görünür tutulur.

AI-CRM notu doğru müşteri, doğrulanmış yazar ve sunucu zamanıyla ilişkilendirilir. Görev sahibine bağlıdır. Aynı adlı iki müşterinin ayrı kimlikleri olabilir; ad eşitliği kayıtları birleştirme gerekçesi değildir. Tasarım incelemesiyle gerçek veritabanı davranışı testi ayrı kanıtlardır.

Dayanak: [Veri modeli](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7), [API sözleşmesi](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8), [Sentetik ilişkiler](../../assets/examples/book-2-chapter-10-integration/synthetic-data.json).

- [ ] **B04-01 — Varlık ve alanlar ihtiyaçtan türetildi mi?** **Kanıt:** Müşteri, not, görev ve hesap modelinin gerekçesi. **Eksikse:** Gerekçesiz tablo ve alanları çıkarın.

- [ ] **B04-02 — Kimlikler adlardan ayrı mı?** **Kanıt:** Aynı adlı müşterileri ayrı tutan anahtarlar. **Eksikse:** Değişebilir adı kalıcı kimlik yerine kullanmayın.

- [ ] **B04-03 — İlişki yönleri ve çokluklar doğru mu?** **Kanıt:** Notun müşterisi/yazarı, görevin müşterisi/sahibi. **Eksikse:** Belirsiz ilişkiyi iş kuralıyla kesinleştirin.

- [ ] **B04-04 — Zorunlu ve isteğe bağlı alanlar ayrıldı mı?** **Kanıt:** NULL, boş metin ve eksik alanın anlamı. **Eksikse:** Aynı anlamdaki çelişkili temsilleri gözden geçirin.

- [ ] **B04-05 — Kısıtların katmanı belli mi?** **Kanıt:** Uygulama doğrulaması ve veritabanı kısıt eşleştirmesi. **Eksikse:** Yalnız form kontrolüne dayanan bütünlük iddiasını düzeltin.

- [ ] **B04-06 — Zaman ve tarih anlamı korunuyor mu?** **Kanıt:** Kayıt zamanı ile hedef takvim gününün ayrımı. **Eksikse:** Açık zaman dilimi kararını rastgele varsaymayın.

- [ ] **B04-07 — Görev durumları tutarlı mı?** **Kanıt:** Açık/tamamlanmış saklama ve türetilen gecikmişlik. **Eksikse:** Üçüncü kalıcı durum ekleyen şemayı düzeltin.

- [ ] **B04-08 — Silme ve geçmiş etkileri düşünüldü mü?** **Kanıt:** İlişkili kayıt davranışı ve saklama kararı. **Eksikse:** Şema davranışından otomatik kullanıcı silme yeteneği çıkarmayın.

- [ ] **B04-09 — Sorgular sahiplikle sınırlı mı?** **Kanıt:** Kişisel görevde aktör kapsamı ve test taslağı. **Eksikse:** Yalnız kimlikle okuyan yolu erişim koşuluyla düzeltin.

- [ ] **B04-10 — Tekrar ve eşzamanlılık birlikte tasarlandı mı?** **Kanıt:** Atomiklik, anahtar kapsamı, yarış ve çatışma yaklaşımı. **Eksikse:** Önce oku sonra yaz sırasını tek başına yarış güvencesi saymayın.

- [ ] **B04-11 — İndeksler gerçek sorguya dayanıyor mu?** **Kanıt:** Sorgu, veri dağılımı ve gerekiyorsa ölçüm. **Eksikse:** Her sütuna otomatik indeks eklemeyin.

- [ ] **B04-12 — Migration ve kurtarma denenebilir mi?** **Kanıt:** Hedef ortamda geçiş, eski veri ve kurtarma planı/sonucu. **Eksikse:** Dosya varlığını migration veya restore başarısı saymayın.

İlk kullanıcı modeli kararı ilk migration öncesinde ele alınır. Boş veritabanı kurulumunun çalışması, veri içeren mevcut kurulumun güvenli geçişini kanıtlamaz. Tasarım kabulüyle yayın kabulünü aynı kutuda birleştirmeyin.

<a id="ek-b-5"></a>

**B.5. Kod Review Kontrol Listesi**

Kod incelemesi değişikliğin amacını, davranışını ve bakım etkisini birlikte değerlendirir. Google'ın rehberi tasarım, işlev, karmaşıklık ve test gibi alanları birlikte ele alır (Google, t.y.). Buradaki liste bu yaklaşımı kitabın değişiklik ve kanıt düzenine uyarlayan özgün çalışma aracıdır.

Görev tamamlama değişikliğinde yalnız yöntem adı değil, sahiplik sorgusu, tekrar etkisi ve hata yanıtı da incelenir. Yetki koşulunu yardımcı fonksiyona taşımak davranışı koruyabilir; koşulu kaldırmak refactoring değildir. Bulgu, tetikleyici ve kullanıcı etkisiyle açıklanmalıdır.

Dayanak: [Temiz kod](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9), [SOLID](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11), [YZ ile inceleme](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-12).

- [ ] **B05-01 — Değişikliğin amacı belli mi?** **Kanıt:** Amaç, kabul ölçütü ve kaynak sürümü. **Eksikse:** Farkın neyi düzeltmesi gerektiğini açıklaştırın.

- [ ] **B05-02 — Fark incelenebilir boyutta mı?** **Kanıt:** Değişen dosyalar ve ilgisiz işlerin ayrımı. **Eksikse:** Bağımsız işleri anlamlı parçalara ayırın.

- [ ] **B05-03 — Davranış değişikliği görünür mü?** **Kanıt:** Önce/sonra örneği ve kullanıcı etkisi. **Eksikse:** Yeni davranışı “temizlik” başlığı altında gizlemeyin.

- [ ] **B05-04 — Yetki ve veri kapsamı korundu mu?** **Kanıt:** Etkin hesap, ekip izni ve kişisel görev koşulu. **Eksikse:** Yardımcı veya sorgu değişikliğinin sınırı kaldırmadığını inceleyin.

- [ ] **B05-05 — Değerlerin kaynağı doğru mu?** **Kanıt:** Sahip, müşteri ve zamanın nereden üretildiği. **Eksikse:** İstemcinin kendine sahiplik veya yetki atamasını önleyin.

- [ ] **B05-06 — Hata ve belirsiz sonuç ayrıldı mı?** **Kanıt:** Ret, kayıt hatası ve yanıt kaybı davranışı. **Eksikse:** Tek genel sonuçla belirsizliği örtmeyin.

- [ ] **B05-07 — Tekrar beklenen etkiyi koruyor mu?** **Kanıt:** Tamamlamada atama ve oluşturmada tekrar sözleşmesi. **Eksikse:** Durumu tersine çeviren veya yeni kayıt üreten yolu düzeltin.

- [ ] **B05-08 — Sorumluluk ve adlandırma anlaşılır mı?** **Kanıt:** Fonksiyon amacı, girdisi, çıktısı ve yan etkisi. **Eksikse:** Yalnız satır sayısına göre bölmeden anlamı iyileştirin.

- [ ] **B05-09 — Soyutlama ve paket gerekçeli mi?** **Kanıt:** Desen veya paketin karşıladığı değişim ihtiyacı. **Eksikse:** Kullanılmayan katman ve yetenekleri çıkarın.

- [ ] **B05-10 — Test beklentisi bağımsız kuruldu mu?** **Kanıt:** Gereksinime dayalı sonuç ve karşı örnek. **Eksikse:** Hatalı kodun çıktısını doğru beklenti diye kopyalamayın.

- [ ] **B05-11 — Kontrol sonucu kaynakla eşleşiyor mu?** **Kanıt:** Komut, ortam, sürüm, çıkış ve sonuç özeti. **Eksikse:** Eski sürümün başarısını yeni farkın kanıtı yapmayın.

- [ ] **B05-12 — Bulgu kapanışı izlenebilir mi?** **Kanıt:** Tetikleyici, etki, düzeltme ve sonraki kontrol. **Eksikse:** Öneri yazıldığında kusuru giderilmiş saymayın.

Önemli bulguları, açık soruları ve kontrol kapsamını birlikte kaydedin. YZ'nin kendi kodunu onaylaması bağımsız ürün doğrulaması değildir; her YZ itirazı da gerçek kusur sayılmaz.

<a id="ek-b-10"></a>

**B.10. AI Çıktısı Doğrulama Kontrol Listesi**

YZ çıktısı kod, plan, test, belge veya açıklama olabilir. Doğrulama biçimi çıktı türüne göre değişir; metnin akıcılığı hiçbir tür için tek başına doğruluk ölçütü değildir. NIST AI RMF, kullanım bağlamı, değerlendirme ve sorumluluğun birlikte ele alınmasını destekler (Tabassi, 2023). Buradaki maddeler kitabın insan–YZ çalışma düzeni için uyarlanmıştır.

AI-CRM örneğinde “testler geçti” diyen yanıtın hangi komutu, hangi sürümde çalıştırdığı aranır. Komut önerilmiş ancak yürütülmemişse sonuç plan düzeyindedir. İkinci modelin aynı görüşe katılması bağımsız ürün kanıtı sayılmaz. Kontrolün amacı her yanıtı reddetmek değil, iddiayı uygun kanıtla eşleştirmektir.

Dayanak: [YZ ile çalışma yöntemi](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5), [YT-25-01](../../assets/examples/book-2-chapter-12-ai-team/README.md), [GÖ-26-01](../../assets/examples/book-2-chapter-13-future/README.md).

- [ ] **B10-01 — Çıktı verilen göreve cevap veriyor mu?** **Kanıt:** Amaç, kapsam ve beklenen çıktı ile eşleştirme. **Eksikse:** İlgisiz genişlemeyi çıkarıp eksik görevi görünür kılın.

- [ ] **B10-02 — Kaynak ve sürüm gerçekten incelendi mi?** **Kanıt:** Kullanılan dosya, belge, tarih ve sürüm bilgisi. **Eksikse:** Görülmeyen kod hakkında kesin kusur veya başarı iddiası kurmayın.

- [ ] **B10-03 — Varsayım ile karar ayrıldı mı?** **Kanıt:** Onaylanmış kural, öneri ve açık soru listesi. **Eksikse:** Modelin tahminini ürün kararı olarak kaydetmeyin.

- [ ] **B10-04 — Kaynak atıfları iddiayı destekliyor mu?** **Kanıt:** Ulaşılabilir birincil kaynak ve ilgili kapsam. **Eksikse:** Başlığı uygun görünen kaynağı içerik kontrolü olmadan kullanmayın.

- [ ] **B10-05 — Üretilen kod sözleşmeyi koruyor mu?** **Kanıt:** Veri, yetki, hata ve tekrar davranışının incelemesi. **Eksikse:** Daha kısa veya akıcı çözümü doğru davranış yerine koymayın.

- [ ] **B10-06 — Örnek ile gerçek sonuç ayrıldı mı?** **Kanıt:** Sentetik veri, beklenen çıktı ve gerçek yürütme etiketleri. **Eksikse:** Hazırlanmış örneği ölçülmüş başarı diye sunmayın.

- [ ] **B10-07 — “Çalıştı” iddiasının kanıtı var mı?** **Kanıt:** Komut, ortam, sürüm, gerçek çıktı ve kontrol kapsamı. **Eksikse:** Kanıt yoksa iddiayı doğrulanmadı olarak düzeltin.

- [ ] **B10-08 — Bağımsız karşı örnek düşünüldü mü?** **Kanıt:** Gereksinimden türetilmiş ret, sınır veya hata senaryosu. **Eksikse:** Yalnız modelin kendi örneklerini tekrar ederek güven oluşturmayın.

- [ ] **B10-09 — Veri paylaşımı ve araç yetkisi uygun mu?** **Kanıt:** Gerekli bağlam, hassas veri ayrımı ve izinli eylem. **Eksikse:** Dış içerikteki talimatı yeni yetki saymayın.

- [ ] **B10-10 — Eksik ve çelişkiler açıkça raporlandı mı?** **Kanıt:** Yapılmayan kontroller, engeller ve uyuşmazlıklar. **Eksikse:** Tamamlanmamış işi “bitti” ifadesiyle örtmeyin.

- [ ] **B10-11 — Devir kaydı yeniden izlenebilir mi?** **Kanıt:** Son kaynak durumu, değişiklik, kanıt ve sonraki açık iş. **Eksikse:** Başka araç veya kişiye bağlamı belirsiz sonuç devretmeyin.

- [ ] **B10-12 — Kabul kararı uygun sorumluya bağlı mı?** **Kanıt:** İddia–kanıt değerlendirmesi ve ilgili karar kaydı. **Eksikse:** Modelin öz değerlendirmesini tek başına kabul veya yayın kararı saymayın.

Sonuç raporu neyin doğrulandığını, neyin yalnız önerildiğini ve neyin açık kaldığını ayrı belirtir. Aynı talimatın farklı model veya bağlamla kullanılması farklı sonuç doğurabilir; eski değerlendirme yeni çıktının otomatik kabulü değildir.

<a id="ek-b-kayit"></a>

**İnceleme kaydı şablonu**

Her çalışma için bu şablondan ayrı bir kayıt oluşturulabilir. Aşağıdaki alanlar örnek doldurma yönergeleridir; gerçek sonuç değildir. Bir kontrol başka bir kayıttaki kanıta dayanıyorsa bağlantıyı ve o kanıtın hangi sürüme ait olduğunu belirtin. Sırları veya gereksiz kişisel veriyi kanıt dosyasına taşımayın.

| Alan | Doldurulacak bilgi |
|---|---|
| İş ve kapsam | İncelenen özellik, değişiklik veya yayın adayı |
| Kontrol kimliği | İlgili B01-01…B10-12 maddesi |
| Dayanak | Gereksinim, sözleşme veya karar kaydı |
| Kaynak durumu | Commit varsa kimliği; yoksa dosya/sürüm durumu ve yerel değişiklikler |
| Ortam | Belge incelemesi, laboratuvar, test, staging veya production |
| İddia ve beklenti | Neyin doğrulanacağı ve hangi sonucun beklendiği |
| Kanıt türü | Belge incelemesi, statik inceleme, test yürütmesi veya operasyon sonucu |
| Yöntem ve kanıt yeri | İncelenen dosya veya gerçekten yürütülen kontrol; ilgili kayıt bağlantısı |
| Gözlenen sonuç | Gerçek sonuç; henüz yoksa boş olduğu açıkça belirtilir |
| Durum ve gerekçe | Beş durumdan biri; kapsam dışı ise uygulanmama nedeni |
| Açık iş ve bağımlılık | Düzeltilecek nokta, bekleyen karar ve etkilenen sonraki iş |
| Sorumlu ve tarih | İnceleyen kişi/rol, inceleme tarihi ve gerekiyorsa karar sahibi |

Çalışma sonunda “120 maddenin 110'u geçti” gibi tek sayıya indirgemek yerine sonucu kapsamıyla anlatın. Hangi maddeler belge düzeyinde doğrulandı, hangi testler yürütüldü, hangileri engelli ve hangi açık konu kabulü etkiliyor? Bu ayrım, çok sayıda düşük etkili kontrolün bir kritik kusuru görünmez kılmasını önler.

<a id="ek-b-ornek"></a>

**Öğretim örneği Bir gereksinim önerisini incelemek**

YZ’nin “müşteriye not ekleme gereksinimi tamamlandı” dediğini, ancak taslağın boş notu kabul ettiğini ve not yazarını belirtmediğini varsayalım. Bu, yazılmış bir öğretim örneğidir; gerçek model görüşmesi veya ürün testi değildir.

| Kontrol | Değerlendirme | İzlenecek iş |
|---|---|---|
| B02-04 — Kabul ölçütleri | Taslak KM-01 ve KM-02 ile karşılaştırılır; notun kaydı ve boş notun reddi görünür olmalıdır. | IK-03 ve IK-04’ün kabul ölçütlerindeki karşılığını göstermek |
| B10-07 — Çalıştı iddiası | Belgenin hazır olması uygulamanın çalıştığını göstermez. | Sonucu “gereksinim taslağı düzeltildi; ürün davranışı henüz sınanmadı” olarak yazmak |

Gereksinimin belge üzerinde uygun bulunması ile gerçek uygulamada doğrulanması farklı aşamalardır. Tasarım kaydı tamamlandığında ilgili karar ve açık işler ikinci kitaptaki geliştirme çalışmasına devredilir.


<a id="ek-b-kaynakca"></a>

**Kaynakça**

Bu ekin listeleri, ilgili bölüm kararlarıyla ilişkilendirilmiş özgün çalışma sorularıdır. Aşağıdaki kaynaklar genel güvenli geliştirme, inceleme, kısıtlar, yetki, yayın ve YZ değerlendirme ilkelerini destekler; AI-CRM'in özel ürün kurallarının kaynağı değildir. Altı birincil kaynak 5 Ekim 2026 tarihinde kontrol edilmiş, ortak bibliyografyadaki mevcut kayıtlar yeniden kullanılmıştır.

Django Software Foundation. (t.y.). [*Deployment checklist*](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/). Django 5.2 documentation.

Google. (t.y.). [*What to look for in a code review*](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Google Engineering Practices.

OWASP Foundation. (t.y.). [*Authorization cheat sheet*](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). OWASP Cheat Sheet Series.

PostgreSQL Global Development Group. (t.y.). [*Constraints*](https://www.postgresql.org/docs/18/ddl-constraints.html). PostgreSQL 18 documentation.

Souppaya, M., Scarfone, K., & Dodson, D. (2022). [*Secure software development framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities*](https://csrc.nist.gov/pubs/sp/800/218/final) (NIST SP 800-218). National Institute of Standards and Technology.

Tabassi, E. (2023). [*Artificial intelligence risk management framework (AI RMF 1.0)*](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) (NIST AI 100-1). National Institute of Standards and Technology.
