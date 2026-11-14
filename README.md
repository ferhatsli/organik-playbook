# organik-playbook

Organik dropshipping ürün yol haritası, Claude için skill olarak paketlendi.

İçinde:
- Rakip analizi
- Marka (ad, logo, bio, öne çıkanlar)
- AI video üretimi (rakip reelini Kling ile düzenleme)
- Instagram testi ve karar noktası
- Shopify satış altyapısı
- Yorum → DM otomasyonu
- Yardımcı scriptler: Apify ve Wiro

Skill adı: `urun-yol-haritasi`. Claude "yeni ürün", "rakip analizi", "storyboard", "bio" gibi işler geldiğinde skill'i kendiliğinden yükler. Elle çağırmak için `/organik-playbook:urun-yol-haritasi`.

## Kurulum

### Claude Code (terminal)
```bash
claude plugin marketplace add ferhatsli/organik-playbook
claude plugin install organik-playbook@organik-playbook
```
Repo özel olduğu için önce GitHub erişimin olmalı. Davet kabul edildikten sonra bir kez çalıştır:
```bash
gh auth login
gh auth setup-git
```

### Claude masaüstü uygulaması / Cowork
**Customize → Plugins → Add → Add marketplace → Add from a repository** → `ferhatsli/organik-playbook`. Ardından **organik-playbook** eklentisini ekle.

### Yalnız claude.ai sohbeti (ZIP)
`plugins/organik-playbook/skills/urun-yol-haritasi` klasörünü ZIP'le. ZIP'in kökünde klasörün kendisi olmalı. Sonra **Customize → Skills → Upload** ile yükle. Bu yolda güncellemeler elle yapılır.

## Güncelleme
- Plugin sahibi `plugin.json` içindeki `version` değerini artırıp push'lar.
- Kullanıcı tarafında:
  ```bash
  claude plugin marketplace update organik-playbook
  claude plugin update organik-playbook@organik-playbook
  ```
- Otomatik güncelleme için: `/plugin` → **Marketplaces** → organik-playbook → **Enable auto-update**.

## API anahtarları
Scriptler anahtarları ortam değişkeninden ya da çalışma klasöründeki dosyadan okur. Anahtarları bu repoya koyma.

| Servis | Değişken | Dosya |
|---|---|---|
| Apify | `APIFY_TOKEN` | `.env.apify` |
| Wiro | `WIRO_API_KEY`, `WIRO_API_SECRET` (isteğe bağlı) | `.env.wiro` |

Ayrıca ffmpeg gerekir. PATH'te yoksa `pip install imageio-ffmpeg` yeterli.
