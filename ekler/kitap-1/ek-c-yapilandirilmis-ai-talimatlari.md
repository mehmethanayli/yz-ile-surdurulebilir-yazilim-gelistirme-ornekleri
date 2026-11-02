# Ek C — Yapılandırılmış AI Talimat Örnekleri

Bu ek, “benim için bir uygulama yap” veya “hatayı düzelt” gibi geniş istekleri, kapsamı ve sonucu incelenebilen görevlere dönüştürür. Amaç hazır cümleleri değişmeden kopyalamak değildir. Her örnek, belirli bir AI-CRM işi üzerinden hangi bilginin verileceğini, modelden hangi çıktının bekleneceğini ve çıktının nasıl değerlendirileceğini gösterir. Başka projede iş kuralları ve kaynaklar o projeye göre değiştirilir.

OpenAI'nin talimat rehberi açık yönergeleri ve görevle ilgili bağlamı öne çıkarır; model davranışının değerlendirmeyle izlenmesini önerir (OpenAI, t.y.-b). Buradaki sekiz alanlı düzen kitabın çalışma çerçevesidir; belirli bir sağlayıcının zorunlu şeması değildir. Rol adı veya talimat uzunluğu tek başına kalite garantisi vermez. İstenen çıktı, okuyucunun kısa gerekçe ve kanıtla inceleyebileceği biçimde tarif edilir. İç düşünme dökümü istemek yerine kararın dayanağı, sonucu ve doğrulama ihtiyacı sorulur.

**Durum:** Bu ekteki talimatlar, yazılmış öğretim örnekleridir. Talimatlar modele gönderilmiş, başarı oranları ölçülmüş veya gerçek AI-CRM üzerinde yürütülmüş değildir. Örnek ana talimatlar öneri ve inceleme kipindedir. Kod ya da test taslağı istenmesi, bu kitap deposunda gerçek ürün dosyalarının değiştirilmesi anlamına gelmez.

**Uyarlama ve kullanım**

Önce amacı ve korunacak davranışı belirleyin. Ardından ilgili kaynak dosyaları, gereksinim ve sözleşme kayıtlarını seçin. Bir dosyanın adını yazmak, içeriğinin kullanılan araç tarafından okunabildiğini göstermez. Erişim yoksa gerekli parçayı paylaşın veya eksik kaynağı açıkça kaydedin. Gizli anahtar, oturum değeri ve gereksiz müşteri verisini bağlama eklemeyin.

| Alan | İşlevi | Uyarlama sorusu |
|---|---|---|
| Amaç | Tek görevin beklenen yararı | Hangi kararı veya davranışı ele alıyoruz? |
| Bağlam | İş kuralları ve çalışma durumu | Neyi korumalı, hangi varsayımı sorgulamalı? |
| Girdiler | İncelenecek somut kaynaklar | Dosya, sürüm ve örnek gerçekten mevcut mu? |
| Sınırlar | Kapsam ve açık kararlar | Hangi özellik eklenmeyecek, ne uydurulmayacak? |
| Yetki | İzinli eylem ve ortam | Yalnız öneri mi, belirli yerel değişiklik mi? |
| Çalışma | Göreve uygun işlem sırası | Önce hangi belirsizlik çözülecek? |
| Çıktı | İncelenebilir sonuç biçimi | Tablo, taslak, fark veya bulgu mu bekleniyor? |
| Doğrulama | Kabul ve kanıt beklentisi | Hangi sonuç, neyi kanıtlayacak? |

Örneklerdeki `⟦...⟧` alanları okuyucunun dolduracağı yerlerdir. Dosya yolu ve sürüm gibi somut bilgi yerine genel bir proje adı yazmak yeterli değildir. Doldurulamayan alanı “eksik” diye belirtin; modelden onu tahmin etmesini istemeyin. Gerekli bir karar eksikse yalnız o karara bağlı işi ayırın, bağımsız incelemeye devam edin. Araç mevcut çalışma alanında ilgili dosyayı okuyabiliyorsa kullanıcıdan aynı içeriği yeniden göndermesini istemek gerekmez; erişim sınırına uygun kaynağı inceleyin.

