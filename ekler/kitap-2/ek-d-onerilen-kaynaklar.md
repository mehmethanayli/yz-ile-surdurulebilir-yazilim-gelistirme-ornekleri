# Ek D — Önerilen Kaynaklar

Kitap 2 için 15 kaynak seçilmiştir. Kaynaklar geliştirme ve incelemeden test, güvenlik, yayın, işletim ve YZ değerlendirmesine uzanır. Veri modeli ve kısıtlar uygulamada yeniden gerekli olduğundan temel başvurular da korunmuştur.

K-D kimlikleri seri genelinde korunur. İki kitapta bulunan bir kaynak aynı kimliği taşır. Başlık altındaki okuma önerileri kaynağın kapsamını ve AI-CRM’de nasıl kullanılabileceğini açıklar. Kaynaklar İngilizcedir; ticari kitaplarda açık tanıtım ve örnek sayfalarına bağlantı verilmiştir. Açık kaynaklarla başlanabilir; satın alma zorunluluğu yoktur.

Yayın ve bağlantı bilgileri ortak kaynak rehberinin 6 Ekim 2026 tarihli incelemesinden alınmıştır. Bu ayrıştırmada web kaynakları yeniden kontrol edilmemiştir. Kaynak okumak, uygulama veya test sonucu oluşturmaz; proje kararı ve gerçek kanıt ayrı kaydedilir.

**İçindekiler**

