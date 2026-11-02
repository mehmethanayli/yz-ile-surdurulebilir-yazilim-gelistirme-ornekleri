# YK-21-01 — Ortamdan bağımsız işlem yönergesi

Bu yönerge masa başı inceleme içindir. Komut yürütmez, yeni yetki vermez ve başarılı deployment kaydı değildir. [Plan dosyası](release-plan.json) ile birlikte okunur.

| Sıra | İşlem | Beklenen kanıt | Durma koşulu |
|---|---|---|---|
| 1 | Aday ve hedefi tanımla | Revizyon, artifact, gerçek ortam kimliği | Kimlik belirsiz veya tutarsız |
| 2 | K01–K12 önkoşullarını değerlendir | Doğru adaya bağlı gerekli kanıt ve kararlar | Gerekli koşul bekliyor/başarısız |
| 3 | Mevcut durumu ve kurtarma yolunu kaydet | Etkin sürüm, şema ve kurtarma bilgisi | Geri dönüş etkisi bilinmiyor |
| 4 | Uyumlu şema/yapılandırma sırasını uygula | İncelenmiş işlemlerin gerçek sonucu | Hata veya beklenmeyen veri etkisi |
| 5 | Yeni süreci hazırla | Doğru artifact, ayar ve readiness sonucu | Süreç trafik almaya hazır değil |
| 6 | Trafiği seçilen yöntemle geçir | Yönlendirme ve devam eden isteklerin durumu | Eski-yeni uyumu veya kapasite bozuluyor |
| 7 | S01–S04 yayın sonrası kontrollerini yürüt | Gerçek uç nokta, erişim ve gözlem sonuçları | Kritik davranış veya erişim hatası |
| 8 | Kabul veya müdahale kararını kaydet | Sonuç, sorumlu, zaman ve açık işler | Kayıt ile gerçek sonuç çelişiyor |

Adım 4 her migration'ın bütün yayınlardan önce yapılması gerektiği anlamına gelmez. Gerçek değişiklik için eski-yeni kod ve şema uyumu belirlenerek adım ayrıntılandırılır. K07 bunun provasını, adım 4 ise gerçek ortamda uygulanacak sırayı temsil eder.

R21-01 trafik öncesi hazır olamama; R21-02 uyum kanıtı gerektiren kod dönüşü; R21-03 şema/veri uyumsuzluğunda ileri düzeltme veya kontrollü kurtarma değerlendirmesidir. Senaryolar yaşanmamış ve provası yapılmamıştır. İptal edilen işin dış etkileri kendiliğinden geri alınmış sayılmaz.

Yazma içeren smoke kontrolü gerekiyorsa yetkili deneme hesabı, sentetik kayıt, temizleme ve beklenmeyen etki planı önceden eklenmelidir. Mevcut örnek, gerçek müşteri kaydına yazma talimatı içermez. Gözlem süresi, kesinti hedefi ve kabul edilebilir veri kaybı ürün/işletim kararıdır; rastgele değer atanmaz.
