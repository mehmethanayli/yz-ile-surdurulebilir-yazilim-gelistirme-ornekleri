# Kitap 2 Bölüm 2 — Git ve Sürüm Kontrolü

**Yerel Git laboratuvarı**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Örnek klasörleri Kitap 2’nin bölüm numaralarını, GO-14-01 gibi kayıt kimlikleri ilk çalışma numaralarını kullanır.

[Kitap 2, Bölüm 2 eşleştirmesi](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-2).

Bu betik yalnızca **yeni bir çıktı klasöründe** sentetik dosyalı Git depoları oluşturur. Kitap deposunu commit etmez, gerçek uzak depoya bağlanmaz ve uygulama geliştirmez. Çıktı klasörü zaten varsa işlem başlamadan reddedilir; yeniden çalıştırmak için yeni ad seçilir. Betik oluşturduğu dosyaları silmez.

## Çalıştırma

Python ve Git komut satırında erişilebilir olmalıdır. Doğrulamada Python 3.13.7 ve Git 2.51.0.windows.1 kullanılmıştır. Kitabın Python 3.14/Django hedef kurulumu bu örnek için yapılmış sayılmaz; standart Python kütüphanesi Git süreçlerini yürütür.

Uygulama deposunun kökünde, daha önce bulunmayan bir deneme hedefi seçerek PowerShell'de:

```powershell
python .\assets\code\book-2-chapter-02-git-lab\run_lab.py --output "$env:TEMP\kitap-git-denemesi-01"
```

Çıktı hedefi sizin yazabildiğiniz bir konum olmalıdır. Kısıtlı çalışma araçlarında Git'in kabuk süreçlerini başlatması ayrıca engellenebilir; bu hata Git kavramı testinin başarısızlığıyla karıştırılmaz. Böyle bir durumda izin verilen yerel deneme ortamı kullanılır; sıradan projelerin kontrolleri veya makine güvenliği topluca kapatılmaz.

Bütün kontroller geçerse süreç `0` ile biter ve `results.json` oluşur. Bu dosya sürümleri, 28 kontrol adını ve yürütülen komutların çıkış kodlarını içerir. Beklenen başarısız işlemler de vardır: örneğin ayrışmış push reddedilir. Betik bunların beklenen sonuçlarını değerlendirir; herhangi bir başarısız komutu atlayıp başarı saymaz. İlk hatada durur, yürütülen çağrıları `commands-before-failure.json` dosyasına yazar. Eksik Git gibi daha erken önkoşul sorunlarında tamamlanmış sonuç dosyası bulunmaz.

## Oluşan yapı

```text
secilen-yeni-klasor/
├── author/                 # Yazar çalışma deposu
├── remote.git/             # Yerel bare paylaşım hedefi
├── peer/                   # İkinci çalışma kopyası
├── empty.gitconfig         # Denemeye özel boş global ayar kaynağı
├── empty-hooks/            # Yalnızca yeni depolar için
├── empty-template/         # Kişisel init şablonundan bağımsızlık
└── results.json            # Başarılı çalışmanın sonuçları
```

Ayar izolasyonu yalnızca alt Git süreçleri ve yeni deneme depoları içindir. Kişisel global Git dosyaları değiştirilmez. Sentetik yazar kimliği `git-lab@example.invalid` adresini kullanır. Git ağ protokolleri bu süreçlerde kapalıdır; yalnızca yerel dosya protokolü açıktır. Gerçek projenin hook veya imza kurallarını devre dışı bırakma önerisi değildir.

## Neler doğrulanır?

Index'in anlık içeriği; staged/unstaged farkı; unstage; fast-forward ve merge commit; yerel clone/fetch/pull/push; ayrışmış aktarımların reddi; çatışma, abort ve çözüm; belirli dosyada restore; yeni kayıtla revert; açıklamalı etiket aktarımı; ignore kuralının izlenen dosyayı geriye dönük çıkarmaması; soft reset ve reflog üzerinden başvuru oluşturma kontrol edilir.

`lab-v0.1.0` etiketi deneyin bir ara kontrol noktasını gösterir; sonradan yapılan bütün alıştırmaları içermez ve AI-CRM sürümü değildir. Son çalışma çizgisi `codex/reset-demo` olur; `codex/recovered-draft` önceki taslak kaydına erişimi korur. Yerel çizgiler ile bare hedefin bütün deney boyunca aynı kalması beklenmez. Sonuç dosyasındaki her kontrol kendi aşamasının gözlemidir.

[Doğrulama özeti](verification.json), kitabın hazırlanmasında tamamlanan çalışmanın sürümlerini ve sonuçlarını içerir. Bilgisayara özgü yolları ve ayrıntılı komutları içermez. Kendi çalışmanızın sonucu yeni çıktı klasöründedir. Gerçek GitHub erişimi, PR, release, branch koruması, CI/CD ve ürün testleri bu doğrulamanın kapsamı dışındadır.
