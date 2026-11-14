# 7 · Yorum → DM otomasyonu

## Seçenekler
| Araç | Ne zaman | Not |
|---|---|---|
| Meta Business Suite otomatik yanıt | Test dönemi | Ücretsiz, basit; anahtar kelime → sabit mesaj |
| ManyChat | Satış başladığında | Yorum → DM, butonlu mesaj, AI yanıt (kredi sınırı var) |
| Kendi bot'un (Cloudflare Worker + D1 kuyruğu) | Hacim artınca | Meta hız sınırına karşı kuyruk ve öncelik; Instagram Graph API, Advanced Access gerekir |

## DM tonu
- Soğuk/robot değil, sıcak bir müşteri temsilcisi gibi: selama selamla karşılık, kısa ve samimi, 3–4 cümle.
- Butonlu her mesajda açıkça yaz: "bu mesajın hemen altındaki "…" butonuna dokun". Müşteriler butonu fark etmeyip "yazdım gelmedi" diyor.
- "Pahalı" diyene hak verme; kapanış cümlesini her mesajda tekrarlama.
- Yasak/kaçınılacak ifadeleri (ör. "ön sipariş", "iade" gibi yanlış beklenti yaratanlar) bilgi bankasına yaz.

## Örnek akış
1. Yorum: "<KELİME>" → herkese açık yanıt: "DM'den gönderdik 🧸" (birkaç varyasyon, aynı cümle tekrar edilmez).
2. DM: "Merhaba 🥰 İlgin için teşekkürler! <ürün, 1 cümle>. Tüm modelleri ve siparişi görmek için bu mesajın hemen altındaki "Ürünü gör" butonuna dokunman yeterli 👇"
3. Takip: soru gelirse AI ya da elle cevap. Müşterilere elle toplu mesaj atılmaz.

## Meta hız sınırı
- Uygulama seviyesinde sınır dolunca yanıtlar gitmez. Kuyruğa al, yeni içeriğin yorumlarına öncelik ver, gerekirse sayfa token'ına geç.
