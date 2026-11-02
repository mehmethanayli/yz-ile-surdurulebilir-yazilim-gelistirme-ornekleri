# Ek D — Önerilen Kaynaklar

Kitap 1 için 12 kaynak seçilmiştir. Okuma sırası gereksinimden veri modeline, kod tasarımına ve mimari kararlara uzanır. Talimat hazırlama ve davranış sözleşmeleri için iki tamamlayıcı kaynak bulunur.

K-D kimlikleri seri genelinde korunur. İki kitapta bulunan bir kaynak aynı kimliği taşır. Başlık altındaki okuma önerileri kaynağın kapsamını ve AI-CRM’de nasıl kullanılabileceğini açıklar. Kaynaklar İngilizcedir; ticari kitaplarda açık tanıtım ve örnek sayfalarına bağlantı verilmiştir. Açık kaynaklarla başlanabilir; satın alma zorunluluğu yoktur.

Yayın ve bağlantı bilgileri ortak kaynak rehberinin 6 Ekim 2026 tarihli incelemesinden alınmıştır. Bu ayrıştırmada web kaynakları yeniden kontrol edilmemiştir. Kaynak okumak, uygulama veya test sonucu oluşturmaz; proje kararı ve gerçek kanıt ayrı kaydedilir.

**İçindekiler**

