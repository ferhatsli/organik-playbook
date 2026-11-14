---
name: urun-yol-haritasi
description: Organik dropshipping ürün yol haritası. Yeni ürün, rakip analizi, marka, logo, bio, AI reel/video, storyboard, Instagram testi, Shopify ya da yorum→DM işlerinde kullan.
---

# Organik dropshipping · Ürün yol haritası

Bir ürüne karar verildikten sonra izlenecek sıra. **Ana ilke:** para ve emek harcamadan önce ilgiyi ölç. Site, tedarik ve otomasyon ancak test videoları ilgi topladıktan sonra gelir.

Kullanıcıyla Türkçe konuş. Her adımın sonunda çıktıyı göster ve onay al; bir sonraki adıma onaysız geçme.

## Adımlar

| # | Adım | Ne yapılır | Ayrıntı |
|---|---|---|---|
| 1 | Rakip ve ürün analizi | Rakip hesaplar ve en iyi reeller çekilir, viral kalıplar ve ürünün gerçek görünüşü çıkarılır | `references/01-rakip-analizi.md` |
| 2 | Marka | Ad adayları (alan adı ve IG kontrolü), logo, profil fotoğrafı, bio, öne çıkanlar, renkler, ses tonu | `references/02-marka.md` |
| 3 | İçerik planı | Kanıtlanmış kalıplara dayanan 10 video kurgusu, sabit kurallar | `references/03-icerik-kurallari.md` |
| 4 | Video üretimi | Storyboard, anahtar kareler, rakip reelin Kling ile düzenlenmesi, ekran yazısı ve caption | `references/04-video-uretimi.md` |
| 5 | Test (karar noktası) | Hesap açılır, 2–4 video paylaşılır, sinyallere bakılır. İlgi yoksa dur | `references/05-test-ve-karar.md` |
| 6 | Satış altyapısı | Tedarik, Shopify sitesi, fiyat ve teslimat süresi | `references/06-satis-altyapisi.md` |
| 7 | Yorum → DM | Anahtar kelime yazana otomatik DM, sıcak ton | `references/07-dm-otomasyonu.md` |
| 8 | Ölçeklendirme | Çalışan kalıptan yeni videolar, fiyat testleri, sezonluk içerik | `references/05-test-ve-karar.md` |

Dosya ve klasör şablonları: `references/sablonlar.md`.

## Önce durumu öğren
Kullanıcı bir ürünle geldiğinde önce hangi adımda olduğunu belirle: çalışma klasöründe `rapor/<ürün>/`, `marka/<ürün>/MARKA.md` ve `icerik/<ürün>/` var mı bak. Yoksa 1. adımdan başla. Belirsizse tek cümleyle sor.

## Çalışma kuralları
- **Önce düşük kalite:** Görsel testleri 1K, video testleri 720p. Yüksek kaliteyi (2K, 1080p) yalnız onaylanan final için kullan. Her üretimden önce tahmini maliyeti söyle.
- **Yalnız isteneni yap:** "Yazıları kaldır" tamamen yazısız demektir; kendi ekran yazını, CTA'nı ya da logonu istenmeden basma. Ek bir öneri varsa önce tek cümleyle sor.
- **Uydurma bilgi yok:** Bilmediğin ürün özelliğini (yaş, ölçü, yıkama, malzeme) yazma; tedarikçiden öğrenilene kadar boş bırak. Sahte yorum ya da sahte müşteri ekran görüntüsü üretme.
- **Taktikleri filtreleme:** Organik içerik taktiklerini olduğu gibi aktar, izlenme odaklı düşün. Ne yapılacağına kullanıcı karar verir.
- **Ürün gerçeğiyle birebir:** Videoda görünen ürün satılacak ürünle aynı olmalı. Satılmayan bir model (renk ya da hayvan) videoda kalırsa düzelt.
- **Gizli anahtarlar:** API anahtarları yalnız `.env.*` dosyalarında ya da ortam değişkenlerinde durur. Ekrana basma, commit'leme.
- **Kullanıcının işi olanlar:** Hesap açma, şifre, ödeme, satın alma, kalıcı silme ve müşterilere elle mesaj atma işlerini kullanıcı yapar.

## Araçlar
- **Apify** (`scripts/apify.py`): Instagram profil, reel ve gönderi verisi. Anahtar: `APIFY_TOKEN` (ortam değişkeni ya da çalışma klasöründe `.env.apify`).
- **Wiro** (`scripts/wiro.py`): Görsel (Nano Banana) ve video (Kling) üretimi. Anahtar: `WIRO_API_KEY`, isteğe bağlı `WIRO_API_SECRET` (ortam değişkeni ya da `.env.wiro`).
- **ffmpeg:** kare çıkarma, kesme, birleştirme. PATH'te yoksa `pip install imageio-ffmpeg` ile gelen binary'yi kullan.

Anahtar yoksa kullanıcıdan dosyayı kendisinin oluşturmasını iste; anahtarı sohbete yazmasını isteme.
