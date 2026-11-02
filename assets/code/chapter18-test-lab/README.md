# Bölüm 5 — Test Laboratuvarı

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[Kitap 2, Bölüm 5 eşleştirmesi](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-5).

Bu klasör, Bölüm 3'ün rapor betiği ve 15 testinin ayrı öğretim kopyasıdır. Üç yeni test, paket metadata okuyucusunun kontrollü sonuçlarını sınar. Uygulama betiği değiştirilmemiştir; yeni ürün davranışı veya dış bağımlılık eklenmez. quality_examples altındaki yanlış/doğru fonksiyonlar Bölüm 4'ten korunmuştur. Önceki bölüm dosyaları değiştirilmemiştir. Gerçek projede her özellik için uygulamayı çoğaltma önerisi değildir.

## Normal test takımı

Komutları bu klasörde çalıştırınız. `python` seçtiğiniz yorumlayıcıdır; sürüm ve ortamı ayrıca kontrol ediniz.

```powershell
python -m unittest discover -s tests -v
```

18 benzersiz yöntem çalışır: 15 korunmuş yöntem ve üç metadata sonucu testi. Fonksiyon testleri ve gerçek alt süreç çağrıları vardır; tarayıcı veya veritabanı yoktur. Alt senaryolar yöntem sayısına eklenmez. Paket metadata testindeki `5.2.8` sentetik cevaptır; gerçek Django kurulumu kanıtı değildir. `PackageNotFoundError` ve beklenmeyen `RuntimeError` ayrı değerlendirilir.

Alt süreç testleri APP_ENV ve APP_DEBUG değerlerini kontrollü olarak kurar. Geçici dizinler yalnızca örnek kökü altında oluşturulur ve temizlenmeden önce kök sınırı doğrulanır. Bu nedenle test sırasında örnek klasörü yazılabilir olmalıdır. Testlerin kullandığı ayrı süreç ortamları kabuğun kalıcı ayarlarını değiştirmez.

## Beklenti kalitesi deneyi

```powershell
python .\verify_test_quality.py
```

Bu komut normal 18 testten ayrıdır. Dört zayıf kontrolün bilerek hatalı fonksiyondan geçtiğini, bağımsız false beklentisinin aynı fonksiyonu reddettiğini ve doğru fonksiyonda geçtiğini doğrular. Beklenen tek assertion başarısızlığı deney içinde yakalanır; komut yalnızca bütün deney koşulları sağlandığında `0` döner. Hatalı işlevin doğru olduğu veya bir modelin gerçek çıktısının ölçüldüğü iddia edilmez.

Yerel CPython 3.13.7 çalışmasında yanlış fonksiyonun gövdesindeki on deyim başlangıç satırının tamamına ulaşılmıştır. Payda AST'deki bu tek fonksiyona ait statement başlangıçlarıdır; `def` satırı ve modül docstring'i dâhil değildir. sys.settrace yalnızca o fonksiyonun line olaylarını toplar; önceki trace işlevi finally ile geri yüklenir. Bu dar öğretim ölçümü genel kapsam aracı, dal/yol kapsamı veya Coverage.py raporu değildir. Coverage.py kurulu değildir ve eklenmemiştir.

[quality-result.json](quality-result.json) gerçek deney sonucunu saklar. Dört zayıf kontrol ve iki varyantta yürütülen tek bağımsız kontrol normal test sayısına eklenmez. Seçilmiş satırlara ulaşmak ile sonuç anlamını denetlemek ayrı şeylerdir.

## Dar başlangıç kontrolü

```powershell
python .\scripts\inspect_environment.py --share
$LASTEXITCODE
```

Geçerli APP_ENV/APP_DEBUG süreç ayarlarıyla JSON ve `0` beklenir. Betik `.env` yüklemez. --share yalnızca çıktının alanlarını seçer; dış hizmete dosya göndermez ve genel anonimlik garantisi vermez. `--require-target` verilmediği için bu komut Python 3.14 koşulunu zorunlu tutmaz. Yardım çıktısı veya temel rapor başarısı hedef ürünün hazır olduğunu göstermez.

## Doğrulama sınırı

18 test yöntemi kurulu Python 3.13.7 ve aynı sürümün pip içermeyen ayrı sanal ortamında geçmiştir. Kalite deneyi kurulu Python 3.13.7 üzerinde yürütülmüştür. [verification.json](verification.json), ortam, kapsam ve LF'ye normalleştirilmiş UTF-8 metnin SHA-256 özetlerini taşır. Özet değerleri imza veya yazar kimliği kanıtı değildir.

Python 3.14, Django/PostgreSQL, tarayıcı akışı, gerçek AI-CRM erişim ve kayıt davranışı, eşzamanlılık, CI/CD ve yayın sınanmamıştır. TS-18-01 bu hedefleri uygulama öncesi strateji olarak tutar. Yerel laboratuvarın geçmesi bu açık işleri kapatmaz.
