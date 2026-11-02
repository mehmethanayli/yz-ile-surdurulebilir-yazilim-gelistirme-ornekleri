# Ek A — Terimler Sözlüğü

Bu sözlük Kitap 1 için seçilmiştir; temeller, gereksinimler, veri modeli, API, kod tasarımı ve mimari konularında 123 terim içerir. Her maddede Türkçe ve İngilizce ad, kısa tanım ve serideki ayrıntılı anlatıma başvuru bulunur. Önceki kitaptan gereken temel tanımlar uygulama sırasında yeniden başvurulabilmesi için ikinci kitapta da yer alır.

Terimler konu kümelerinde sıralanır. İngilizce dizin ve kısaltmalar tablosu aynı maddelere yönlendirir. Projeye özgü FG-01 veya AS-08-01 gibi kayıt kimlikleri Ek F’dedir. Bölüm 1–13 ilk kitaba, Kitap 2, Bölüm 1–13 ikinci kitaba aittir.

Tanımlar ortak sözlükten alınmıştır; mevcut kaynak kontrol tarihi 5 Ekim 2026’dır. Bir terimin bulunması, örnek üründe o özelliğin uygulandığını göstermez.

**İçindekiler**

- [Temel sistem kavramları](#ek-a-kume-1)
- [Gereksinim, kapsam ve çalışma biçimi](#ek-a-kume-2)
- [Veri modeli ve kalıcılık](#ek-a-kume-3)
- [HTTP ve API iletişimi](#ek-a-kume-4)
- [Alan adı ve DNS](#ek-a-kume-5)
- [Kod, tasarım ve mimari](#ek-a-kume-6)
- [Geliştirme ortamı ve sürüm kontrolü](#ek-a-kume-7)
- [Test, hata ayıklama ve kanıt](#ek-a-kume-8)
- [Güvenlik ve veri sorumluluğu](#ek-a-kume-9)
- [Yayın, işletim ve SaaS](#ek-a-kume-10)
- [Yapay zekâ, ajanlar ve insan denetimi](#ek-a-kume-11)
- [Sık karıştırılan kavramlar](#ek-a-ayrimlar)
- [Kısaltmalar ve arama adları](#ek-a-kisaltmalar)
- [İngilizce–Türkçe dizin](#ek-a-dizin)
- [Kaynakça](#ek-a-kaynakca)

<a id="ek-a-kume-1"></a>

**Temel sistem kavramları**

<a id="terim-algoritma"></a>

**Algoritma — Algorithm**

Bir problemi çözmek için tanımlanan adımlar ve karar kurallarıdır. Müşteri listesini filtrelemek bir algoritma içerebilir; doğru sonuç için boş liste ve hatalı girdi gibi yollar da düşünülür.

[Bkz. Bölüm 9.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="terim-bulut"></a>

**Bulut bilişim — Cloud computing**

İşlem, depolama ve ağ gibi kaynakların hizmet olarak sağlandığı modeldir. Kaynak kullanma biçimini değiştirir; uygulamanın verisini koruma, yapılandırma ve maliyet sorumluluğunu kendiliğinden kaldırmaz.

[Bkz. Kitap 2, Bölüm 8.6](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-istemci"></a>

**İstemci — Client**

Başka bir bileşenden hizmet isteyen taraftır. Tarayıcı veya mobil uygulama istemci olabilir. İstemcinin gönderdiği müşteri kimliği, kullanıcının o kayda erişme hakkını tek başına göstermez.

[Bkz. Bölüm 2.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-json"></a>

**JSON — JavaScript Object Notation**

Nesne, dizi, metin, sayı, mantıksal değer ve null ile veri temsil eden metin biçimidir. JSON içinde tarih için ayrı temel tür yoktur; tarih metninin biçimi API sözleşmesinde belirlenir.

[Bkz. Bölüm 8.16](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-frontend"></a>

**Kullanıcı arayüzü tarafı — Frontend**

Kullanıcının etkileştiği ekran ve arayüz davranışlarını kapsar. Düğmeyi gizlemek kullanılabilirliği düzenleyebilir; sunucu tarafındaki yetki kontrolünün yerine geçmez.

[Bkz. Bölüm 2.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-library"></a>

**Kütüphane — Library**

Uygulamanın belirli amaçla çağırdığı hazır işlev veya bileşenler bütünüdür. Çatıyla arasındaki fark yalnız büyüklük değildir; çalışma akışını kimin yönettiği önemlidir. Her yeni kütüphane bakım ve bağımlılık kararıdır.

[Bkz. Bölüm 6.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-6).

<a id="terim-programlama-dili"></a>

**Programlama dili — Programming language**

Bilgisayarın işleyeceği davranışı belirli sözdizimi ve anlam kurallarıyla ifade etme aracıdır. Doğal dildeki isteğin koda çevrilmesi, istekte eksik olan iş kuralının kendiliğinden kesinleşmesini sağlamaz.

[Bkz. Bölüm 6.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-6).

<a id="terim-sunucu"></a>

**Sunucu — Server**

İstekleri karşılayıp hizmet sunan yazılımı veya bağlama göre onun çalıştığı bilgisayarı anlatır. “Sunucu kapandı” ifadesinde uygulama süreci, makine ve ağ erişimi ayrı incelenmelidir.

[Bkz. Bölüm 2.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-backend"></a>

**Sunucu tarafı — Backend**

İş kuralları, veri erişimi ve yetki kontrolleri gibi sorumlulukların yürütüldüğü uygulama tarafıdır. Yalnız veritabanından ibaret değildir; notun yazarını doğrulanmış kullanıcıdan belirlemek de bu tarafta yapılır.

[Bkz. Bölüm 2.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-api"></a>

**Uygulama programlama arayüzü (API) — Application programming interface**

Yazılım bileşenlerinin hangi işlemleri, girdileri ve sonuçları kullanarak iletişim kuracağını tanımlar. Web API bunun bir türüdür; her API internet üzerinden çalışmaz. AI-CRM'de not eklemenin davranışı API sözleşmesiyle açıklanır.

[Bkz. Bölüm 8.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-veritabani"></a>

**Veritabanı — Database**

Verilerin düzenli tutulduğu ve belirli yöntemlerle erişildiği yapıdır. Veritabanı yönetim sistemi bu yapıyı yönetir. Ekranda görünen geçici liste, kaydın kalıcı olarak saklandığının tek başına kanıtı değildir.

[Bkz. Bölüm 7.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-framework"></a>

**Yazılım çatısı — Framework**

Uygulamanın yapısını ve çalışma akışının bir bölümünü düzenleyen altyapıdır. Uygulama kodu çatının belirlediği noktalarda çağrılabilir. Hazır bileşenler, ürünün iş kuralı ve yetki tasarımını tamamlamış sayılmaz.

[Bkz. Bölüm 6.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-6).

<a id="terim-yazilim-yasam-dongusu"></a>

**Yazılım geliştirme yaşam döngüsü (SDLC) — Software development life cycle**

Gereksinim, tasarım, geliştirme, doğrulama, yayın ve bakım çalışmalarının bütünüdür. Tek yönlü, değişmez bir sıra olmak zorunda değildir; yeni bilgi önceki kararlara dönmeyi gerektirebilir.

[Bkz. Bölüm 3.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3).

<a id="terim-yazilim-muhendisligi"></a>

**Yazılım mühendisliği — Software engineering**

Yazılımı gereksinimden bakım ve işletime kadar sistemli biçimde geliştirme ve değerlendirme disiplinidir. Kod üretiminin yanında tasarım, doğrulama, maliyet, risk ve değişim sorumluluklarını da kapsar.

[Bkz. Kitap 2, Bölüm 13.9](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="ek-a-kume-2"></a>

**Gereksinim, kapsam ve çalışma biçimi**

<a id="terim-mvp"></a>

**Asgari uygulanabilir ürün (MVP) — Minimum viable product**

Belirli kullanıcı ihtiyacını sınamak için seçilmiş sınırlı ama anlamlı ürün kapsamıdır. Temel yetki kontrolleri eksik bir taslakla aynı şey değildir. Kapsamın dar olması doğruluk sorumluluğunu kaldırmaz.

[Bkz. Bölüm 4.18](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-cevik"></a>

**Çevik yaklaşım — Agile**

Geri bildirim, iş birliği ve değişime uyumla değer üretmeyi öne çıkaran yaklaşımdır. Planlamayı veya belgeyi kaldırmak anlamına gelmez; kararlar öğrenilen bilgiyle güncellenir.

[Bkz. Bölüm 3.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3).

<a id="terim-devops"></a>

**Geliştirme ve işletim iş birliği — DevOps**

Geliştirme ve işletim sorumluluklarının ortak hedef, geri bildirim ve çalışma düzeniyle ele alınmasıdır. Otomasyon bunu destekleyebilir; bir araç veya ekibin adı tek başına DevOps pratiğini oluşturmaz.

[Bkz. Bölüm 3.16](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3).

<a id="terim-gereksinim"></a>

**Gereksinim — Requirement**

Sistemin karşılaması gereken ihtiyaç, davranış veya koşuldur. “Güzel ekran” belirsizken, “ekip üyesi müşteri adına göre arama yapabilir” daha sınanabilir bir beklentidir.

[Bkz. Bölüm 4.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-islevsel-gereksinim"></a>

**İşlevsel gereksinim — Functional requirement**

Sistemin ne yapacağını belirtir. Müşteri oluşturmak veya not eklemek örnektir. Başarı ölçütleri ve hata yolları yazılmadığında işlevin adı tek başına uygulama için yeterli değildir.

[Bkz. Bölüm 4.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-is-kurali"></a>

**İş kuralı — Business rule**

İş alanında geçerli karar veya sınırlamadır. AI-CRM'de kişisel görevi yalnız sahibinin okuyup tamamlaması bir iş kuralıdır; modelin önerdiği yaygın rol şeması bu kuralı sessizce değiştiremez.

[Bkz. Bölüm 4.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kabul-olcutu"></a>

**Kabul ölçütü — Acceptance criterion**

Bir sonucun kabul edilebilmesi için sağlanacak gözlenebilir koşuldur. Notun doğru müşteriyle ve doğrulanmış yazarla ilişkilendirilmesi örnektir. Ölçütün yazılması, koşulun gerçek uygulamada sınandığı anlamına gelmez.

[Bkz. Bölüm 4.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kalite-gereksinimi"></a>

**Kalite gereksinimi — Quality requirement; non-functional requirement**

Performans, güvenlik ve kullanılabilirlik gibi niteliklere ilişkin beklentidir. İşlevsel olmayan gereksinimler bunların yanında kısıtları da içerebilir. “Hızlı olsun” yerine ölçüm koşulu ve kabul sınırı gerekir.

[Bkz. Bölüm 4.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kapsam-kaymasi"></a>

**Kapsam kayması — Scope creep**

Başlangıçta kararlaştırılan işin etkisi değerlendirilmeden büyümesidir. İlk MVP'ye görev atama veya ödeme eklemek küçük bir arayüz değişikliği sayılmaz; veri ve yetki kararlarını da etkiler.

[Bkz. Bölüm 4.17](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kullanici-hikayesi"></a>

**Kullanıcı hikâyesi — User story**

Kullanıcının ihtiyacını ve beklenen değerini kısa biçimde anlatır. Ayrıntılı veri, yetki ve hata sözleşmesini tek başına içermez; konuşma ve kabul ölçütleriyle tamamlanır.

[Bkz. Bölüm 4.9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kullanim-senaryosu"></a>

**Kullanım senaryosu — Use case**

Bir aktörün hedefe ulaşırken sistemle kurduğu etkileşimi, ön koşulları ve alternatif yolları açıklar. Not kaydında başarı, doğrulama hatası ve sonucu belirsiz istek ayrı yollardır.

[Bkz. Bölüm 4.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-prototip"></a>

**Prototip — Prototype**

Bir fikir veya etkileşim hakkındaki soruyu araştırmak için hazırlanan erken temsildir. Çalışan ekran, gerçek veri güvenliği ve işletim düzeninin tamamlandığını göstermez.

[Bkz. Kitap 2, Bölüm 11.1](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-scrum"></a>

**Scrum — Scrum**

Karmaşık problemlerde değer üretimini kısa çalışma aralıkları ve inceleme–uyarlama yoluyla düzenleyen hafif çerçevedir. Bir görev panosu kullanmak tek başına Scrum değildir. Kitapta AI-CRM için uygulanması zorunlu süreç olarak seçilmemiştir.

[Bkz. Bölüm 3.15](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3).

<a id="terim-yinelemeli-artimli"></a>

**Yinelemeli ve artımlı geliştirme — Iterative and incremental development**

Yinelemeli geliştirme çözümü tekrar değerlendirip iyileştirir; artımlı geliştirme işlevi parça parça ekler. Aynı çalışmada birlikte kullanılabilirler: müşteri aramasını iyileştirmek ve ardından not akışını eklemek farklı hareketlerdir.

[Bkz. Bölüm 3.12](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3).

<a id="ek-a-kume-3"></a>

**Veri modeli ve kalıcılık**

<a id="terim-acid"></a>

**ACID — Atomicity, consistency, isolation, durability**

Atomiklik, tutarlılık, yalıtım ve kalıcılık özelliklerini birlikte anan kısaltmadır. İşlemin bütünlüğünü düşünmeye yardım eder. Yalıtım düzeyleri farklı davranışlar gösterebilir; ACID, yedekleme veya uygulama yetkilendirmesinin yerine geçmez.

[Bkz. Bölüm 7.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-birincil-anahtar"></a>

**Birincil anahtar — Primary key**

Tablodaki her satırı benzersiz belirleyen anahtardır; tek veya birden fazla sütundan oluşabilir. Müşteri adı gibi değişebilir ve yinelenebilir bir alanı kimlikle karıştırmamak gerekir.

[Bkz. Bölüm 7.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-iliski"></a>

**İlişki — Relationship**

Varlıkların birbirine nasıl bağlandığını anlatır. Bire bir, bire çok ve çoka çok ilişkiler farklı katılım kuralları taşır. Bir müşterinin çok notu bulunması, bu notların tek metin alanında biriktirilmesini gerektirmez.

[Bkz. Bölüm 7.8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-indeks"></a>

**İndeks — Index**

Belirli veri erişimlerini hızlandırabilen yardımcı yapıdır. Okuma yararı yanında yazma ve depolama maliyeti vardır. Her sütuna indeks eklemek otomatik olarak daha iyi performans sağlamaz.

[Bkz. Bölüm 7.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-kisit"></a>

**Kısıt — Constraint**

Verinin uyması gereken koşulu uygular. Benzersizlik, boş olamama ve yabancı anahtar örnektir. Form doğrulamasıyla veritabanı kısıtları farklı noktalarda çalışır; biri diğerinin bütün görevlerini üstlenmez.

[Bkz. Bölüm 7.12](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-orm"></a>

**Nesne–ilişkisel eşleme (ORM) — Object–relational mapping**

Uygulama nesneleriyle ilişkisel veri erişimi arasında eşleme sağlayan yaklaşımdır. Sorgu üretimini kolaylaştırır; sorgu maliyetini, işlem sınırlarını veya kişisel görev sahipliği kontrolünü ortadan kaldırmaz.

[Bkz. Bölüm 7.25](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-nitelik"></a>

**Nitelik — Attribute**

Bir varlığın özelliğidir. Müşteri adı ve görevin hedef günü örnektir. Kavramsal nitelik veritabanında sütunla temsil edilebilir; kullanıcıdan gelen her alan doğrudan saklanmak zorunda değildir.

[Bkz. Bölüm 7.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-normalizasyon"></a>

**Normalizasyon — Normalization**

İlişkisel tasarımda bağımlılıkları düzenleyerek gereksiz tekrar ve güncelleme tutarsızlıklarını azaltma yaklaşımıdır. Her ihtiyacın ayrı tablo olması gerektiği anlamına gelmez; veri anlamı ve kullanım birlikte değerlendirilir.

[Bkz. Bölüm 7.16](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-nosql"></a>

**NoSQL — NoSQL databases**

Belge, anahtar–değer veya graf gibi farklı veri modellerini kullanan veritabanı aileleri için kullanılan genel addır. “Hiç şema veya işlem yoktur” anlamına gelmez; özellikler seçilen sisteme göre incelenir.

[Bkz. Bölüm 7.18](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-sql"></a>

**SQL — Structured Query Language**

İlişkisel veriyi tanımlamak, sorgulamak ve değiştirmek için kullanılan dildir. Kullanıcı girdisini sorgu metnine birleştirmekle parametre olarak iletmek farklıdır; bu fark SQL enjeksiyonu riskini etkiler.

[Bkz. Bölüm 7.17](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-sema"></a>

**Şema — Schema**

Verinin yapısını ve ilişkili kuralları tanımlar. Veritabanı şeması ile API'nin istek/yanıt şeması farklı sözleşmelerdir. Bir tablonun bütün sütunlarını dış API'ye açmak zorunlu değildir.

[Bkz. Bölüm 7.20](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-migration"></a>

**Şema veya veri geçişi — Migration**

Veri yapısını ya da mevcut veriyi sürümler arasında dönüştüren kontrollü değişikliktir. Kodun eski sürümüne dönmek yapılan veri dönüşümünü otomatik geri almaz; uyumluluk ve kurtarma ayrıca planlanır.

[Bkz. Bölüm 7.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-tablo"></a>

**Tablo, satır ve sütun — Table, row and column**

İlişkisel tabloda satır bir kaydı, sütun belirli veri alanını temsil eder. Sütunun türü ve kısıtları izin verilen değerleri etkiler; aynı görünen müşteri adı kayıtların aynı olduğunu göstermez.

[Bkz. Bölüm 7.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-varlik"></a>

**Varlık — Entity**

İş alanında kimliği ve anlamı bulunan kavramdır. Müşteri ve görev örnektir. Her varlığın mutlaka tek tabloyla temsil edilmesi gerekmez; kavramsal model ile fiziksel saklama tasarımı ayrılır.

[Bkz. Bölüm 7.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-islem"></a>

**Veritabanı işlemi — Transaction**

Bir veya daha çok veri işleminin belirli bütünlük ve yalıtım kuralları içinde ele alınmasıdır. Birden fazla kaydın tutarlılığını korumaya yardım eder; ağ yanıtının kullanıcıya ulaştığını garanti etmez.

[Bkz. Bölüm 7.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-veri-butunlugu"></a>

**Veri bütünlüğü — Data integrity**

Verinin belirlenen ilişki ve geçerlilik kurallarını korumasıdır. Var olmayan müşteriye bağlı notun önlenmesi örnektir. Bir kaydın biçimsel olarak geçerli olması, iş açısından doğru veya erişimin yetkili olduğunu kanıtlamaz.

[Bkz. Bölüm 7.15](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-yabanci-anahtar"></a>

**Yabancı anahtar — Foreign key**

Bir kaydın başka veya aynı tablodaki anahtarla ilişkisini veritabanı düzeyinde kısıtlar. Notun müşteri bağlantısını koruyabilir; notu okuyacak kullanıcının yetkisini kendiliğinden belirlemez.

[Bkz. Bölüm 7.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="ek-a-kume-4"></a>

**HTTP ve API iletişimi**

<a id="terim-baslik-govde"></a>

**Başlık ve gövde — Header and body**

Başlıklar iletiyle ilgili üst bilgiyi, gövde ise varsa içeriği taşır. JSON gövdesiyle gönderilen iş verisi, kimlik ve yetki kararlarının otomatik olarak güvenilir kaynağı değildir.

[Bkz. Bölüm 8.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-delete"></a>

**DELETE — DELETE method**

Hedef URI ile onun mevcut işlevi arasındaki ilişkiyi kaldırmayı ister. Fiziksel diskten bütün izlerin silinmesini garanti etmez (Fielding vd., 2022).

[Bkz. Bölüm 8.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-get"></a>

**GET — GET method**

Hedef kaynağın temsilini istemek için kullanılır. Semantiği güvenlidir: istemci bir durum değişikliği talep etmez. Günlük yazılması gibi yan etkilerin hiç olmayacağı anlamına gelmez (Fielding vd., 2022).

[Bkz. Bölüm 8.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-graphql"></a>

**GraphQL — GraphQL**

API için sorgu dili ve tanımlı tür sistemiyle bu sorguları çalıştırma yaklaşımıdır. İstemci istediği alanları seçebilir; bu seçim erişim yetkisi vermez. AI-CRM'in seçilmiş HTTP/JSON sözleşmesini kendiliğinden değiştirmez (GraphQL Foundation, t.y.).

[Bkz. Bölüm 8.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-http"></a>

**HTTP — Hypertext Transfer Protocol**

İstemci ve sunucu arasında istek ve yanıt anlamlarını tanımlayan uygulama katmanı protokolüdür. Durum kodu, yöntem ve başlıklar bu anlamın parçalarıdır (Fielding vd., 2022).

[Bkz. Bölüm 2.9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-durum-kodu"></a>

**HTTP durum kodu — HTTP status code**

İsteğin sonucunu üç basamaklı kodla sınıflandırır. Kod tek başına iş sonucunun bütün ayrıntılarını açıklamaz. AI-CRM'in 400, 403, 404, 409 ve 422 ayrımları kendi API sözleşmesinde tanımlıdır.

[Bkz. Bölüm 8.12](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-idempotency"></a>

**İdempotentlik — Idempotency**

Aynı isteğin tekrarlanmasının amaçlanan sunucu etkisinin tek isteğinkiyle aynı olmasıdır. Her yanıtın aynı kodu taşıması gerekmez (Fielding vd., 2022). Uygulama tekrar anahtarlarının kapsamı ve saklama süresi ayrıca belirlenir.

[Bkz. Bölüm 8.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-rate-limit"></a>

**İstek sınırlama — Rate limiting**

Belirli zaman veya kaynak koşulunda istek kullanımını sınırlar. Anahtarın kullanıcı, adres veya başka boyutla tanımlanması etkiyi değiştirir. Kimlik doğrulama ve yetkilendirmenin yerine geçmez.

[Bkz. Bölüm 8.24](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-istek-yanit"></a>

**İstek ve yanıt — Request and response**

İstek yapılması beklenen işlemi, yanıt ise sunucunun sonucunu taşır. Yanıt alınamaması işlemin hiç yapılmadığını göstermez; AI-CRM not kaydında sonuç belirsiz kalabilir.

[Bkz. Bölüm 2.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-kaynak"></a>

**Kaynak — Resource**

API'nin tanımladığı ve üzerinde işlem sunabildiği kavramdır. Müşteri veya görev kaynak olabilir. Kaynak gösterimi, veritabanı satırının bire bir kopyası olmak zorunda değildir.

[Bkz. Bölüm 8.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-webhook"></a>

**Olay bildirimi çağrısı — Webhook**

Bir olay oluştuğunda başka sistemin belirli adrese istek göndermesiyle kurulan bildirim düzenidir. Teslimler tekrarlanabilir veya sırası değişebilir; alıcı kabul, doğrulama ve işleme durumlarını ayırır.

[Bkz. Bölüm 8.22](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-patch"></a>

**PATCH — PATCH method**

Kaynağa kısmi değişiklik uygulamak için kullanılır. Tekrar davranışı değişiklik biçimine bağlıdır. AI-CRM görev örneğinde durumu tamamlandıya atamak, her çağrıda durumu tersine çevirmekten farklıdır.

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-post"></a>

**POST — POST method**

Gönderilen içeriğin hedef kaynağın kurallarına göre işlenmesini ister. Oluşturma için kullanılabilir; tekrarının etkisi uygulama sözleşmesine bağlıdır (Fielding vd., 2022).

[Bkz. Bölüm 8.8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-put"></a>

**PUT — PUT method**

Hedef kaynağın durumunu gönderilen temsile göre oluşturma veya değiştirme isteğidir. Amaçlanan etki bakımından idempotenttir; ilk MVP'de sırf bu yöntem var diye müşteri güncelleme işlemi açılmaz (Fielding vd., 2022).

[Bkz. Bölüm 8.9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-rest"></a>

**REST — Representational State Transfer**

Kaynaklar, temsiller ve tekbiçimli arayüz gibi kısıtlarla açıklanan mimari yaklaşımdır. Yalnız HTTP üzerinden JSON döndürmek bütün REST kısıtlarını karşıladığını göstermez.

[Bkz. Bölüm 8.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-endpoint"></a>

**Uç nokta — Endpoint**

API'de bir işlemin erişildiği adres ve kullanım bağlamıdır. HTTP yönteminin de bilinmesi gerekir; aynı yol için okuma ve oluşturma davranışları farklı olabilir.

[Bkz. Bölüm 8.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="ek-a-kume-5"></a>

**Alan adı ve DNS**

<a id="terim-alan-adi"></a>

**Alan adı — Domain name**

DNS ad alanındaki hiyerarşik addır. Uygulamanın adı, barındırıldığı makine ve tam URL farklı kavramlardır. Bir alan adı birden fazla hizmetin kayıtlarını taşıyabilir.

[Bkz. Bölüm 2.12](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="ek-a-kume-6"></a>

**Kod, tasarım ve mimari**

<a id="terim-ocp"></a>

**Açık–kapalı ilkesi (OCP) — Open/closed principle**

Beklenen değişim ekseninde mevcut davranışı sürekli bozmak yerine genişletilebilir sınırlar kurmayı önerir. Bütün olası geleceklere önceden eklenti mekanizması hazırlamak anlamına gelmez.

[Bkz. Bölüm 11.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-arayuz"></a>

**Arayüz — Interface**

Bileşenin sunduğu işlemleri ve kullanım beklentilerini tanımlar. Buradaki arayüz ekran anlamındaki kullanıcı arayüzüyle aynı bağlamda değildir. Kullanıcıların ihtiyaç duymadığı işlemlere bağımlı bırakılmaması önemlidir.

[Bkz. Bölüm 11.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-isp"></a>

**Arayüz ayrımı ilkesi (ISP) — Interface segregation principle**

Kullanan bileşenlerin ihtiyaç duymadıkları işlemlere bağımlı bırakılmamasını önerir. Sırf ortak ad altında toplandı diye salt okuma bileşenine silme davranışı yüklenmez.

[Bkz. Bölüm 11.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-dip"></a>

**Bağımlılıkların tersine çevrilmesi (DIP) — Dependency inversion principle**

Üst düzey politikayla ayrıntıların uygun soyutlamalar üzerinden bağlanmasını önerir. Bağımlılık enjeksiyonu bunu destekleyebilir; iki terim aynı kavram değildir.

[Bkz. Bölüm 11.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-di"></a>

**Bağımlılık enjeksiyonu (DI) — Dependency injection**

Bir bileşenin kullandığı bağımlılıkların dışarıdan verilmesidir. Testte sahte saat geçirmek örnektir. Çatı veya container kullanmak zorunlu değildir; basit fonksiyon parametresi yeterli olabilir.

[Bkz. Bölüm 12.9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-kiss"></a>

**Basit tutma ilkesi (KISS) — Keep it simple**

Gereksinimi anlaşılır ve yeterli çözümle karşılamayı önerir. Kontrolleri kaldırıp daha kısa kod yazmakla aynı değildir; hata yolları da anlaşılabilir olmalıdır.

[Bkz. Bölüm 10.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10).

<a id="terim-bagimlilik"></a>

**Bileşenler arası bağımlılık — Coupling**

Bir bileşendeki değişikliğin diğerlerini ne kadar etkileyebileceğiyle ilgilidir. Düşük bağımlılık, hiç iletişim olmaması değil, gerekli ilişkinin açık ve sınırlı kurulmasıdır.

[Bkz. Bölüm 10.8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10).

<a id="terim-fonksiyon"></a>

**Fonksiyon — Function**

Belirli girdilerle bir işi gerçekleştiren adlandırılmış kod birimidir. Döndürdüğü değerle veri değiştirme gibi yan etkileri ayrı düşünülür. “Notu kaydet” fonksiyonunun hata ve tekrar davranışı da sorumluluğuna dahildir.

[Bkz. Bölüm 9.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="terim-yagni"></a>

**Gerekmeyeni şimdiden yapmama (YAGNI) — You aren't gonna need it**

Henüz gerekli olmayan yetenekleri varsayımsal ihtiyaç için uygulamaktan kaçınma ilkesidir. İlk MVP'ye ileride gerekebilir diye çok kiracılık eklememek örnektir; mevcut güvenlik ihtiyacını erteleme gerekçesi değildir.

[Bkz. Bölüm 10.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10).

<a id="terim-observer"></a>

**Gözlemci deseni — Observer pattern**

Bir değişiklikten ilgilenen bileşenlerin haberdar olmasını düzenler. Bildirim bağı kurmak, olayın kalıcı ve tam bir kez işlendiğini garanti etmez; hata ve yaşam döngüsü yönetimi ayrıca gerekir.

[Bkz. Bölüm 12.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-reliability"></a>

**Güvenilirlik — Reliability**

Sistemin belirtilen koşullarda beklenen işi zaman içinde doğru ve tutarlı biçimde yapabilmesidir. Erişilebilir bir uygulamanın notu yanlış müşteriye bağlaması güvenilir davranış değildir.

[Bkz. Bölüm 13.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-availability"></a>

**Hizmetin erişilebilirliği — Availability**

Hizmetin gerektiğinde kullanılabilir olmasıdır. Arayüzün kullanım kolaylığını anlatan usability ile aynı değildir. Çalışan sunucu süreci, kullanıcının müşteri kaydını başarıyla okuyabildiğini tek başına göstermez.

[Bkz. Bölüm 13.12](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-baglilik"></a>

**İç bağlılık — Cohesion**

Bir modülün parçalarının ortak amaca ne kadar hizmet ettiğini anlatır. Yüksek iç bağlılık, birbiriyle ilişkili davranışların birlikte bulunmasıdır. Modüller arası bağımlılıkla karıştırılmamalıdır.

[Bkz. Bölüm 10.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10).

<a id="terim-kod-kokusu"></a>

**Kod kokusu — Code smell**

Tasarımın incelenmesini gerektirebilecek belirtidir. Çok uzun fonksiyon veya dağılmış tekrar örnektir. Belirti otomatik hata kararı değildir; bağlam ve değişiklik ihtiyacı değerlendirilir.

[Bkz. Bölüm 9.9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="terim-lsp"></a>

**Liskov yerine geçme ilkesi (LSP) — Liskov substitution principle**

Bir alt türün üst tür yerine kullanıldığında beklenen davranış sözleşmesini korumasını ister. Aynı yöntem adlarına sahip olmak yeterli değildir; girdiler, sonuçlar ve hata beklentileri de önemlidir.

[Bkz. Bölüm 11.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-mikroservis"></a>

**Mikroservis — Microservice**

Belirli iş sorumluluklarını bağımsız hizmetler ve dağıtım sınırlarıyla düzenleyen yaklaşımdır. Ağ, veri tutarlılığı ve işletim maliyetleri getirir; küçük fonksiyonlara bölmekle aynı değildir.

[Bkz. Bölüm 13.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-adr"></a>

**Mimari karar kaydı (ADR) — Architecture decision record**

Bir mimari kararın bağlamını, seçeneklerini, gerekçesini ve sonuçlarını saklar. Kararın yazılması uygulanmış olduğunu göstermez. AI-CRM'de mimari tercihlerin sonradan sorgulanmasını kolaylaştırır.

[Bkz. Bölüm 13.19](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-mvc"></a>

**Model–görünüm–denetleyici (MVC) — Model–view–controller**

Veri/iş davranışı, sunum ve etkileşim denetimini ayıran tasarım düzenidir. Çatılar bu sorumlulukları farklı adlarla sunabilir; adların benzerliği mimarinin bire bir aynı olduğunu kanıtlamaz.

[Bkz. Bölüm 12.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-moduler-monolit"></a>

**Modüler monolit — Modular monolith**

Tek dağıtım birimi içinde belirgin modül sınırları kurulan mimaridir. Müşteri, not ve görev alanları ayrı sorumluluklar taşıyabilir; ayrı sunuculara dağıtılmaları gerekmez.

[Bkz. Bölüm 13.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-scalability"></a>

**Ölçeklenebilirlik — Scalability**

İş yükü büyürken hedeflenen davranışı uygun kaynak ve maliyetle sürdürebilme yeteneğidir. Tek isteğin hızlı olması artan eşzamanlı kullanıcı sayısında aynı sonucu garanti etmez; yük ve ölçüm koşulları belirtilmelidir.

[Bkz. Bölüm 13.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-sinif-nesne"></a>

**Sınıf ve nesne — Class and object**

Sınıf, nesnelerin veri ve davranışını tanımlayan yapıdır; nesne bu yapının bir örneğidir. Birlikte kullanılmaları her davranış için yeni sınıf oluşturmayı gerektirmez.

[Bkz. Bölüm 10.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10).

<a id="terim-solid"></a>

**SOLID — SOLID principles**

Tek sorumluluk, açık–kapalı, Liskov yerine geçme, arayüz ayrımı ve bağımlılıkların tersine çevrilmesi ilkelerinin ortak adıdır. Bağlama göre tasarım değerlendirmesine yardım eder; her yerde daha fazla sınıf üretme kuralı değildir.

[Bkz. Bölüm 11.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-sorumluluk-ayrimi"></a>

**Sorumlulukların ayrılması — Separation of concerns**

Farklı amaç taşıyan işleri uygun sınırlarla ayırır. Ekran biçimlendirme, iş kuralı ve veri erişiminin ayrılması değişiklik etkisini anlamayı kolaylaştırabilir; dosya sayısını artırmak tek başına yeterli değildir.

[Bkz. Bölüm 10.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10).

<a id="terim-soyutlama"></a>

**Soyutlama — Abstraction**

Bir bileşenin gerekli özelliklerini öne çıkarıp ayrıntılarını uygun sınır arkasında tutmaktır. Ayrıntıları gizlemek, onların etkisini yok etmez; veri erişim soyutlamasının işlem ve hata davranışı bilinmelidir.

[Bkz. Bölüm 11.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-strategy"></a>

**Strateji deseni — Strategy pattern**

Aynı amaca hizmet eden değiştirilebilir davranışları ortak sözleşme altında ayırır. Her küçük koşul ifadesi için ayrı strateji sınıfı açmak gerekmez.

[Bkz. Bölüm 12.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-serverless"></a>

**Sunucusuz çalıştırma — Serverless**

Sunucu yönetiminin önemli kısmını sağlayıcının üstlendiği çalıştırma modelidir. Sunucuların hiç olmadığı anlamına gelmez; uygulama sınırları, veri erişimi ve hizmet maliyetleri yine tasarlanır.

[Bkz. Bölüm 13.8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-desen"></a>

**Tasarım deseni — Design pattern**

Tekrarlayan tasarım problemine bağlama göre uyarlanabilen çözüm düzenidir. Hazır kod kopyası veya her projede zorunlu katman değildir; getirdiği karmaşıklık sağladığı yararla karşılaştırılır.

[Bkz. Bölüm 12.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-teknik-borc"></a>

**Teknik borç — Technical debt**

Bugünkü tasarım veya uygulama kararlarının gelecekteki değişiklikleri zorlaştıran maliyetini anlatır. Her kusurla aynı şey değildir; borcun etkisi, gerekçesi ve giderme önceliği açıklanmalıdır.

[Bkz. Bölüm 9.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="terim-dry"></a>

**Tekrarı azaltma ilkesi (DRY) — Don't repeat yourself**

Aynı bilginin birden fazla bağımsız yerde tutulmasını azaltmayı amaçlar. Yalnız benzer görünen satırları birleştirmek, farklı iş kurallarını gereksiz yere birbirine bağlayabilir.

[Bkz. Bölüm 10.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-10).

<a id="terim-srp"></a>

**Tek sorumluluk ilkesi (SRP) — Single responsibility principle**

Bir modülün farklı değişim nedenlerini gereksiz yere bir araya getirmemesini önerir. “Her fonksiyonda yalnız bir satır” gibi mekanik bir kural değildir; sorumluluk iş bağlamıyla anlaşılır.

[Bkz. Bölüm 11.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11).

<a id="terim-adapter"></a>

**Uyarlayıcı deseni — Adapter pattern**

Bir bileşenin arayüzünü kullanan tarafın beklediği biçime uyarlar. Alan adlarını çevirmek kadar hata ve veri anlamını korumak da önemlidir.

[Bkz. Bölüm 12.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-factory"></a>

**Üretici deseni — Factory pattern**

Nesne oluşturma kararını onu kullanan davranıştan ayırır. Oluşturma biçimi gerçekten değişiyorsa yararlı olabilir; tek ve basit kurulum için gereksiz sınıf ağı kurmayı gerektirmez.

[Bkz. Bölüm 12.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-repository-pattern"></a>

**Veri erişim deseni — Repository pattern**

Veri koleksiyonuna erişimi belirli arayüz arkasında toplar. Git deposu anlamındaki repository ile farklıdır. ORM bulunan her uygulamaya zorunlu ek katman değildir.

[Bkz. Bölüm 12.8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-refactoring"></a>

**Yeniden yapılandırma — Refactoring**

Gözlenebilir davranışı koruyarak kodun iç yapısını iyileştirmektir. Görevlerin erişim kuralını değiştirmek refactoring diye gizlenemez; davranış değişikliği ayrıca tanımlanır ve doğrulanır.

[Bkz. Bölüm 9.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="ek-a-kume-7"></a>

**Geliştirme ortamı ve sürüm kontrolü**

<a id="terim-git"></a>

**Git — Git**

Kaynak geçmişini yerel ve uzak depolarla izlemeye yarayan dağıtık sürüm kontrol sistemidir. Git ile GitHub aynı şey değildir; yerel commit ağ bağlantısı olmadan da oluşturulabilir.

[Bkz. Kitap 2, Bölüm 2.2](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="ek-a-kume-8"></a>

**Test, hata ayıklama ve kanıt**

<a id="terim-birim-test"></a>

**Birim testi — Unit test**

Dar bir davranış birimini belirlenen sınırlar içinde sınar. Bir iş kuralı fonksiyonunun doğru sonucu, HTTP katmanı ve veritabanının birlikte doğru çalıştığını tek başına kanıtlamaz.

[Bkz. Kitap 2, Bölüm 5.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-butunlesme-test"></a>

**Bütünleşme testi — Integration test**

Birden fazla bileşenin birlikte davranışını sınar. Uygulama–veritabanı etkileşimi örnektir. Hangi bileşenlerin gerçek, hangilerinin yerine geçilmiş olduğu raporda açıklanır.

[Bkz. Kitap 2, Bölüm 5.6](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="ek-a-kume-9"></a>

**Güvenlik ve veri sorumluluğu**

<a id="terim-api-key"></a>

**API anahtarı — API key**

API kullanımında istemciyi veya uygulamayı tanımak ve erişimi denetlemek için kullanılan değerdir. Tek başına son kullanıcının bütün yetkilerini temsil etmek zorunda değildir; gizli tutulması gerekebilir.

[Bkz. Bölüm 8.20](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-secret"></a>

**Gizli erişim bilgisi — Secret**

Açığa çıkması erişim veya işlem yetkisi verebilen parola, anahtar gibi bilgidir. .env dosyasında bulunması tek başına koruma sağlamaz; paylaşım ve günlük yolları da denetlenir.

[Bkz. Kitap 2, Bölüm 6.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-guvenlik-token"></a>

**Güvenlik belirteci — Security token**

Kimlik veya erişim akışında belirli anlam taşıyan değerdir. YZ token'ından farklıdır. Her token JWT değildir; içeriği, doğrulaması ve süresi kullanılan sözleşmeyle belirlenir.

[Bkz. Bölüm 8.19](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-kimlik"></a>

**Kimlik doğrulama — Authentication**

Bir aktörün iddia ettiği kimliği doğrulama sürecidir. Başarılı giriş, bütün kayıtlara erişim hakkı vermez (OWASP Foundation, t.y.-a).

[Bkz. Kitap 2, Bölüm 6.4](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-oturum"></a>

**Oturum — Session**

İstekler arasında kullanıcıyla ilişkili durumun izlenmesini sağlar. AI-CRM'in sunucu oturumu örneğinde hesabın devre dışı bırakılması sonraki korumalı istekte değerlendirilir; eski oturum varlığı erişim garantisi değildir.

[Bkz. Bölüm 8.17](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-sentetik-veri"></a>

**Sentetik veri — Synthetic data**

Gerçek kişi veya işlem kaydını temsil etmek zorunda olmayan, örnek veya test amacıyla hazırlanmış veridir. Bu kitapta elle hazırlanmış örnekler de bu adla anılır; gerçek ölçüm yerine sunulmaz.

[Bkz. Kitap 2, Bölüm 7.3](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-7).

<a id="terim-yetki"></a>

**Yetkilendirme — Authorization**

Aktörün belirli kaynağa belirli işlemi yapıp yapamayacağını belirler. AI-CRM'de ekip üyeliği ortak müşteri erişimi sağlayabilir; başkasının kişisel görevini açmaz (OWASP Foundation, t.y.-b).

[Bkz. Kitap 2, Bölüm 6.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-oauth"></a>

**Yetki devri çerçevesi — OAuth**

Bir uygulamanın belirli kaynaklara sınırlı erişim almasını düzenleyen çerçevedir. Kendi başına kullanıcı kimliği doğrulama protokolü diye yorumlanmaz; kapsam ve ilgili kimlik katmanı ayrıca incelenir.

[Bkz. Bölüm 8.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="ek-a-kume-10"></a>

**Yayın, işletim ve SaaS**

<a id="terim-production"></a>

**Canlı kullanım ortamı — Production**

Gerçek kullanıcıya hizmet verilen ortamdır. Yerel laboratuvarın başarılı olması bu ortamın kurulduğunu veya doğrulandığını göstermez; veri, erişim ve işletim sorumlulukları farklıdır.

[Bkz. Kitap 2, Bölüm 8.1](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-deployment"></a>

**Dağıtım — Deployment**

Uygulama çıktısını hedef ortama yerleştirme ve çalıştırma işlemidir. Özelliğin kullanıcılara açılması ayrı bir karar olabilir; başarılı dosya aktarımı bütün yayın doğrulamasını karşılamaz.

[Bkz. Kitap 2, Bölüm 8.14](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-ci"></a>

**Sürekli bütünleştirme (CI) — Continuous integration**

Küçük değişikliklerin ortak kaynakla sık bütünleştirilmesi ve otomatik kontrollerle geri bildirim alınması pratiğidir. Bir CI işlem hattı build ve test gibi kontrolleri yürütür; yalnız zamanlanmış build çalıştırmak bütün pratiği karşılamaz.

[Bkz. Kitap 2, Bölüm 8.17](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-tls"></a>

**Taşıma katmanı güvenliği (TLS) — Transport Layer Security**

Bağlantıda gizlilik ve bütünlük ile ilgili kimlik doğrulama mekanizmalarını sağlar. HTTPS, HTTP iletişimini TLS ile korur. TLS, uygulamanın iş kuralı ve kayıt erişim yetkisini denetlemez (Rescorla, 2018).

[Bkz. Kitap 2, Bölüm 8.11](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="ek-a-kume-11"></a>

**Yapay zekâ, ajanlar ve insan denetimi**

<a id="terim-baglam"></a>

**Bağlam — Context**

Görevi yorumlamak için modele sağlanan ilgili bilgi ve koşullardır. Gereksinim, dosya sürümü ve açık kararlar örnektir. Gereksiz veri eklemek önemli bilgiyi bulmayı zorlaştırabilir.

[Bkz. Bölüm 5.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-baglam-penceresi"></a>

**Bağlam penceresi — Context window**

Modelin belirli işlemde ele alabildiği içerik sınırını anlatır. Sınır token gibi birimlerle ifade edilebilir. İçeriğin pencereye sığması her ayrıntının doğru kullanılacağını garanti etmez.

[Bkz. Bölüm 5.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-llm"></a>

**Büyük dil modeli (LLM) — Large language model**

Dil verileri üzerinde öğrenilmiş örüntülerden yararlanarak metin işleyen ve üreten model ailesidir. Kod üretebilir; belirli API veya yerel dosyanın gerçekten var olduğunu doğrulamadan doğru biliyor sayılmaz.

[Bkz. Bölüm 1.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-1).

<a id="terim-hallucination"></a>

**Dayanaksız üretim — Hallucination**

Modelin yanlış veya dayanağı olmayan içeriği doğruymuş gibi üretmesini anlatır. Var olmayan paket işlevi ya da kaynak göstermek örnektir. Çıktının kendinden emin tonu kanıt değildir.

[Bkz. Bölüm 5.15](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-vibe-coding"></a>

**Sezgisel ve çıktı odaklı kod üretimi — Vibe coding**

Kitapta, doğal dil yönlendirmesi ve görünen sonuç üzerinden hızlı ilerleyen çalışma biçimini tartışmak için kullanılır. Terimin sınırları sabit değildir; kapsamlı mühendislik ve doğrulama yapıldığı varsayılmaz.

[Bkz. Bölüm 1.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-1).

<a id="terim-prompt-engineering"></a>

**Talimat tasarımı — Prompt engineering**

Model girdisini görev ve değerlendirme amacıyla sistemli biçimde düzenleme çalışmasıdır. Doğru gereksinim ve sonuç incelemesinin yerine geçmez; aynı şablon her işte aynı başarıyı sağlamaz.

[Bkz. Bölüm 5.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-prompt"></a>

**Talimat veya istem — Prompt**

Modele verilen görevi, soruyu ve ilgili bilgiyi taşıyan girdidir. Amaç, kısıt ve beklenen çıktı açık olduğunda değerlendirme kolaylaşır. Uzun olması tek başına iyi talimat olduğu anlamına gelmez.

[Bkz. Bölüm 5.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-uretken-yz"></a>

**Üretken yapay zekâ — Generative AI**

Metin, kod veya başka içerik üreten sistemleri anlatır. Üretilen içeriğin akıcı ve ayrıntılı olması doğruluğu, özgünlüğü veya verilen göreve uygunluğu kendiliğinden kanıtlamaz.

[Bkz. Bölüm 1.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-1).

<a id="terim-yz"></a>

**Yapay zekâ (YZ) — Artificial intelligence (AI)**

Algılama, çıkarım veya üretim gibi işlerde kullanılan geniş yöntem ve sistem alanıdır. Kitabın odağı özellikle üretken YZ ile yazılım geliştirmedir; her otomasyon bir dil modeli kullanmaz.

[Bkz. Bölüm 1.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-1).

<a id="terim-ajan"></a>

**YZ ajanı — AI agent**

Bu kitapta araç kullanabilen ve ara sonuçlara göre sonraki eylemi seçebilen sistem için kullanılır. Terimin kullanım alanları değişebilir. Görev, ortam ve yetki sınırı belirtilmelidir (Erik S. ve Zhang, 2024).

[Bkz. Kitap 2, Bölüm 1.17](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

<a id="terim-eval"></a>

**YZ çıktısı değerlendirmesi — Evaluation; eval**

Çıktıyı belirlenmiş örnek ve ölçütlere göre inceleme çalışmasıdır. YZ yanıtının değerlendirilmesi ile üretilen uygulamanın test edilmesi farklı kanıtlardır. Hazırlanmış değerlendirme planı sonuç raporu değildir.

[Bkz. Kitap 2, Bölüm 12.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-12).

<a id="terim-yz-token"></a>

**YZ metin birimi (token) — Token in language models**

Modelin metni işlerken kullandığı parçalama birimidir; her zaman tam sözcük değildir. Güvenlik belirteci veya API anahtarıyla farklı kavramdır. Türkçe sözcük sayısını sabit katsayıyla token sayısına çevirmek güvenilir değildir.

[Bkz. Bölüm 5.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="ek-a-ayrimlar"></a>

**Sık karıştırılan kavramlar**

Aşağıdaki karşılaştırmalar aynı sözcüğün farklı bağlamlarda kullanılmasından veya yakın kavramların birleştirilmesinden doğan hataları önlemek içindir. Özellikle YZ'den öneri alınırken yanıtın hangi anlamı kullandığı açıklaştırılmalıdır.

| Kavramlar | Kitapta korunan ayrım |
|---|---|
| [Kimlik doğrulama](#terim-kimlik) / [yetkilendirme](#terim-yetki) | Aktörün kimliği ile hangi işlemi yapabileceği ayrı sorulardır. |
| [Güvenlik token'ı](#terim-guvenlik-token) / [YZ token'ı](#terim-yz-token) | Erişim akışındaki değer ile metin işleme birimi farklıdır. |
| [İç bağlılık](#terim-baglilik) / [bileşen bağımlılığı](#terim-bagimlilik) | Modül içindeki ortak amaç ile modüller arasındaki değişim etkisi ayrılır. |
| [DIP](#terim-dip) / [DI](#terim-di) | Tasarım ilkesi ile bağımlılığın dışarıdan verilmesi aynı kavram değildir. |
| [MVP](#terim-mvp) / [prototip](#terim-prototip) | Sınırlı ürün kapsamı ile bir soruyu araştıran erken temsil aynı kabul düzeyini taşımaz. |

<a id="ek-a-kisaltmalar"></a>

**Kısaltmalar ve arama adları**

Bir kısaltmanın açılımı, onun projede kullanıldığı veya kurulduğu anlamına gelmez. CD ve token gibi birden fazla anlam taşıyan adlarda bağlam belirtilmelidir.

| Kısaltma veya ad | Başvurulacak madde |
|---|---|
| ACID | [ACID](#terim-acid) |
| ADR | [Mimari karar kaydı (ADR)](#terim-adr) |
| AI / YZ | [Yapay zekâ (YZ)](#terim-yz) |
| API | [Uygulama programlama arayüzü (API)](#terim-api) |
| API key | [API anahtarı](#terim-api-key) |
| CI | [Sürekli bütünleştirme (CI)](#terim-ci) |
| CI/CD | [Sürekli bütünleştirme (CI)](#terim-ci) |
| DI | [Bağımlılık enjeksiyonu (DI)](#terim-di) |
| DIP | [Bağımlılıkların tersine çevrilmesi (DIP)](#terim-dip) |
| DRY | [Tekrarı azaltma ilkesi (DRY)](#terim-dry) |
| Eval | [YZ çıktısı değerlendirmesi](#terim-eval) |
| GraphQL | [GraphQL](#terim-graphql) |
| HTTP | [HTTP](#terim-http) |
| HTTPS / TLS | [Taşıma katmanı güvenliği (TLS)](#terim-tls) |
| ISP | [Arayüz ayrımı ilkesi (ISP)](#terim-isp) |
| JSON | [JSON](#terim-json) |
| KISS | [Basit tutma ilkesi (KISS)](#terim-kiss) |
| LLM | [Büyük dil modeli (LLM)](#terim-llm) |
| LSP | [Liskov yerine geçme ilkesi (LSP)](#terim-lsp) |
| MVC | [Model–görünüm–denetleyici (MVC)](#terim-mvc) |
| MVP | [Asgari uygulanabilir ürün (MVP)](#terim-mvp) |
| OCP | [Açık–kapalı ilkesi (OCP)](#terim-ocp) |
| ORM | [Nesne–ilişkisel eşleme (ORM)](#terim-orm) |
| REST | [REST](#terim-rest) |
| SDLC | [Yazılım geliştirme yaşam döngüsü (SDLC)](#terim-yazilim-yasam-dongusu) |
| SOLID | [SOLID](#terim-solid) |
| SQL | [SQL](#terim-sql) |
| SRP | [Tek sorumluluk ilkesi (SRP)](#terim-srp) |
| YAGNI | [Gerekmeyeni şimdiden yapmama (YAGNI)](#terim-yagni) |

<a id="ek-a-dizin"></a>

**İngilizce–Türkçe dizin**

İngilizce karşılıklar alfabetik sıralanır. Birlikte açıklanan yakın terimler aynı maddeye gider; tarayıcı veya editör araması Türkçe ad ve kısaltmalar için de kullanılabilir.

| İngilizce ad | Türkçe madde |
|---|---|
| Abstraction | [Soyutlama](#terim-soyutlama) |
| Acceptance criterion | [Kabul ölçütü](#terim-kabul-olcutu) |
| Adapter pattern | [Uyarlayıcı deseni](#terim-adapter) |
| Agile | [Çevik yaklaşım](#terim-cevik) |
| AI agent | [YZ ajanı](#terim-ajan) |
| Algorithm | [Algoritma](#terim-algoritma) |
| API key | [API anahtarı](#terim-api-key) |
| Application programming interface | [Uygulama programlama arayüzü (API)](#terim-api) |
| Architecture decision record | [Mimari karar kaydı (ADR)](#terim-adr) |
| Artificial intelligence (AI) | [Yapay zekâ (YZ)](#terim-yz) |
| Atomicity, consistency, isolation, durability | [ACID](#terim-acid) |
| Attribute | [Nitelik](#terim-nitelik) |
| Authentication | [Kimlik doğrulama](#terim-kimlik) |
| Authorization | [Yetkilendirme](#terim-yetki) |
| Availability | [Hizmetin erişilebilirliği](#terim-availability) |
| Backend | [Sunucu tarafı](#terim-backend) |
| Business rule | [İş kuralı](#terim-is-kurali) |
| Class and object | [Sınıf ve nesne](#terim-sinif-nesne) |
| Client | [İstemci](#terim-istemci) |
| Cloud computing | [Bulut bilişim](#terim-bulut) |
| Code smell | [Kod kokusu](#terim-kod-kokusu) |
| Cohesion | [İç bağlılık](#terim-baglilik) |
| Constraint | [Kısıt](#terim-kisit) |
| Context | [Bağlam](#terim-baglam) |
| Context window | [Bağlam penceresi](#terim-baglam-penceresi) |
| Continuous integration | [Sürekli bütünleştirme (CI)](#terim-ci) |
| Coupling | [Bileşenler arası bağımlılık](#terim-bagimlilik) |
| Data integrity | [Veri bütünlüğü](#terim-veri-butunlugu) |
| Database | [Veritabanı](#terim-veritabani) |
| DELETE method | [DELETE](#terim-delete) |
| Dependency injection | [Bağımlılık enjeksiyonu (DI)](#terim-di) |
| Dependency inversion principle | [Bağımlılıkların tersine çevrilmesi (DIP)](#terim-dip) |
| Deployment | [Dağıtım](#terim-deployment) |
| Design pattern | [Tasarım deseni](#terim-desen) |
| DevOps | [Geliştirme ve işletim iş birliği](#terim-devops) |
| Domain name | [Alan adı](#terim-alan-adi) |
| Don't repeat yourself | [Tekrarı azaltma ilkesi (DRY)](#terim-dry) |
| Endpoint | [Uç nokta](#terim-endpoint) |
| Entity | [Varlık](#terim-varlik) |
| Evaluation; eval | [YZ çıktısı değerlendirmesi](#terim-eval) |
| Factory pattern | [Üretici deseni](#terim-factory) |
| Foreign key | [Yabancı anahtar](#terim-yabanci-anahtar) |
| Framework | [Yazılım çatısı](#terim-framework) |
| Frontend | [Kullanıcı arayüzü tarafı](#terim-frontend) |
| Function | [Fonksiyon](#terim-fonksiyon) |
| Functional requirement | [İşlevsel gereksinim](#terim-islevsel-gereksinim) |
| Generative AI | [Üretken yapay zekâ](#terim-uretken-yz) |
| GET method | [GET](#terim-get) |
| Git | [Git](#terim-git) |
| GraphQL | [GraphQL](#terim-graphql) |
| Hallucination | [Dayanaksız üretim](#terim-hallucination) |
| Header and body | [Başlık ve gövde](#terim-baslik-govde) |
| HTTP status code | [HTTP durum kodu](#terim-durum-kodu) |
| Hypertext Transfer Protocol | [HTTP](#terim-http) |
| Idempotency | [İdempotentlik](#terim-idempotency) |
| Index | [İndeks](#terim-indeks) |
| Integration test | [Bütünleşme testi](#terim-butunlesme-test) |
| Interface | [Arayüz](#terim-arayuz) |
| Interface segregation principle | [Arayüz ayrımı ilkesi (ISP)](#terim-isp) |
| Iterative and incremental development | [Yinelemeli ve artımlı geliştirme](#terim-yinelemeli-artimli) |
| JavaScript Object Notation | [JSON](#terim-json) |
| Keep it simple | [Basit tutma ilkesi (KISS)](#terim-kiss) |
| Large language model | [Büyük dil modeli (LLM)](#terim-llm) |
| Library | [Kütüphane](#terim-library) |
| Liskov substitution principle | [Liskov yerine geçme ilkesi (LSP)](#terim-lsp) |
| Microservice | [Mikroservis](#terim-mikroservis) |
| Migration | [Şema veya veri geçişi](#terim-migration) |
| Minimum viable product | [Asgari uygulanabilir ürün (MVP)](#terim-mvp) |
| Model–view–controller | [Model–görünüm–denetleyici (MVC)](#terim-mvc) |
| Modular monolith | [Modüler monolit](#terim-moduler-monolit) |
| Normalization | [Normalizasyon](#terim-normalizasyon) |
| NoSQL databases | [NoSQL](#terim-nosql) |
| OAuth | [Yetki devri çerçevesi](#terim-oauth) |
| Object–relational mapping | [Nesne–ilişkisel eşleme (ORM)](#terim-orm) |
| Observer pattern | [Gözlemci deseni](#terim-observer) |
| Open/closed principle | [Açık–kapalı ilkesi (OCP)](#terim-ocp) |
| PATCH method | [PATCH](#terim-patch) |
| POST method | [POST](#terim-post) |
| Primary key | [Birincil anahtar](#terim-birincil-anahtar) |
| Production | [Canlı kullanım ortamı](#terim-production) |
| Programming language | [Programlama dili](#terim-programlama-dili) |
| Prompt | [Talimat veya istem](#terim-prompt) |
| Prompt engineering | [Talimat tasarımı](#terim-prompt-engineering) |
| Prototype | [Prototip](#terim-prototip) |
| PUT method | [PUT](#terim-put) |
| Quality requirement; non-functional requirement | [Kalite gereksinimi](#terim-kalite-gereksinimi) |
| Rate limiting | [İstek sınırlama](#terim-rate-limit) |
| Refactoring | [Yeniden yapılandırma](#terim-refactoring) |
| Relationship | [İlişki](#terim-iliski) |
| Reliability | [Güvenilirlik](#terim-reliability) |
| Repository pattern | [Veri erişim deseni](#terim-repository-pattern) |
| Representational State Transfer | [REST](#terim-rest) |
| Request and response | [İstek ve yanıt](#terim-istek-yanit) |
| Requirement | [Gereksinim](#terim-gereksinim) |
| Resource | [Kaynak](#terim-kaynak) |
| Scalability | [Ölçeklenebilirlik](#terim-scalability) |
| Schema | [Şema](#terim-sema) |
| Scope creep | [Kapsam kayması](#terim-kapsam-kaymasi) |
| Scrum | [Scrum](#terim-scrum) |
| Secret | [Gizli erişim bilgisi](#terim-secret) |
| Security token | [Güvenlik belirteci](#terim-guvenlik-token) |
| Separation of concerns | [Sorumlulukların ayrılması](#terim-sorumluluk-ayrimi) |
| Server | [Sunucu](#terim-sunucu) |
| Serverless | [Sunucusuz çalıştırma](#terim-serverless) |
| Session | [Oturum](#terim-oturum) |
| Single responsibility principle | [Tek sorumluluk ilkesi (SRP)](#terim-srp) |
| Software development life cycle | [Yazılım geliştirme yaşam döngüsü (SDLC)](#terim-yazilim-yasam-dongusu) |
| Software engineering | [Yazılım mühendisliği](#terim-yazilim-muhendisligi) |
| SOLID principles | [SOLID](#terim-solid) |
| Strategy pattern | [Strateji deseni](#terim-strategy) |
| Structured Query Language | [SQL](#terim-sql) |
| Synthetic data | [Sentetik veri](#terim-sentetik-veri) |
| Table, row and column | [Tablo, satır ve sütun](#terim-tablo) |
| Technical debt | [Teknik borç](#terim-teknik-borc) |
| Token in language models | [YZ metin birimi (token)](#terim-yz-token) |
| Transaction | [Veritabanı işlemi](#terim-islem) |
| Transport Layer Security | [Taşıma katmanı güvenliği (TLS)](#terim-tls) |
| Unit test | [Birim testi](#terim-birim-test) |
| Use case | [Kullanım senaryosu](#terim-kullanim-senaryosu) |
| User story | [Kullanıcı hikâyesi](#terim-kullanici-hikayesi) |
| Vibe coding | [Sezgisel ve çıktı odaklı kod üretimi](#terim-vibe-coding) |
| Webhook | [Olay bildirimi çağrısı](#terim-webhook) |
| You aren't gonna need it | [Gerekmeyeni şimdiden yapmama (YAGNI)](#terim-yagni) |

<a id="ek-a-kaynakca"></a>

**Kaynakça**

Buradaki tarihsiz OWASP kayıtları bu ek içinde başlık sırasına göre a/b ile ayrılmıştır. Yalnız bir Mockapetris eseri kullanıldığından yıl harfi gerekmez; ortak bibliyografyadaki anahtarı `Mockapetris1987Implementation` olarak korunur. Diğer kavramların ayrıntılı dayanakları ilgili bölüm kaynakçalarındadır.

Erik S., & Zhang, B. (2024). [*Building effective agents*](https://www.anthropic.com/engineering/building-effective-agents).

Fielding, R., Nottingham, M., & Reschke, J. (Eds.). (2022). [*HTTP semantics*](https://www.rfc-editor.org/rfc/rfc9110.html). RFC 9110. Internet Engineering Task Force.

Git Project. (t.y.). [*gitglossary*](https://git-scm.com/docs/gitglossary).

GraphQL Foundation. (t.y.). [*Introduction to GraphQL*](https://graphql.org/learn/introduction/).

Gulbrandsen, A., Vixie, P., & Esibov, L. (2000). [*A DNS RR for specifying the location of services (DNS SRV)*](https://www.rfc-editor.org/rfc/rfc2782.html). RFC 2782. Internet Engineering Task Force.

Hallam-Baker, P., Stradling, R., & Hoffman-Andrews, J. (2019). [*DNS certification authority authorization (CAA) resource record*](https://www.rfc-editor.org/rfc/rfc8659.html). RFC 8659. Internet Engineering Task Force.

Mockapetris, P. (1987). [*Domain names—Implementation and specification*](https://www.rfc-editor.org/rfc/rfc1035.html). RFC 1035. Internet Engineering Task Force.

OWASP Foundation. (t.y.-a). [*Authentication cheat sheet*](https://cheatsheetseries.owasp.org/cheatsheets/Authentication_Cheat_Sheet.html).

OWASP Foundation. (t.y.-b). [*Authorization cheat sheet*](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html).

Rescorla, E. (2018). [*The Transport Layer Security (TLS) protocol version 1.3*](https://www.rfc-editor.org/rfc/rfc8446.html). RFC 8446. Internet Engineering Task Force.

Thomson, S., Huitema, C., Ksinant, V., & Souissi, M. (2003). [*DNS extensions to support IP version 6*](https://www.rfc-editor.org/rfc/rfc3596.html). RFC 3596. Internet Engineering Task Force.
