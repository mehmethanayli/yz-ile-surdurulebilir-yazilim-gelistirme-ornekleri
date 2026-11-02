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

**Bu kitaptaki seçim:** 6 liste, 72 kontrol maddesi. Liste ve madde numaraları seri boyunca korunur; atlayan numaralar bu kitaba alınmayan listelerdir. B05–B10 kod inceleme, güvenlik, test, yayın, işletim ve YZ çıktısını kapsar. Gereksinim veya tasarım yeniden açılırsa Kitap 1’deki B01–B04 listelerine dönülür.

**İçindekiler**

- [B.5. Kod Review Kontrol Listesi](#ek-b-5)
- [B.6. Güvenlik Kontrol Listesi](#ek-b-6)
- [B.7. Test Kontrol Listesi](#ek-b-7)
- [B.8. Deployment Kontrol Listesi](#ek-b-8)
- [B.9. Production Kontrol Listesi](#ek-b-9)
- [B.10. AI Çıktısı Doğrulama Kontrol Listesi](#ek-b-10)
- [İnceleme kaydı şablonu](#ek-b-kayit)
- [Öğretim örneği: bir sonuç iddiasını incelemek](#ek-b-ornek)
- [Kaynakça](#ek-b-kaynakca)

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

<a id="ek-b-6"></a>

**B.6. Güvenlik Kontrol Listesi**

Güvenlik kontrolü, “güvenli görünüyor” yargısından somut aktör, kaynak ve eylem koşullarına geçmelidir. OWASP yetkilendirme rehberi kimlikle erişim iznini ayırır; en az yetki ve her istekte denetim ihtiyacını vurgular (OWASP Foundation, t.y.). Liste bir uygunluk sertifikası veya bütün tehditleri kapsayan denetim değildir; değişikliğin etkisine göre daha ayrıntılı inceleme gerekebilir.

AI-CRM örneğinde A ve B etkin ekip üyeleri, S yalnız hesap yöneticisi, D ise devre dışı hesaptır. A'nın kişisel görevine B'nin erişimi reddedilir. Hem ekip hem yönetici rolü taşıyan aktör de başkasının kişisel görevini açamaz. Kontrol bu davranışları arayüzden bağımsız, korumalı sunucu yollarında araştırır.

Dayanak: [Güvenlik](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6), [Veri ve paylaşım incelemesi](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-7), [Kabul senaryoları](../../assets/examples/chapter23-integration/acceptance-cases.json).

- [ ] **B06-01 — Varlık, aktör ve güven sınırı belirli mi?** **Kanıt:** Korunan veri, giriş yolları ve olası kötüye kullanım örnekleri. **Eksikse:** Yalnız genel güvenlik etiketiyle yetinmeyin.

- [ ] **B06-02 — Kimlik doğrulaması doğru kaynağa bağlı mı?** **Kanıt:** Oturumun doğrulanması ve hesapla ilişkisinin incelenmesi. **Eksikse:** İstemcinin gönderdiği kullanıcı kimliğine güvenmeyin.

- [ ] **B06-03 — Devre dışı hesabın eski oturumu reddediliyor mu?** **Kanıt:** D için sonraki korumalı isteğin yanıtı ve veri etkisi. **Eksikse:** Oturum varlığını güncel hesap etkinliği yerine koymayın.

- [ ] **B06-04 — Rol ile kaynak sahipliği birlikte korunuyor mu?** **Kanıt:** A/B/S ve birleşik rol için okuma/tamamlama sonuçları. **Eksikse:** Yöneticiliğin kendiliğinden iş verisi veya başkasının görevi yetkisi vermesini düzeltin.

- [ ] **B06-05 — Reddedilen istek veri açığa çıkarıyor mu?** **Kanıt:** Durum kodunun yanında yanıt içeriği ve kayıt etkisi. **Eksikse:** Doğru hata kodunu tek başına güvenli ret saymayın.

- [ ] **B06-06 — CSRF koruması uygun yollarda sınanıyor mu?** **Kanıt:** Oturumlu durum değiştirme isteklerinin koruma ve ret örnekleri. **Eksikse:** CSRF kontrolünü kaynak yetkisinin yerine kullanmayın.

- [ ] **B06-07 — Girdi doğrulama ve sorgu kullanımı güvenli mi?** **Kanıt:** Tür, biçim, alan izinleri ve parametreli veri erişimi. **Eksikse:** Kullanıcı girdisini komut veya sorgu metnine birleştiren yolları giderin.

- [ ] **B06-08 — Çıktı bağlamına uygun kodlanıyor mu?** **Kanıt:** Notun HTML veya başka bağlamda gösterilme yöntemi. **Eksikse:** Tek genel temizlik işlevini bütün çıktı bağlamlarının koruması saymayın.

- [ ] **B06-09 — Parola ve sırlar uygun yöntemle korunuyor mu?** **Kanıt:** Çatının parola mekanizması, sır kaynağı ve erişim kapsamı. **Eksikse:** Düz metin saklama veya sırların depoya/loga taşınmasını giderin.

- [ ] **B06-10 — Bağımlılık ve yapılandırma riski incelendi mi?** **Kanıt:** Kullanılan sürümler, ilgili bulgular ve ortam ayarları. **Eksikse:** Tarama çıktısını bağlamsız başarı rozeti olarak sunmayın.

- [ ] **B06-11 — Hata ve günlükler gereksiz veri taşıyor mu?** **Kanıt:** Maskeleme, erişim ve örnek hata yanıtı. **Eksikse:** Parola, oturum değeri ve gereksiz müşteri içeriğini çıkarın.

- [ ] **B06-12 — Ek yeteneklerin kapsamı açık mı?** **Kanıt:** Dosya yükleme, dış servis veya çok kiracılık varsa ilgili kontroller. **Eksikse:** İlk MVP'de bulunmayan yeteneği zorunlu uygulama işi yapmayın; ileride eklendiğinde yeniden inceleyin.

Güvenlik bulgusu varsa etkilediği kullanım sınırını ve düzeltme doğrulamasını kaydedin. Bir kontrolün çalıştırılamaması, saldırı olmadığının veya uygulamanın güvenli olduğunun kanıtı değildir.

<a id="ek-b-7"></a>

**B.7. Test Kontrol Listesi**

Test incelemesi, test dosyasının bulunmasından beklenen davranışın doğru kurulmasına kadar uzanır. Gereksinim yanlışsa ona uyan test yanıltıcı güven verebilir. Test düzeyi, kullanılan gerçek ve yerine geçen bileşenler, ortam ve sonuç birlikte açıklanmalıdır. Sayı ve kapsam yüzdesi tek başına yeterli kabul gerekçesi değildir.

AI-CRM için not kabul ölçütleriyle bütün ürün kapsamı ayrılır. Bölüm 10'teki senaryolar hazırlanmış planlardır; dosyalarının mevcut olması gerçek Django ve PostgreSQL üzerinde koştukları anlamına gelmez. Yerel öğretim laboratuvarının sonucu yalnız kendi sınırları içinde aktarılır.

Dayanak: [Test stratejisi](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5), [Uygulama kabul planı](../../assets/examples/chapter23-integration/acceptance-cases.json), [Hata ayıklama](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-4).

- [ ] **B07-01 — Beklenti gereksinimden türetildi mi?** **Kanıt:** Gereksinim, girdi ve beklenen sonuç bağı. **Eksikse:** Mevcut çıktıyı sorgulamadan doğru sonuç kabul etmeyin.

- [ ] **B07-02 — Test kapsamı işlevleri izliyor mu?** **Kanıt:** FG-01–FG-05, KM-01–KM-05 ve ortak kontrol eşleştirmesi. **Eksikse:** Yalnız not akışıyla tüm ürünü doğruladığınızı söylemeyin.

- [ ] **B07-03 — Düzey ve ortam açık mı?** **Kanıt:** Birim, bütünleşme veya uçtan uca kapsam; kullanılan servisler. **Eksikse:** Test adından gerçek bileşen kapsamı çıkarmayın.

- [ ] **B07-04 — Mutlu yolun yanında ret yolları var mı?** **Kanıt:** Boş not, geçersiz veri, yetkisiz aktör ve bulunamayan kaynak örnekleri. **Eksikse:** Yalnız başarı yanıtını sınayan kapsamı tamamlayın.

- [ ] **B07-05 — Kişisel görev yetkisi bağımsız sınanıyor mu?** **Kanıt:** A'nın görevi için B, S, D ve birleşik rol koşullarının gerçek yanıt ve kayıt etkileri. **Eksikse:** Ortak müşteri erişimini görev yetkisi sanan beklentiyi düzeltin.

- [ ] **B07-06 — Kayıp yanıt ve tekrar incelendi mi?** **Kanıt:** Aynı eylem, değişen içerik, eşzamanlı tekrar ve belirsiz sonuç senaryolarının planı; davranış iddiası için gerçek sonuçları. **Eksikse:** Sırayla yapılan tek örneği yarış testi diye raporlamayın.

- [ ] **B07-07 — Tarih ve arama sınırları seçilmiş kurala bağlı mı?** **Kanıt:** Bugün/dün hedefi, açık/tamamlanmış görev ve arama beklentisi. **Eksikse:** Açık karar için test içinde rastgele ürün kuralı üretmeyin.

- [ ] **B07-08 — Test verisi temsil edici ve ayrılmış mı?** **Kanıt:** Aynı adlı iki müşteri, farklı sahipler ve sentetik kayıtlar. **Eksikse:** Gerçek veriyi gerekçesiz kopyalamayın; örnek ilişkilerini düzeltin.

- [ ] **B07-09 — Test doubles'ın sınırı biliniyor mu?** **Kanıt:** Hangi saat, ağ veya veri bileşeninin yerine geçildiği. **Eksikse:** Sahte bileşen sonucunu gerçek entegrasyon başarısı saymayın.

- [ ] **B07-10 — Kontrol gerçekten yürütüldü mü?** **Kanıt:** Komut, sürüm, ortam, çıkış kodu ve anlamlı sonuç. **Eksikse:** Planı veya dosya varlığını başarılı çalışma diye işaretlemeyin.

- [ ] **B07-11 — Atlanan ve kararsız testler görünür mü?** **Kanıt:** Skip, ortam engeli, aralıklı hata ve yeniden deneme kaydı. **Eksikse:** Başarı sayısından düşen kontrolleri raporda gizlemeyin.

- [ ] **B07-12 — Düzeltme sonrası ilgili regresyon kontrol edildi mi?** **Kanıt:** İlk kusurun yeniden üretimi ve etkilenen yakın davranışlar. **Eksikse:** Kodu değiştirmekle incelemeyi kapatmayın; ilgisiz testleri tekrarlayarak kanıtı şişirmeyin.

Bir kontrol çalışıp beklenen davranışı bulmadıysa “uygunsuz”, ortam nedeniyle çalışmadıysa “çalıştırılamadı” yazılır. İkinci durumda ürünün doğru veya yanlış olduğu sonucuna atlanmaz. Yapılmış incelemenin kapsamı kadar yapılmamış işler de görünür olmalıdır.

<a id="ek-b-8"></a>

**B.8. Deployment Kontrol Listesi**

Yayın incelemesi belirli aday, hedef ortam ve veri durumuna bağlanır. Aynı commit için bile yapılandırma ve migration değişikliği sonucu etkileyebilir. Sürekli teslim ile sürekli dağıtımın hangi anlamda kullanıldığı ve production'a geçiş kararının nasıl verildiği açık tutulur.

Django'nun deployment listesi production ayarları, HTTPS, sırlar ve ortam farklarını kontrol etmeyi; dağıtım kontrollerini ilgili ayarlara karşı yürütmeyi açıklar (Django Software Foundation, t.y.). Kitaptaki hedef teknoloji tercihiyle gerçek ortam doğrulaması ayrıdır. Bu bölüm bir komut çalıştırmaz ve mevcut yayın onayı üretmez; gerçek yayın için YK-21-01'in somutlaştırılması gerekir.

Dayanak: [Deployment ve CI/CD](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8), [YK-21-01](../../assets/examples/chapter21-release/README.md), [Ortam kararı](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

- [ ] **B08-01 — Yayın adayı açıkça tanımlı mı?** **Kanıt:** Kaynak sürümü, build çıktısı ve artifact kimliği. **Eksikse:** Hangi çıktının yayına gideceği belirsizken işlemi başlatmayın.

- [ ] **B08-02 — Hedef ortam ve yetki kapsamı kesin mi?** **Kanıt:** Hedef adres, hesap, proje, ortam ve izinli eylemler. **Eksikse:** Yerel veya staging bilgisini production hedefi yerine kullanmayın.

- [ ] **B08-03 — Build ve gerekli kontroller aynı adaya ait mi?** **Kanıt:** Kaynak–artifact bağı ve ilgili test/inceleme sonuçları. **Eksikse:** Başka sürümün yeşil sonucunu adayın kanıtı saymayın.

- [ ] **B08-04 — CI/CD adımları ve karar noktası açık mı?** **Kanıt:** Build, test, artifact, dağıtım, kontrol ve başarısızlık yolları. **Eksikse:** Teslim ile otomatik canlıya geçişi aynı terimle belirsiz bırakmayın.

- [ ] **B08-05 — Production yapılandırması incelendi mi?** **Kanıt:** Debug kapalı, izinli hostlar, sırlar ve sunucu çalıştırma düzeni. **Eksikse:** Geliştirme ayarlarını doğrudan canlıya taşımayın.

- [ ] **B08-06 — DNS kayıtları amaçlarına uygun mu?** **Kanıt:** Gereken A/AAAA veya CNAME, yetkili DNS ve TTL bilgisi; varsa diğer kayıtlar. **Eksikse:** MX'i web yönlendirmesi, CNAME'i HTTP redirect sanmayın; gerekmeyen kayıt eklemeyin.

- [ ] **B08-07 — TLS ve uygulama yolu birlikte çalışıyor mu?** **Kanıt:** Ad–sertifika uyumu, HTTPS erişimi ve ilgili HTTP akışının sonucu. **Eksikse:** DNS çözümünü tek başına güvenli uygulama erişimi saymayın.

- [ ] **B08-08 — Migration geçişi adaya uygun mu?** **Kanıt:** Mevcut veri, eski/yeni kod uyumu ve geçiş kontrolü. **Eksikse:** Yalnız boş kurulum denemesini mevcut veri geçişi kanıtı saymayın.

- [ ] **B08-09 — Yedek ve geri yükleme hazırlığı gerçek mi?** **Kanıt:** Gerekli kapsam, okunabilir kopya ve ilgili restore prova sonucu. **Eksikse:** Yedek dosyasını kurtarma başarısı saymayın.

- [ ] **B08-10 — Geri dönüş koşulu ve sınırı belli mi?** **Kanıt:** Tetikleyici, sorumlu, kod/veri uyumu ve uygulanabilir işlem sırası. **Eksikse:** Her veri değişimini rollback ile tersine çevrilebilir varsaymayın.

- [ ] **B08-11 — Yayın sonrası kullanıcı yolu kontrolü hazır mı?** **Kanıt:** Oturum, müşteri, not ve kişisel görev için adayla ilişkili kontrol planı. **Eksikse:** Yalnız süreç sağlık yanıtını ürün kabulü saymayın.

- [ ] **B08-12 — Yayın kararı ve açık işler kayıtlı mı?** **Kanıt:** Gereken kanıtlar, riskler, karar sahibi ve karar zamanı. **Eksikse:** Liste işaretlerini kendiliğinden yayın yetkisi olarak yorumlamayın.

Başarısızlıkta hangi işlemin duracağı ve hangi kanıtın korunacağı yayın planında bulunur. DNS değişikliği, gerçek migration veya restore burada öneri metni olarak kalır; uygulanmış sonuç alanları ancak gerçek çalışma sonrasında doldurulur.

<a id="ek-b-9"></a>

**B.9. Production Kontrol Listesi**

Production kontrolü tek seferlik yayın kapanışı değildir. Hizmetin gerçek kullanıcı yolları, ölçüm koşulları, bakım ve olay müdahalesi birlikte izlenir. Ne sıklıkta inceleme yapılacağı hizmet ihtiyacına göre belirlenir; bu ekte tüm projelere aynı saat veya kota atanmaz.

AI-CRM'de müşteriyi okumak başarılıyken not yazma yolu bozulabilir. Tek sağlık adresinin yanıt vermesi bütün işlevleri kapsamaz. Hata oranı için payda, zaman aralığı ve hangi retlerin beklenen davranış olduğu bilinmelidir. Bir modelin günlükleri özetlemesi de gerçek olay müdahalesi yapıldığı anlamına gelmez.

Dayanak: [Production sonrası bakım](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9), [İB-22-01](../../assets/examples/chapter22-operations/README.md), [SaaS işletimi](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

- [ ] **B09-01 — İzlenen kullanıcı yolları belirli mi?** **Kanıt:** Okuma, kayıt ve görev işlemleri için anlamlı hizmet kontrolleri. **Eksikse:** Tek sağlık adresinden tüm ürünün durumunu çıkarmayın.

- [ ] **B09-02 — Metrik tanımı açık mı?** **Kanıt:** Birim, payda, zaman aralığı, başarılı sonuç ve ölçüm noktası. **Eksikse:** İstek temelli oranla kesinti süresini doğrudan eşitlemeyin.

- [ ] **B09-03 — Uyarı eyleme bağlanıyor mu?** **Kanıt:** Koşul, sorumlu ve ilk inceleme adımı. **Eksikse:** Sahipsiz uyarı veya sürekli gürültüyü izleme başarısı saymayın.

- [ ] **B09-04 — Günlükler teşhise yeterli ve sınırlı mı?** **Kanıt:** İlişkilendirme bilgisi, erişim ve veri minimizasyonu. **Eksikse:** Hassas içerik toplayarak teşhis açığını kapatmayın.

- [ ] **B09-05 — Güncel yedeklerin kapsamı doğrulanıyor mu?** **Kanıt:** Veri kapsamı, saklama ve son başarılı yedek kaydı. **Eksikse:** Eksik bileşeni veya başarısız işi görünür kılın.

- [ ] **B09-06 — Restore sonucu kullanılabilirliği gösteriyor mu?** **Kanıt:** Ayrılmış ortamda geri yükleme ve işlev/bütünlük kontrolü. **Eksikse:** Yalnız dosya açılmasını tam kurtarma saymayın.

- [ ] **B09-07 — Olay müdahalesi yürütülebilir mi?** **Kanıt:** Etkiyi sınırlama, iletişim, kurtarma ve kayıt sorumluları. **Eksikse:** Genel “yeniden başlat” önerisi yerine olaya uygun yol belirleyin.

- [ ] **B09-08 — Hesap ve yetki değişimleri etkili mi?** **Kanıt:** Devre dışı hesap, rol değişimi ve kişisel erişim kontrolleri. **Eksikse:** Eski oturum veya önbelleğin erişim sınırını aşmasını araştırın.

- [ ] **B09-09 — Güncellemeler etkisiyle ele alınıyor mu?** **Kanıt:** Bağımlılık, güvenlik ve veri geçişi için aday ve kontrol kaydı. **Eksikse:** Bütün paketleri tek seferde körlemesine yükseltmeyin.

- [ ] **B09-10 — Performans sorunu ölçülmüş mü?** **Kanıt:** Yük, gecikme dağılımı, sorgu ve kaynak kullanımı. **Eksikse:** Ölçülmemiş darboğaza sunucu eklemeyi kesin çözüm saymayın.

- [ ] **B09-11 — Maliyet ve kapasite varsayımları güncel mi?** **Kanıt:** Kullanım, kapasite ve seçilmiş bütçe/uyarı sınırları. **Eksikse:** Sınır bilinmiyorsa açık karar olarak kaydedin.

- [ ] **B09-12 — Olay ve kullanıcı geri bildirimi geliştirmeye dönüyor mu?** **Kanıt:** Önceliklendirilmiş bulgu, düzeltme ve sonraki doğrulama. **Eksikse:** Olay kapanışını yalnız semptomun geçici kaybolmasına bağlamayın.

Bu liste sürekli izleme aracı veya otomasyon kurmaz. İnceleme kaydının zamanı ve hizmet sürümü belirtilmelidir. Geçmiş bir iyi sonuç, sonraki değişikliklerin veya bütün gelecek dönemlerin güvencesi değildir.

<a id="ek-b-10"></a>

**B.10. AI Çıktısı Doğrulama Kontrol Listesi**

YZ çıktısı kod, plan, test, belge veya açıklama olabilir. Doğrulama biçimi çıktı türüne göre değişir; metnin akıcılığı hiçbir tür için tek başına doğruluk ölçütü değildir. NIST AI RMF, kullanım bağlamı, değerlendirme ve sorumluluğun birlikte ele alınmasını destekler (Tabassi, 2023). Buradaki maddeler kitabın insan–YZ çalışma düzeni için uyarlanmıştır.

AI-CRM örneğinde “testler geçti” diyen yanıtın hangi komutu, hangi sürümde çalıştırdığı aranır. Komut önerilmiş ancak yürütülmemişse sonuç plan düzeyindedir. İkinci modelin aynı görüşe katılması bağımsız ürün kanıtı sayılmaz. Kontrolün amacı her yanıtı reddetmek değil, iddiayı uygun kanıtla eşleştirmektir.

Dayanak: [YZ ile çalışma yöntemi](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5), [YT-25-01](../../assets/examples/chapter25-ai-team/README.md), [GÖ-26-01](../../assets/examples/chapter26-future/README.md).

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

**Öğretim örneği: bir sonuç iddiasını incelemek**

Aşağıdaki durum tamamen yazılmış bir öğretim örneğidir; gerçek model görüşmesi veya test yürütmesi değildir. Örnek yanıtta “Görev yetkisi düzeltildi, bütün testler geçti” denildiğini, fakat yalnız önerilmiş kod ve bir test komutunun bulunduğunu varsayalım. Kod uygulanmamış ve komut çalıştırılmamıştır.

| Kontrol | Örnekteki değerlendirme | İzlenecek iş |
|---|---|---|
| B10-07 — Çalıştı iddiası | İddia kanıtla desteklenmediği için çıktı incelemesi **Uygunsuz**. | Yanıtı “değişiklik ve test önerisi hazır; yürütülmedi” olarak düzeltmek |
| B07-05 — Görev yetkisi | Ürün davranışı kontrolü **Bekliyor**; gerçek sonuç yok. | Uygulama ve ortam hazır olduğunda aktör senaryolarını çalıştırmak |
| B07-10 — Gerçek yürütme | Yalnız komut önerisi var; kontrol **Bekliyor**. | Komutun ilgili ortamda gerçek sonucunu kaydetmek |

Burada raporun kanıtsız olması, ürün testinin çalışıp başarısız olduğu anlamına gelmez. Daha sonra kontrol başlatılır ancak veritabanına erişilemezse ilgili çalışma **Çalıştırılamadı** olur. Test çalışır ve B kullanıcısına A'nın görevi açılırsa ürün davranışı **Uygunsuz** olur. Test geçerse ancak o sürüm, ortam ve senaryo kapsamı için **Doğrulandı** yazılır. Tek görev testi bütün uygulama kabulünü veya yayın hazırlığını kapatmaz.

Bu kayıt, yalnız raporun dilini düzeltmekle yetinmez: iddianın hangi kısmının belgesel olarak incelenebildiğini ve hangi kısmının gerçek yürütme beklediğini ayırır. YZ'ye verilecek sonraki görev de bu ayrımdan türetilir; örneğin önce ilgili dosyayı uygulamak ve gerekli test koşullarını hazırlamak. Kapsam dışı yayın veya dış sistem eylemi kendiliğinden bu göreve eklenmez.

<a id="ek-b-kaynakca"></a>

**Kaynakça**

Bu ekin listeleri, ilgili bölüm kararlarıyla ilişkilendirilmiş özgün çalışma sorularıdır. Aşağıdaki kaynaklar genel güvenli geliştirme, inceleme, kısıtlar, yetki, yayın ve YZ değerlendirme ilkelerini destekler; AI-CRM'in özel ürün kurallarının kaynağı değildir. Altı birincil kaynak 5 Ekim 2026 tarihinde kontrol edilmiş, ortak bibliyografyadaki mevcut kayıtlar yeniden kullanılmıştır.

Django Software Foundation. (t.y.). [*Deployment checklist*](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/). Django 5.2 documentation.

Google. (t.y.). [*What to look for in a code review*](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Google Engineering Practices.

OWASP Foundation. (t.y.). [*Authorization cheat sheet*](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). OWASP Cheat Sheet Series.

PostgreSQL Global Development Group. (t.y.). [*Constraints*](https://www.postgresql.org/docs/18/ddl-constraints.html). PostgreSQL 18 documentation.

Souppaya, M., Scarfone, K., & Dodson, D. (2022). [*Secure software development framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities*](https://csrc.nist.gov/pubs/sp/800/218/final) (NIST SP 800-218). National Institute of Standards and Technology.

Tabassi, E. (2023). [*Artificial intelligence risk management framework (AI RMF 1.0)*](https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10) (NIST AI 100-1). National Institute of Standards and Technology.