- [D.1. Yazılım Mühendisliği](#ek-d-1)
- [D.3. Temiz Kod ve Refactoring](#ek-d-3)
- [D.5. Veritabanı Tasarımı](#ek-d-5)
- [D.6. Yazılım Testi](#ek-d-6)
- [D.7. Yazılım Güvenliği](#ek-d-7)
- [D.8. DevOps ve Deployment](#ek-d-8)
- [D.9. Yapay Zekâ Destekli Yazılım Geliştirme](#ek-d-9)
- [D.10. İleri Okumalar](#ek-d-10)
- [Okuma notunu çalışmaya dönüştürmek](#ek-d-okuma-notu)
- [Kaynakça](#ek-d-kaynakca)

<a id="ek-d-1"></a>

**D.1. Yazılım Mühendisliği**

**K-D02 — Software Engineering at Google**

**Kaynak ve erişim:** Winters ve diğerlerinin (2020) hazırladığı [Software Engineering at Google](https://abseil.io/resources/swe-book), Abseil üzerinden ücretsiz HTML olarak okunabilir; basılı sürümü de vardır.

**Nasıl okunmalı?** Küçük bir kod tabanını okuma ve değiştirme deneyimi yararlıdır. Başlangıçta yazılım mühendisliğinin ne olduğu sorusunu ele alan açılış kısmını, ardından o anki ihtiyaca göre kod inceleme veya test konularını seçin. Kaynağın odağı kodun zaman içinde sürdürülebilmesi ve mühendislik uygulamalarıdır; bir dilin sözdizimini öğretmek değildir.

Google ölçeğindeki bir uygulamayı küçük ekibe doğrudan taşımadan önce hangi sorunu çözdüğünü yazın. AI-CRM için yararlı çıktı, her araç ve rolü kopyalamak değil, bir değişikliğin gerekçesini başka geliştiricinin anlayabileceği kısa inceleme kaydıdır. Bu uyarlama, kitabımızın küçük ekip bağlamına yönelik çalışma önerisidir.

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

<a id="ek-d-6"></a>

**D.6. Yazılım Testi**

**K-D11 — Writing and Running Tests**

**Kaynak ve erişim:** Django Software Foundation'ın (t.y.-b) [Django 5.2 test belgesi](https://docs.djangoproject.com/en/5.2/topics/testing/overview/) ücretsizdir.

**Nasıl okunmalı?** Temel Python, Django model kavramı ve geliştirme ortamı bilgisi gerekir. Test yazma, test çalıştırma ve test veritabanı kısımlarını birlikte okuyun. Belge test keşfini, test sınıflarını ve veritabanı kullanan testlerin ayrılmasını açıklar. Komutun doğru yazılması, uygun ortamın kurulmuş olduğunu göstermez.

AI-CRM'de geçerli notun kaydedilmesi ile boş notun reddedilmesini ayrı beklentilere dönüştürün. Mevcut kitap deposundaki küçük laboratuvarın sonucu ile henüz kurulmamış hedef Django uygulamasının sonucunu karıştırmayın. YZ'nin test taslağında kullandığı model ve alanların gerçekten bulunup bulunmadığını kontrol edin.

**K-D12 — Mocks Aren't Stubs**

**Kaynak ve erişim:** Fowler'ın (2007) [Mocks Aren't Stubs](https://martinfowler.com/articles/mocksArentStubs.html) yazısı ücretsizdir.

**Nasıl okunmalı?** Birim testin hazırlık, eylem ve doğrulama adımları bilinmelidir. Önce normal test örneğini, sonra mock ile örneği ve test karşılıkları arasındaki ayrımı okuyun. Metin, nesnenin son durumunu kontrol etmekle beklenen etkileşimi kontrol etmek arasındaki farkı tartışır. Tarihsel Java kütüphanesi örnekleri güncel Python kurulumu önerisi değildir.

AI-CRM testinde veri erişim çağrısını taklit ettiğinizde, gerçek veritabanı kısıtını sınadığınızı ileri sürmeyin. Kontrollü karşılığın neyi kolaylaştırdığını ve hangi davranışı test dışında bıraktığını belirtin. YZ'den çok sayıda mock üretmesini istemek yerine, her karşılığın sınadığı sözleşmeyi açıklamasını isteyin.

<a id="ek-d-7"></a>

**D.7. Yazılım Güvenliği**

**K-D13 — Secure Software Development Framework, sürüm 1.1**

**Kaynak ve erişim:** Souppaya ve diğerlerinin (2022) [NIST SP 800-218 raporu](https://csrc.nist.gov/pubs/sp/800/218/final) ücretsizdir. Bu öneri açıkça sürüm 1.1'e yöneliktir.

**Nasıl okunmalı?** Geliştirme yaşam döngüsü ve temel güvenlik kavramları yeterlidir. Önce çerçevenin amacını, ardından kendi geliştirme işinizle ilişkili uygulamaları inceleyin. SSDF, güvenli geliştirme uygulamalarını yaşam döngüsüne katmak ve ortak bir dil oluşturmak için üst düzey bir çerçeve sunar.

AI-CRM'de bir bağımlılık veya kaynak kod değişikliğinin nasıl inceleneceğini ve bulunan sorunun nasıl izleneceğini yazın. Büyük kurumların tüm süreçlerini küçük ekibe aynen taşımak gerekmez; fakat sorumlusu ve kanıtı bulunmayan bir uygulama da yalnız adı yazıldığı için yürütülmüş sayılmaz. YZ önerisini mevcut süreçte karşılığı olan somut işe dönüştürün.

**K-D14 — Authorization Cheat Sheet**

**Kaynak ve erişim:** OWASP Foundation'ın (t.y.) [yetkilendirme rehberi](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html) ücretsizdir.

**Nasıl okunmalı?** Kimlik doğrulama ile yetkilendirme ayrımı ve HTTP istek akışı bilinmelidir. En az yetki, varsayılan ret ve her istekte izin denetimi kısımlarıyla başlayın. Rehber, çatı varsayımlarına güvenmek yerine uygulamanın erişim mantığının açıkça incelenmesini sağlar.

AI-CRM'de oturum açmış olmak, başkasının kişisel görevini okuma veya tamamlama izni vermez. Hesap yönetimi rolünün iş verisine erişimle aynı şey olmadığını da kontrol edin. YZ'nin yalnız giriş ekranını veya görünür düğmeleri değiştirmesi, sunucu tarafındaki nesne yetkisini doğrulamaz. Okumayı farklı kullanıcılarla beklenen izin/ret tablosuna dönüştürün.

<a id="ek-d-8"></a>

**D.8. DevOps ve Deployment**

**K-D15 — Deployment Checklist**

**Kaynak ve erişim:** Django Software Foundation'ın (t.y.-a) [Django 5.2 yayın kontrol listesi](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/) ücretsizdir.

**Nasıl okunmalı?** Geliştirme ve üretim ortamı ayrımı, HTTPS ve yapılandırma kavramları bilinmelidir. Önce kritik ayarları ve ortama bağlı ayarları okuyun; `check --deploy` kontrolünü hangi yapılandırmaya karşı çalıştıracağınızı belirleyin. Belge, bu komutun kontrollerin bir kısmını otomatikleştirdiğini belirtir; sonuç bütün yayın hazırlığının tamamlandığı anlamına gelmez.

AI-CRM yayın planında gizli anahtar, hata ayıklama ayarı, alan adı ve HTTPS kararlarını sorumlu ve kanıtla ilişkilendirin. YZ'nin ürettiği örnek ortam dosyasına gerçek sır eklemeyin. Belgedeki dosya yükleme gibi genel konuların bulunması, ilk MVP kapsamına o özelliğin girdiği anlamına gelmez.

**K-D16 — Site Reliability Engineering: How Google Runs Production Systems**

**Kaynak ve erişim:** Beyer ve diğerlerinin (2016) editörlüğündeki [Site Reliability Engineering kitabının ilk baskısı](https://sre.google/sre-book/table-of-contents/) Google üzerinden ücretsiz okunabilir. Bu bağlantı özellikle ilk baskıya yöneliktir; sonraki baskılarla bölüm numaraları karıştırılmamalıdır.

**Nasıl okunmalı?** Yayın, hata kaydı ve temel ölçüm kavramları gerekir. İlk geçiş için hizmet seviyesi hedefleri, izleme, yayın mühendisliği ve olay sonrası öğrenme başlıklarını seçin. Kitap büyük ölçekli işletim deneyimini aktarır; bütün altyapı düzenini küçük ekibe taşımak okuma hedefi değildir.

AI-CRM için kullanıcı açısından anlamlı bir hizmet davranışı ve bunun bozulmasını fark ettirecek ölçüm tanımlayın. Kaynaktaki bir hedefi bağlamından kopararak kendi hizmetinizin taahhüdü yapmayın. YZ'ye alarm taslağı hazırlatılırsa, ölçüm kaynağı ve alarm sonrası yapılacak iş açık kalmalıdır.

<a id="ek-d-9"></a>

**D.9. Yapay Zekâ Destekli Yazılım Geliştirme**

**K-D17 — Prompt Engineering**

**Kaynak ve erişim:** OpenAI'nin (t.y.) [talimat hazırlama rehberi](https://developers.openai.com/api/docs/guides/prompt-engineering) ücretsizdir. Okuma için API hesabı veya ücretli model çağrısı gerekmez.

**Nasıl okunmalı?** Görev, bağlam ve beklenen çıktı kavramları yeterlidir; kod örnekleri için temel API bilgisi yararlıdır. Açık talimat, ilgili bağlam, örnekler ve değerlendirme ihtiyacı üzerine kısımlarla başlayın. Rehber sağlayıcıya özgü API ayrıntıları da içerir; model adları ve arayüz örnekleri kalıcı mühendislik ilkeleriyle aynı şekilde ele alınmamalıdır.

[Ek C](ek-c-yapilandirilmis-ai-talimatlari.md) içinden bir talimat seçerek beklenen çıktıyı ve kanıt sınırını netleştirin. Rehberdeki teknikleri uygulamak doğruluğu garanti etmez. Müşteri verisini modele aktarmayı gerektirmeyen sentetik örneklerle çalışabilirsiniz; bu okuma, ilk MVP'ye YZ ile müşteri içeriği işleme özelliği eklemez.

**K-D18 — Building Effective Agents**

**Kaynak ve erişim:** Erik S. ve Zhang'ın (2024) [Building Effective Agents](https://www.anthropic.com/engineering/building-effective-agents) yazısı ücretsizdir. Sayfa, 2024'teki araç ortamının değiştiğini ayrıca belirtir.

**Nasıl okunmalı?** Model çağrısı, araç kullanımı ve iş akışı kavramları bilinmelidir. Önceden tanımlanmış iş akışları ile modelin adımları yönettiği ajanlar arasındaki ayrımla başlayın. Ardından karmaşıklığın hangi durumda gerekli olduğunu tartışan kısmı okuyun. Yazıyı güncel araç kurulumu veya belirli bir ürün satın alma rehberi olarak kullanmayın.

AI-CRM geliştirmesinde bir kod inceleme görevini ele alın: tek bir inceleme çağrısı yeterli mi, yoksa araçlı bir döngüye neden ihtiyaç var? YZ'nin yetkisini, durma koşulunu ve incelenecek çıktıyı açıklayın. Sağlayıcının deneyimlerini kendi projenizde ölçülmüş başarı gibi sunmayın.

**K-D19 — We Are Changing Our Developer Productivity Experiment Design**

**Kaynak ve erişim:** Becker ve arkadaşlarının (2026) METR'de yayımladığı [geliştirici verimliliği deney tasarımı yazısı](https://metr.org/blog/2026-02-24-uplift-update/) ücretsizdir. Yazarlar, sayfanın önerdiği atıf kaydında Joel Becker, Nate Rush, Tom Cunningham, David Rein ve Khalid Mahamud olarak belirtilmiştir.

**Nasıl okunmalı?** Ortalama, belirsizlik ve karşılaştırma grubu kavramları yararlıdır. Önce katılımcı seçiminin ve görev süresini ölçmenin sonuçları nasıl etkilediğine ilişkin açıklamaları okuyun. Metin, yeni verinin yorumlanmasındaki sınırlamaları tartışır; bütün geliştiriciler için tek bir hızlanma oranı çıkarmaya elverişli değildir.

AI-CRM için yapılabilecek bir değerlendirmede yalnız kod üretim süresini değil, inceleme ve düzeltme emeğini de tanımlayın. YZ'den araştırmayı özetlemesini isterseniz çalışma koşullarını, gözlenen sonucu ve yazarların yorumunu ayrı yazmasını isteyin. Gerçek ölçüm yapılmadığında örnek süreler “sentetik” olarak kalır.

<a id="ek-d-10"></a>

**D.10. İleri Okumalar**

**K-D20 — Artificial Intelligence Risk Management Framework, AI RMF 1.0**

**Kaynak ve erişim:** Tabassi'nin (2023) [NIST AI RMF 1.0 raporu](https://doi.org/10.6028/NIST.AI.100-1) ücretsizdir.

**Nasıl okunmalı?** YZ sisteminin kim tarafından, hangi bağlamda kullanıldığını açıklayabilmek gerekir. Önce çerçevenin amaç ve kapsamını okuyun; ardından kendi kullanımınız için hangi risklerin ve sorumlulukların incelenmesi gerektiğini seçin. Kaynak farklı sektör ve büyüklükteki kuruluşlara uyarlanabilecek gönüllü bir çerçevedir; tek bir modelin güvenli olduğunu onaylayan sertifika değildir.

AI-CRM geliştirme yardımcısının yanlış kod üretmesiyle gelecekte müşteriye doğrudan YZ yanıtı sunan bir ürünün risklerini ayırın. İlk MVP'de bulunmayan ikinci kullanımı mevcut özellik gibi yazmayın. YZ'den risk notu taslağı alabilirsiniz; sorumluluk ve kabul kararı çalışma bağlamında insanlar tarafından belirlenir.

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

Becker, J., Rush, N., Cunningham, T., Rein, D., & Mahamud, K. (2026, 24 Şubat). [*We are changing our developer productivity experiment design*](https://metr.org/blog/2026-02-24-uplift-update/). METR.

Beyer, B., Jones, C., Petoff, J., & Murphy, N. R. (Ed.). (2016). [*Site reliability engineering: How Google runs production systems*](https://sre.google/sre-book/table-of-contents/). O'Reilly Media.

Django Software Foundation. (t.y.-a). [*Deployment checklist*](https://docs.djangoproject.com/en/5.2/howto/deployment/checklist/). Django 5.2 documentation. Erişim tarihi: 6 Ekim 2026.

Django Software Foundation. (t.y.-b). [*Writing and running tests*](https://docs.djangoproject.com/en/5.2/topics/testing/overview/). Django 5.2 documentation. Erişim tarihi: 6 Ekim 2026.

Erik S., & Zhang, B. (2024, 19 Aralık). [*Building effective agents*](https://www.anthropic.com/engineering/building-effective-agents). Anthropic.

Fowler, M. (2007, 2 Ocak). [*Mocks aren't stubs*](https://martinfowler.com/articles/mocksArentStubs.html).

Fowler, M. (2018). [*Refactoring: Improving the design of existing code*](https://martinfowler.com/books/refactoring.html) (2. baskı). Addison-Wesley Professional.

Google. (t.y.). [*What to look for in a code review*](https://google.github.io/eng-practices/review/reviewer/looking-for.html). Google Engineering Practices. Erişim tarihi: 6 Ekim 2026.

OpenAI. (t.y.). [*Prompt engineering*](https://developers.openai.com/api/docs/guides/prompt-engineering). Erişim tarihi: 6 Ekim 2026.

OWASP Foundation. (t.y.). [*Authorization cheat sheet*](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html). OWASP Cheat Sheet Series. Erişim tarihi: 6 Ekim 2026.

PostgreSQL Global Development Group. (t.y.-a). [*Constraints*](https://www.postgresql.org/docs/18/ddl-constraints.html). PostgreSQL 18 documentation. Erişim tarihi: 6 Ekim 2026.

PostgreSQL Global Development Group. (t.y.-b). [*Tutorial*](https://www.postgresql.org/docs/18/tutorial.html). PostgreSQL 18 documentation. Erişim tarihi: 6 Ekim 2026.

Souppaya, M., Scarfone, K., & Dodson, D. (2022). [*Secure Software Development Framework (SSDF) version 1.1: Recommendations for mitigating the risk of software vulnerabilities*](https://doi.org/10.6028/NIST.SP.800-218) (NIST SP 800-218). National Institute of Standards and Technology.

Tabassi, E. (2023). [*Artificial intelligence risk management framework (AI RMF 1.0)*](https://doi.org/10.6028/NIST.AI.100-1) (NIST AI 100-1). National Institute of Standards and Technology.

Winters, T., Manshreck, T., & Wright, H. (Ed.). (2020). [*Software engineering at Google: Lessons learned from programming over time*](https://abseil.io/resources/swe-book). O'Reilly Media.
