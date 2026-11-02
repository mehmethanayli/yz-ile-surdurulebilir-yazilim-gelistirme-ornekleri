# Bölüm 6 — Yerel Güvenlik Laboratuvarı

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[Kitap 2, Bölüm 6 eşleştirmesi](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-6).

Bu bağımsız öğretim örneği, etkin hesap ve görev sahipliğini, parametreli SQL ile kayıt kapsamının ayrımını ve sabit HTML paragrafındaki metin kodlamasını gösterir. AI-CRM uygulaması veya hazır güvenlik katmanı değildir. Önceki bölüm örnekleri değiştirilmemiştir.

## Çalıştırma

Bu klasörde seçtiğiniz Python yorumlayıcısıyla çalıştırınız:

```powershell
python -m unittest discover -s tests -v
```

14 benzersiz test yöntemi vardır: sekiz sahiplik/durum, dört sorgu ve iki çıktı kontrolü. Alt senaryolar yöntem sayısına eklenmez. Testler kurulu Python 3.13.7 ve aynı sürümün pip içermeyen ayrı sanal ortamında geçmiştir. Yerel SQLite kitaplığı 3.50.4'tür. Dış paket eklenmemiştir.

## Güven sınırı

`Actor` ve `Task`, doğrulanmış sunucu kimliği ve sunucudan alınmış kayıt varsayımı taşır. Bu sınıflar istek gövdesinin doğrulayıcısı değildir. İstemciden gelen kimlik veya etkinlik alanlarını bu nesnelere aktararak güvenilir kimlik üretilemez. Gerçek HTTP, oturum ve veri erişim katmanı ayrıca kurulmalıdır.

`complete_task`, izin varsa yeni bir tamamlanmış nesne döndürür; kaynak nesneyi değiştirmez. Tamamlanmış nesnenin tekrar tamamlanması aynı durum değerini korur. Bu dar nesne davranışı gerçek API istek kimliği, kalıcı transaction veya eşzamanlılık garantisi değildir.

`find_own_tasks`, önce etkin kimlik koşulunu değerlendirir, ardından hem sahip hem başlık değerini parametre olarak bağlar. Aynı başlıklı iki kullanıcının kayıtları test edilir. Kesme işaretli meşru başlık korunur; sorgu benzeri sentetik metin ek satır açmaz. Test veritabanı yalnızca `:memory:` SQLite'tır ve her testin sonunda bağlantı kapanır. Hedef PostgreSQL seçimi değiştirilmez.

`render_note_text`, yalnızca sabit `<p>` öğesinin metin içeriği içindir. HTML öznitelikleri, URL, JavaScript veya CSS için genel kodlayıcı değildir. Django'nun şablon kaçışı yerine eklenmiş değildir. Üretilen dizeler sınanmıştır; tarayıcı çalıştırılmamış ve genel XSS güvenliği kanıtlanmamıştır.

## Sonuç ve açık işler

[verification.json](verification.json), gerçek çalışma bağlamını ve LF'ye normalleştirilmiş UTF-8 kaynak özetlerini saklar. Bu özetler içerik eşleştirme içindir; imza veya güvenlik sertifikası değildir. İki ortamda aynı 14 yöntemin geçmesi 28 farklı kontrol anlamına gelmez.

Python 3.14, Django/PostgreSQL, gerçek oturum, parola saklama, CSRF, tarayıcı, eşzamanlılık, kota, bağımlılık taraması ve CI/CD sınanmamıştır. Gİ-19-01 bunları ürün uygulamasına taşır. Yerel testlerin geçmesi tam ürün güvenliği veya ASVS uygunluğu iddiası oluşturmaz.
