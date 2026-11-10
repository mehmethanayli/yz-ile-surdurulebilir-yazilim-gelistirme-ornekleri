# Kitap 2 Bölüm 7 — Gizlilik, Etik, Lisans ve Hukuki Sorular

**Sentetik inceleme örnekleri**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[VLS-20-01](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-7), veri paylaşımı, lisans kökeni ve insan sorumluluğunu birlikte düşünmek için hazırlanmıştır. [review-cases.json](review-cases.json) dört öğretim senaryosu içerir. Veriler baştan kurgulanmıştır; gerçek kaydın maskelenmiş veya anonimleştirilmiş sürümü değildir.

| Senaryo | İncelenen konu | Beklenen okuma |
|---|---|---|
| D20-01 | Kaynak inceleme bağlamı | A etkin sahip, B başka etkin kullanıcı; A erişir, B reddedilir |
| D20-02 | Gereksiz alanların çıkarılması | A/B sahiplik farkı ve T1 görevi korunur |
| L20-03 | Kökeni belirsiz bileşen | Tamamen kurgusal ad; sürüm, kaynak ve lisans bilinmiyor |
| R20-04 | İnsan görevleri | Rol adları var; gerçek kişi veya verilmiş onay yok |

`null` bilinmeyen veya henüz atanmamış bilgidir. `false` değerleri yanında alan adı okunmalıdır: örneğin `external_transfer_performed: false` aktarım yapılmadığını, `legal_approval: false` hukuki onay verilmediğini belirtir. Bunlar gerçek bir kuruma yönelik ret kararı değildir.

D20-02'de `customer_label`, `contact_placeholder` ve `note` alanları amaç için gereksiz bulunduğundan önerilen bağlama alınmamıştır. Bu örnek genel amaçlı kişisel veri algılama veya anonimleştirme algoritması değildir. Eşitlik ve farklılık ilişkilerinin korunması, sahiplik sorusunun anlaşılabilmesini sağlar. Gerçek kullanıcı kimliğini istemci girdisinden kabul etme yöntemi önerilmez.

L20-03 gerçek paket önerisi değildir; hiçbir bileşen kurulmamış, ürüne eklenmemiş veya lisanslandırılmamıştır. Kaydın gelecekte doldurulması için gerçek bileşen ve kullanım biçimi seçilmelidir. R20-04 operasyonel görevleri gösterir; tarafların hukuki sorumluluğunu belirlemez.

## Yapılan kontrolün kapsamı

[verification.json](verification.json), dört kaydın kimlikleri, gerekli alanları, A/B/T1 ilişkileri, çıkarılan alanlar, bilinmeyen lisans alanları ve yapılmamış onayları için yürütülen dosya kontrollerini kaydeder. `review-cases.json` dosyasının SHA-256 özeti UTF-8 metin ve LF satır sonlarına göre hesaplanmıştır. Dosya değiştirilirse eski kontrol kaydı güncel içerik için kanıt sayılmaz.

Kontrol; gerçek kişisel veriyi tespit etmez, anonimlik ölçmez, lisans uygunluğu kararı vermez, kurum veya uzman onayı oluşturmaz. Dış hizmete aktarım yapılmamıştır. Bu klasörde çalıştırılabilir uygulama veya ürün test paketi yoktur. Bölüm 6'nın yerel güvenlik testleri bu çalışma için yeniden çalıştırılmamıştır.

## Okuyucu çalışması

Önce dört kaydı okuyunuz. Her senaryo için amaç, eldeki kanıt ve eksik kararları kendi cümlelerinizle açıklayınız. Ardından gerçek veri kullanmadan başka bir sentetik sahiplik örneği kurunuz. Minimizasyonun güven varsayımını veya beklenen ret nedenini silip silmediğini kontrol ediniz. Gerçek bir kurumda uygulama yapılacaksa sağlayıcı, sözleşme, paylaşım yetkisi ve sorumlu kişiler ayrıca değerlendirilmelidir.
