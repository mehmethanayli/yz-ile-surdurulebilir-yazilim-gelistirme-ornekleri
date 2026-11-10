# Kitap 2 Bölüm 8 — Deployment: Bilgisayarımdan İnternete

**Yayın planı örneği**

> **Bölüm numarası:** Bu paket Kitap 2’nin bağımsız 1–13 numaralandırmasına göre listelenir. Klasör adları ve GO-14-01 gibi kayıt kimlikleri kaynak dosyalarla uyum için korunmuştur.

[Kitap 2, Bölüm 8 eşleştirmesi](../../../docs/bolum-eslestirmesi.md#kitap-2-bolum-8).

YK-21-01, gerçek ortam seçilmeden önce incelenebilen bir öğretim planıdır. [release-plan.json](release-plan.json) 12 yayın öncesi koşul, üç geri dönüş senaryosu ve dört yayın sonrası kontrol içerir. [İşlem yönergesi](runbook.md) bu kararların nasıl sıraya konulacağını gösterir.

`pending` değerlendirilmemiş koşul, `not_run` çalıştırılmamış kontrol veya prova, `null` bilinmeyen/atanmamış bilgi anlamına gelir. `release_approved: false` verilmiş bir yayın onayı olmadığını belirtir. Bu kayıt otomatik bir yayın engelleyicisi veya çalışır pipeline değildir; onu okuyan bir deployment aracı uygulanmamıştır.

DNS örnekleri `example.com` ad alanını ve dokümantasyon için ayrılmış `192.0.2.10` adresini kullanır. Üç kayıt bir DNS bölgesinin tamamı değildir; gerçek sunucu, TTL veya kayıt sağlayıcısı tanımlamaz. CNAME adı ile A kaydının adı farklıdır. Bir kaydın biçimini göstermek DNS/TLS/HTTP'nin çalıştığını kanıtlamaz.

## Doğrulama sınırı

[verification.json](verification.json) yalnızca örnek dosyaların yapısal kontrolünü kaydeder. Benzersiz koşul/senaryo kimlikleri, açık alanlar, yapılmamış onaylar ve örnek DNS kayıtları kontrol edilmiştir. Dosya özetleri UTF-8 ve LF satır sonlarıyla hesaplanır. Bir dosya değişirse önceki özet o içeriğe ait olmaz.

Gerçek build, Docker, CI/CD, DNS sorgusu/değişikliği, TLS bağlantısı, sunucu, migration, rollback veya restore çalıştırılmamıştır. Önceki laboratuvar testleri yeniden çalıştırılmamıştır. Bu klasör müşteri verisi, sır, üretim adresi veya uygulanabilir altyapı komutu içermez.

Okuyucu önce her koşul için gereken kanıtı açıklar, sonra runbook'u masa başında inceler. Gerçek altyapı seçildiğinde adres, yetki, aday ve komutlar ayrıca doğrulanarak plan somutlaştırılır; canlı işlem bu örneğin dosya kontrolünden türetilmez.
