# Bölüm 11 — SaaS Geçiş Taslağı

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

Bu paket [Bölüm 11](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-11) için hazırlanmış **SG-24-01** öğretim çıktısıdır. Gerçek SaaS uygulaması, ödeme entegrasyonu veya izolasyon testi değildir. [UÇ-23-01](../chapter23-integration/README.md) tek kurumlu ilk MVP sınırını korur; yeni ihtiyaçlar bu ayrı taslakta değerlendirilir.

- [Geçiş planı](transition-plan.json): 12 açık karar grubu, altı planlı aşama ve korunacak erişim kuralları.
- [Sentetik veri](synthetic-data.json): iki kurum, beş aktör, beş üyelik, iki müşteri, üç görev ve aynı olayın iki teslim gösterimi.
- [Kabul senaryoları](acceptance-cases.json): 18 planlı senaryo; sonuç ve kanıt alanları boştur.
- [Doğrulama kaydı](verification.json): dosya ilişkileri, durumlar ve özetler için yerel belge kontrolü.

## Örneği okumak

Kurumların kimlikleri K-A ve K-B'dir. A her iki kurumda ekip üyesidir; K-B'de ayrıca kurum yöneticisidir. B yalnız K-A, C yalnız K-B ekip üyesidir. S yalnız platform hesap yönetimi rolündedir. D'nin üyeliği etkin görünse bile genel hesabı kapalıdır; etkin üyelik tek başına genel hesap kontrolünü geçersiz kılmaz. Aynı görünen müşteri adı ve aynı yerel kimlikler, yanlış kapsamla eşleştirmeyi görünür kılmak için seçilmiştir. Bunlar üretimde yerel kimlik kullanılacağı kararı değildir.

Kurumun ortak müşteri ve notlarıyla kişisel görevleri farklı erişim sınırı taşır. Kurum yöneticisi olmak başkasının görevini açmaz. Abonelik veya daha kapsamlı plan satın almak da bu sınırı değiştirmez. Yeni API'nin hata kodları ve gövdeleri henüz seçilmediğinden kabul beklentileri anlam ve veri etkisi düzeyindedir.

## Kullanım sırası

G01–G06 geçiş aşamaları belge üzerinde sırayla okunur. G01 mevcut MVP kanıtı ve SaaS ihtiyacını değerlendirir. G02 sözleşmeyi, G03 izolasyonu, G04 aboneliği, G05 ek yeteneklerin hata yollarını, G06 kontrollü pilotu ele alır. Bu doğrulama sırası, bağımsız araştırmanın daha erken yapılamayacağı anlamına gelmez. Her aşamanın ürün kabulü önceki kanıta dayanır.

Bir senaryoyu gerçek uygulamada yürütmeden önce bağlı açık kararlar tamamlanır ve test ortamı hazırlanır. İstek, aktör, kurum, kaynak, gerçek sonuç ve veri etkisi kayıt altına alınır. Yalnız dosyayı okumak veya beklenen sonucu tartışmak `not_run` durumunu değiştirmez. Senaryolar başlangıç kümesidir; eksiksiz test kapsamı iddiası taşımaz.

## Doğrulamanın sınırı

Yerel kontrol kimlikleri, aşama bağımlılıklarını, karar referanslarını, sentetik ilişkileri ve gerçek işlem yapılmadığını belirten durumları inceler. Django, PostgreSQL, RLS, webhook imzası, kuyruk, worker, DNS, dosya sağlayıcısı, migration, CI/CD veya restore çalıştırmaz. Gerçek kullanıcı görüşmesi ve ödeme yapılmaz. Kaynak dosyaların SHA-256 özetleri UTF-8 metinde satır sonları LF'ye çevrilerek hesaplanır.
