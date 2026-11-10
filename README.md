# Yapay Zekâ ile Sürdürülebilir Yazılım Geliştirme

**Kitapların uygulama örnekleri ve dijital ekleri** · Mehmet Can Hanaylı

Bu depo, iki kitaplık seriyi okurken kullanabileceğiniz Python laboratuvarlarını,
plan ve senaryo dosyalarını, sentetik örnek verileri ve her kitabın Ek A–F
başvuru materyallerini bir araya getirir.

## Dijital ekler ve indirme

- [Kitap 1 Ek A–F](ekler/kitap-1/README.md)
- [Kitap 2 Ek A–F](ekler/kitap-2/README.md)
- [Bütün materyalleri ZIP olarak indir](indir/kitap-materyalleri-v0.1.2.zip)
- [Kitap ve bölüm eşleştirmesi](docs/bolum-eslestirmesi.md)

Ekler Markdown biçimindedir; GitHub üzerinde doğrudan okunabilir. ZIP paketini
indirip açarak dosyalara çevrimdışı ulaşabilirsiniz. Git kullanmak zorunlu değildir.

## Uygulamalara başlarken

Önce çalışacağınız paketin README dosyasını okuyun. Komutları o dosyada belirtilen
dizinde çalıştırın. İlk altı paket bağımsız Python laboratuvarlarıdır; sonraki yedi
paket plan, senaryo ve değerlendirme çalışmalarıdır. Dosyalar tamamlanmış bir CRM
ürünü olarak sunulmaz; her paket kendi kapsamını ve doğrulama sınırını açıklar.

Kitap 2’nin örnek klasörleri `book-2-chapter-01` ile `book-2-chapter-13` arasında numaralandırılır. Kayıt kimlikleri ilk çalışma düzenindeki sayılarını korur.

| Kitap 2 bölümü | Kitaptaki bölüm adı | Dosyalar |
|---|---|---|
| 1 | Geliştirme Ortamını Anlamak | [Paketi aç](assets/code/book-2-chapter-01-environment/README.md) |
| 2 | Git ve Sürüm Kontrolü | [Paketi aç](assets/code/book-2-chapter-02-git-lab/README.md) |
| 3 | AI ile Kod Geliştirme Stratejisi | [Paketi aç](assets/code/book-2-chapter-03-share-report/README.md) |
| 4 | Hata Ayıklama | [Paketi aç](assets/code/book-2-chapter-04-debug-lab/README.md) |
| 5 | Yazılım Testi | [Paketi aç](assets/code/book-2-chapter-05-test-lab/README.md) |
| 6 | Yazılım Güvenliği | [Paketi aç](assets/code/book-2-chapter-06-security-lab/README.md) |
| 7 | Gizlilik, Etik, Lisans ve Hukuki Sorular | [Paketi aç](assets/examples/book-2-chapter-07-review/README.md) |
| 8 | Deployment: Bilgisayarımdan İnternete | [Paketi aç](assets/examples/book-2-chapter-08-release/README.md) |
| 9 | Production Sonrası Hayat | [Paketi aç](assets/examples/book-2-chapter-09-operations/README.md) |
| 10 | Baştan Sona AI Destekli Bir Uygulama Geliştirmek | [Paketi aç](assets/examples/book-2-chapter-10-integration/README.md) |
| 11 | Prototipten SaaS Ürününe | [Paketi aç](assets/examples/book-2-chapter-11-saas/README.md) |
| 12 | AI Yazılım Takımını Yönetmek | [Paketi aç](assets/examples/book-2-chapter-12-ai-team/README.md) |
| 13 | Yazılım Geliştirmenin Geleceği | [Paketi aç](assets/examples/book-2-chapter-13-future/README.md) |

Kitap 1’in planlama ve tasarım çalışmalarında [dijital eklerden](ekler/kitap-1/README.md)
yararlanabilirsiniz. Bölüm metinleri kitaplarda okunur.

## Sürüm ve geri bildirim

Güncel dijital paket **v0.1.2** (10 Kasım 2026). Örnek klasörleri Kitap 2’nin bölüm numaralarına göre adlandırıldı. Güncellemeler [değişiklik kaydında](CHANGELOG.md) belirtilir.
Hata bildirirken kitap, bölüm, dosya ve kullandığınız paket sürümünü yazın.

Paketlerdeki `verification.json` dosyaları önceki laboratuvar incelemelerini
kaydeder. Okur yönergeleri yeni depo ve bölüm düzenine uyarlanmıştır; eski
kayıtlardaki README özetleri özgün çalışma kopyasına ait olabilir. Dağıtılan
dosyaların güncel özetleri `distribution-manifest.json` içindedir.

## Kullanım koşulları

`assets/code` ve `assets/examples` altındaki yazılım örnekleri, örnek veri ve
beraberindeki paket açıklamaları [MIT lisansıyla](LICENSE) paylaşılır.
`ekler` klasöründeki başvuru metinleri ise [okuma ve kişisel çalışma koşullarına](ekler/LICENSE.md)
tabidir; MIT lisansının kapsamı dışındadır. Kaynakçada listelenen üçüncü taraf
eserlerin hakları kendi hak sahiplerine aittir.