- [D.1. Yazılım Mühendisliği](#ek-d-1)
- [D.2. Yazılım Mimarisi](#ek-d-2)
- [D.3. Temiz Kod ve Refactoring](#ek-d-3)
- [D.4. Tasarım Desenleri](#ek-d-4)
- [D.5. Veritabanı Tasarımı](#ek-d-5)
- [D.9. Yapay Zekâ Destekli Yazılım Geliştirme](#ek-d-9)
- [D.10. İleri Okumalar](#ek-d-10)
- [Okuma notunu çalışmaya dönüştürmek](#ek-d-okuma-notu)
- [Kaynakça](#ek-d-kaynakca)

<a id="ek-d-1"></a>

**D.1. Yazılım Mühendisliği**

**K-D01 — SWEBOK Guide, v4.0a**

**Kaynak ve erişim:** Washizaki'nin (2026) editörlüğündeki [SWEBOK Guide](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf), IEEE Computer Society tarafından sunulan ücretsiz PDF'dir. Seçilen dosyanın kapağı Ağustos 2026 sürümünü belirtir; v4.0 ile v4.0a aynı kayıt olarak kullanılmamalıdır.

**Nasıl okunmalı?** Temel yaşam döngüsü kavramlarını bilmek yeterlidir. İlk okumada gereksinimler bilgi alanındaki gereksinim türleri, kabul ölçütleri, doğrulama ve izlenebilirlik başlıklarına odaklanın. Rehber bir programlama öğreticisi değil, konular arasında yön bulma kaynağıdır. Her bilgi alanını aynı ayrıntıda okumak başlangıç için gerekli değildir.

AI-CRM'de “müşteriye not ekleme” isteğini işlevsel gereksinim, yetki sınırı ve kabul ölçütü olarak ayırmak için kullanın. Rehberden bir kavramın adını almak, projenin kararını vermek değildir; notun kime ait sayılacağı gibi kurallar kitapta tanımlanan kapsamdan gelir.

**K-D02 — Software Engineering at Google**

**Kaynak ve erişim:** Winters ve diğerlerinin (2020) hazırladığı [Software Engineering at Google](https://abseil.io/resources/swe-book), Abseil üzerinden ücretsiz HTML olarak okunabilir; basılı sürümü de vardır.

**Nasıl okunmalı?** Küçük bir kod tabanını okuma ve değiştirme deneyimi yararlıdır. Başlangıçta yazılım mühendisliğinin ne olduğu sorusunu ele alan açılış kısmını, ardından o anki ihtiyaca göre kod inceleme veya test konularını seçin. Kaynağın odağı kodun zaman içinde sürdürülebilmesi ve mühendislik uygulamalarıdır; bir dilin sözdizimini öğretmek değildir.

Google ölçeğindeki bir uygulamayı küçük ekibe doğrudan taşımadan önce hangi sorunu çözdüğünü yazın. AI-CRM için yararlı çıktı, her araç ve rolü kopyalamak değil, bir değişikliğin gerekçesini başka geliştiricinin anlayabileceği kısa inceleme kaydıdır. Bu uyarlama, kitabımızın küçük ekip bağlamına yönelik çalışma önerisidir.

<a id="ek-d-2"></a>

**D.2. Yazılım Mimarisi**

**K-D03 — Software Architecture Guide**

**Kaynak ve erişim:** Fowler'ın (2019) [Software Architecture Guide](https://martinfowler.com/architecture/) sayfası, ücretsiz bir açıklama ve konu rehberidir. Sayfadaki ayrı makalelerin yazar ve tarihleri rehberinkinden farklı olabilir.

**Nasıl okunmalı?** HTTP isteğinin uygulama ve veritabanı boyunca izlediği yolu bilmek yararlıdır. Önce mimarinin anlamı ve önemi, sonra uygulama mimarisi kısmını okuyun. Rehber, önemli tasarım kararlarını değişim ve bakım bağlamında düşünmeye yardım eder. Listelenen bütün mimari yaklaşımlar aynı projede uygulanacak bileşenler değildir.

AI-CRM için müşteri, not ve kişisel görev sorumluluklarının sınırını açıklayan bir paragraf yazın. Mikroservis gibi bir seçenekle karşılaştığınızda, mevcut küçük ekip ve tek kurum kapsamındaki somut ihtiyacı belirtmeden öneriyi karara dönüştürmeyin. Bir mimari adını kullanmak, erişim kurallarının nerede uygulandığını açıklamaz.

**K-D04 — Documenting Architecture Decisions**

**Kaynak ve erişim:** Nygard'ın (2011) [Documenting Architecture Decisions](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions) yazısı ücretsizdir.

**Nasıl okunmalı?** Biçimsel mimari bilgisi gerekmez; üzerinde karar verilecek bir problem bulunmalıdır. Bağlam, karar, durum ve sonuçlar alanlarını birlikte okuyun. Metin, tek önemli kararın küçük bir kayıtla açıklanmasını ve değiştirilen kararın geçmişinin korunmasını önerir. Sonuçlara yalnız yararlar değil, yükler ve sınırlamalar da girer.

AI-CRM'de aynı kökenli HTTP/JSON ve sunucu oturumu tercihinin nedenlerini açıklamak için mevcut ADR kaydını inceleyin. Önerilen karar ile kabul edilen kararı ayırın. YZ'nin makul görünen bir gerekçe üretmesi, ekibin o kararı geçmişte gerçekten verdiğini kanıtlamaz; sonradan üretilen açıklama, tarihsel kayıt gibi sunulmamalıdır.

<a id="ek-d-3"></a>

**D.3. Temiz Kod ve Refactoring**

**K-D05 — Refactoring: Improving the Design of Existing Code, 2. baskı**

**Kaynak ve erişim:** Fowler'ın (2018) [Refactoring kitabının yazar sayfası](https://martinfowler.com/books/refactoring.html) açıklama, katalog ve açılış bölümü bağlantıları sunar. Tam kitap ticari yayındır. İkinci baskının yayın yılı 2018, yayınevinin belirttiği telif yılı 2019'dur; burada yayın yılı kullanılmıştır.

**Nasıl okunmalı?** Fonksiyon, koşul, veri yapısı ve temel test bilgisi gerekir. Açılış örneği, refactoring ilkeleri ve testin rolüyle başlayın; bütün dönüşüm kataloğunu ezberlemeye çalışmayın. Kaynağın temel yaklaşımı, gözlemlenebilir davranışı koruyan küçük dönüşümlerdir.

AI-CRM'de not doğrulamasını daha anlaşılır bir işleve ayırma önerisini inceleyin. Boş notun reddedilmesi veya yazarın doğrulanmış kullanıcıdan alınması değişiyorsa, iş yalnız refactoring olarak adlandırılamaz. YZ'den önce korunacak davranışları, sonra her küçük değişikliğin etkisini açıklamasını isteyin.

**K-D06 — What to Look for in a Code Review**

**Kaynak ve erişim:** Google'ın (t.y.) [kod inceleme rehberi](https://google.github.io/eng-practices/review/reviewer/looking-for.html) ücretsizdir.

**Nasıl okunmalı?** Bir değişiklik farkını okuyabilmek yeterlidir. Tasarım, işlevsellik, karmaşıklık ve test kısımlarını birlikte ele alın; yalnız adlandırma ve biçimlendirmeyle sınırlamayın. Rehber, gereksiz genelleştirmeleri ve testlerin gerçekten anlamlı olup olmadığını da inceleme konusu yapar.

AI-CRM değişikliğinde “bu isim hoşuma gitmedi” ile “bu sorgu başkasının görevini döndürüyor” aynı ağırlıkta bulgu değildir. Kaynağı, bulgunun davranışa etkisini ve dayanağını yazmak için kullanın. YZ tarafından üretilen inceleme yorumunu da kaynak kodla karşılaştırın; satır veya çağrı uyduran bir yorum, teknik görünse bile kabul edilmez.

<a id="ek-d-4"></a>

**D.4. Tasarım Desenleri**

**K-D07 — Design Patterns: Elements of Reusable Object-Oriented Software**

**Kaynak ve erişim:** Gamma ve diğerlerinin (1994) [Design Patterns kitabının yayınevi sayfası](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-software-9780201633610), açık açıklama ve örnek içerik bağlantıları sunar; tam kitap ticari yayındır. Yayınevi yayın tarihini 1994, telif yılını 1995 olarak gösterir.

**Nasıl okunmalı?** Nesne, arayüz, bileşim ve kalıtım bilgisi gerekir. Önce desenin amaç, uygulanabilirlik ve sonuçlarının nasıl anlatıldığını inceleyin; ardından Bölüm 12'de karşılaştığınız tek deseni seçin. Kitaptaki C++ ve Smalltalk örnekleri, Python projesine satır satır aktarılacak güncel çatı kodu değildir.

AI-CRM'de değişmesi beklenmeyen tek bir işlemi sırf bir desen göstermek için karmaşıklaştırmayın. Desenli öneriyi doğrudan fonksiyonla çözülen seçenekle karşılaştırın. Çalışmanın çıktısı, desenin adı kadar onu kullanmama gerekçesini de içerebilir.

**K-D08 — Inversion of Control Containers and the Dependency Injection Pattern**

**Kaynak ve erişim:** Fowler'ın (2004) [bağımlılık aktarımı yazısı](https://martinfowler.com/articles/injection.html) ücretsizdir. Metin tarihsel Java örnekleri içerir.

**Nasıl okunmalı?** Bir nesnenin başka bir bileşeni çağırması ve bağımlılığın ne olduğu bilinmelidir. Önce basit örneği ve bağımlılık aktarımı biçimlerini, sonra yapılandırmanın kullanımdan ayrılması tartışmasını okuyun. Metindeki araç adlarını bugünün zorunlu kurulum listesine çevirmeyin.

AI-CRM'de test sırasında bir bağımlılığın kontrollü karşılıkla nasıl değiştirilebileceğini düşünün. Bunun için mutlaka bir DI container kurmak gerektiğini varsaymayın. YZ'den bileşenin neyi bildiğini ve bağımlılığı kimin sağladığını açıklamasını isteyin; açıklama gerçek çağrı ve veri akışıyla eşleşmelidir.

<a id="ek-d-5"></a>

**D.5. Veritabanı Tasarımı**

**K-D09 — PostgreSQL 18 Tutorial**

**Kaynak ve erişim:** PostgreSQL Global Development Group'un (t.y.-b) [PostgreSQL 18 öğreticisi](https://www.postgresql.org/docs/18/tutorial.html) ücretsizdir ve sürüm bağlantısı açıktır.

**Nasıl okunmalı?** Genel bilgisayar kullanımı yeterlidir; SQL'e yeni başlayanlar için uygundur. Tablo oluşturma, satır sorgulama ve tabloları birleştirme konularından başlayın; sonra yabancı anahtar ve transaction başlıklarına geçin. Öğretici giriş niteliğindedir, tüm SQL davranışlarının ayrıntılı başvuru kaynağı değildir.

AI-CRM'in müşteri ve not ilişkisini küçük, sentetik verilerle kâğıt üzerinde kurun. Hangi sütunun hangi varlığa ait olduğunu ve birleşim sonucunda hangi satırların beklendiğini yazın. Ürün kapsamı bir silme işlemi içermiyorsa, öğreticide silme komutunun bulunması o özelliği uygulamaya ekleme gerekçesi olmaz.

**K-D10 — PostgreSQL Constraints**

**Kaynak ve erişim:** PostgreSQL Global Development Group'un (t.y.-a) [Constraints belgesi](https://www.postgresql.org/docs/18/ddl-constraints.html) ücretsizdir; burada 18 sürümü esas alınmıştır.

**Nasıl okunmalı?** Tablo, anahtar ve `NULL` kavramları bilinmelidir. `NOT NULL`, `CHECK`, birincil ve yabancı anahtar başlıklarıyla başlayın. Özellikle `CHECK` ifadesinin `NULL` sonucuyla sağlanmış sayılabilmesini ve başka satırlara bağlı kurallar için sınırlarını inceleyin. Sütun türü tek başına bütün iş kurallarını korumaz.

AI-CRM'de bir notun geçerli müşteriye bağlanması ile o notu hangi kullanıcının ekleyebileceğini ayırın. Yabancı anahtar ilişki bütünlüğüne yardım eder; uygulamanın nesneye erişim yetkisini kendiliğinden kanıtlamaz. YZ'nin önerdiği her kısıt için hangi geçersiz veriyi engellediğini ve hangi kuralı kapsamadığını yazın.

<a id="ek-d-9"></a>

**D.9. Yapay Zekâ Destekli Yazılım Geliştirme**

**K-D17 — Prompt Engineering**

**Kaynak ve erişim:** OpenAI'nin (t.y.) [talimat hazırlama rehberi](https://developers.openai.com/api/docs/guides/prompt-engineering) ücretsizdir. Okuma için API hesabı veya ücretli model çağrısı gerekmez.

**Nasıl okunmalı?** Görev, bağlam ve beklenen çıktı kavramları yeterlidir; kod örnekleri için temel API bilgisi yararlıdır. Açık talimat, ilgili bağlam, örnekler ve değerlendirme ihtiyacı üzerine kısımlarla başlayın. Rehber sağlayıcıya özgü API ayrıntıları da içerir; model adları ve arayüz örnekleri kalıcı mühendislik ilkeleriyle aynı şekilde ele alınmamalıdır.

[Ek C](ek-c-yapilandirilmis-ai-talimatlari.md) içinden bir talimat seçerek beklenen çıktıyı ve kanıt sınırını netleştirin. Rehberdeki teknikleri uygulamak doğruluğu garanti etmez. Müşteri verisini modele aktarmayı gerektirmeyen sentetik örneklerle çalışabilirsiniz; bu okuma, ilk MVP'ye YZ ile müşteri içeriği işleme özelliği eklemez.

<a id="ek-d-10"></a>

**D.10. İleri Okumalar**

**K-D21 — A Behavioral Notion of Subtyping**

**Kaynak ve erişim:** Liskov ve Wing'in (1994) [davranışsal alt tipleme makalesi](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf), yazarın üniversite sayfasında PDF olarak erişilebilirdir.

**Nasıl okunmalı?** Nesne yönelimli tasarım, üst/alt tip ve ön koşul/son koşul bilgisi gerekir. Önce özet ve girişteki davranış ilişkisini okuyun; biçimsel ayrıntıları daha sonra izleyin. Makale, alt tipin üst tip hakkında geçerli özellikleri koruması üzerinden sözleşme düşüncesini derinleştirir. Tek bir sınıf diyagramı çizmek bu ilişkinin kanıtı değildir.

AI-CRM'e yeni kalıtım yapısı eklemek yerine, [Bölüm 11](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-11) içindeki Liskov Yerine Geçme İlkesi örneğini değerlendirin. YZ'nin önerdiği alt tip aynı imzayı korurken kabul edilen girdileri daraltıyor veya vaat edilen sonucu değiştiriyor mu? Önce bu soruya anlaşılır bir karşı örnek üretin.

<a id="ek-d-okuma-notu"></a>

**Okuma notunu çalışmaya dönüştürmek**

Bir kaynağı kapattıktan sonra hatırlanan genel izlenim, karar vermek için yeterli olmayabilir. Aşağıdaki kısa kayıt, okumanın hangi işe katkı verdiğini gösterir. Kaynak başlığını yazmakla yetinmeyin; kullanılan sürümü ve ilgili kısmı da belirtin. Web belgesinde bölüm adı, bir kitapta ise eriştiğiniz baskının gerçek sayfa bilgisi kullanılabilir. Görmediğiniz sayfa numarasını YZ'ye tamamlatmayın.

| Kayıt alanı | Yazılacak bilgi |
|---|---|
| Soru | Okumadan önce çözmek istediğiniz tek problem |
| Kaynak | Yazar/kurum, başlık, sürüm veya baskı, bağlantı ve erişim tarihi |
| İncelenen kısım | Gerçekten okunan başlık veya görülen sayfa aralığı |
| Kaynağın açıklaması | Kendi cümlelerinizle, kaynağın kapsamını aşmayan not |
| Projeye uyarlama | AI-CRM kararıyla ilişkisi ve sizin çıkardığınız sonuç |
| Sınır veya karşı örnek | Açıklamanın tek başına çözmediği durum |
| Sonraki iş | Belge düzeltmesi, karar ihtiyacı veya belirli doğrulama |
| Durum ve kanıt | Okundu, taslak hazırlandı, uygulandı veya doğrulandı ayrımı; varsa gerçek çıktı |

Örneğin `K-D10` okumasından sonra “notun müşteriyle ilişkisi yabancı anahtarla korunabilir” notu alınabilir. Buradan “not oluşturma yetkisi doğrulandı” sonucu çıkmaz. İkinci iddia için uygulamanın kullanıcı ve müşteri ilişkisini nasıl denetlediğinin ayrıca incelenmesi gerekir. Bu, tamamen yazılmış bir öğretim örneğidir; gerçek veritabanı veya yetki testi raporu değildir.

Kaynaklar arasında farklı yaklaşım görürseniz önce bağlamı karşılaştırın: kullanılan dil, ekip büyüklüğü, yayın sıklığı, veri riski veya araştırma koşulu aynı olmayabilir. Bir metnin daha yeni olması, farklı probleme daha uygun olduğu anlamına gelmez. Buna karşılık sürüme bağlı bir komut için eski kavramsal kitabı güncel ürün belgesinin yerine koymayın. Önce sorunun kavramsal mı, uygulama ayrıntısı mı, yoksa deneysel bir iddia mı olduğunu belirleyin.

Bağlantı sonradan değişirse önce yazarın, kurumun veya yayınevinin resmî sayfasında başlık ve baskıyla arayın. Sürüm bağlantısını yeni bir sürüme sessizce değiştirmek yerine, yeni belgenin örneğinize etkisini inceleyin. Kitapların kendi bölüm kaynakçaları daha geniş başvuru listeleridir; bu seçki onların yerine geçmez. Yeni bir kaynak eklerken, mevcut sorulardan hangisini daha iyi cevapladığını açıklayabiliyor olmak sayıyı artırmaktan daha değerlidir.

<a id="ek-d-kaynakca"></a>

**Kaynakça**

Fowler, M. (2004, 23 Ocak). [*Inversion of control containers and the dependency injection pattern*](https://martinfowler.com/articles/injection.html).

Fowler, M. (2018). [*Refactoring: Improving the design of existing code*](https://martinfowler.com/books/refactoring.html) (2. baskı). Addison-Wesley Professional.

Fowler, M. (2019, 1 Ağustos). [*Software architecture guide*](https://martinfowler.com/architecture/).

Gamma, E., Helm, R., Johnson, R., & Vlissides, J. (1994). [*Design patterns: Elements of reusable object-oriented software*](https://www.informit.com/store/design-patterns-elements-of-reusable-object-oriented-software-9780201633610). Addison-Wesley Professional.

Google. (t.y.). [*What to look for in a code review*](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Google Engineering Practices. Erişim tarihi: 6 Ekim 2026.

Liskov, B. H., & Wing, J. M. (1994). [A behavioral notion of subtyping](https://www.cs.cmu.edu/~wing/publications/LiskovWing94.pdf). *ACM Transactions on Programming Languages and Systems, 16*(6), 1811–1841.

Nygard, M. (2011, 15 Kasım). [*Documenting architecture decisions*](https://cognitect.com/blog/2011/11/15/documenting-architecture-decisions). Cognitect.

OpenAI. (t.y.). [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering). Erişim tarihi: 6 Ekim 2026.

PostgreSQL Global Development Group. (t.y.-a). [*Constraints*](https://www.postgresql.org/docs/18/ddl-constraints.html). PostgreSQL 18 documentation. Erişim tarihi: 6 Ekim 2026.

PostgreSQL Global Development Group. (t.y.-b). [*Tutorial*](https://www.postgresql.org/docs/18/tutorial.html). PostgreSQL 18 documentation. Erişim tarihi: 6 Ekim 2026.

Washizaki, H. (Ed.). (2026). [*Guide to the software engineering body of knowledge (SWEBOK Guide)*](https://ieeecs-media.computer.org/media/education/swebok/swebok-v4.pdf) (Sürüm 4.0a). IEEE Computer Society.

Winters, T., Manshreck, T., & Wright, H. (Ed.). (2020). [*Software engineering at Google: Lessons learned from programming over time*](https://abseil.io/resources/swe-book). O'Reilly Media.
