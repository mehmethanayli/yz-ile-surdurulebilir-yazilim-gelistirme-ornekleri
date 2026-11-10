# Kitap 2 Bölüm 12 — AI Yazılım Takımını Yönetmek

**YZ Görev ve Denetim Kaydı**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Örnek klasörleri Kitap 2’nin bölüm numaralarını, GO-14-01 gibi kayıt kimlikleri ilk çalışma numaralarını kullanır.

**YT-25-01**, [Bölüm 12](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-12) için hazırlanmış öğretim paketidir. Altı görev kartı herhangi bir modele gönderilmemiştir. Sekiz aday yanıt parçası öğretim için yazılmıştır; gerçek model çıktısı değildir. Çoklu ajan çalışması, model performans deneyi ve ürün testi yürütülmemiştir.

- [Denetim planı](oversight-plan.json): dört örnek rol, kanıt düzeyleri, kaynak özetleri ve durma koşulları.
- [Görev kartları](task-cards.json): amaç, kapsam, yetki, çıktı ve açık işler.
- [Değerlendirme ölçütleri](evaluation-rubric.json): kapsam, sözleşme, kanıt, yetki, belirsizlik ve kullanılabilirlik.
- [Sentetik vakalar](evaluation-cases.json): sekiz aday parça için beklenen karar ve gerekçe.
- [Devir şablonu](handoff-template.json): sürüm, değişiklik, kontrol ve açık iş alanları.
- [Yerel doğrulama](verification.json): yalnız dosya ve kayıt ilişkisi denetimi.

## Okuma ve uygulama

Önce [UÇ-23-01](../book-2-chapter-10-integration/README.md) ile [SG-24-01](../book-2-chapter-11-saas/README.md) kapsamlarını ayırın. T25-01, T25-02, T25-04 ve T25-05 ilk MVP; T25-03 gelecek SaaS; T25-06 belge ve devir tasarımı içindir. Kartlar tek bir yürütme zinciri değildir; farklı görev türlerinin örnekleridir. Örnek uygulayıcı rolünün planda bulunması, bu salt inceleme kartlarına dosya değiştirme yetkisi vermez.

Vakaları önce beklenen kararı okumadan inceleyin. Ardından gerekçeyle karşılaştırın. Üç vaka dar kapsamı içinde kabul edilebilir, beş vaka revizyon gerektirir. Bu dağılım model başarısı değildir; öğretim kümesinin hazırlanmış etiket dağılımıdır. Gerçek değerlendirme yapılırsa model, talimat, bağlam, ortam, çıktı ve bağımsız karar kaydedilmelidir. Bu küçük ve açık küme üzerinde iyi sonuç almak genelleme kanıtı sayılmaz; ayrı değerlendirme örnekleri gerekir.

Devir şablonunda çalıştırılan komutun ortamı ve sonucu, hangi kaynak sürümünü kapsadığıyla birlikte tutulur. Boş alanlar gerçekleşmiş işlemleri temsil etmez. İncelenmeyen dosya veya yapılmayan test açıkça belirtilir. Kaynak değiştiğinde eski raporun yeni durumu kapsadığı varsayılmaz. Rol ve gözetim sorumluları bu öğretim paketinde atanmış değildir.

## Doğrulama sınırı

Yerel denetim benzersiz kimlikleri, görev ve ölçüt bağlantılarını, beklenen kararların tutarlılığını, boş gerçek sonuç alanlarını ve kaynak özetlerini kontrol eder. YZ'nin gerçekten doğru karar verdiğini, aracın güvenli çalıştığını veya CRM'nin işlevsel olduğunu test etmez. Gerçek hesap, sır, dış alıcı veya ağ çağrısı içermez. Özetler UTF-8 metinde satır sonları LF'ye dönüştürülerek hesaplanır.
