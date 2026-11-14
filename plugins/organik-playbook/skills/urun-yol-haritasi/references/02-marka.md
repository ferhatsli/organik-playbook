# 2 · Marka

## Ad
- 3–4 aday üret: tek kelime, kolay söylenen, ürünün faydasını ya da karakterini çağrıştıran.
- Her biri için kontrol et:
  - **.com:** `https://rdap.verisign.com/com/v1/domain/<ad>.com` 404 dönerse boş.
  - **Instagram:** `@<ad>` ve `@<ad>.tr`; Apify profil sorgusu boş dönerse büyük olasılıkla boş.
- Tabloyla sun: ad, anlamı, .com, Instagram, not. Seçimi kullanıcı yapar.

## Logo ve profil fotoğrafı
1. 3–4 logo seçeneği, 1K test (Nano Banana; `scripts/wiro.py`). Hepsini tek görselde yan yana göster (`secenekler.jpg`).
2. Kullanıcı seçer → seçilen logoyu referans verip 2K final üret.
3. Profil fotoğrafı: yalnız amblem, yazısız, karenin ~%70'ini dolduracak şekilde, düz zemin. Küçük dairede okunmalı.

Nano Banana parametre örneği (`p.json`):
```json
{"prompt": "...", "resolution": "1K", "aspectRatio": "1:1", "outputFormat": "png"}
```
Komut: `python scripts/wiro.py calistir google nano-banana-2-1 p.json cikti/ referans.png`

## Bio (≤150 karakter)
```
<Ad> <emoji> <kısa vaat>
<emoji> <ürün ne yapar, tek cümle>
<emoji> <model/renk sayısı>
💬 <ANAHTAR KELİME> yaz, bilgileri DM'den atalım
```
İsim alanına aranabilirlik için ürün türünü yaz: `<Ad> · <Ürün türü>`.

## Öne çıkanlar
| Başlık | İçerik |
|---|---|
| Modeller | Giriş sayfası + her modelin stüdyo fotoğrafı |
| Nasıl kullanılır | 3 adım, numaralı, video karelerinden |
| Yorumlar | Şimdilik giriş sayfası; gerçek yorumlar ve DM ekran görüntüleri geldikçe eklenir. Sahte yorum konmaz |
| Sorular | Yalnız bildiğimiz yanıtlar: modeller, kullanım, ne işe yarar, nasıl sipariş verilir. Bilinmeyen özellik yazılmaz |

- **Kapaklar:** 1080x1920, düz marka rengi zemin, ortada logo tarzında ikon, yazısız.
- **Hikâyeler:** 1080x1920. Üstte küçük logo hapı (üst 170 px Instagram arayüzü altında kalır). Yazılar marka fontunda; emojiler yazı satırıyla dikeyde ortalı.

## Renkler ve ses tonu
- 4 renk: ana, koyu, zemin, vurgu (HEX ile).
- Ses tonu: hedef kitleye kendi dilinden konuşur. Örnek: anne anneye "Anneler 🥹". Kısa, emojili.

## Çıktı
`marka/<ürün>/MARKA.md` (ad tablosu, logo notları, renkler, ses tonu, bio, öne çıkanlar, sıra listesi), `logo/`, `pp/`.