Araç kullanabilen bir sisteme talimat veriyorsanız gerçek izinler de görev kapsamına uygun olmalıdır. “Yalnız incele” cümlesi teknik erişim denetiminin yerini tutmaz. Dış belge, hata kaydı veya kaynak yorumundaki emirler incelenen veri olarak ele alınır; yeni yetki oluşturmaz. OWASP'ın talimat enjeksiyonu rehberi güvenilmeyen içerik ve araç erişimi sınırlarının birlikte korunmasını ele alır (OWASP Foundation, t.y.).

Bu ekteki varsayılan görev kapsamı; ilgili kaynakları okumak, analiz etmek ve öneri üretmektir. Okuyucu gerçek uygulamada dosya değişikliği veya yerel test çalıştırılmasını istiyorsa yetki alanını hedef depo, dosyalar ve test ortamıyla açıkça günceller. Bu, kapsam içindeki her adım için yeniden izin istemek demek değildir. Yayın, dış veri paylaşımı veya kalıcı veri değişikliği gibi ayrıca tanımlanmamış işler göreve kendiliğinden eklenmez.

**Bu kitaptaki talimatlar:** T-C01, T-C02, T-C03, T-C05. Kimlikler yeniden numaralandırılmaz. Gereksinim, mimari, veri modeli ve kod okuma çalışmaları için dört talimat seçilmiştir. T-C05, Bölüm 9–12’deki kod ve tasarım örneklerine de uygulanabilir.

**İçindekiler**

