# GÖ-26-01 — Gelecek, Ölçüm ve Öğrenme Kaydı

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[Bölüm 13](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-13) için hazırlanmış öğretim paketidir. Gerçek model çıktısı, ajan çalışması, kullanıcı araştırması veya ürün testi içermez. İlk AI-CRM MVP kapsamını değiştirmez.

- [Çalışma planı](future-plan.json): üç alternatif senaryo, ön koşullar ve durdurma koşulları. Senaryolar zorunlu bir ilerleme sırası değildir; hepsi `not_run` durumundadır.
- [İddia örnekleri](claim-cases.json): altı yazılmış örnek; araştırma bulgusu, yorum, koşullu senaryo ve dayanaksız genellemeyi ayırır. Etiketler yazarın öğretim amaçlı beklentileridir.
- [Ölçüm örnekleri](measurement-examples.json): üç sentetik süre hesabı. Sırasıyla 120 → 120 dakika (%0 azalma), 120 → 90 dakika (%25 azalma), 0 → 20 dakika (geçerli başlangıç olmadığı için yüzde hesaplanamaz). Birimler çakışmayan, ardışık geçen dakikalardır. Kalite kanıtı içermez.
- [Öğrenme planı](learning-plan.json): altı yetkinlik çalışması; gerçek öğrenci çıktıları ve değerlendirmeleri boştur.
- [Yerel doğrulama](verification.json): dosya ilişkileri, örnek aritmetiği ve kaynak özetleri. Ürün başarısı raporu değildir.

Önce bir iddiayı sınıflandırın, sonra kaynak ve kapsamını açıklayın. Bir kullanım senaryosu seçerken ön koşulları somutlaştırın; henüz belirlenmemiş araç bütçesine rastgele değer atamayın. Gerçek bir yerel deneme daha sonra yapılırsa başlangıç ve aday koşullarını, kalite ölçütlerini, sürümleri ve inceleme yükünü kaydedin. Bu özgün sentetik örnekleri gerçek sonuçmuş gibi yeniden etiketlemeyin; kendi ölçümünüzü ayrı kayda alın.

Bibliyografya anahtarları [ortak kaynakçada](../../../references/references.bib) bulunur. Araştırma kapsamı ve APA kaynakları bölüm metnindedir. Kaynak özetleri UTF-8 metnin CRLF/CR satır sonları LF olarak normalleştirilerek hesaplanır; `verification.json` kendi özetini içermez.
