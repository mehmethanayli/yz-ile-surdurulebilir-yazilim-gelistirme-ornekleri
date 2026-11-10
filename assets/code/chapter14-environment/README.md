# Kitap 2 Bölüm 1 — Geliştirme Ortamını Anlamak

**Bağımsız ortam örneği**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[Kitap 2, Bölüm 1 eşleştirmesi](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-1).

Bu klasör AI-CRM sunucusu değildir. Standart kütüphaneli inceleme betiği yorumlayıcıyı, çalışma dizinini, sanal ortamı ve yalnızca APP_ENV/APP_DEBUG ayarlarını raporlar. `.env` okumaz, paket kurmaz, ağa veya veritabanına bağlanmaz. Paket sürümünün görünmesi çalışabilirlik testi değildir.

Klasörü ayrı bir deneme konumuna kopyalayın ve PowerShell'de o köke geçin. Python 3.14'ün kurulu ve `py -3.14` ile seçilebilir olması gerekir. Var olan `.venv` üzerine kurmayın; önce kullanılan yorumlayıcıyı kontrol edin. Etkinleştirme veya yürütme politikası değişikliği gerekmez.

```powershell
py -3.14 --version
py -3.14 -m venv .venv
.\.venv\Scripts\python.exe -m pip --version
.\.venv\Scripts\python.exe .\scripts\inspect_environment.py --require-target
```

Betiğin 0 çıkışı, bu çağrıda ayarların geçerli, Python serisinin 3.14 ve ortamın sanal olduğunu gösterir. Django/PostgreSQL hazır olma kanıtı değildir. Hedef dışı yorumlayıcı/sanal ortam için 1, geçersiz yapılandırma için 2 döner. Bayrak olmadan geçerli ayarlarda hedef dışı sürüm de bilgi raporlayabilir.

İstenirse, yalnızca bu deneme ortamında aday paketleri kurma akışı:

```powershell
.\.venv\Scripts\python.exe -m pip install -r requirements.in
.\.venv\Scripts\python.exe -m pip check
.\.venv\Scripts\python.exe -m django --version
.\.venv\Scripts\python.exe -c "import psycopg; print(psycopg.__version__)"
.\.venv\Scripts\python.exe -m pip freeze | Set-Content -Encoding utf8 requirements.resolved.txt
```

Komutları tek tek yürütün; başarısız adım sonrası devam etmeden nedeni inceleyin. `requirements.in` sürüm aralıklarını taşır. Üretilen `requirements.resolved.txt` kurulmuş paketlerin kaydıdır; tam ve platformlar arası bir kilit dosyası sayılmaz. Bu dosya hedef kurulum yapılmadan depoya uydurma içerikle eklenmemiştir. Gerçek kurulumda Python, pip, işletim sistemi ve mimari de kaydedilir. Psycopg binary seçeneği yerel kolaylık içindir; üretim paketleme kararı değildir.

```powershell
$env:APP_ENV = 'development'
$env:APP_DEBUG = 'false'
.\.venv\Scripts\python.exe .\scripts\inspect_environment.py
```

Değerler süreç ortamından okunur. Eksik ayarlarda development ve false kullanılır; boş/yanlış değerler reddedilir. Yalnızca true/false kabul edilir; production ile true reddedilir. Bu, Django ayarlarının kendisi değil, ayar okuma öğretimidir. Gerçek sırlar bu örneğe konulmamalıdır. Paylaşılan çıktıda yerel kullanıcı dizini de gözden geçirilir.

macOS/Linux için Python 3.14 mevcutsa `python3.14 -m venv .venv` kullanılır; sonraki yorumlayıcı yolu `./.venv/bin/python` olur. PowerShell değişken sözdizimi Bash/zsh ile aynı değildir.

**Doğrulama:** Yerel kontrol kapsamı bölüm sonundaki GO-14-01 kaydında belirtilir. Python 3.14 hedef kurulumu ve Django/PostgreSQL bütünleşmesi burada yapılmış sayılmaz.


Testleri örnek kökünde aynı yorumlayıcıyla çalıştırma:

```powershell
.\.venv\Scripts\python.exe -m unittest discover -s tests -v
```

Dokuz test yöntemi varsayılanları, altı ortam/debug birleşimini, normalleştirmeyi, on geçersiz değeri, farklı çalışma dizinini, hata/çıkış davranışını, gereksiz ortam değerlerinin çıktıya alınmamasını ve örtük `.env` yüklenmemesini sınar. Hedef sürüm testi gerçekten kullanılan yorumlayıcıyı değerlendirir; Python 3.14 kurulmuş gibi davranmaz.