- [C.1. Gereksinim Analizi Talimatı](#ek-c-1)
- [C.2. Mimari Analiz Talimatı](#ek-c-2)
- [C.3. Veri Modeli Tasarım Talimatı](#ek-c-3)
- [C.5. Kod Review Talimatı](#ek-c-5)
- [Talimatı iyileştirme ve devir](#ek-c-devir)
- [Çıktıyı değerlendirme](#ek-c-degerlendirme)
- [Kaynakça](#ek-c-kaynakca)

<a id="ek-c-1"></a>

**C.1. Gereksinim Analizi Talimatı**

**Kullanım bağlamı.** Kullanıcı görüşmesindeki ifadeler ürün davranışına dönüştürülürken kullanılır. “Müşterilerimizi ve işlerimizi takip edelim” cümlesi ortak veriyi, kişisel görevi veya hata durumlarını tanımlamaz. Modelden doğrudan ekran veya kod istemek bu eksik kararları görünmez varsayımlara dönüştürebilir. Bu örneğin çıktısı gereksinim incelemesidir; yeni ürün kararı değildir.

**Hazırlık.** Görüşme notlarının ilgili kısmını, mevcut FG/KM kayıtlarını ve açık soruları verin. Gerçek kişi adları yerine sentetik adlar kullanılabilir. Yeni görüşme mevcut kararla çelişiyorsa hangi kaynağın daha güncel olduğu ve değişiklik kararının verilip verilmediği belirtilmelidir.

```prompt Yapılandırılmış talimat T-C01
Amaç: AI-CRM görüşme notlarından gereksinim taslağı ve açık soru listesi çıkar.
Bağlam: İlk MVP tek kurumlu küçük ekip içindir. Müşteri ve notlar ortaktır;
kişisel görev yalnız sahibi tarafından okunur ve tamamlanır. Hesap yöneticisi
rolü tek başına iş verisi yetkisi vermez.
Girdiler: Görüşme notu ⟦ilgili metin⟧; mevcut gereksinimler ⟦kaynak ve sürüm⟧;
FG-01–FG-05, KM-01–KM-05 ve açık kararlar ⟦ilgili parçalar⟧.
Sınırlar: Ödeme, dosya yükleme, görev atama, hatırlatma, çok kiracılık veya
müşteri içeriğini YZ ile işleme ekleme. Uzunluk, kota ve zaman dilimi uydurma.
Yetki: Yalnız verilen/erişilebilen kaynakları incele ve öneri metni üret.
Çalışma: Önce ifadeleri ihtiyaç, iş kuralı, varsayım ve öneri olarak ayır.
Çelişkiyi kaynağıyla göster. Eksik bilgide ilgili karara bağlı işleri belirt;
bağımsız gereksinim incelemesini sürdür. Yeni karar vermek yerine seçenek sun.
Çıktı: Gereksinim, kaynak, aktör, kabul koşulu ve açık konu sütunlu tablo;
ardından öncelikli karar soruları ve kapsam dışı öneriler.
Doğrulama: Her gereksinimin dayanağını göster. Ortak müşteri erişiminden ortak
görev erişimi çıkarma. Not ölçütlerini bütün uygulamanın kabul kapsamı sayma.
Bu çıktıyı kullanıcıyla doğrulanmış gereksinim olarak sunma.
```

**Çıktıyı inceleme.** Tabloda bir kararın görüşmede mi, mevcut sözleşmede mi bulunduğu anlaşılmalıdır. Modelin yazdığı kabul koşulu doğru görünebilir ama kaynağı belirsizse henüz öneridir. Sırf açık soru sayısını azaltmak için seçilmiş varsayım kabul edilmez.

**İkinci tur örneği.** “Tablodaki görev görünürlüğü ortak erişim öneriyor. Mevcut kişisel görev kuralıyla çelişkiyi gider; değişiklik önerisini ayrı yaz ve yalnız etkilenen kabul koşullarını güncelle.” Bu geri bildirim belirsiz “daha iyi yap” isteğinden farklı olarak değişmesi gereken noktayı gösterir.

**Bağlantılar:** [Bölüm 4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4), [Ek B — Gereksinim](ek-b-kontrol-listeleri.md#ek-b-2).

<a id="ek-c-2"></a>

**C.2. Mimari Analiz Talimatı**

**Kullanım bağlamı.** Bir mimari önerinin gerçekten gerekli olup olmadığını karşılaştırmak için kullanılır. “Modern mimari kur” isteği, ekip ve işletim ihtiyacından bağımsız servisler üretebilir. Bu örnekte modelin görevi mevcut modüler monolit kararını gerekçeleriyle değerlendirmek, yeni bir mimariyi peşinen kazanan ilan etmemektir.

**Hazırlık.** İlgili ADR, modül sınırları, bilinen iş yükü ve gerçek işletim kısıtları gerekir. Ölçüm yoksa bunu açıkça yazın. Gelecek SaaS varsayımlarını ilk MVP'nin mevcut yükü gibi sunmayın; mimari karşılaştırmanın dayandığı dönem değişir.

```prompt Yapılandırılmış talimat T-C02
Amaç: AI-CRM için önerilen mimari değişikliği mevcut çözümle karşılaştır.
Bağlam: İlk MVP tek kurumlu; müşteri, not ve kişisel görevler modüler monolit
sınırlarında ele alınıyor. Gelecek SaaS taslağı ayrı çalışma kapsamıdır.
Girdiler: ADR-13-01 ⟦ilgili metin/sürüm⟧; öneri ⟦değişiklik⟧;
ekip ve işletim koşulları ⟦bilinenler⟧; ölçüm ⟦varsa, yoksa eksik⟧.
Sınırlar: Yük, bütçe ve ekip kapasitesi uydurma. Mikroservis, kuyruk veya
önbelleği yalnız popüler olduğu için gerekli sayma. Ürün yetkisini değiştirme.
Yetki: Mimari analiz ve karar taslağı üret; dosya, hizmet veya altyapı değiştirme.
Çalışma: Kararın çözdüğü sorunu tanımla. Mevcut çözüm, küçük iyileştirme ve
önerilen değişikliği aynı ölçütlerle değerlendir. Güven sınırı, veri tutarlılığı,
bağımlılık, yayın ve bakım etkisini incele. Ölçüm gerektiren iddiayı ayır.
Çıktı: Seçenek karşılaştırması; koşullu öneri; ADR güncelleme taslağı;
kararı değiştirebilecek bilgi ve en küçük anlamlı ölçüm planı.
Doğrulama: Öneriyi bilinen ihtiyaçla ilişkilendir. Sunucu sayısından kapasite
veya erişilebilirlik garantisi çıkarma. Uygulanmamış mimariyi kurulmuş gibi yazma.
```

**Çıktıyı inceleme.** İyi karşılaştırma her seçeneğin aynı soruya verdiği cevabı gösterir. Mevcut çözümün işletim maliyeti yazılmayıp yalnız yeni çözümün yararları sıralanıyorsa karşılaştırma eksiktir. Koşullu öneri, bilinmeyenleri gizleyen kesin hükümden daha kullanışlıdır.

**İkinci tur örneği.** “Kapasite üstünlüğü için ölçüm yok. Bu cümleyi hipotez olarak yeniden yaz; modüler monolitte önce sorgu incelemesini hangi bulgunun haklı çıkaracağını belirt.” Amaç daha uzun mimari metin değil, kararı değiştirecek kanıtı belirlemektir.

**Bağlantılar:** [Bölüm 13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13), [Ek B — Mimari](ek-b-kontrol-listeleri.md#ek-b-3).

<a id="ek-c-3"></a>

**C.3. Veri Modeli Tasarım Talimatı**

**Kullanım bağlamı.** Gereksinimlerin varlık, alan, ilişki ve kısıta dönüşmesini inceler. “CRM veritabanı çiz” isteği, yaygın ürünlerden alınmış ama bu projede gerekmeyen alanlar üretebilir. Notun yazarı, müşterisi ve eklenme zamanı gibi değerlerin kaynağı da modelde açık olmalıdır; yalnız tablo adlarını yazmak yeterli değildir.

**Hazırlık.** Güncel veri modeli ve API alanları birlikte paylaşılır. Kavramsal tasarım inceleniyorsa henüz uygulanmış ORM modeli varmış gibi davranılmaz. İsteğe bağlı iletişim alanlarının boş değer temsili gibi seçilmiş kararlar korunur; açık alan uzunlukları yeni sayılarla tamamlanmaz.

```prompt Yapılandırılmış talimat T-C03
Amaç: AI-CRM not ve görev ilişkilerini gereksinimle karşılaştıran model taslağı hazırla.
Bağlam: Not müşterisi istek yolundan, yazarı doğrulanmış aktörden, zamanı sunucudan
gelir. Görev kişiseldir; başlık ve hedef takvim günü gerekir. Durum açık veya
tamamlanmıştır; gecikmişlik açık görev ve geçmiş hedef güne göre türetilir.
Girdiler: VD-07-01 ve AS-08-01 ⟦ilgili parçalar⟧; mevcut model ⟦varsa kaynak/sürüm⟧;
sentetik müşteri, not ve görev ilişkileri ⟦örnek⟧.
Sınırlar: Alan uzunluğu, boşluk normalleştirme ve zaman dilimi uydurma.
Silme ilişkisi tasarlarken ilk MVP'ye kullanıcıya açık silme işlemi ekleme.
Yetki: Model ve kısıt önerisi üret; migration oluşturma veya veritabanı değiştirme.
Çalışma: Varlık, kimlik, ilişki çokluğu ve değer kaynağını çıkar. Mevcut kararlarla
çelişkiyi göster. Veri bütünlüğü kısıtıyla kullanıcı yetkisini ayrı değerlendir.
Tekrar ve eşzamanlı kayıt için gereken açık kararları belirt.
Çıktı: Alan–anlam–kaynak–kısıt tablosu; ilişki açıklaması; hata/sınır örnekleri;
seçilmiş kararlar ve karar bekleyen fiziksel tasarım konuları.
Doğrulama: Aynı adlı iki müşteri ayrı kimlikte kalmalı. Başkasının görevi ortak
müşteri ilişkisiyle açılmamalı. Yabancı anahtarı erişim denetimi sayma; tasarım
kontrolünü gerçek veritabanı testi diye raporlama.
```

**Çıktıyı inceleme.** Modelin “NOT NULL” yazması alanın doğru kullanıcıdan geldiğini kanıtlamaz. Benzer şekilde “transaction kullan” önerisi, aynı anda gelen oluşturma istekleri için tekrar sözleşmesini tamamlamaz. Tasarımın hangi kuralı hangi katmanda karşıladığı incelenir.

**İkinci tur örneği.** “Not yazarını istemci alanından almışsın. Aktör kaynağını düzelt; yalnız bu değişikliğin etkilediği model, doğrulama ve API alanlarını yeniden göster.” Bu tur yeni tablo üretmek yerine mevcut hatanın etkisine odaklanır.

**Bağlantılar:** [Bölüm 7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7), [Ek B — Veritabanı](ek-b-kontrol-listeleri.md#ek-b-4).

<a id="ek-c-5"></a>

**C.5. Kod Review Talimatı**

**Kullanım bağlamı.** İnceleme talimatı, “bu kod güzel mi?” sorusunu koşul, etki ve dayanağı olan bulgulara dönüştürür. Google'ın kod inceleme rehberi tasarım, işlev, karmaşıklık ve test gibi konuların birlikte değerlendirilmesini önerir (Google, t.y.). Burada odak, not oluşturma değişikliğinin mevcut sözleşmeyi korumasıdır.

**Hazırlık.** Yalnız son dosyayı değil, incelenecek farkı ve önceki tabanı verin. Gerekli komşu kaynaklar ve test sonuçları ayrıca belirtilmelidir. İnceleyenin değiştirilmiş kodu görmemesi “kusur bulunmadı” sonucuna temel olmaz; kapsam eksikliği olarak raporlanır.

```prompt Yapılandırılmış talimat T-C05
Amaç: Not oluşturma değişikliğini doğruluk ve sözleşme bakımından incele.
Bağlam: Not müşterisi yoldan, yazarı aktörden, zamanı sunucudan gelir.
Yanıt kaybolduğunda sonuç belirsiz olabilir; tekrar davranışı AS-08-01'e bağlıdır.
Girdiler: Fark ve taban sürüm ⟦kaynak⟧; ilgili uygulama/test dosyaları ⟦yollar⟧;
KM-01–KM-05 ve AS-08-01 ⟦metin⟧; gerçek kontrol raporu ⟦varsa⟧.
Sınırlar: Yeni gereksinim koyma. Stil tercihini davranış hatası gibi sunma.
İncelemediğin dosya veya çalıştırmadığın senaryo hakkında kesin sonuç verme.
Yetki: Salt okunur inceleme yap; dosya değiştirme veya testi çalıştırma.
Çalışma: Farkı çevresindeki akışla oku. Yetki, girdi kaynağı, kayıt/yanıt ayrımı,
tekrar ve eşzamanlılık etkisini değerlendir. Her şüphe için tetikleyen koşul ve
ilgili dayanağı bul. Gerçek kusur ile açık soru veya hipotezi ayır.
Çıktı: Öncelikli bulgular; her birinde konum, koşul, kullanıcı/veri etkisi,
dayanak, dar düzeltme önerisi ve gereken doğrulama. Ayrıca inceleme sınırı.
Doğrulama: Çalıştırılmış test varsa hangi sürümü kapsadığını kontrol et.
Bulgu bulunmazsa yalnız incelenen kapsam için bunu söyle; uygulamayı bütünüyle
güvenli veya yayına hazır ilan etme.
```

**Çıktıyı inceleme.** Bulgunun şiddeti, cümledeki sertliğe değil etkisine bağlıdır. “Race condition olabilir” gibi genel ifade, yarışın hangi iki istek arasında nasıl oluştuğunu açıklamıyorsa araştırma sorusu olarak kalabilir. Buna karşılık sırf tek test geçti diye gerçek bir yetki kusuru göz ardı edilmez.

**İkinci tur örneği.** “İkinci bulgu yalnız satır sayısını gerekçe gösteriyor. Bunu tercih olarak ayır; kayıt tekrarına ilişkin bulguyu tetikleyici istek sırası ve beklenen kalıcı etkiyle açıkla.” Böylece düzeltme işi, ölçülemeyen genel tavsiyelerden ayrılır.

**Bağlantılar:** [Bölüm 9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9), [Bölüm 10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10), [Ek B — Kod Review](ek-b-kontrol-listeleri.md#ek-b-5).

<a id="ek-c-devir"></a>

**Talimatı iyileştirme ve devir**

Bir yanıt beklentiyi karşılamadığında bütün görevi yeniden yazmak gerekmez. Önce hangi ölçütün bozulduğunu bulun: kaynak eksikliği mi, yanlış varsayım mı, kapsam kayması mı, yoksa gerçek davranış hatası mı? Sonraki talimat hatalı kısmı, korunacak doğru kısımları ve beklenen düzeltmeyi açıklar. “Daha profesyonel yap” yerine “kişisel görev sınırını geri getir, yalnız etkilenen sorgu ve testi güncelle” gibi gözlenebilir bir hedef verilir.

Birden fazla denemeyi karşılaştırırken aynı görevi ve kaynak tabanını koruyun. Kaynak değiştiyse sonuç farkını yalnız talimat iyileşmesine bağlamayın. Değişen modeli, bağlamı veya araç yetkisini de kaydedin. Bu, kullanıcıya her küçük adımda yeni bir onay sorusu sormak için değil, sonucun neden değiştiğini anlamak için gereklidir.

| Devir alanı | Yazılacak bilgi |
|---|---|
| Görev ve amaç | T-C01, T-C02, T-C03, T-C05 içinden uyarlanan iş ve beklenen sonuç |
| Kaynak tabanı | Okunan dosya/sürüm ve varsa yerel farklar |
| Korunan kararlar | İlgili gereksinim, yetki ve API kuralları |
| Yetki kapsamı | Öneri veya belirli yerel uygulama; izinli araç/ortam |
| Üretilen çıktı | Taslak, öneri farkı, inceleme bulgusu veya gerçek değişiklik |
| Gerçek yürütme | Varsa komut, ortam ve sonuç; yoksa yürütülmedi |
| Açık iş | Eksik kaynak, karar, kontrol veya düzeltme |
| Sonraki adım | Ön koşulu ve kapsamı belirli devam işi |

Devir kaydı, başka bir kişinin veya aracın eski varsayımı fark etmesini kolaylaştırır. Önceki yanıtın “bitti” demesi sonraki inceleme için yeterli dayanak değildir. Tersi de geçerlidir: bağlam gerçekten yeterliyse ve görev kapsamı açıksa sırf şablonda soru alanı var diye iş durdurulmaz. Eksik bilgi yalnız etkilediği karar için ele alınır.

<a id="ek-c-degerlendirme"></a>

**Çıktıyı değerlendirme**

OpenAI'nin değerlendirme rehberi, ölçütlerin göreve uygun kurulmasını ve insan değerlendirmesiyle ilişkilendirilmesini vurgular (OpenAI, t.y.-a). Burada bu yaklaşım, talimatın verdiği sonucu gereksinim ve kanıtla karşılaştırmak için kullanılır. Belirli bir API veya değerlendirme hizmetinin kurulması önerilmez. Bu ekte gerçek model denemesi yapılmamıştır.

| Ölçüt | İncelenecek soru | Yetersiz sonuç örneği |
|---|---|---|
| Göreve uygunluk | Verilen amaç karşılanıyor mu? | Not akışı yerine yeni CRM modülleri öneriyor. |
| Sözleşme tutarlılığı | Seçilmiş veri ve yetki kararları korunuyor mu? | Yönetici rolüne başkasının görevini açıyor. |
| Kaynak doğruluğu | Dosya ve atıf gerçekten incelenmiş mi? | Var olmayan dosya yolunu kesin konum gösteriyor. |
| Belirsizlik yönetimi | Bilinmeyenler açıkça ayrılıyor mu? | Açık alan uzunluğunu rastgele belirliyor. |
| Kanıt dürüstlüğü | Öneri, uygulanmış değişiklik ve test sonucu ayrılıyor mu? | Komut önerip “test geçti” diyor. |
| Yetki ve veri sınırı | İzinli eylem ve paylaşım kapsamı korunuyor mu? | Kaynak yorumunu yeni yetki sayıp dış işlem yürütüyor. |
| İncelenebilirlik | Sonuç, karar vermeye yetecek kadar somut mu? | Etki veya tetikleyici vermeden genel kusur listeliyor. |

Bu ölçütler için zorunlu başarı yüzdesi atanmaz. Ciddi bir yetki ihlalinin çok sayıda düzgün başlıkla telafi edildiği toplam puan yanıltıcı olabilir. Sonuç, [Ek B'nin durumlarıyla](ek-b-kontrol-listeleri.md) kapsamı belirtilerek raporlanabilir. Çalıştırılamayan kontrolün nedeni görünür tutulur; davranışın yanlış olduğuna ilişkin gerçek sonuçla karıştırılmaz.

Örneğin tamamen yazılmış bir öğretim durumunda, C.5 yanıtı doğru inceleme taslağı üretmiş ama test komutu yürütmeden “testler geçti” demiş olsun. Taslağın sözleşme incelemesi ayrı yapılabilir; yürütme iddiası ise düzeltilmelidir. Doğru rapor “değişiklik önerildi; testler yürütülmedi” olur. Bu düzeltme testlerin başarılı veya başarısız olduğu sonucunu üretmez.

Talimatı geliştirmek için kullanılan örnekler ile son değerlendirme örneklerini ayırmak yararlıdır. Hep aynı örneğin beklentisini talimata yerleştirip sonra o örnekteki başarıyı genel yetenek kanıtı saymayın. Yeni bir karşı örnekte sahiplik sınırının korunması veya belirsizliğin doğru raporlanması, çalışmanın başka bağlama aktarılmasını değerlendirmeye yardım eder. Gerçek deneme yapılırsa görev, model, tarih, kaynak, yetki ve değerlendirme koşulları sonuçla birlikte kaydedilir. Bu kayıt alanları kitabın çalışma önerisidir; göreve özgü değerlendirme ve ayrı örneklerle sınama yaklaşımı rehberle ilişkilidir (OpenAI, t.y.-a).

<a id="ek-c-kaynakca"></a>

**Kaynakça**

Dört birincil kaynak 6 Ekim 2026 tarihinde kontrol edilmiştir. Açıklamalar ve talimatlar bu kitap için yazılmıştır; kaynaklardaki örneklerin kopyası değildir. AI-CRM'e özgü kuralların ayrıntılı dayanakları bölüm bağlantılarındadır. OpenAI kayıtları bu ek içinde başlık sırasına göre a/b ile ayrılmıştır; ortak bibliyografya anahtarları korunur.

Google. (t.y.). [*What to look for in a code review*](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Google Engineering Practices.

OpenAI. (t.y.-a). [*Evaluation best practices*](https://developers.openai.com/api/docs/guides/evaluation-best-practices).

OpenAI. (t.y.-b). [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering).

OWASP Foundation. (t.y.). [*LLM prompt injection prevention cheat sheet*](https://cheatsheetseries.owasp.org/cheatsheets/LLM_Prompt_Injection_Prevention_Cheat_Sheet.html). OWASP Cheat Sheet Series.
