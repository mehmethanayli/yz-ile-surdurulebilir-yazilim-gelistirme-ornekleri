# Bölüm 4 — Hata Ayıklama Laboratuvarı

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[Kitap 2, Bölüm 4 eşleştirmesi](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-4).

Bu örnek kasıtlı bir boolean dönüşüm kusurunu yeniden üretir. `settings_faulty.py` öğretim için yanlıştır; ürün ayarı olarak kullanılmaz. `settings_fixed.py`, Bölüm 3'ün doğru `read_settings` işlevini korur. Önceki bölüm dosyaları değiştirilmemiştir. Yeni dış paket, ağ, veritabanı, gerçek kullanıcı verisi veya kurulum işlemi yoktur.

Komutlar bu klasörde çalıştırılır. `python`, seçtiğiniz yorumlayıcıdır. Gerçek süreç ortamındaki APP_ENV/APP_DEBUG değerleri ve `.env` okunmaz; komut argümanları sentetik bir sözlüğe dönüşür. `production` etiketi canlı ortama bağlanmaz. Örnek sabit sayıda küçük girdi için hazırlanmıştır.

## Önce / sonra

```powershell
python .\reproduce.py --variant faulty --app-env production --debug false
$LASTEXITCODE
python .\reproduce.py --variant fixed --app-env production --debug false
$LASTEXITCODE
```

İlk komut stderr'e `APP_DEBUG must be false in production.` yazar; stdout boş, çıkış `2` olur. Bu beklenen öğretim başarısızlığıdır. İkinci komut `{"app_env": "production", "debug": false}` JSON'unu stdout'a yazar ve `0` döner. `$LASTEXITCODE`, hemen önceki yerel programın kodunu gösterir.

```powershell
python .\reproduce.py --variant faulty --app-env test --debug false
python .\minimal_repro.py
python .\reproduce.py --variant fixed --debug true
```

Test etiketinde hatalı sürüm `debug: true` üretir ve `0` ile biter; exception olmaması doğruluk değildir. Minimal örnek `'false' True False` yazar. Son komut üretimde gerçek true değerini reddederek `2` döner; doğru sürüm korumayı kaldırmaz.

## Çağrı izi ve debugger

```powershell
python .\reproduce.py --variant faulty --trace
python -m pdb .\reproduce.py --variant faulty --trace
```

İlk komut exception'ı yakalamaz; yerel Python 3.13.7 denemesinde traceback ve `1` çıkışı gözlenmiştir. İkinci komut etkileşimlidir: ilk duruşta `c`; hata sonrası `where`, `p raw_debug`, `p debug`; çıkış için `q` kullanılır. Son çerçevede ham değer `'false'`, yanlış boolean `True` görünür. Debugger'ın kendi çıkış kodu örnek programın iş başarısı olarak yorumlanmaz.

İlk kurulu yorumlayıcıyla pdb denemesinde, örnek mantığı başlamadan `readline.backend` için AttributeError oluşmuştur. Aynı komut, Python 3.13.7'nin pip içermeyen ayrı sanal ortamında başarıyla incelenmiştir. Kurulu ortamın readline sorunu onarılmamıştır. [Oturum kaydı](pdb-session.txt) yolları yer tutucularla gösterir; kayıt stdout ve stderr'i ayrı yakalayıp ardışık sunar, zaman sırası iddiası taşımaz. Normal çalıştırmanın traceback'i yerel yollar içerir; paylaşmadan önce inceleyiniz.

## Günlük ve testler

```powershell
python .\reproduce.py --log
python -m unittest discover -s tests -v
```

`--log`, sınırlı olay bilgisini stderr'e ekler. Normal JSON stdout'ta kalır. Geçersiz ham değer mesajda veya bu günlük kaydında tekrar edilmez. `--trace` özellikle yakalamayı atladığı için hata durumunda olağan `settings_rejected` log yolu da atlanır; seçeneklerin amacı farklıdır.

12 test yöntemi iki Python 3.13.7 bağlamında geçmiştir. Normalleştirme, varsayılanlar, altı ortam/debug birleşimi, on geçersiz değer, kasıtlı kusurun yeniden üretimi, komut çıktıları, korumanın sürmesi, çağrı zinciri, sınırlı log ve beklenmeyen RuntimeError'ın gizlenmemesi kontrol edilir. Alt senaryolar ayrı test yöntemi sayılmaz. Yanlış varyantın beklenen yanlış sonucu verdiğini kontrol eden testin geçmesi, yanlış kodun doğru olduğu anlamına gelmez.

[fix.diff](fix.diff) yalnızca iki `read_settings` fonksiyonunu karşılaştırır; dosyaların öğretim docstring'lerini veya gerçek bir PR'ı temsil etmez. [verification.json](verification.json), ortam ve kapsamı kaydeder. SHA-256 değerleri LF'ye normalleştirilmiş UTF-8 metin üzerinden hesaplanır; imza veya kaynak kimliği kanıtı değildir.

Python 3.14, tarayıcı, Django/PostgreSQL, AI-CRM davranışı, CI/CD ve yayın doğrulanmamıştır. HA-17-01 yalnızca bu yerel öğretim kusurunun araştırılması ve doğru varyantın belirtilen sözleşmesiyle sınırlıdır.
