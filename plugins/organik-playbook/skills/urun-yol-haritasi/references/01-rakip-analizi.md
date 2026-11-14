# 1 · Rakip ve ürün analizi

## Veri toplama (Apify)
`scripts/apify.py <actor> <girdi.json> <cikti.json>` komutu actor'ı çalıştırır ve dataset'i JSON olarak kaydeder.

| İş | Actor | Örnek girdi |
|---|---|---|
| Profil bilgisi (takipçi, bio, gönderi sayısı) | `apify~instagram-profile-scraper` | `{"usernames": ["rakiphesap"]}` |
| Hesabın son reelleri | `apify~instagram-reel-scraper` | `{"username": ["rakiphesap"], "resultsLimit": 60}` |
| Tek reel / gönderi ayrıntısı | `apify~instagram-scraper` | `{"directUrls": ["https://www.instagram.com/reel/XXXX/"], "resultsType": "details"}` |
| Bir hesabın gönderileri | `apify~instagram-scraper` | `{"directUrls": ["https://www.instagram.com/rakiphesap/"], "resultsType": "posts", "resultsLimit": 50}` |
| Kullanıcı adı boş mu? | `apify~instagram-profile-scraper` | Sonuç boş dönerse ad büyük olasılıkla boştur |

Ücretsiz planın aylık kredisi sınırlı; `resultsLimit` küçük tutulur.

## Analiz
1. Reelleri izlenmeye göre sırala. En iyi 3–5 reelin `videoUrl`'sini indir (`rakip.mp4`).
2. Kare çıkar: `ffmpeg -i rakip.mp4 -vf "fps=2,scale=180:-1,tile=6x4" -frames:v 1 serit.jpg`. Sahne geçişleri için: `-vf "select='gt(scene,0.25)',showinfo"`.
3. Her reel için şunları çıkar:
   - **Kanca:** ilk 1–2 saniyede ne oluyor, ekran yazısı ne?
   - **Ödül anı:** kaçıncı saniyede geliyor?
   - **Kalıp:** aşağıdaki kalıplardan hangisi?
   - **Yorumlar:** en çok hangi kelime yazılmış? Rakip anahtar kelime CTA'sı kullanıyor mu?
   - **Ürün:** modeller, renkler, detaylar. Videoda görünen ürün bizim satacağımızla aynı olmalı.
4. Rakibin ürün sayfası varsa fiyat, varyant ve ürün bilgisini oku (Shopify sitelerinde `/products/<handle>.json`).

## Sık görülen kalıplar
- **A · Sorun → çözüm:** Sorun ilk 3 saniyede net gösterilir (başı düşen çocuk, dağınık oda), sonra ürünle çözüm gelir. POV yazısı iyi çalışır.
- **B · Mağaza şoku:** "Anneler… X'e KOŞUN 😱" → ürün rafta → kullanımı → "Şaka şaka… biz satıyoruz". Yetişkinin şaşkın tepkisi kancadır.
- **C · Kendim yaptım:** "Bunu kendim diktim / kurdum". Merak ve "nereden aldın" yorumları çeker.
- **D · Hediye ya da sezon:** Yılbaşı, bayram yolu, doğum günü; paket açma ve tepki.
- **E · Karşılaştırma:** öncesi/sonrası, "X'li vs X'siz".

## Çıktı
`rapor/<ürün>/RAPOR.md` (hesaplar, en iyi reeller tablosu, kalıplar, ürün notları), `veri/*.json`, `reels/*.mp4`, `kare/*.jpg`.
