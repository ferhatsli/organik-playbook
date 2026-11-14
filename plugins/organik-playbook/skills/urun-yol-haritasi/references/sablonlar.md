# Klasör ve dosya şablonları

## Klasör yapısı
```
rapor/<ürün>/            RAPOR.md, veri/, reels/, kare/
marka/<ürün>/            MARKA.md, logo/, pp/
icerik/<ürün>/           VIDEOLAR.md, PAYLASIM-1-2.md, one-cikanlar/
icerik/<ürün>/video-01-<ad>/
    STORYBOARD.md, storyboard.jpg, rakip.mp4
    kare/orijinal/tX.png, kare/p-tX.json, kare/yeni-tX.png
    kanca/                (Kling çıktıları, p.json, serit.jpg)
    video-01-<ad>-yazisiz.mp4
.env.apify, .env.wiro    (gizli; git'e girmez)
```

## MARKA.md
```markdown
# <Ürün> · marka kiti (<tarih>)
**Ürün:** ...  **Rakip analizi:** rapor/<ürün>/RAPOR.md
**Test planı:** ...
## Ad adayları   (tablo: Ad | Anlamı | .com | Instagram | Not)
## Logo testleri
## Renkler       (tablo: Rol | Renk | HEX)
## Ses ve ton
## Bio
## Modeller
## Öne çıkanlar
## Yorum CTA'sı  (anahtar kelime)
## Sıra          (yol haritası adımları, [x] / [ ])
```

## STORYBOARD.md
```markdown
# <Ürün> · Video N · "<başlık>" · Storyboard
Taban: <rakip hesap> `<reel kodu>` (rakip.mp4, X sn, Y izlenme). Kalıp: A/B/C.
Neden: ...
| Sn | Görüntü | Değişen |
## Ekran yazısı   (saniyeleriyle; videoya basılmaz)
## Ses
## Caption
## Sabit yorum
## Üretim         (adımlar ve komutlar)
```

## PAYLASIM-*.md
Her video için: ekran yazısı 1 (0 → X sn), ekran yazısı 2 (X sn → son), caption, sabit yorum, paylaşım saati. Hepsi kopyalanabilir kod bloklarında.
