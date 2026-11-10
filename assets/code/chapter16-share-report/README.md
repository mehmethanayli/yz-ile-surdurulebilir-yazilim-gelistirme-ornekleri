# Kitap 2 Bölüm 3 — AI ile Kod Geliştirme Stratejisi

**Ortam raporunun isteğe bağlı paylaşım görünümü**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[Kitap 2, Bölüm 3 eşleştirmesi](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-3).

Bu örnek, [Bölüm 1 betiğinin](../chapter14-environment/README.md) ayrı öğretim kopyasıdır. Eski dosyaları değiştirmez. Normal raporun alanları ve ayar kuralları korunur; yeni `--share` seçeneği yerel yolları içermeyen, açık şemalı JSON üretir. Seçenek yalnızca stdout içeriğini değiştirir; dosya göndermez, ağ isteği yapmaz, paket kurmaz veya veritabanına bağlanmaz. `.env` yüklemez.

## Davranış sözleşmesi

- Bayrak yoksa proje kökü, çalışma dizini ve Python yürütülebilir dosyası dahil sekiz üst alan kalır.
- `--share` ile yalnızca `python_version`, `in_virtualenv`, `python314`, `settings` ve `packages` alanları bulunur.
- `settings` yalnızca `app_env` ve `debug`; `packages` yalnızca `Django` ve `psycopg` içerir.
- Yardımcı dönüşüm tam raporu değiştirmez; alt sözlükleri yeni oluşturur. Yaprak değerler bu uygulamada metin, boolean veya `None` türündedir.
- Geçersiz ayarlar `2` çıkışıyla ve boş stdout ile reddedilir. `--require-target`, paylaşım seçeneğiyle birlikte de Python 3.14 ve sanal ortam koşulunu değerlendirir; koşul yoksa `1` döner.
- Genel anonimleştirme garantisi verilmez. Kalan sürüm ve yapılandırma bilgileri paylaşmadan önce gözden geçirilir. Bayrağı kullanmak gerçek hedef ortam kurulumunun kanıtı değildir.

## Çalıştırma

PowerShell'de bu örneğin kökünde, kullanmak istediğiniz Python yorumlayıcısını seçerek:

```powershell
python .\scripts\inspect_environment.py
python .\scripts\inspect_environment.py --share
python .\scripts\inspect_environment.py --share --require-target
```

Komutları ayrı değerlendiriniz. Son çağrı hedef dışı yorumlayıcıda JSON üretebilir ve yine `1` dönebilir. Çıkış kodunu hemen ardından `$LASTEXITCODE` ile okuyabilirsiniz. Yeni paket kurulumu gerekmez. Doğrulama Python 3.13.7'de yapılmıştır; kitabın Python 3.14 hedefi bu çalışmada kurulmuş sayılmaz.

```powershell
python -m unittest discover -s tests -v
python .\verify_review_examples.py
```

İlk komut 15 benzersiz test yöntemini çalıştırır: dokuz eski davranış testi ve altı yeni test. Alt senaryolar ayrı test yöntemi sayılmaz. Testler örnek kökü altında benzersiz geçici klasör açar; temizleme yolunun kök içinde olduğunu doğrulayarak bu klasörleri kaldırır. Örnek kökü test sırasında yazılabilir olmalıdır.

İkinci komut üç kasıtlı yanlış öneriyi sentetik test içinde dener: tam raporu döndürme, yalnızca üst alanları seçme ve giriş sözlüğünü değiştirme. Her öneride sözleşme testinin beklenen doğrulama hatasını üretmesi gerekir. Betik bu retleri başarılı kontrol olarak raporlar; normal testlerin başarısızlığını gizlemez. Diskteki uygulama kodunu değiştirmez. Bu adaylar belirli bir YZ modelinden alınmış ölçüm örnekleri değildir.

## Dosyalar ve kanıt

`change.diff`, iki bölümün inceleme betikleri arasındaki metin karşılaştırmasıdır; gerçek commit veya PR farkı değildir. Yeni test dosyası ve README ayrıca okunmalıdır. `baseline.json`, karşılaştırılan Bölüm 1 kaynaklarının özetlerini içerir. `verification.json`, gerçekten kullanılan sürümü, test sayısını, kapsam dışı işleri ve sınanan Python dosyalarının SHA-256 değerlerini kaydeder. Her iki kayıtta da SHA-256, satır sonları LF biçimine normalleştirilmiş UTF-8 metin üzerinden hesaplanır. Böylece Windows ve Linux satır sonları aynı içerik için farklı özet üretmez. Özet değerleri imza veya güvenilir yazar kanıtı değildir.

Bütünleşmiş AI-CRM sunucusu, gerçek kullanıcı verisi, Python 3.14/Django/PostgreSQL hedef ortamı, CI/CD ve yayın bu örneğin kapsamı dışındadır. GK-16-01, öğretim değişikliğinin tamamlanmasıyla ürün ortamının hazır olmasını ayrı kaydeder.
