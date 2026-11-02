# Ek A — Terimler Sözlüğü

Bu sözlük Kitap 2 için seçilmiştir; geliştirme ortamı, Git, test, güvenlik, yayın, işletim, SaaS ve YZ ile çalışma konularında 161 terim içerir. Her maddede Türkçe ve İngilizce ad, kısa tanım ve serideki ayrıntılı anlatıma başvuru bulunur. Önceki kitaptan gereken temel tanımlar uygulama sırasında yeniden başvurulabilmesi için ikinci kitapta da yer alır.

Terimler konu kümelerinde sıralanır. İngilizce dizin ve kısaltmalar tablosu aynı maddelere yönlendirir. Projeye özgü FG-01 veya AS-08-01 gibi kayıt kimlikleri Ek F’dedir. Kitap 1, Bölüm 1–13 ilk kitaba, Bölüm 1–13 ikinci kitaba aittir.

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

[Bkz. Kitap 1, Bölüm 9.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="terim-bulut"></a>

**Bulut bilişim — Cloud computing**

İşlem, depolama ve ağ gibi kaynakların hizmet olarak sağlandığı modeldir. Kaynak kullanma biçimini değiştirir; uygulamanın verisini koruma, yapılandırma ve maliyet sorumluluğunu kendiliğinden kaldırmaz.

[Bkz. Bölüm 8.6](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-istemci"></a>

**İstemci — Client**

Başka bir bileşenden hizmet isteyen taraftır. Tarayıcı veya mobil uygulama istemci olabilir. İstemcinin gönderdiği müşteri kimliği, kullanıcının o kayda erişme hakkını tek başına göstermez.

[Bkz. Kitap 1, Bölüm 2.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-json"></a>

**JSON — JavaScript Object Notation**

Nesne, dizi, metin, sayı, mantıksal değer ve null ile veri temsil eden metin biçimidir. JSON içinde tarih için ayrı temel tür yoktur; tarih metninin biçimi API sözleşmesinde belirlenir.

[Bkz. Kitap 1, Bölüm 8.16](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-frontend"></a>

**Kullanıcı arayüzü tarafı — Frontend**

Kullanıcının etkileştiği ekran ve arayüz davranışlarını kapsar. Düğmeyi gizlemek kullanılabilirliği düzenleyebilir; sunucu tarafındaki yetki kontrolünün yerine geçmez.

[Bkz. Kitap 1, Bölüm 2.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-library"></a>

**Kütüphane — Library**

Uygulamanın belirli amaçla çağırdığı hazır işlev veya bileşenler bütünüdür. Çatıyla arasındaki fark yalnız büyüklük değildir; çalışma akışını kimin yönettiği önemlidir. Her yeni kütüphane bakım ve bağımlılık kararıdır.

[Bkz. Kitap 1, Bölüm 6.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-6).

<a id="terim-programlama-dili"></a>

**Programlama dili — Programming language**

Bilgisayarın işleyeceği davranışı belirli sözdizimi ve anlam kurallarıyla ifade etme aracıdır. Doğal dildeki isteğin koda çevrilmesi, istekte eksik olan iş kuralının kendiliğinden kesinleşmesini sağlamaz.

[Bkz. Kitap 1, Bölüm 6.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-6).

<a id="terim-sunucu"></a>

**Sunucu — Server**

İstekleri karşılayıp hizmet sunan yazılımı veya bağlama göre onun çalıştığı bilgisayarı anlatır. “Sunucu kapandı” ifadesinde uygulama süreci, makine ve ağ erişimi ayrı incelenmelidir.

[Bkz. Kitap 1, Bölüm 2.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-backend"></a>

**Sunucu tarafı — Backend**

İş kuralları, veri erişimi ve yetki kontrolleri gibi sorumlulukların yürütüldüğü uygulama tarafıdır. Yalnız veritabanından ibaret değildir; notun yazarını doğrulanmış kullanıcıdan belirlemek de bu tarafta yapılır.

[Bkz. Kitap 1, Bölüm 2.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-api"></a>

**Uygulama programlama arayüzü (API) — Application programming interface**

Yazılım bileşenlerinin hangi işlemleri, girdileri ve sonuçları kullanarak iletişim kuracağını tanımlar. Web API bunun bir türüdür; her API internet üzerinden çalışmaz. AI-CRM'de not eklemenin davranışı API sözleşmesiyle açıklanır.

[Bkz. Kitap 1, Bölüm 8.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-veritabani"></a>

**Veritabanı — Database**

Verilerin düzenli tutulduğu ve belirli yöntemlerle erişildiği yapıdır. Veritabanı yönetim sistemi bu yapıyı yönetir. Ekranda görünen geçici liste, kaydın kalıcı olarak saklandığının tek başına kanıtı değildir.

[Bkz. Kitap 1, Bölüm 7.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-framework"></a>

**Yazılım çatısı — Framework**

Uygulamanın yapısını ve çalışma akışının bir bölümünü düzenleyen altyapıdır. Uygulama kodu çatının belirlediği noktalarda çağrılabilir. Hazır bileşenler, ürünün iş kuralı ve yetki tasarımını tamamlamış sayılmaz.

[Bkz. Kitap 1, Bölüm 6.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-6).

<a id="terim-yazilim-yasam-dongusu"></a>

**Yazılım geliştirme yaşam döngüsü (SDLC) — Software development life cycle**

Gereksinim, tasarım, geliştirme, doğrulama, yayın ve bakım çalışmalarının bütünüdür. Tek yönlü, değişmez bir sıra olmak zorunda değildir; yeni bilgi önceki kararlara dönmeyi gerektirebilir.

[Bkz. Kitap 1, Bölüm 3.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3).

<a id="terim-yazilim-muhendisligi"></a>

**Yazılım mühendisliği — Software engineering**

Yazılımı gereksinimden bakım ve işletime kadar sistemli biçimde geliştirme ve değerlendirme disiplinidir. Kod üretiminin yanında tasarım, doğrulama, maliyet, risk ve değişim sorumluluklarını da kapsar.

[Bkz. Bölüm 13.9](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="ek-a-kume-2"></a>

**Gereksinim, kapsam ve çalışma biçimi**

<a id="terim-mvp"></a>

**Asgari uygulanabilir ürün (MVP) — Minimum viable product**

Belirli kullanıcı ihtiyacını sınamak için seçilmiş sınırlı ama anlamlı ürün kapsamıdır. Temel yetki kontrolleri eksik bir taslakla aynı şey değildir. Kapsamın dar olması doğruluk sorumluluğunu kaldırmaz.

[Bkz. Kitap 1, Bölüm 4.18](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-devops"></a>

**Geliştirme ve işletim iş birliği — DevOps**

Geliştirme ve işletim sorumluluklarının ortak hedef, geri bildirim ve çalışma düzeniyle ele alınmasıdır. Otomasyon bunu destekleyebilir; bir araç veya ekibin adı tek başına DevOps pratiğini oluşturmaz.

[Bkz. Kitap 1, Bölüm 3.16](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-3).

<a id="terim-gereksinim"></a>

**Gereksinim — Requirement**

Sistemin karşılaması gereken ihtiyaç, davranış veya koşuldur. “Güzel ekran” belirsizken, “ekip üyesi müşteri adına göre arama yapabilir” daha sınanabilir bir beklentidir.

[Bkz. Kitap 1, Bölüm 4.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-islevsel-gereksinim"></a>

**İşlevsel gereksinim — Functional requirement**

Sistemin ne yapacağını belirtir. Müşteri oluşturmak veya not eklemek örnektir. Başarı ölçütleri ve hata yolları yazılmadığında işlevin adı tek başına uygulama için yeterli değildir.

[Bkz. Kitap 1, Bölüm 4.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-is-kurali"></a>

**İş kuralı — Business rule**

İş alanında geçerli karar veya sınırlamadır. AI-CRM'de kişisel görevi yalnız sahibinin okuyup tamamlaması bir iş kuralıdır; modelin önerdiği yaygın rol şeması bu kuralı sessizce değiştiremez.

[Bkz. Kitap 1, Bölüm 4.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kabul-olcutu"></a>

**Kabul ölçütü — Acceptance criterion**

Bir sonucun kabul edilebilmesi için sağlanacak gözlenebilir koşuldur. Notun doğru müşteriyle ve doğrulanmış yazarla ilişkilendirilmesi örnektir. Ölçütün yazılması, koşulun gerçek uygulamada sınandığı anlamına gelmez.

[Bkz. Kitap 1, Bölüm 4.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kalite-gereksinimi"></a>

**Kalite gereksinimi — Quality requirement; non-functional requirement**

Performans, güvenlik ve kullanılabilirlik gibi niteliklere ilişkin beklentidir. İşlevsel olmayan gereksinimler bunların yanında kısıtları da içerebilir. “Hızlı olsun” yerine ölçüm koşulu ve kabul sınırı gerekir.

[Bkz. Kitap 1, Bölüm 4.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kapsam-kaymasi"></a>

**Kapsam kayması — Scope creep**

Başlangıçta kararlaştırılan işin etkisi değerlendirilmeden büyümesidir. İlk MVP'ye görev atama veya ödeme eklemek küçük bir arayüz değişikliği sayılmaz; veri ve yetki kararlarını da etkiler.

[Bkz. Kitap 1, Bölüm 4.17](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-kullanim-senaryosu"></a>

**Kullanım senaryosu — Use case**

Bir aktörün hedefe ulaşırken sistemle kurduğu etkileşimi, ön koşulları ve alternatif yolları açıklar. Not kaydında başarı, doğrulama hatası ve sonucu belirsiz istek ayrı yollardır.

[Bkz. Kitap 1, Bölüm 4.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4).

<a id="terim-prototip"></a>

**Prototip — Prototype**

Bir fikir veya etkileşim hakkındaki soruyu araştırmak için hazırlanan erken temsildir. Çalışan ekran, gerçek veri güvenliği ve işletim düzeninin tamamlandığını göstermez.

[Bkz. Bölüm 11.1](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="ek-a-kume-3"></a>

**Veri modeli ve kalıcılık**

<a id="terim-acid"></a>

**ACID — Atomicity, consistency, isolation, durability**

Atomiklik, tutarlılık, yalıtım ve kalıcılık özelliklerini birlikte anan kısaltmadır. İşlemin bütünlüğünü düşünmeye yardım eder. Yalıtım düzeyleri farklı davranışlar gösterebilir; ACID, yedekleme veya uygulama yetkilendirmesinin yerine geçmez.

[Bkz. Kitap 1, Bölüm 7.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-birincil-anahtar"></a>

**Birincil anahtar — Primary key**

Tablodaki her satırı benzersiz belirleyen anahtardır; tek veya birden fazla sütundan oluşabilir. Müşteri adı gibi değişebilir ve yinelenebilir bir alanı kimlikle karıştırmamak gerekir.

[Bkz. Kitap 1, Bölüm 7.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-iliski"></a>

**İlişki — Relationship**

Varlıkların birbirine nasıl bağlandığını anlatır. Bire bir, bire çok ve çoka çok ilişkiler farklı katılım kuralları taşır. Bir müşterinin çok notu bulunması, bu notların tek metin alanında biriktirilmesini gerektirmez.

[Bkz. Kitap 1, Bölüm 7.8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-indeks"></a>

**İndeks — Index**

Belirli veri erişimlerini hızlandırabilen yardımcı yapıdır. Okuma yararı yanında yazma ve depolama maliyeti vardır. Her sütuna indeks eklemek otomatik olarak daha iyi performans sağlamaz.

[Bkz. Kitap 1, Bölüm 7.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-kisit"></a>

**Kısıt — Constraint**

Verinin uyması gereken koşulu uygular. Benzersizlik, boş olamama ve yabancı anahtar örnektir. Form doğrulamasıyla veritabanı kısıtları farklı noktalarda çalışır; biri diğerinin bütün görevlerini üstlenmez.

[Bkz. Kitap 1, Bölüm 7.12](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-orm"></a>

**Nesne–ilişkisel eşleme (ORM) — Object–relational mapping**

Uygulama nesneleriyle ilişkisel veri erişimi arasında eşleme sağlayan yaklaşımdır. Sorgu üretimini kolaylaştırır; sorgu maliyetini, işlem sınırlarını veya kişisel görev sahipliği kontrolünü ortadan kaldırmaz.

[Bkz. Kitap 1, Bölüm 7.25](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-nitelik"></a>

**Nitelik — Attribute**

Bir varlığın özelliğidir. Müşteri adı ve görevin hedef günü örnektir. Kavramsal nitelik veritabanında sütunla temsil edilebilir; kullanıcıdan gelen her alan doğrudan saklanmak zorunda değildir.

[Bkz. Kitap 1, Bölüm 7.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-normalizasyon"></a>

**Normalizasyon — Normalization**

İlişkisel tasarımda bağımlılıkları düzenleyerek gereksiz tekrar ve güncelleme tutarsızlıklarını azaltma yaklaşımıdır. Her ihtiyacın ayrı tablo olması gerektiği anlamına gelmez; veri anlamı ve kullanım birlikte değerlendirilir.

[Bkz. Kitap 1, Bölüm 7.16](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-nosql"></a>

**NoSQL — NoSQL databases**

Belge, anahtar–değer veya graf gibi farklı veri modellerini kullanan veritabanı aileleri için kullanılan genel addır. “Hiç şema veya işlem yoktur” anlamına gelmez; özellikler seçilen sisteme göre incelenir.

[Bkz. Kitap 1, Bölüm 7.18](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-sql"></a>

**SQL — Structured Query Language**

İlişkisel veriyi tanımlamak, sorgulamak ve değiştirmek için kullanılan dildir. Kullanıcı girdisini sorgu metnine birleştirmekle parametre olarak iletmek farklıdır; bu fark SQL enjeksiyonu riskini etkiler.

[Bkz. Kitap 1, Bölüm 7.17](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-sema"></a>

**Şema — Schema**

Verinin yapısını ve ilişkili kuralları tanımlar. Veritabanı şeması ile API'nin istek/yanıt şeması farklı sözleşmelerdir. Bir tablonun bütün sütunlarını dış API'ye açmak zorunlu değildir.

[Bkz. Kitap 1, Bölüm 7.20](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-migration"></a>

**Şema veya veri geçişi — Migration**

Veri yapısını ya da mevcut veriyi sürümler arasında dönüştüren kontrollü değişikliktir. Kodun eski sürümüne dönmek yapılan veri dönüşümünü otomatik geri almaz; uyumluluk ve kurtarma ayrıca planlanır.

[Bkz. Kitap 1, Bölüm 7.21](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-tablo"></a>

**Tablo, satır ve sütun — Table, row and column**

İlişkisel tabloda satır bir kaydı, sütun belirli veri alanını temsil eder. Sütunun türü ve kısıtları izin verilen değerleri etkiler; aynı görünen müşteri adı kayıtların aynı olduğunu göstermez.

[Bkz. Kitap 1, Bölüm 7.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-varlik"></a>

**Varlık — Entity**

İş alanında kimliği ve anlamı bulunan kavramdır. Müşteri ve görev örnektir. Her varlığın mutlaka tek tabloyla temsil edilmesi gerekmez; kavramsal model ile fiziksel saklama tasarımı ayrılır.

[Bkz. Kitap 1, Bölüm 7.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-islem"></a>

**Veritabanı işlemi — Transaction**

Bir veya daha çok veri işleminin belirli bütünlük ve yalıtım kuralları içinde ele alınmasıdır. Birden fazla kaydın tutarlılığını korumaya yardım eder; ağ yanıtının kullanıcıya ulaştığını garanti etmez.

[Bkz. Kitap 1, Bölüm 7.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-veri-butunlugu"></a>

**Veri bütünlüğü — Data integrity**

Verinin belirlenen ilişki ve geçerlilik kurallarını korumasıdır. Var olmayan müşteriye bağlı notun önlenmesi örnektir. Bir kaydın biçimsel olarak geçerli olması, iş açısından doğru veya erişimin yetkili olduğunu kanıtlamaz.

[Bkz. Kitap 1, Bölüm 7.15](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="terim-yabanci-anahtar"></a>

**Yabancı anahtar — Foreign key**

Bir kaydın başka veya aynı tablodaki anahtarla ilişkisini veritabanı düzeyinde kısıtlar. Notun müşteri bağlantısını koruyabilir; notu okuyacak kullanıcının yetkisini kendiliğinden belirlemez.

[Bkz. Kitap 1, Bölüm 7.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7).

<a id="ek-a-kume-4"></a>

**HTTP ve API iletişimi**

<a id="terim-baslik-govde"></a>

**Başlık ve gövde — Header and body**

Başlıklar iletiyle ilgili üst bilgiyi, gövde ise varsa içeriği taşır. JSON gövdesiyle gönderilen iş verisi, kimlik ve yetki kararlarının otomatik olarak güvenilir kaynağı değildir.

[Bkz. Kitap 1, Bölüm 8.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-delete"></a>

**DELETE — DELETE method**

Hedef URI ile onun mevcut işlevi arasındaki ilişkiyi kaldırmayı ister. Fiziksel diskten bütün izlerin silinmesini garanti etmez (Fielding vd., 2022).

[Bkz. Kitap 1, Bölüm 8.11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-get"></a>

**GET — GET method**

Hedef kaynağın temsilini istemek için kullanılır. Semantiği güvenlidir: istemci bir durum değişikliği talep etmez. Günlük yazılması gibi yan etkilerin hiç olmayacağı anlamına gelmez (Fielding vd., 2022).

[Bkz. Kitap 1, Bölüm 8.7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-graphql"></a>

**GraphQL — GraphQL**

API için sorgu dili ve tanımlı tür sistemiyle bu sorguları çalıştırma yaklaşımıdır. İstemci istediği alanları seçebilir; bu seçim erişim yetkisi vermez. AI-CRM'in seçilmiş HTTP/JSON sözleşmesini kendiliğinden değiştirmez (GraphQL Foundation, t.y.).

[Bkz. Kitap 1, Bölüm 8.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-http"></a>

**HTTP — Hypertext Transfer Protocol**

İstemci ve sunucu arasında istek ve yanıt anlamlarını tanımlayan uygulama katmanı protokolüdür. Durum kodu, yöntem ve başlıklar bu anlamın parçalarıdır (Fielding vd., 2022).

[Bkz. Kitap 1, Bölüm 2.9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-durum-kodu"></a>

**HTTP durum kodu — HTTP status code**

İsteğin sonucunu üç basamaklı kodla sınıflandırır. Kod tek başına iş sonucunun bütün ayrıntılarını açıklamaz. AI-CRM'in 400, 403, 404, 409 ve 422 ayrımları kendi API sözleşmesinde tanımlıdır.

[Bkz. Kitap 1, Bölüm 8.12](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-idempotency"></a>

**İdempotentlik — Idempotency**

Aynı isteğin tekrarlanmasının amaçlanan sunucu etkisinin tek isteğinkiyle aynı olmasıdır. Her yanıtın aynı kodu taşıması gerekmez (Fielding vd., 2022). Uygulama tekrar anahtarlarının kapsamı ve saklama süresi ayrıca belirlenir.

[Bkz. Kitap 1, Bölüm 8.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-rate-limit"></a>

**İstek sınırlama — Rate limiting**

Belirli zaman veya kaynak koşulunda istek kullanımını sınırlar. Anahtarın kullanıcı, adres veya başka boyutla tanımlanması etkiyi değiştirir. Kimlik doğrulama ve yetkilendirmenin yerine geçmez.

[Bkz. Kitap 1, Bölüm 8.24](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-istek-yanit"></a>

**İstek ve yanıt — Request and response**

İstek yapılması beklenen işlemi, yanıt ise sunucunun sonucunu taşır. Yanıt alınamaması işlemin hiç yapılmadığını göstermez; AI-CRM not kaydında sonuç belirsiz kalabilir.

[Bkz. Kitap 1, Bölüm 2.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-2).

<a id="terim-kaynak"></a>

**Kaynak — Resource**

API'nin tanımladığı ve üzerinde işlem sunabildiği kavramdır. Müşteri veya görev kaynak olabilir. Kaynak gösterimi, veritabanı satırının bire bir kopyası olmak zorunda değildir.

[Bkz. Kitap 1, Bölüm 8.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-webhook"></a>

**Olay bildirimi çağrısı — Webhook**

Bir olay oluştuğunda başka sistemin belirli adrese istek göndermesiyle kurulan bildirim düzenidir. Teslimler tekrarlanabilir veya sırası değişebilir; alıcı kabul, doğrulama ve işleme durumlarını ayırır.

[Bkz. Kitap 1, Bölüm 8.22](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-patch"></a>

**PATCH — PATCH method**

Kaynağa kısmi değişiklik uygulamak için kullanılır. Tekrar davranışı değişiklik biçimine bağlıdır. AI-CRM görev örneğinde durumu tamamlandıya atamak, her çağrıda durumu tersine çevirmekten farklıdır.

[Bkz. Kitap 1, Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-post"></a>

**POST — POST method**

Gönderilen içeriğin hedef kaynağın kurallarına göre işlenmesini ister. Oluşturma için kullanılabilir; tekrarının etkisi uygulama sözleşmesine bağlıdır (Fielding vd., 2022).

[Bkz. Kitap 1, Bölüm 8.8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-put"></a>

**PUT — PUT method**

Hedef kaynağın durumunu gönderilen temsile göre oluşturma veya değiştirme isteğidir. Amaçlanan etki bakımından idempotenttir; ilk MVP'de sırf bu yöntem var diye müşteri güncelleme işlemi açılmaz (Fielding vd., 2022).

[Bkz. Kitap 1, Bölüm 8.9](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-rest"></a>

**REST — Representational State Transfer**

Kaynaklar, temsiller ve tekbiçimli arayüz gibi kısıtlarla açıklanan mimari yaklaşımdır. Yalnız HTTP üzerinden JSON döndürmek bütün REST kısıtlarını karşıladığını göstermez.

[Bkz. Kitap 1, Bölüm 8.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="terim-endpoint"></a>

**Uç nokta — Endpoint**

API'de bir işlemin erişildiği adres ve kullanım bağlamıdır. HTTP yönteminin de bilinmesi gerekir; aynı yol için okuma ve oluşturma davranışları farklı olabilir.

[Bkz. Kitap 1, Bölüm 8.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8).

<a id="ek-a-kume-5"></a>

**Alan adı ve DNS**

<a id="terim-aaaa"></a>

**AAAA kaydı — AAAA record**

Bir adı IPv6 adresiyle ilişkilendirir. A kaydının dört kez yazılması değil, ayrı DNS kayıt türüdür (Thomson vd., 2003).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-dns"></a>

**Alan Adı Sistemi (DNS) — Domain Name System**

Adlarla ilişkili kayıtları çözümleyen dağıtık sistemdir. Adres, posta ve hizmet bilgileri farklı kayıt türleriyle temsil edilir; DNS, HTTP yönlendirmesiyle aynı işlem değildir (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-a"></a>

**A kaydı — A record**

Bir adı IPv4 adresiyle ilişkilendirir. Web hizmetinin IPv4 üzerinden bulunmasında kullanılır (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-caa"></a>

**CAA kaydı — Certification Authority Authorization record**

Alan adı için hangi sertifika otoritelerinin sertifika düzenleyebileceğine ilişkin politika bildirir. Kendisi TLS sertifikası değildir (Hallam-Baker vd., 2019).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-cname"></a>

**CNAME kaydı — Canonical name record**

Bir takma adı kanonik ada bağlar. IP adresi taşımaz ve tarayıcıya HTTP yönlendirmesi yapmaz (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-mx"></a>

**MX kaydı — Mail exchange record**

Alan adının posta alışveriş sunucularını tercih değerleriyle belirtir. Web uygulamasının HTTP adresini belirlemez (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-ns"></a>

**NS kaydı — Name server record**

Bir DNS bölgesi için yetkili ad sunucusunu belirtir. Uygulama sunucusunun IP adresi kaydı değildir (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-ptr"></a>

**PTR kaydı — Pointer record**

Başka bir alan adına işaret eder; yaygın kullanımı IP adresinden ada ters çözümlemedir (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-soa"></a>

**SOA kaydı — Start of authority record**

Bölgenin yönetim bilgilerini, seri numarasını ve ilgili zamanlama alanlarını taşır (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-srv"></a>

**SRV kaydı — Service record**

Bir hizmetin hedef sunucusunu ve portunu öncelik ve ağırlıkla belirtir. Kullanan istemci ilgili hizmet keşfini desteklemelidir (Gulbrandsen vd., 2000).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-txt"></a>

**TXT kaydı — Text record**

DNS'te metin bilgisi taşır. Alan doğrulama ve e-posta politikaları gibi amaçlarda anlamı ilgili kullanım kuralı belirler (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-ttl"></a>

**Yaşam süresi (TTL) — Time to live**

DNS bağlamında bir kaydın önbellekte tutulabileceği süreyi belirtir. Kayıt türü değildir; değişikliğin tüm istemcilere tek anda ulaştığı garantisini vermez (Mockapetris, 1987).

[Bkz. Bölüm 8.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="ek-a-kume-6"></a>

**Kod, tasarım ve mimari**

<a id="terim-adr"></a>

**Mimari karar kaydı (ADR) — Architecture decision record**

Bir mimari kararın bağlamını, seçeneklerini, gerekçesini ve sonuçlarını saklar. Kararın yazılması uygulanmış olduğunu göstermez. AI-CRM'de mimari tercihlerin sonradan sorgulanmasını kolaylaştırır.

[Bkz. Kitap 1, Bölüm 13.19](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-mvc"></a>

**Model–görünüm–denetleyici (MVC) — Model–view–controller**

Veri/iş davranışı, sunum ve etkileşim denetimini ayıran tasarım düzenidir. Çatılar bu sorumlulukları farklı adlarla sunabilir; adların benzerliği mimarinin bire bir aynı olduğunu kanıtlamaz.

[Bkz. Kitap 1, Bölüm 12.10](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-12).

<a id="terim-moduler-monolit"></a>

**Modüler monolit — Modular monolith**

Tek dağıtım birimi içinde belirgin modül sınırları kurulan mimaridir. Müşteri, not ve görev alanları ayrı sorumluluklar taşıyabilir; ayrı sunuculara dağıtılmaları gerekmez.

[Bkz. Kitap 1, Bölüm 13.6](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13).

<a id="terim-teknik-borc"></a>

**Teknik borç — Technical debt**

Bugünkü tasarım veya uygulama kararlarının gelecekteki değişiklikleri zorlaştıran maliyetini anlatır. Her kusurla aynı şey değildir; borcun etkisi, gerekçesi ve giderme önceliği açıklanmalıdır.

[Bkz. Kitap 1, Bölüm 9.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="terim-refactoring"></a>

**Yeniden yapılandırma — Refactoring**

Gözlenebilir davranışı koruyarak kodun iç yapısını iyileştirmektir. Görevlerin erişim kuralını değiştirmek refactoring diye gizlenemez; davranış değişikliği ayrıca tanımlanır ve doğrulanır.

[Bkz. Kitap 1, Bölüm 9.13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-9).

<a id="ek-a-kume-7"></a>

**Geliştirme ortamı ve sürüm kontrolü**

<a id="terim-merge"></a>

**Birleştirme — Merge**

Farklı gelişim hatlarının değişikliklerini ortak sonuçta birleştirir. Çatışma olmadan tamamlanması, birleşmiş davranışın doğru olduğunu kanıtlamaz (Git Project, t.y.).

[Bkz. Bölüm 2.9](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-merge-conflict"></a>

**Birleştirme çatışması — Merge conflict**

Değişikliklerin otomatik olarak uzlaştırılamadığı durumdur. İşaretleri silmek yeterli değildir; hangi davranışın korunacağı anlaşılmalı ve sonuç doğrulanmalıdır.

[Bkz. Bölüm 2.14](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-ide"></a>

**Bütünleşik geliştirme ortamı (IDE) — Integrated development environment**

Kod düzenleme, hata ayıklama ve proje araçlarını birlikte sunar. IDE'nin uyarısız görünmesi uygulamanın kabul testlerinden geçtiği anlamına gelmez.

[Bkz. Bölüm 1.2](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

<a id="terim-commit"></a>

**Commit — Commit**

Projenin bir durumunu üst bilgisi ve geçmiş bağlantılarıyla kaydeder. Bir commit'in oluşması uzak depoya gönderildiğini veya yayına alındığını göstermez (Git Project, t.y.).

[Bkz. Bölüm 2.6](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-calisma-agaci"></a>

**Çalışma ağacı — Working tree**

Dosyaların üzerinde çalışılan sürümüdür. Kaydedilmiş dosya, sonraki commit'e otomatik olarak dahil edilmiş sayılmaz (Git Project, t.y.).

[Bkz. Bölüm 2.4](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-branch"></a>

**Dal — Branch**

Bir gelişim hattının ucunu izleyen referanstır. Ayrı dal, kendi başına ayrı çalışma dizini ya da güvenlik yalıtımı oluşturmaz (Git Project, t.y.).

[Bkz. Bölüm 2.8](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-pr"></a>

**Değişiklik inceleme isteği — Pull request**

Bir değişiklik kümesini tartışma ve birleştirme amacıyla sunan platform iş akışıdır. Git'in temel nesne türü değildir; açılmış olması kabul edildiği anlamına gelmez.

[Bkz. Bölüm 2.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-tag-release"></a>

**Etiket ve sürüm yayını — Tag and release**

Tag belirli Git nesnesini adlandırır. Release ise dağıtım çıktıları ve notları da içerebilen sürüm sunumudur. Etiketin bulunması gerçek deployment kanıtı değildir.

[Bkz. Bölüm 2.16](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-gelistirme-ortami"></a>

**Geliştirme ortamı — Development environment**

Kodu düzenlemek, çalıştırmak ve incelemek için gereken araç ve yapılandırmaların bütünüdür. Araç adlarının listelenmesi ortamın kurulup birlikte doğrulandığını göstermez.

[Bkz. Bölüm 1.1](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

<a id="terim-git"></a>

**Git — Git**

Kaynak geçmişini yerel ve uzak depolarla izlemeye yarayan dağıtık sürüm kontrol sistemidir. Git ile GitHub aynı şey değildir; yerel commit ağ bağlantısı olmadan da oluşturulabilir.

[Bkz. Bölüm 2.2](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-push-pull"></a>

**Gönderme ve alma — Push and pull**

Push yerel referans güncellemelerini uzak depoya iletir. Pull uzaktan veriyi alıp yapılandırılmış yöntemle yerel dala bütünleştirir. Pull request, pull komutuyla aynı işlem değildir.

[Bkz. Bölüm 2.12](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-index"></a>

**Hazırlama alanı — Staging area; index**

Bir sonraki commit için hazırlanan içeriği temsil eder. Dosyanın tüm değişiklikleri veya seçilmiş parçaları burada farklı durumda olabilir (Git Project, t.y.).

[Bkz. Bölüm 2.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-repo"></a>

**Kaynak deposu — Repository**

Projenin sürüm geçmişi ve ilgili Git verilerinin bulunduğu depodur. Kitap deposu, öğretim laboratuvarı ve gelecekteki uygulama deposu ayrı çalışma bağlamlarıdır.

[Bkz. Bölüm 2.3](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

<a id="terim-ortam-degiskeni"></a>

**Ortam değişkeni — Environment variable**

Bir sürece ortam üzerinden iletilen ad–değer bilgisidir. Yapılandırma taşımak için kullanılabilir; gizli değerin günlükte veya alt süreçte açığa çıkmasını kendiliğinden engellemez.

[Bkz. Bölüm 1.11](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

<a id="terim-paket"></a>

**Paket ve bağımlılık — Package and dependency**

Paket dağıtılabilir yazılım birimidir; bağımlılık başka bileşenin çalışmasına duyulan gereksinimdir. Yeni paket eklemek sürüm, bakım ve güvenlik yükü de getirir.

[Bkz. Bölüm 1.8](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

<a id="terim-terminal"></a>

**Terminal ve komut satırı — Terminal and command line**

Terminal metin etkileşiminin arayüzüdür; komutları kabuk yorumlar. Komut metni, çalışma dizini ve ortam değişkenleri sonucu etkiler. Bir komutun önerilmesi çalıştırıldığı anlamına gelmez.

[Bkz. Bölüm 1.4](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

<a id="ek-a-kume-8"></a>

**Test, hata ayıklama ve kanıt**

<a id="terim-verification"></a>

**Belirtime uygunluk doğrulaması — Verification**

Çıktının tanımlanan gereksinim veya sözleşmeye uygunluğunu değerlendirir. Bu kitapta validation ile ayrımı görünür kılmak için kullanılır; Türkçe kaynaklarda terim karşılıkları değişebilir.

[Bkz. Bölüm 5.2](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-birim-test"></a>

**Birim testi — Unit test**

Dar bir davranış birimini belirlenen sınırlar içinde sınar. Bir iş kuralı fonksiyonunun doğru sonucu, HTTP katmanı ve veritabanının birlikte doğru çalıştığını tek başına kanıtlamaz.

[Bkz. Bölüm 5.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-butunlesme-test"></a>

**Bütünleşme testi — Integration test**

Birden fazla bileşenin birlikte davranışını sınar. Uygulama–veritabanı etkileşimi örnektir. Hangi bileşenlerin gerçek, hangilerinin yerine geçilmiş olduğu raporda açıklanır.

[Bkz. Bölüm 5.6](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-yigin-izi"></a>

**Çağrı yığını izi — Stack trace**

Hata anındaki çağrı zincirine ilişkin bilgi verir. Son görünen satır her zaman sorunun ilk nedeni değildir; girdi, bağlam ve önceki işlemlerle birlikte okunur.

[Bkz. Bölüm 4.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-4).

<a id="terim-kanit"></a>

**Doğrulama kanıtı — Verification evidence**

Belirli sürüm, ortam ve koşulda ne yapıldığını ve sonucunu gösteren kayıttır. Plan, beklenen sonuç ve gerçek sonuç ayrı tutulur; sentetik örneğin hesabı ürün testi değildir.

[Bkz. Bölüm 10.25](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-10).

<a id="terim-hata-ayiklama"></a>

**Hata ayıklama — Debugging**

Gözlenen sorunu yeniden üretip nedenini araştırma ve düzeltmeyi doğrulama sürecidir. Hata mesajını gizlemek veya rastgele kod değiştirmek sorunun giderildiğini göstermez.

[Bkz. Bölüm 4.20](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-4).

<a id="terim-validation"></a>

**İhtiyaca uygunluk geçerlemesi — Validation**

Çözümün amaçlanan kullanıcı ihtiyacını ve kullanım bağlamını karşılayıp karşılamadığını değerlendirir. Yanlış tanımlanmış sözleşmeye kusursuz uyan kod yine de ihtiyacı karşılamayabilir.

[Bkz. Bölüm 5.2](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-kabul-test"></a>

**Kabul testi — Acceptance test**

Ürünün kabul koşullarını karşılayıp karşılamadığını değerlendirir. Her birim testini “kabul testi” diye adlandırmak kullanıcı ihtiyacının doğrulandığını göstermez.

[Bkz. Bölüm 5.8](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-negatif-test"></a>

**Olumsuz senaryo testi — Negative testing**

Geçersiz veya izin verilmeyen koşullarda sistemin doğru reddi ve etkisini sınar. Başkasının kişisel görevini istemek örnektir; yalnız hata kodu değil veri sızıntısı ve kayıt etkisi de incelenir.

[Bkz. Bölüm 5.12](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-regresyon"></a>

**Regresyon testi — Regression test**

Bir değişiklik sonrasında daha önce beklenen davranışların bozulup bozulmadığını araştırır. Yeni görev özelliği eklenirken not akışının korunması örnektir.

[Bkz. Bölüm 5.9](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-sinir-durumu"></a>

**Sınır durum — Edge case**

Olağan örneklerin dışında, kuralın sınırını zorlayan durumdur. Boş not, aynı adlı iki müşteri veya bugün hedefli açık görev farklı sınırları görünür kılar.

[Bkz. Bölüm 5.11](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-smoke"></a>

**Temel çalışırlık testi — Smoke test**

Sistemin temel yollarının çalıştığını kısa ve sınırlı kontrollerle araştırır. Yayın sonrası giriş ve temel okuma örnektir; tüm güvenlik ve kabul kapsamını karşılamaz.

[Bkz. Bölüm 5.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-test-double"></a>

**Testte yerine geçen bileşen — Test double**

Testte gerçek bileşenin yerini alan yardımcıların genel adıdır. Stub hazır yanıt sağlayabilir; mock beklenen etkileşimi denetleyebilir. Bu yardımcıyla başarı gerçek dış hizmetin çalıştığını kanıtlamaz.

[Bkz. Bölüm 5.15](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-kapsama"></a>

**Test kapsamı — Test coverage**

Testlerin hangi kod, koşul veya gereksinimlere ulaştığını belirtilen ölçüte göre gösterir. Yüksek satır kapsamı, beklentilerin doğru olduğu veya bütün iş kurallarının sınandığı anlamına gelmez.

[Bkz. Bölüm 5.13](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="terim-e2e"></a>

**Uçtan uca test — End-to-end test**

Bir kullanıcı veya sistem akışını ilgili uçlar arasında sınar. Her uçtan uca testin gerçek production üzerinde yapılması gerekmez; ortam ve kapsam sonuçla birlikte belirtilir.

[Bkz. Bölüm 5.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

<a id="ek-a-kume-9"></a>

**Güvenlik ve veri sorumluluğu**

<a id="terim-en-az-yetki"></a>

**En az yetki ilkesi — Principle of least privilege**

Aktöre yalnız gereken iş için gerekli erişimi vermeyi önerir. Hata alan YZ aracına yönetici erişimi eklemekten önce görevin ve reddin nedeni incelenir (OWASP Foundation, t.y.-b).

[Bkz. Bölüm 6.19](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-secret"></a>

**Gizli erişim bilgisi — Secret**

Açığa çıkması erişim veya işlem yetkisi verebilen parola, anahtar gibi bilgidir. .env dosyasında bulunması tek başına koruma sağlamaz; paylaşım ve günlük yolları da denetlenir.

[Bkz. Bölüm 6.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-kimlik"></a>

**Kimlik doğrulama — Authentication**

Bir aktörün iddia ettiği kimliği doğrulama sürecidir. Başarılı giriş, bütün kayıtlara erişim hakkı vermez (OWASP Foundation, t.y.-a).

[Bkz. Bölüm 6.4](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-hash"></a>

**Özetleme ve parola özeti — Hashing and password hashing**

Özetleme girdiden özet üretir; şifrelemeyle aynı işlem değildir. Parolalar için genel hızlı özet yeterli sayılmaz; uygun parola özetleme yöntemi ve parametreleri gerekir. Parolanın doğrulanmasını destekler; özgün parolayı geri açma amacı taşımaz.

[Bkz. Bölüm 6.6](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-sentetik-veri"></a>

**Sentetik veri — Synthetic data**

Gerçek kişi veya işlem kaydını temsil etmek zorunda olmayan, örnek veya test amacıyla hazırlanmış veridir. Bu kitapta elle hazırlanmış örnekler de bu adla anılır; gerçek ölçüm yerine sunulmaz.

[Bkz. Bölüm 7.3](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-7).

<a id="terim-xss"></a>

**Siteler arası betik çalıştırma (XSS) — Cross-site scripting**

Güvenilmeyen içeriğin tarayıcıda yürütülebilir içerik olarak yorumlanmasıyla oluşan açık sınıfıdır. Çıktının yerleştiği bağlama uygun kodlama gerekir; girişte genel bir temizlik her bağlamı korumaz.

[Bkz. Bölüm 6.12](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-csrf"></a>

**Siteler arası istek sahteciliği (CSRF) — Cross-site request forgery**

Tarayıcının otomatik eklediği kimlik bilgileriyle istenmeyen işlemin tetiklenmesi riskidir. Sunucu oturumuna dayalı AI-CRM'de CSRF ve yetki kontrolleri farklı sorumluluklar taşır; biri diğerinin yerine geçmez.

[Bkz. Bölüm 6.13](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-sql-injection"></a>

**SQL enjeksiyonu — SQL injection**

Güvenilmeyen girdinin sorgunun veri alanından çıkıp komut anlamını etkilemesidir. Parametreli sorgular veri–komut ayrımına yardım eder; kullanıcının kayıt erişim yetkisi ayrıca kontrol edilir.

[Bkz. Bölüm 6.11](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="terim-veri-minimizasyonu"></a>

**Veri minimizasyonu — Data minimization**

Belirli amaç için gereken veriyle çalışma ilkesidir. Bir YZ incelemesine bütün müşteri arşivi yerine gerekli yapıyı gösteren sentetik örnek vermek kitabın öğretim yaklaşımıdır; hukuki uygunluk incelemesi ayrıca yapılır.

[Bkz. Bölüm 7.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-7).

<a id="terim-lisans"></a>

**Yazılım lisansı — Software license**

Yazılımın kullanım, değişiklik ve dağıtım koşullarını belirleyen izin düzenidir. Kaynağın internette erişilebilir olması sınırsız kullanım izni anlamına gelmez; somut lisans ve kullanım biçimi Bölüm 7'de birlikte değerlendirilir.

[Bkz. Bölüm 7.8](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-7).

<a id="terim-yetki"></a>

**Yetkilendirme — Authorization**

Aktörün belirli kaynağa belirli işlemi yapıp yapamayacağını belirler. AI-CRM'de ekip üyeliği ortak müşteri erişimi sağlayabilir; başkasının kişisel görevini açmaz (OWASP Foundation, t.y.-b).

[Bkz. Bölüm 6.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

<a id="ek-a-kume-10"></a>

**Yayın, işletim ve SaaS**

<a id="terim-background-job"></a>

**Arka plan işi — Background job**

İsteğin doğrudan yanıt yolundan ayrı yürütülen iştir. Hata, tekrar ve kalıcı kabul durumu tasarlanır. İlk MVP için zorunlu ek bileşen değildir.

[Bkz. Bölüm 11.14](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-production"></a>

**Canlı kullanım ortamı — Production**

Gerçek kullanıcıya hizmet verilen ortamdır. Yerel laboratuvarın başarılı olması bu ortamın kurulduğunu veya doğrulandığını göstermez; veri, erişim ve işletim sorumlulukları farklıdır.

[Bkz. Bölüm 8.1](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-multi-tenancy"></a>

**Çok kiracılık — Multi-tenancy**

Bir hizmetin birden fazla tenant'a hizmet vermesidir. Paylaşılan bileşenlerle birlikte veri ve yetki sınırları tasarlanır. İlk tek kurumlu AI-CRM MVP'sine uygulanmış sayılmaz.

[Bkz. Bölüm 11.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-deployment"></a>

**Dağıtım — Deployment**

Uygulama çıktısını hedef ortama yerleştirme ve çalıştırma işlemidir. Özelliğin kullanıcılara açılması ayrı bir karar olabilir; başarılı dosya aktarımı bütün yayın doğrulamasını karşılamaz.

[Bkz. Bölüm 8.14](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-artifact"></a>

**Dağıtım çıktısı — Artifact**

Build veya başka üretim adımında elde edilen, sürümü izlenebilen çıktıdır. Container image veya paket örnektir. Hangi kaynak sürümünden üretildiği ve neyin yayına gittiği ilişkilendirilir.

[Bkz. Bölüm 8.13](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-audit-log"></a>

**Denetim izi — Audit log**

Kim, ne zaman, hangi işlem gibi sorulara cevap vermeyi amaçlayan iz kaydıdır. Genel hata günlüğünden amacı farklıdır; içeriği, erişimi ve korunması ayrıca tasarlanır.

[Bkz. Bölüm 11.19](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-build"></a>

**Derleme veya dağıtım çıktısı hazırlama — Build**

Kaynağı kullanılacak çıktıya dönüştüren hazırlık sürecidir; derleme, paketleme veya statik dosya üretimi içerebilir. Build başarısı, çıktının hedef ortamda yayımlandığını göstermez.

[Bkz. Bölüm 8.13](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-restore"></a>

**Geri yükleme — Restore**

Yedekten veriyi veya gerekli durumu geri kurma işlemidir. Restore testi, geri kurulan sistemin işlev ve bütünlüğünü de değerlendirir. Yalnız yedek komutunun başarılı olması bu kanıtı sağlamaz.

[Bkz. Bölüm 9.8](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9).

<a id="terim-logging"></a>

**Günlükleme — Logging**

Sistemdeki olayları incelemeye uygun kayıtlar hâlinde tutmaktır. Kayıtlar teşhise yardım eder; parola, oturum değeri ve gereksiz müşteri içeriğini günlüğe taşımak yeni risk oluşturur.

[Bkz. Bölüm 9.3](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9).

<a id="terim-tenant"></a>

**Hizmet alan kurum veya kapsam — Tenant**

SaaS bağlamında verisi ve üyelikleri ayrı sınırda ele alınan müşteri kapsamıdır. Kitabın gelecek SaaS taslağında kurumla ilişkilendirilir; tek bir kullanıcıyla aynı şey değildir.

[Bkz. Bölüm 11.6](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-saas"></a>

**Hizmet olarak yazılım (SaaS) — Software as a service**

Yazılım yeteneklerinin hizmet olarak sunulduğu ürün ve işletim modelidir. Yalnız internette açılan prototip değildir; erişim, bakım, destek ve hizmet sorumlulukları da düşünülür.

[Bkz. Bölüm 11.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-incident"></a>

**Hizmet olayı — Incident**

Hizmetin beklenen işleyişini bozan veya acil müdahale gerektiren durumdur. Yönetimi etkiyi sınırlama, iletişim, kurtarma ve sonradan öğrenmeyi kapsar; yalnız kod düzeltmesi değildir.

[Bkz. Bölüm 9.14](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9).

<a id="terim-monitoring"></a>

**İzleme — Monitoring**

Sistemin belirlenmiş göstergelerini izleyip beklenmeyen durumları fark etme çalışmasıdır. Ulaşılabilirlik kontrolü ile doğru iş sonucu farklı sinyallerdir; yeşil panel tüm kullanıcı akışlarının sağlıklı olduğunu göstermez.

[Bkz. Bölüm 9.2](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9).

<a id="terim-container"></a>

**Konteyner — Container**

Uygulamayı süreç ve kaynak yalıtımıyla çalıştırma yaklaşımıdır. Sanal makineyle bire bir aynı değildir; image, çalışan container ve kalıcı veri ayrı kavramlardır.

[Bkz. Bölüm 8.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-image"></a>

**Konteyner imajı — Container image**

Container başlatılırken kullanılan katmanlı dosya sistemi ve çalıştırma bilgisini taşıyan çıktıdır. Image'ın silinmesi veya değiştirilmesi kalıcı verinin güvenli yönetimini kendiliğinden çözmez.

[Bkz. Bölüm 8.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-queue"></a>

**Kuyruk — Queue**

İş veya iletilerin üreticiyle tüketici arasında aktarılmasını düzenler. Teslim ve işleme garantileri kullanılan sisteme ve tasarıma bağlıdır; kuyruğa yazmak işin bittiği anlamına gelmez.

[Bkz. Bölüm 11.15](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-metric"></a>

**Metrik — Metric**

Belirli anlam ve birimle sayısallaştırılmış göstergedir. Hata oranı için payda ve zaman aralığı, gecikme için dağılım önemlidir. Tek ortalama bütün kullanıcı deneyimini açıklamayabilir.

[Bkz. Bölüm 9.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9).

<a id="terim-cache"></a>

**Önbellek — Cache**

Tekrar erişimi kolaylaştırmak için tutulan yeniden üretilebilir veri kopyasıdır. Güncellik ve anahtar kapsamı önemlidir; yanlış tenant anahtarı veri sınırını bozabilir. Ana kayıt kaynağıyla karıştırılmaz.

[Bkz. Bölüm 11.17](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-rollback"></a>

**Önceki sürüme dönüş — Rollback**

Uygulama veya yapılandırmayı önceki duruma döndürme işlemidir. Yeni sürümün değiştirdiği veri kendiliğinden eski hâline gelmeyebilir; migration uyumluluğu ve kurtarma planı ayrıca değerlendirilir.

[Bkz. Bölüm 8.19](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-rbac"></a>

**Rol tabanlı erişim denetimi (RBAC) — Role-based access control**

İzinleri roller üzerinden düzenler. Rol adı tek başına her kaydı açmaz; kurum üyeliği ve kaynak sahipliği gibi koşullar da gerekebilir (OWASP Foundation, t.y.-b).

[Bkz. Bölüm 11.9](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11).

<a id="terim-ci"></a>

**Sürekli bütünleştirme (CI) — Continuous integration**

Küçük değişikliklerin ortak kaynakla sık bütünleştirilmesi ve otomatik kontrollerle geri bildirim alınması pratiğidir. Bir CI işlem hattı build ve test gibi kontrolleri yürütür; yalnız zamanlanmış build çalıştırmak bütün pratiği karşılamaz.

[Bkz. Bölüm 8.17](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-continuous-deployment"></a>

**Sürekli dağıtım — Continuous deployment**

Tanımlı kontrolleri geçen değişikliklerin production'a otomatik aktarılması yaklaşımıdır. Sürekli teslimle aynı anlamda kullanılmamalıdır; “CD” kısaltmasının hangi anlamı taşıdığı belirtilir.

[Bkz. Bölüm 8.17](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-continuous-delivery"></a>

**Sürekli teslim — Continuous delivery**

Değişiklikleri doğrulanmış ve yayımlanmaya hazır durumda tutma yaklaşımıdır. Production'a geçiş ayrı karar veya onay içerebilir; her başarılı değişiklik zorunlu olarak canlıya çıkmaz.

[Bkz. Bölüm 8.17](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-tls"></a>

**Taşıma katmanı güvenliği (TLS) — Transport Layer Security**

Bağlantıda gizlilik ve bütünlük ile ilgili kimlik doğrulama mekanizmalarını sağlar. HTTPS, HTTP iletişimini TLS ile korur. TLS, uygulamanın iş kuralı ve kayıt erişim yetkisini denetlemez (Rescorla, 2018).

[Bkz. Bölüm 8.11](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-staging"></a>

**Yayın öncesi ortam — Staging**

Yayın adayını hedefe benzer koşullarda incelemek için kullanılan ortamdır. Production ile bütün yönlerden aynı olduğu varsayılmaz; veri, trafik ve yapılandırma farkları sonucu etkileyebilir.

[Bkz. Bölüm 8.1](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

<a id="terim-backup"></a>

**Yedekleme — Backup**

Veriyi veya gerekli sistem bilgisini kurtarma amacıyla kopyalama sürecidir. Yedek dosyasının oluşması okunabilir, eksiksiz veya geri yüklenebilir olduğunu tek başına kanıtlamaz.

[Bkz. Bölüm 9.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9).

<a id="ek-a-kume-11"></a>

**Yapay zekâ, ajanlar ve insan denetimi**

<a id="terim-agentic"></a>

**Ajan destekli yazılım mühendisliği — Agentic software engineering**

Yazılım işlerinin bir bölümünde araç kullanan ve ara sonucu değerlendiren ajanlardan yararlanılmasıdır. Bölümün çalışma tanımıdır; görevin devri ürün kararını veya yayın yetkisini otomatik devretmez.

[Bkz. Bölüm 13.4](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="terim-baglam"></a>

**Bağlam — Context**

Görevi yorumlamak için modele sağlanan ilgili bilgi ve koşullardır. Gereksinim, dosya sürümü ve açık kararlar örnektir. Gereksiz veri eklemek önemli bilgiyi bulmayı zorlaştırabilir.

[Bkz. Kitap 1, Bölüm 5.3](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-baglam-penceresi"></a>

**Bağlam penceresi — Context window**

Modelin belirli işlemde ele alabildiği içerik sınırını anlatır. Sınır token gibi birimlerle ifade edilebilir. İçeriğin pencereye sığması her ayrıntının doğru kullanılacağını garanti etmez.

[Bkz. Kitap 1, Bölüm 5.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-llm"></a>

**Büyük dil modeli (LLM) — Large language model**

Dil verileri üzerinde öğrenilmiş örüntülerden yararlanarak metin işleyen ve üreten model ailesidir. Kod üretebilir; belirli API veya yerel dosyanın gerçekten var olduğunu doğrulamadan doğru biliyor sayılmaz.

[Bkz. Kitap 1, Bölüm 1.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-1).

<a id="terim-hallucination"></a>

**Dayanaksız üretim — Hallucination**

Modelin yanlış veya dayanağı olmayan içeriği doğruymuş gibi üretmesini anlatır. Var olmayan paket işlevi ya da kaynak göstermek örnektir. Çıktının kendinden emin tonu kanıt değildir.

[Bkz. Kitap 1, Bölüm 5.15](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-is-akisi"></a>

**İş akışı — Workflow**

İş adımlarının ve aralarındaki geçişlerin düzenidir. Önceden tanımlı kod yolları kullanan akış, sonraki adımı modelin dinamik seçtiği ajan düzeninden ayrılabilir (Erik S. ve Zhang, 2024).

[Bkz. Bölüm 13.4](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="terim-hitl"></a>

**Karar döngüsünde insan — Human-in-the-loop**

Bu kitapta belirli kritik karar veya eylem gerçekleşmeden insan katılımı gereken düzeni anlatır. Onay düğmesinin varlığı, kişinin yeterli bağlamla gerçek inceleme yaptığını tek başına göstermez.

[Bkz. Bölüm 12.12](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-12).

<a id="terim-benchmark"></a>

**Karşılaştırmalı görev ölçümü — Benchmark**

Belirli veri kümesi ve ölçütlerle performansı değerlendiren sınamadır. Sonuç kendi görev kapsamıyla okunur; yüksek puan bütün kullanıcı ihtiyaçları ve işletim koşullarının çözüldüğünü göstermez.

[Bkz. Bölüm 13.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="terim-ozerklik"></a>

**Özerklik — Autonomy**

Bir sistemin belirlenen sınırlar içinde insanın her adımı seçmesine ihtiyaç duymadan eylem gerçekleştirebilmesidir. Dosya düzenleme yetkisi, production verisini değiştirme yetkisiyle aynı düzey değildir.

[Bkz. Bölüm 13.5](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="terim-hotl"></a>

**Süreci gözeten insan — Human-on-the-loop**

Bu kitapta sistem belirli sınırlar içinde çalışırken insanın izleme ve müdahale sorumluluğu taşıdığı düzeni anlatır. Müdahale kanalı ve durma koşulları olmadan yalnız kayıt tutmak yeterli gözetim değildir.

[Bkz. Bölüm 12.13](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-12).

<a id="terim-prompt-injection"></a>

**Talimat enjeksiyonu — Prompt injection**

Güvenilmeyen içerikteki ifadelerin modelin görev veya araç davranışını yönlendirmeye çalışmasıdır. İncelenen hata kaydı yeni yetki kaynağı sayılmaz; araç erişimi ayrıca sınırlandırılır.

[Bkz. Bölüm 13.10](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="terim-prompt-engineering"></a>

**Talimat tasarımı — Prompt engineering**

Model girdisini görev ve değerlendirme amacıyla sistemli biçimde düzenleme çalışmasıdır. Doğru gereksinim ve sonuç incelemesinin yerine geçmez; aynı şablon her işte aynı başarıyı sağlamaz.

[Bkz. Kitap 1, Bölüm 5.2](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-prompt"></a>

**Talimat veya istem — Prompt**

Modele verilen görevi, soruyu ve ilgili bilgiyi taşıyan girdidir. Amaç, kısıt ve beklenen çıktı açık olduğunda değerlendirme kolaylaşır. Uzun olması tek başına iyi talimat olduğu anlamına gelmez.

[Bkz. Kitap 1, Bölüm 5.1](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-uretken-yz"></a>

**Üretken yapay zekâ — Generative AI**

Metin, kod veya başka içerik üreten sistemleri anlatır. Üretilen içeriğin akıcı ve ayrıntılı olması doğruluğu, özgünlüğü veya verilen göreve uygunluğu kendiliğinden kanıtlamaz.

[Bkz. Kitap 1, Bölüm 1.5](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-1).

<a id="terim-yz"></a>

**Yapay zekâ (YZ) — Artificial intelligence (AI)**

Algılama, çıkarım veya üretim gibi işlerde kullanılan geniş yöntem ve sistem alanıdır. Kitabın odağı özellikle üretken YZ ile yazılım geliştirmedir; her otomasyon bir dil modeli kullanmaz.

[Bkz. Kitap 1, Bölüm 1.4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-1).

<a id="terim-ajan"></a>

**YZ ajanı — AI agent**

Bu kitapta araç kullanabilen ve ara sonuçlara göre sonraki eylemi seçebilen sistem için kullanılır. Terimin kullanım alanları değişebilir. Görev, ortam ve yetki sınırı belirtilmelidir (Erik S. ve Zhang, 2024).

[Bkz. Bölüm 1.17](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

<a id="terim-eval"></a>

**YZ çıktısı değerlendirmesi — Evaluation; eval**

Çıktıyı belirlenmiş örnek ve ölçütlere göre inceleme çalışmasıdır. YZ yanıtının değerlendirilmesi ile üretilen uygulamanın test edilmesi farklı kanıtlardır. Hazırlanmış değerlendirme planı sonuç raporu değildir.

[Bkz. Bölüm 12.7](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-12).

<a id="terim-yz-token"></a>

**YZ metin birimi (token) — Token in language models**

Modelin metni işlerken kullandığı parçalama birimidir; her zaman tam sözcük değildir. Güvenlik belirteci veya API anahtarıyla farklı kavramdır. Türkçe sözcük sayısını sabit katsayıyla token sayısına çevirmek güvenilir değildir.

[Bkz. Kitap 1, Bölüm 5.14](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-5).

<a id="terim-ai-native"></a>

**YZ'nin sürece baştan yerleştirilmesi — AI native software development**

Kitapta görev, bağlam, kontrol ve geri bildirim düzeninin YZ kullanımı düşünülerek kurulmasını anlatır. Evrensel standart etiketi olarak kullanılmaz; ürünün müşteri verisini YZ ile işlediğini göstermez.

[Bkz. Bölüm 13.3](../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13).

<a id="ek-a-ayrimlar"></a>

**Sık karıştırılan kavramlar**

Aşağıdaki karşılaştırmalar aynı sözcüğün farklı bağlamlarda kullanılmasından veya yakın kavramların birleştirilmesinden doğan hataları önlemek içindir. Özellikle YZ'den öneri alınırken yanıtın hangi anlamı kullandığı açıklaştırılmalıdır.

| Kavramlar | Kitapta korunan ayrım |
|---|---|
| [Kimlik doğrulama](#terim-kimlik) / [yetkilendirme](#terim-yetki) | Aktörün kimliği ile hangi işlemi yapabileceği ayrı sorulardır. |
| [Verification](#terim-verification) / [validation](#terim-validation) | Belirtime uygunluk ile amaçlanan ihtiyaca uygunluk farklı değerlendirmelerdir. |
| [Sürekli teslim](#terim-continuous-delivery) / [sürekli dağıtım](#terim-continuous-deployment) | Yayına hazır tutmak ile kontroller sonrasında otomatik canlıya almak ayrılır. |
| [Build](#terim-build) / [deployment](#terim-deployment) | Çıktının hazırlanması ile hedef ortama alınması ayrı işlerdir. |
| [Yedekleme](#terim-backup) / [geri yükleme](#terim-restore) | Kopya üretmek ile o kopyadan kullanılabilir durum kurmak farklı kanıt ister. |
| [Rollback](#terim-rollback) / [migration](#terim-migration) | Eski kod sürümüne dönüş, yeni veriyi otomatik geri dönüştürmez. |
| [DNS](#terim-dns) / [HTTP](#terim-http) | Ad çözümleme, HTTP isteğinin yönlendirilmesi değildir. |
| [MVP](#terim-mvp) / [prototip](#terim-prototip) | Sınırlı ürün kapsamı ile bir soruyu araştıran erken temsil aynı kabul düzeyini taşımaz. |
| [İş akışı](#terim-is-akisi) / [ajan](#terim-ajan) | Önceden belirlenmiş yol ile ara sonuca göre dinamik eylem seçimi ayrılır. |
| [YZ değerlendirmesi](#terim-eval) / [ürün testi](#terim-kabul-test) | Model yanıtını incelemek, uygulamanın gerçek davranışını sınamakla aynı kanıt değildir. |

<a id="ek-a-kisaltmalar"></a>

**Kısaltmalar ve arama adları**

Bir kısaltmanın açılımı, onun projede kullanıldığı veya kurulduğu anlamına gelmez. CD ve token gibi birden fazla anlam taşıyan adlarda bağlam belirtilmelidir.

| Kısaltma veya ad | Başvurulacak madde |
|---|---|
| ACID | [ACID](#terim-acid) |
| ADR | [Mimari karar kaydı (ADR)](#terim-adr) |
| AI / YZ | [Yapay zekâ (YZ)](#terim-yz) |
| AI native | [YZ'nin sürece baştan yerleştirilmesi](#terim-ai-native) |
| API | [Uygulama programlama arayüzü (API)](#terim-api) |
| CAA | [CAA kaydı](#terim-caa) |
| CD — delivery | [Sürekli teslim](#terim-continuous-delivery) |
| CD — deployment | [Sürekli dağıtım](#terim-continuous-deployment) |
| CI | [Sürekli bütünleştirme (CI)](#terim-ci) |
| CI/CD | [Sürekli bütünleştirme (CI)](#terim-ci) |
| CNAME | [CNAME kaydı](#terim-cname) |
| CSRF | [Siteler arası istek sahteciliği (CSRF)](#terim-csrf) |
| DNS | [Alan Adı Sistemi (DNS)](#terim-dns) |
| E2E | [Uçtan uca test](#terim-e2e) |
| Eval | [YZ çıktısı değerlendirmesi](#terim-eval) |
| GraphQL | [GraphQL](#terim-graphql) |
| HITL | [Karar döngüsünde insan](#terim-hitl) |
| HOTL | [Süreci gözeten insan](#terim-hotl) |
| HTTP | [HTTP](#terim-http) |
| HTTPS / TLS | [Taşıma katmanı güvenliği (TLS)](#terim-tls) |
| IDE | [Bütünleşik geliştirme ortamı (IDE)](#terim-ide) |
| JSON | [JSON](#terim-json) |
| LLM | [Büyük dil modeli (LLM)](#terim-llm) |
| MVC | [Model–görünüm–denetleyici (MVC)](#terim-mvc) |
| MVP | [Asgari uygulanabilir ürün (MVP)](#terim-mvp) |
| MX | [MX kaydı](#terim-mx) |
| NS | [NS kaydı](#terim-ns) |
| ORM | [Nesne–ilişkisel eşleme (ORM)](#terim-orm) |
| PR | [Değişiklik inceleme isteği](#terim-pr) |
| PTR | [PTR kaydı](#terim-ptr) |
| RBAC | [Rol tabanlı erişim denetimi (RBAC)](#terim-rbac) |
| REST | [REST](#terim-rest) |
| SaaS | [Hizmet olarak yazılım (SaaS)](#terim-saas) |
| SDLC | [Yazılım geliştirme yaşam döngüsü (SDLC)](#terim-yazilim-yasam-dongusu) |
| SOA — DNS kaydı | [SOA kaydı](#terim-soa) |
| SQL | [SQL](#terim-sql) |
| SRV | [SRV kaydı](#terim-srv) |
| TTL | [Yaşam süresi (TTL)](#terim-ttl) |
| TXT | [TXT kaydı](#terim-txt) |
| XSS | [Siteler arası betik çalıştırma (XSS)](#terim-xss) |

<a id="ek-a-dizin"></a>

**İngilizce–Türkçe dizin**

İngilizce karşılıklar alfabetik sıralanır. Birlikte açıklanan yakın terimler aynı maddeye gider; tarayıcı veya editör araması Türkçe ad ve kısaltmalar için de kullanılabilir.

| İngilizce ad | Türkçe madde |
|---|---|
| A record | [A kaydı](#terim-a) |
| AAAA record | [AAAA kaydı](#terim-aaaa) |
| Acceptance criterion | [Kabul ölçütü](#terim-kabul-olcutu) |
| Acceptance test | [Kabul testi](#terim-kabul-test) |
| Agentic software engineering | [Ajan destekli yazılım mühendisliği](#terim-agentic) |
| AI agent | [YZ ajanı](#terim-ajan) |
| AI native software development | [YZ'nin sürece baştan yerleştirilmesi](#terim-ai-native) |
| Algorithm | [Algoritma](#terim-algoritma) |
| Application programming interface | [Uygulama programlama arayüzü (API)](#terim-api) |
| Architecture decision record | [Mimari karar kaydı (ADR)](#terim-adr) |
| Artifact | [Dağıtım çıktısı](#terim-artifact) |
| Artificial intelligence (AI) | [Yapay zekâ (YZ)](#terim-yz) |
| Atomicity, consistency, isolation, durability | [ACID](#terim-acid) |
| Attribute | [Nitelik](#terim-nitelik) |
| Audit log | [Denetim izi](#terim-audit-log) |
| Authentication | [Kimlik doğrulama](#terim-kimlik) |
| Authorization | [Yetkilendirme](#terim-yetki) |
| Autonomy | [Özerklik](#terim-ozerklik) |
| Backend | [Sunucu tarafı](#terim-backend) |
| Background job | [Arka plan işi](#terim-background-job) |
| Backup | [Yedekleme](#terim-backup) |
| Benchmark | [Karşılaştırmalı görev ölçümü](#terim-benchmark) |
| Branch | [Dal](#terim-branch) |
| Build | [Derleme veya dağıtım çıktısı hazırlama](#terim-build) |
| Business rule | [İş kuralı](#terim-is-kurali) |
| Cache | [Önbellek](#terim-cache) |
| Canonical name record | [CNAME kaydı](#terim-cname) |
| Certification Authority Authorization record | [CAA kaydı](#terim-caa) |
| Client | [İstemci](#terim-istemci) |
| Cloud computing | [Bulut bilişim](#terim-bulut) |
| Commit | [Commit](#terim-commit) |
| Constraint | [Kısıt](#terim-kisit) |
| Container | [Konteyner](#terim-container) |
| Container image | [Konteyner imajı](#terim-image) |
| Context | [Bağlam](#terim-baglam) |
| Context window | [Bağlam penceresi](#terim-baglam-penceresi) |
| Continuous delivery | [Sürekli teslim](#terim-continuous-delivery) |
| Continuous deployment | [Sürekli dağıtım](#terim-continuous-deployment) |
| Continuous integration | [Sürekli bütünleştirme (CI)](#terim-ci) |
| Cross-site request forgery | [Siteler arası istek sahteciliği (CSRF)](#terim-csrf) |
| Cross-site scripting | [Siteler arası betik çalıştırma (XSS)](#terim-xss) |
| Data integrity | [Veri bütünlüğü](#terim-veri-butunlugu) |
| Data minimization | [Veri minimizasyonu](#terim-veri-minimizasyonu) |
| Database | [Veritabanı](#terim-veritabani) |
| Debugging | [Hata ayıklama](#terim-hata-ayiklama) |
| DELETE method | [DELETE](#terim-delete) |
| Deployment | [Dağıtım](#terim-deployment) |
| Development environment | [Geliştirme ortamı](#terim-gelistirme-ortami) |
| DevOps | [Geliştirme ve işletim iş birliği](#terim-devops) |
| Domain Name System | [Alan Adı Sistemi (DNS)](#terim-dns) |
| Edge case | [Sınır durum](#terim-sinir-durumu) |
| End-to-end test | [Uçtan uca test](#terim-e2e) |
| Endpoint | [Uç nokta](#terim-endpoint) |
| Entity | [Varlık](#terim-varlik) |
| Environment variable | [Ortam değişkeni](#terim-ortam-degiskeni) |
| Evaluation; eval | [YZ çıktısı değerlendirmesi](#terim-eval) |
| Foreign key | [Yabancı anahtar](#terim-yabanci-anahtar) |
| Framework | [Yazılım çatısı](#terim-framework) |
| Frontend | [Kullanıcı arayüzü tarafı](#terim-frontend) |
| Functional requirement | [İşlevsel gereksinim](#terim-islevsel-gereksinim) |
| Generative AI | [Üretken yapay zekâ](#terim-uretken-yz) |
| GET method | [GET](#terim-get) |
| Git | [Git](#terim-git) |
| GraphQL | [GraphQL](#terim-graphql) |
| Hallucination | [Dayanaksız üretim](#terim-hallucination) |
| Hashing and password hashing | [Özetleme ve parola özeti](#terim-hash) |
| Header and body | [Başlık ve gövde](#terim-baslik-govde) |
| HTTP status code | [HTTP durum kodu](#terim-durum-kodu) |
| Human-in-the-loop | [Karar döngüsünde insan](#terim-hitl) |
| Human-on-the-loop | [Süreci gözeten insan](#terim-hotl) |
| Hypertext Transfer Protocol | [HTTP](#terim-http) |
| Idempotency | [İdempotentlik](#terim-idempotency) |
| Incident | [Hizmet olayı](#terim-incident) |
| Index | [İndeks](#terim-indeks) |
| Integrated development environment | [Bütünleşik geliştirme ortamı (IDE)](#terim-ide) |
| Integration test | [Bütünleşme testi](#terim-butunlesme-test) |
| JavaScript Object Notation | [JSON](#terim-json) |
| Large language model | [Büyük dil modeli (LLM)](#terim-llm) |
| Library | [Kütüphane](#terim-library) |
| Logging | [Günlükleme](#terim-logging) |
| Mail exchange record | [MX kaydı](#terim-mx) |
| Merge | [Birleştirme](#terim-merge) |
| Merge conflict | [Birleştirme çatışması](#terim-merge-conflict) |
| Metric | [Metrik](#terim-metric) |
| Migration | [Şema veya veri geçişi](#terim-migration) |
| Minimum viable product | [Asgari uygulanabilir ürün (MVP)](#terim-mvp) |
| Model–view–controller | [Model–görünüm–denetleyici (MVC)](#terim-mvc) |
| Modular monolith | [Modüler monolit](#terim-moduler-monolit) |
| Monitoring | [İzleme](#terim-monitoring) |
| Multi-tenancy | [Çok kiracılık](#terim-multi-tenancy) |
| Name server record | [NS kaydı](#terim-ns) |
| Negative testing | [Olumsuz senaryo testi](#terim-negatif-test) |
| Normalization | [Normalizasyon](#terim-normalizasyon) |
| NoSQL databases | [NoSQL](#terim-nosql) |
| Object–relational mapping | [Nesne–ilişkisel eşleme (ORM)](#terim-orm) |
| Package and dependency | [Paket ve bağımlılık](#terim-paket) |
| PATCH method | [PATCH](#terim-patch) |
| Pointer record | [PTR kaydı](#terim-ptr) |
| POST method | [POST](#terim-post) |
| Primary key | [Birincil anahtar](#terim-birincil-anahtar) |
| Principle of least privilege | [En az yetki ilkesi](#terim-en-az-yetki) |
| Production | [Canlı kullanım ortamı](#terim-production) |
| Programming language | [Programlama dili](#terim-programlama-dili) |
| Prompt | [Talimat veya istem](#terim-prompt) |
| Prompt engineering | [Talimat tasarımı](#terim-prompt-engineering) |
| Prompt injection | [Talimat enjeksiyonu](#terim-prompt-injection) |
| Prototype | [Prototip](#terim-prototip) |
| Pull request | [Değişiklik inceleme isteği](#terim-pr) |
| Push and pull | [Gönderme ve alma](#terim-push-pull) |
| PUT method | [PUT](#terim-put) |
| Quality requirement; non-functional requirement | [Kalite gereksinimi](#terim-kalite-gereksinimi) |
| Queue | [Kuyruk](#terim-queue) |
| Rate limiting | [İstek sınırlama](#terim-rate-limit) |
| Refactoring | [Yeniden yapılandırma](#terim-refactoring) |
| Regression test | [Regresyon testi](#terim-regresyon) |
| Relationship | [İlişki](#terim-iliski) |
| Repository | [Kaynak deposu](#terim-repo) |
| Representational State Transfer | [REST](#terim-rest) |
| Request and response | [İstek ve yanıt](#terim-istek-yanit) |
| Requirement | [Gereksinim](#terim-gereksinim) |
| Resource | [Kaynak](#terim-kaynak) |
| Restore | [Geri yükleme](#terim-restore) |
| Role-based access control | [Rol tabanlı erişim denetimi (RBAC)](#terim-rbac) |
| Rollback | [Önceki sürüme dönüş](#terim-rollback) |
| Schema | [Şema](#terim-sema) |
| Scope creep | [Kapsam kayması](#terim-kapsam-kaymasi) |
| Secret | [Gizli erişim bilgisi](#terim-secret) |
| Server | [Sunucu](#terim-sunucu) |
| Service record | [SRV kaydı](#terim-srv) |
| Smoke test | [Temel çalışırlık testi](#terim-smoke) |
| Software as a service | [Hizmet olarak yazılım (SaaS)](#terim-saas) |
| Software development life cycle | [Yazılım geliştirme yaşam döngüsü (SDLC)](#terim-yazilim-yasam-dongusu) |
| Software engineering | [Yazılım mühendisliği](#terim-yazilim-muhendisligi) |
| Software license | [Yazılım lisansı](#terim-lisans) |
| SQL injection | [SQL enjeksiyonu](#terim-sql-injection) |
| Stack trace | [Çağrı yığını izi](#terim-yigin-izi) |
| Staging | [Yayın öncesi ortam](#terim-staging) |
| Staging area; index | [Hazırlama alanı](#terim-index) |
| Start of authority record | [SOA kaydı](#terim-soa) |
| Structured Query Language | [SQL](#terim-sql) |
| Synthetic data | [Sentetik veri](#terim-sentetik-veri) |
| Table, row and column | [Tablo, satır ve sütun](#terim-tablo) |
| Tag and release | [Etiket ve sürüm yayını](#terim-tag-release) |
| Technical debt | [Teknik borç](#terim-teknik-borc) |
| Tenant | [Hizmet alan kurum veya kapsam](#terim-tenant) |
| Terminal and command line | [Terminal ve komut satırı](#terim-terminal) |
| Test coverage | [Test kapsamı](#terim-kapsama) |
| Test double | [Testte yerine geçen bileşen](#terim-test-double) |
| Text record | [TXT kaydı](#terim-txt) |
| Time to live | [Yaşam süresi (TTL)](#terim-ttl) |
| Token in language models | [YZ metin birimi (token)](#terim-yz-token) |
| Transaction | [Veritabanı işlemi](#terim-islem) |
| Transport Layer Security | [Taşıma katmanı güvenliği (TLS)](#terim-tls) |
| Unit test | [Birim testi](#terim-birim-test) |
| Use case | [Kullanım senaryosu](#terim-kullanim-senaryosu) |
| Validation | [İhtiyaca uygunluk geçerlemesi](#terim-validation) |
| Verification | [Belirtime uygunluk doğrulaması](#terim-verification) |
| Verification evidence | [Doğrulama kanıtı](#terim-kanit) |
| Webhook | [Olay bildirimi çağrısı](#terim-webhook) |
| Workflow | [İş akışı](#terim-is-akisi) |
| Working tree | [Çalışma ağacı](#terim-calisma-agaci) |

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
