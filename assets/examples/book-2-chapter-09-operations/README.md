# Kitap 2 Bölüm 9 — Production Sonrası Hayat

**İşletim planı ve sentetik ölçümler**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Örnek klasörleri Kitap 2’nin bölüm numaralarını, GO-14-01 gibi kayıt kimlikleri ilk çalışma numaralarını kullanır.

Bu örnek **İB-22-01 — İşletim ve Bakım Kaydı**dır. [Bölüm 9](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-9) ile birlikte okunur. AI-CRM henüz hedef ortamda yayımlanmamıştır. Gerçek izleme, yedekleme, restore, güncelleme, incident veya kullanıcı bildirimi gerçekleştirilmez.

## Dosyalar

- [operations-plan.json](operations-plan.json): beş gözlem tanımı, altı restore ölçütü ve altı olay yönetimi adımı. Hedefler, ortam ve sorumlu kişiler bilinmiyor; kanıt alanları boştur.
- [measurement-examples.json](measurement-examples.json): yalnızca üç sentetik aritmetik örneğinin girdileri ve varsayımları.
- [verification.json](verification.json): yerel hesap sonuçları, dosya kontrolleri ve normalize UTF-8/LF SHA-256 özetleri. Ürün testi veya işletim onayı değildir.

## Hesapların yeniden incelenmesi

M22-01'de W1 için başarı oranı `990 / 1000 = 0,99`, W2 için `10 / 10 = 1` olur. Pencereler aynı tanımı kullanır ve çakışmaz. Birleşik oran `(990 + 10) / (1000 + 10) = 1000 / 1010`, yani yaklaşık `%99,0099`dur. İki yüzdenin aritmetik ortalaması `%99,5` verir ve bu birleşik istek kümesi için yanlış olur. Bu hesap zamana dayalı kesinti dakikasına çevrilmez.

M22-02'de uygun istek sayısı sıfırdır. Bölme yapılmaz; sonuç `null`, durum `no_observations` olur. Gerçek sistemde sıfır trafik olduğunu bilmek ile ölçüm alamamak farklıdır. Bu dosya telemetri arızası denemesi yapmaz.

M22-03'te on sekiz adet 50 ms, bir adet 500 ms ve bir adet 1000 ms bulunur. Toplam 2400 ms, ortalama 120 ms, medyan 50 ms'dir. En yakın sıra yönteminde `ceil(0,95 × 20) = 19`; birden başlayan 19. değer olan 500 ms, p95 sonucudur. Başka araçların ara değerleme veya histogram tahmini farklı sonuç verebilir. Bu yirmi değer, M22-01'in istekleriyle aynı veri kümesi değildir.

| Örnek | Yerel sonuç | Kapsam sınırı |
|---|---|---|
| M22-01 | 1000 / 1010; yaklaşık %99,0099 | Sentetik istek oranı |
| M22-02 | null; no_observations | Sıfır payda aritmetiği |
| M22-03 | Ortalama 120, medyan 50, p95 500 ms | Yirmi sentetik süre |

## Planın kullanımı

Gözlem kayıtları henüz araç yapılandırması değildir. Gerçek uygulamada payda, başarı tanımı, veri güncelliği, alarm davranışı ve sorumlu kişi seçilmelidir. RPO/RTO ve kurtarma süresinin başlangıç/bitişi de ihtiyaçla belirlenir; örnek bu alanlara sayı atamaz.

Restore ölçütleri R01–R06 `not_run` durumundadır. İleride izole prova hedefi, yedek/araç/anahtar erişimi, içe aktarım, veri ilişkileri, uygulama davranışı ve ölçülen süre ayrı kanıtlarla doldurulacaktır. Gerçek veri kullanımı ayrıca yetki ve koruma düzeni gerektirir.

I01–I06 olay adımları planlıdır; gerçek olay zamanı, kişi veya müdahale sonucu bulunmaz. İletişim yalnız I05'te başlamaz, olay boyunca sürer. Planın tablo sırası katı çalışma sırası değildir.

## Doğrulama sınırı

4 Ekim 2026'da Python 3.13.7 ile dosya alanları, sıralı kimlikler, açık durumlar ve yukarıdaki aritmetik kontrol edilmiştir. Dosya özetleri metin UTF-8 okunup satır sonları LF'ye normalleştirilerek hesaplanır. Bu nedenle Windows/Git satır sonu dönüşümü içerik değişikliği sayılmaz.

Genel amaçlı monitoring uygulaması, alarm motoru veya yeni test çatısı eklenmemiştir. Hedef Python 3.14/Django/PostgreSQL kurulumu, performans, eşzamanlılık, migration, restore ve CI/CD doğrulanmamıştır. Önceki laboratuvar kanıtlarının kapsamı genişletilmez. Gerçek müşteri verisi ve sır yoktur; dış servise veri gönderilmez.
