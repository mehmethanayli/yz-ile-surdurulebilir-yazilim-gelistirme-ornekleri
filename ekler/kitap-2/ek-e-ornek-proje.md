# Ek E — AI CRM Uygulama ve Laboratuvar Rehberi

Bu ek, Kitap 1’den devralınan AI-CRM tasarımını Kitap 2’nin geliştirme, test ve işletim çalışmalarına bağlar. Bölüm 1–6 için bağımsız Python laboratuvarları; Bölüm 7–13 için plan, senaryo ve değerlendirme dosyaları bulunur. Başlangıç kapsamı Kitap 1’in Ek E’sinde, kayıtların açıklamaları bu kitabın Ek F’sindedir.

Laboratuvar yönergeleri ve önceki doğrulama bilgileri ortak örnek proje ekinin 6 Ekim 2026 tarihli kaydından alınmıştır. Bu dosya, bütünleşmiş Django/PostgreSQL CRM’in kurulumu veya ürün test sonucu olarak okunmamalıdır. Her örnekte önce ilgili README ve teslim edilen dosyalar kontrol edilir. Kaynak sürümü E.3’teki yöntemle kaydedilir.

**İçindekiler**

- [E.1. Örnek Projenin Kaynak Kodu](#ek-e-1)
- [E.2. Repository Yapısı](#ek-e-2)
- [E.3. Bölüm ve Kaynak Sürümünü Eşleştirme](#ek-e-3)
- [E.4. Sürüm ve Doğrulama Kaydı](#ek-e-4)
- [E.5. Örnek Veri Seti](#ek-e-5)
- [E.6. Kurulum Talimatları](#ek-e-6)
- [Kaynakça](#ek-e-kaynakca)

<a id="ek-e-1"></a>

**E.1. Örnek Projenin Kaynak Kodu**

Öğretim dosyaları bu uygulama deposunda paylaşılır. Başlangıç için kök [README](../../README.md) dosyasını ve [bölüm eşleştirmesini](../../docs/bolum-eslestirmesi.md) kullanın. Bu depo bağımsız laboratuvarları ve öğretim paketlerini içerir; kitapların bölüm metinleri basılı kitaplarda okunur.

Mevcut kaynaklar üç düzeyde okunur. İlk düzey, bölüm metinlerindeki açıklayıcı kod ve tasarım örnekleridir. Bunlar iş kuralını veya düşünme biçimini anlatır; her parça tek başına çalıştırılabilir bir program değildir. İkinci düzey, `assets/code` altında README ve çalıştırma yönergeleri bulunan bağımsız laboratuvarlardır. Üçüncü düzey ise `assets/examples` altındaki JSON ve Markdown öğretim paketleridir. Bu paketlerin bazıları dosya ilişkileri ve aritmetik bakımından doğrulanmıştır; gerçek uygulama davranışı bakımından çalıştırılmış değildir.

Örneğin [Bölüm 6'nın güvenlik örneği](../../assets/code/chapter19-security-lab/security_example.py), etkin aktör ve görev sahipliği üzerinden küçük bir davranış gösterir. Dosyada bir `Actor` sınıfının bulunması parola doğrulayan bir oturum altyapısı kurulduğu anlamına gelmez. Benzer biçimde [Bölüm 10'un kabul senaryoları](../../assets/examples/chapter23-integration/acceptance-cases.json), hedef davranışları tarif eder; HTTP isteği gönderen test kodu değildir. Bir dosyayı kullanmadan önce hangi düzeyde olduğunu belirlemek, yanlış tamamlanma iddialarını önler.

AI-CRM'in ilk kapsamı tek kurumda çalışan küçük bir ekiptir. Müşteriler ve müşteri notları ortak, görevler kişiseldir. Bir ekip üyesinin müşteri kaydını görebilmesi, başka üyeye ait görevi görebileceği veya tamamlayabileceği anlamına gelmez. Yalnız hesap yönetimi rolü iş verisine erişim vermez; bu rolle ekip üyeliğinin birleşmesi de başkasının görevini açmaz. Korumalı işlemlerde hesap etkinliği ayrıca değerlendirilir. İlk sürümde ödeme, dosya yükleme, çok kiracılık veya müşteri içeriğinin YZ ile işlenmesi bulunmaz.

Bu kuralların tasarım dayanakları [Kitap 1, Bölüm 4](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-4), [Kitap 1, Bölüm 7](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-7), [Kitap 1, Bölüm 8](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-8) ve [Kitap 1, Bölüm 13](../../docs/bolum-eslestirmesi.md#kitap-1-bolum-13) içindedir. [Bölüm 10 bütünleştirme planı](../../assets/examples/chapter23-integration/integration-plan.json), FG-01–FG-05 gereksinimlerini, KM-01–KM-05 not ölçütlerini, 12 açık karar grubunu ve altı geliştirme paketini bir araya getirir. Kaynaklar arasında başlangıç noktası arayan okuyucu önce bu planı, sonra işin dayandığı bölüm kararını okumalıdır.

YZ'den bir örneği genişletmesini istediğinizde dosyanın öğretim amacı ile hedef ürün davranışını ayrı belirtin. Örneğin SQLite kullanan dar laboratuvarın varlığı, hedef ürünün PostgreSQL kararını değiştirmez. Açık alan uzunlukları, zaman dilimi, oturum süresi veya istek anahtarı kuralları da modelin tahminiyle kesinleşmez. Bu ek, mevcut dosyaları bulmayı kolaylaştırır; açık ürün kararlarını tamamlanmış uygulama gibi göstermenin yolu değildir.

<a id="ek-e-2"></a>

**E.2. Repository Yapısı**

Depoda uygulamalar ve dijital ekler bulunur. Bölüm metinlerine yapılan başvurular bölüm eşleştirme rehberine gider; ilgili açıklama kitaptan okunur.

```text
yz-ile-surdurulebilir-yazilim-gelistirme-ornekleri/
├── README.md
├── assets/
│   ├── code/       # Altı bağımsız Python laboratuvarı
│   └── examples/   # Yedi plan, senaryo ve değerlendirme paketi
├── ekler/
│   ├── kitap-1/    # Ek A–F
│   └── kitap-2/    # Ek A–F
├── docs/bolum-eslestirmesi.md
├── references/references.bib
└── indir/          # Bütün materyallerin ZIP paketi
```

Bir örneğin kökünde bulunan README, o örneğin giriş noktasıdır. Komutun hangi dizinde çalıştırılacağını, gerekli yorumlayıcıyı, beklenen sonucu ve kapsam dışı işleri açıklar. Aynı adlı `tests` veya `scripts` klasörleri farklı laboratuvarlara ait olabilir. Bütün test klasörlerini tek bir ürünün test ağacıymış gibi birleştirmek yerine ilgili örnek kökünü kullanın.

| Bölüm | Paket ve giriş dosyası | Kullanım amacı |
|---|---|---|
| 1 | [Ortam örneği](../../assets/code/chapter14-environment/README.md) | Yorumlayıcı, sanal ortam ve sınırlı ayar raporu |
| 2 | [Git laboratuvarı](../../assets/code/chapter15-git-lab/README.md) | Yeni yerel deneme depolarında 28 Git kontrolü |
| 3 | [Paylaşım görünümü](../../assets/code/chapter16-share-report/README.md) | Ortam raporuna küçük değişiklik, test ve inceleme |
| 4 | [Hata ayıklama laboratuvarı](../../assets/code/chapter17-debug-lab/README.md) | Kasıtlı kusuru yeniden üretme ve doğru varyantı inceleme |
| 5 | [Test laboratuvarı](../../assets/code/chapter18-test-lab/README.md) | 18 test yöntemi ve ayrı beklenti kalitesi deneyi |
| 6 | [Güvenlik laboratuvarı](../../assets/code/chapter19-security-lab/README.md) | Sahiplik, sorgu kapsamı ve sınırlı metin kodlama |
| 7 | [İnceleme senaryoları](../../assets/examples/chapter20-review/README.md) | Veri paylaşımı, köken ve sorumluluk örnekleri |
| 8 | [Yayın planı](../../assets/examples/chapter21-release/README.md) | Yayın öncesi karar, kanıt ve geri dönüş hazırlığı |
| 9 | [İşletim planı](../../assets/examples/chapter22-operations/README.md) | Ölçüm, olay ve bakım kayıtlarını okuma |
| 10 | [Bütünleştirme paketi](../../assets/examples/chapter23-integration/README.md) | İlk MVP'nin tasarım ve kabul bağlantıları |
| 11 | [SaaS geçiş taslağı](../../assets/examples/chapter24-saas/README.md) | İlk MVP'den ayrı gelecek ürün senaryoları |
| 12 | [YZ görev ve denetim paketi](../../assets/examples/chapter25-ai-team/README.md) | Görev kartları, değerlendirme ölçütleri ve devir |
| 13 | [Gelecek ve öğrenme paketi](../../assets/examples/chapter26-future/README.md) | İddia inceleme, sentetik ölçüm ve öğrenme çalışmaları |

Bu 13 paketin amacı aynı değildir. Bölüm 1–6'da yürütülebilir Python örnekleri bulunur; Bölüm 7–13 paketleri ağırlıkla okunacak ve ilişkilendirilecek öğretim verileridir. `verification.json` adını görmek tek başına ürün testi sonucuna işaret etmez. Kaydın kapsamını, tarihini ve gerçekten yürütülen kontrollerini okuyun. Bölüm 1'in doğrulama açıklaması kendi README'sinde ve GO-14-01 kaydındadır; her pakette aynı dosya düzeninin bulunması zorunlu değildir.

Kitabın şekil ve dizgi üretim betikleri bu dağıtıma dahil değildir. Kitabı okumak veya test laboratuvarını çalıştırmak için bütün şekilleri yeniden üretmeniz gerekmez. Bu ayrım, gereksiz bağımlılık kurulmasını önler. Bir YZ aracına “depoyu kur” gibi geniş bir görev vermek yerine, örneğin “Bölüm 5 README'sini ve test yapısını incele; gereken ortamı ve çalıştırma dizinini belirle” demek daha somut bir başlangıçtır.

<a id="ek-e-3"></a>

**E.3. Bölüm ve Kaynak Sürümünü Eşleştirme**

E.2 tablosu Bölüm 1–13’ü ilgili öğretim paketine bağlar. Kullanılan kopyanın sürümünü ayrıca kaydedin. Bir dosyanın çalışma klasöründe bulunması commit’e girdiğini veya uzak depoda bulunduğunu göstermez. Gerçek kısa veya tam kimliği aşağıdaki salt inceleme komutlarının çıktısından alın; eksik kimliği tahmin etmeyin.

```powershell
git rev-parse HEAD
git status --short --untracked-files=all
git log --format="%H %ad %s" --date=short -- assets/code/chapter18-test-lab
```

Git geçmişi kaydedilmiş içeriği, durum çıktısı ise çalışma alanı ile kaydedilmiş içerik arasındaki farkı gösterir (Git Project, t.y.-a, t.y.-b). Bu komutlar uygulama deposunun kökünde kullanılır. Git bilgisi içermeyen bir dağıtım kopyasında bunun yerine teslim paketinin adı, tarihi ve dosya sürümü yazılır. Boş log, yerel dosyanın bulunmadığını kanıtlamaz.


<a id="ek-e-4"></a>

**E.4. Sürüm ve Doğrulama Kaydı**

Bir laboratuvarın sonucu yalnız kullanılan dosyaları, ortamı ve yürütülen kontrolleri kapsar. GO-14-01, TS-18-01 ve UÇ-23-01 çalışma veya kanıt kaydıdır; ürün sürümü değildir. Bölüm 2’nin lab-v0.1.0 etiketi deneme deposuna aittir. Bölüm 3’ün change.diff ve Bölüm 4’ün fix.diff dosyaları öğretim karşılaştırmalarıdır.

| Kayıt | Nasıl okunmalı? |
|---|---|
| Commit veya teslim paketi | İncelenen dosyaların sürümünü gösterir |
| README ve verification.json | Kaydedilmiş ortamı, yöntemi ve kontrol kapsamını açıklar |
| Bölüm karar ve kanıt kimliği | İşin dayanağı, durumu ve açık konulara yönlendirir |
| Gerçek ürün yayın kaydı | Uygulama çıktısı, test, ortam ve yayın sonucu hazırlandığında doldurulur |

Önceki doğrulama kaydı, testlerin okuyucunun makinesinde yeniden çalıştığını göstermez. SHA-256 karşılaştırırken kayıtta belirtilen satır sonu normalleştirmesini ve yöntemini kullanın. Gerçek ürün sürümünde kaynak, çözümlenmiş bağımlılıklar, test sonuçları, dağıtım çıktısı ve yayın sonucu birlikte izlenir.


<a id="ek-e-5"></a>

**E.5. Örnek Veri Seti**

İlk MVP'yi incelemek için ortak başlangıç verisi [Bölüm 10'un synthetic-data.json dosyasıdır](../../assets/examples/chapter23-integration/synthetic-data.json). Dosya gerçek kişi veya müşteri kaydından türetilmemiş sentetik ilişkiler içerir. Dört aktör, iki müşteri, bir not ve iki görev vardır. Bu dosya bir Django fixture veya veritabanına doğrudan aktarılacak seed betiği değildir; `loaddata` ile yüklenmesi beklenmez.

| Aktör | Etkinlik ve rol | İncelenecek erişim sınırı |
|---|---|---|
| A | Etkin ekip üyesi | Ortak müşteri/notlar ve kendi görevi |
| B | Etkin ekip üyesi | Aynı ortak müşteri/notlar; A'nın görevi değil, kendi görevi |
| S | Etkin, yalnız hesap yönetimi | Rolü tek başına müşteri/not/görev erişimi sağlamaz |
| D | Devre dışı ekip üyesi | Eski oturum varlığı korumalı isteği kabul ettirmez |

Müşteri `101` ve `102` aynı görünen ada, “Deniz Kaya” adına sahiptir. Farklı kimlikler, adın tek başına kayıt seçme anahtarı olmadığını gösterir. Not `501`, yalnız müşteri `102` ile ilişkilidir; yazarı A'dır. Görev `701` A'nın, `702` B'nindir. İki görev de müşteri `102` ile ilişkilidir ve aynı başlığı taşır. Ortak müşteri ve aynı görev başlığı, görev sahipliğini ortaklaştırmaz.

Müşterilerin e-posta ve telefon alanları `null` değerindedir. Bu seçim bütün iletişim biçimi kararlarının tamamlandığını göstermez; dolu değerlerin nasıl doğrulanacağı açık kararlar arasındadır. Dış temsilde kimlikler metindir. JSON'daki tarih ve zamanlar öğretim değerleridir; sunucudan alınmış olay kaydı veya ürün zaman dilimi kararı olarak kullanılamaz.

| Veri üzerinden sorulacak soru | Beklenen okuma |
|---|---|
| `501` numaralı not hangi müşteri ayrıntısında görülmeli? | Müşteri `102`; aynı adlı `101` ile karışmamalı |
| B, `701` numaralı görevi tamamlayabilir mi? | Hayır; görevin sahibi A |
| Yalnız S rolü müşteri notlarını açar mı? | Hayır; hesap yönetimi tek başına iş verisi yetkisi değil |
| D'nin daha önce oturum açmış olması yeterli mi? | Hayır; korumalı istekte etkin hesap koşulu sürer |
| Değerlendirme günü örnek olarak 1 Ekim 2026 seçilirse hangi açık görev gecikmiştir? | Hedef günü 30 Eylül olan `701`; 2 Ekim hedefli `702` henüz gecikmemiştir |

Son satırdaki gün bu alıştırma için seçilmiştir; makinenin bugünkü tarihine bağlı değildir. Gecikme, açık durum ile hedef gününün değerlendirme gününden önce olmasından türetilir; dosyaya üçüncü bir kalıcı görev durumu eklenmez. Geçmiş hedef gününe sahip görev oluşturulabilmesi mevcut kapsamla uyumludur. Okuyucu aynı veriyi başka bir gün için yorumlarsa sonucunu kullanılan günle birlikte kaydetmelidir.

Bu beklentiler, erişim denetimini JSON dosyasının yaptığı anlamına gelmez. Gerçek uygulamada aktör, istek gövdesinden güvenilir kabul edilerek alınmaz; kimlik doğrulama ve sunucunun erişim kararı gerekir. Not oluştururken müşteri yol parametresinden, yazar doğrulanmış aktörden, oluşturma zamanı sunucudan gelir. Görev sahibi de doğrulanmış aktördür. Sentetik dosyadaki alanlar bu ilişkileri görünür kılar; istemcinin sunucu adına bu değerleri belirlemesine izin vermez.

[Bölüm 11'in sentetik verisi](../../assets/examples/chapter24-saas/synthetic-data.json) ise iki kurumlu ayrı SaaS taslağına aittir. İlk MVP verisiyle birleştirilip aynı şemanın sonraki satırları gibi yüklenmemelidir. Benzer biçimde Bölüm 12'teki aday yanıtlar gerçek model çıktısı, Bölüm 13'daki süreler gerçek ekip ölçümü değildir. Dosyanın türü ve ait olduğu senaryo, tek tek değerler kadar önemlidir.

YZ ile veri üretme çalışmasında önce ilişkileri ve beklenen karşı örnekleri tanımlayın. Yeni veri dosyasını özgün öğretim dosyasından ayrı tutun; kimliklerin benzersizliğini, bağlantıların varlığını ve yetki beklentilerini kontrol edin. Daha fazla satır üretmek daha iyi test kapsamı anlamına gelmez. Aynı ada sahip iki müşteri veya aynı başlıklı iki kişisel görev gibi bir karşı örnek, belirli bir hatayı görünür kıldığı için değerlidir.

<a id="ek-e-6"></a>

**E.6. Kurulum Talimatları**

Kuruluma başlamadan önce hedefi seçin: yalnız kitabı okumak, bağımsız bir laboratuvarı çalıştırmak veya gerçek AI-CRM uygulamasını geliştirmek. İlk iş için Markdown okuyabilen bir araç yeterlidir. İkinci iş için ilgili paketin dosyaları ve uygun Python yorumlayıcısı gerekir; Git laboratuvarı ayrıca Git ister. Üçüncü iş, mevcut örneklerin ötesinde karar, geliştirme ve kabul çalışması gerektirir.

**Dosya ve ortamı kontrol etmek**

Aşağıdaki komutlar PowerShell içindir ve **kitap deposunun kökünde** başlatılır. Python olarak hangi yürütülebilir dosyanın seçildiğini görün. Ardından örnek README'sinin gerçekten mevcut olup olmadığını kontrol edin. Dosya eksikse bir sonraki adıma geçmeden önce kullanılan kitap kopyasının E.3'teki durumunu değerlendirin; yalnız eksikliği gidermek için rastgele bir paketi kurmayın.

```powershell
python --version
python -c "import sys; print(sys.executable)"
Test-Path -LiteralPath .\assets\code\chapter18-test-lab\README.md
```

Öğretim laboratuvarlarının mevcut kayıtlarında Python 3.13.7 ile yapılan kontroller bulunur. Bu, bütün Python sürümlerinin doğrulandığı anlamına gelmez. Kitabın **ürün hedefi** Python 3.14, Django 5.2 serisi, PostgreSQL 18 ve Psycopg 3'tür. Bölüm 1'teki aday bağımlılık dosyası `Django>=5.2.8,<5.3` ve `psycopg[binary]>=3,<4` aralıklarını içerir. Bunlar kurulmuş ve kilitlenmiş bir üretim ortamı değildir; gerçek geliştirmede çözümlenen sürümler ayrıca kaydedilir.

**Bağımsız test örneğini çalıştırmak**

İlk deneme için Bölüm 5 laboratuvarını ayrı bir klasöre kopyalamak, özgün öğretim dosyalarını korumayı kolaylaştırır. Aşağıdaki akış daha önce bulunmayan bir geçici hedef seçer. İlk kontrolde README yoksa veya kopyalama başarısızsa sonraki komutları çalıştırmayın. Oluşturulan deneme klasörü otomatik silinmez.

```powershell
$ornekKaynak = (Resolve-Path -LiteralPath .\assets\code\chapter18-test-lab -ErrorAction Stop).Path
$ornekHedef = Join-Path $env:TEMP ("kitap-test-" + [guid]::NewGuid().ToString('N'))
Copy-Item -LiteralPath $ornekKaynak -Destination $ornekHedef -Recurse -ErrorAction Stop
Set-Location -LiteralPath $ornekHedef -ErrorAction Stop
if (Test-Path -LiteralPath .venv) { throw 'Kopyada mevcut .venv var; temiz kaynakla yeni deneme hazırlayın.' }
python -m venv --without-pip .venv
```

Komutları tek tek değerlendirin. Sanal ortam oluşturma işlemi başarısız olursa test aşamasına geçmeyin. Kopyaya daha önce oluşturulmuş bir `.venv` taşınmışsa koruma satırı işlemi durdurur; bu ortam yeniden kullanılmaz. Sanal ortamlar yeni konumda yeniden oluşturulmalıdır. Bu standart kütüphane örneği dış paket gerektirmediğinden `--without-pip` seçilmiştir. Sanal ortamı etkinleştirmek zorunlu değildir; yorumlayıcının açık yolu kullanılabilir (Python Software Foundation, t.y.-b).

```powershell
.\.venv\Scripts\python.exe --version
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
$LASTEXITCODE
```

`unittest discover`, testleri belirtilen başlangıç dizininden keşfeder (Python Software Foundation, t.y.-a). Bu örneğin mevcut normal takımında 18 test yöntemi beklenir. Başarılı tamamlanmada test özeti ve `0` çıkış kodu görülmelidir. `Ran 0 tests` çıktısı, başarılı çıkış verse bile beklenen takımın çalıştığını göstermez. Hata çıktısını atlayıp yalnız son satıra bakmayın; çalıştırma dizini, yorumlayıcı, yöntem sayısı ve başarısızlıkları birlikte değerlendirin.

Beklenti kalitesi deneyi aynı örnek kökünde ayrı çalıştırılır:

```powershell
.\.venv\Scripts\python.exe .\verify_test_quality.py
$LASTEXITCODE
```

Bu deney kasıtlı yanlış işlevi zayıf beklentilerin neden yakalayamadığını gösterir. Beklenen bir assertion reddi deney içinde değerlendirilir; tam deney başarılıysa süreç `0` ile biter. Bu sonucu normal takımdaki 18 yönteme ekleyerek yeni bir toplam test sayısı üretmeyin. Kendi çalışmanızın çıktısını, paketteki önceki doğrulama kaydının yerine geçtiğini varsaymadan tarih ve ortamıyla saklayın.

Diğer Python laboratuvarları için E.2 tablosundan ilgili README'ye geçin. Bölüm 4'ün kasıtlı hatalı varyantı, “bütün komutlar sıfır dönmeli” beklentisiyle kullanılmaz. Bölüm 2 ise yeni deneme depoları oluşturur ve gerçek kitap deposuna commit atmaz; kendi çıktı dizini koşullarını izlemek gerekir. Laboratuvarların birbirinden farklı beklenen davranışlarını tek bir genel başarı kuralıyla değerlendirmeyin.

**Hedef uygulama ortamına geçiş**

Gerçek AI-CRM geliştirmesine hazırlanırken [Bölüm 1 ortam örneği](../../assets/code/chapter14-environment/README.md) ve [Bölüm 10 uygulama sırası](../../assets/examples/chapter23-integration/implementation-sequence.md) birlikte okunur. Önce hedef Python kurulumu, sanal ortam ve bağımlılıklar doğrulanır; sonra kullanıcı modeli, oturum, veri modeli ve API kararları gerçek uygulamada somutlaştırılır. `requirements.in` dosyasını kurmak kendi başına Django projesi, veritabanı veya kullanıcı hesabı oluşturmaz.

Mevcut kitap deposunda bütünleşmiş ürüne ait `manage.py`, çalışır müşteri/not/görev sunucusu, gerçek migration dizisi veya ürün CI/CD akışı bulunmaz. Bu yüzden bu ekte varsayımsal `migrate`, hesap oluşturma veya sunucu başlatma komutları tamamlanmış kurulum adımları olarak verilmemiştir. Ürün kaynakları hazırlandığında bu kısım gerçek dosya yolları, ortam değişkenleri, örnek veri yükleme yöntemi ve doğrulanmış başlatma adımlarıyla güncellenmelidir.

macOS/Linux üzerinde sanal ortamın yorumlayıcı yolu genellikle `./.venv/bin/python` biçimindedir; yukarıdaki PowerShell klasör ve değişken komutları Bash/zsh'ye aynen yapıştırılmaz. İşletim sistemi değiştiğinde ilgili ortam açıklamasını izleyin. Yeni ortamın test çıktısını eski Windows doğrulamasının kopyası gibi sunmayın.

**Kurulum kaydı:** Denenen paket yolu, kitap commit'i varsa kimliği, yerel değişiklik durumu, işletim sistemi, Python sürümü, çalıştırılan komut, yöntem sayısı, çıkış kodu ve açık sorunlar birlikte kaydedilir. YZ'den yardım alınırsa bu sınırlı bağlam yeterli olabilir; gerçek sırlar veya müşteri verisi eklenmez. Bir hata için önerilen çözüm uygulandıktan sonra aynı kontrol yeniden yürütülür ve gözlenen sonuç yazılır. Bu ek hazırlanırken hedef ürün kurulumu veya yeni bir ürün testi yapılmamıştır.

<a id="ek-e-kaynakca"></a>

**Kaynakça**

Depo durumu, dosya envanteri ve commit eşleştirmeleri 6 Ekim 2026 tarihli yerel incelemeye dayanır. Öğretim paketlerinin önceki test sonuçları kendi README ve doğrulama kayıtları üzerinden aktarılmıştır; bu ekte yeni çalıştırılmış ürün testi olarak sunulmaz. Aşağıdaki resmî belgeler aynı tarihte kontrol edilmiştir. Tarihsiz kayıtlar kurum içinde başlık sırasına göre a/b ile ayrılmıştır.

Git Project. (t.y.-a). [*git-log*](https://git-scm.com/docs/git-log). Erişim tarihi: 6 Ekim 2026.

Git Project. (t.y.-b). [*git-status*](https://git-scm.com/docs/git-status). Erişim tarihi: 6 Ekim 2026.

Python Software Foundation. (t.y.-a). [*unittest — Unit testing framework*](https://docs.python.org/3.14/library/unittest.html). Python 3.14 documentation. Erişim tarihi: 6 Ekim 2026.

Python Software Foundation. (t.y.-b). [*venv — Creation of virtual environments*](https://docs.python.org/3.14/library/venv.html). Python 3.14 documentation. Erişim tarihi: 6 Ekim 2026.
