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

En kolayı: Claude'una bu repo linkini ver ve "Bunu kur" de. Agent aşağıdaki adımları izler.

### Agent için kurulum talimatı (Claude bu bölümü uygular)
1. Plugin'i kur:
   ```bash
   claude plugin marketplace add ferhatsli/organik-playbook
   claude plugin install organik-playbook@organik-playbook
   ```
   `claude` komutu yoksa (masaüstü uygulaması ya da Cowork), kullanıcıya şu yolu söyle: **Customize → Plugins → Add → Add marketplace → Add from a repository** → `ferhatsli/organik-playbook`, sonra **organik-playbook**'u ekle.
2. Kurulumu doğrula: `claude plugin list` çıktısında `organik-playbook@organik-playbook` **enabled** görünmeli.
3. Araçları hazırla:
   - Python 3.10+ olmalı.
   - ffmpeg PATH'te yoksa `pip install imageio-ffmpeg` çalıştır.
4. API anahtarları:
   - Kullanıcının çalışma klasöründe `.env.apify` ve `.env.wiro` var mı kontrol et; yoksa boş şablon olarak oluştur:
     ```
     # .env.apify
     APIFY_TOKEN=
     # .env.wiro
     WIRO_API_KEY=
     WIRO_API_SECRET=
     ```
   - Kullanıcıdan anahtarları **bu dosyalara kendisinin yapıştırmasını** iste; anahtarları sohbete yazdırma.
   - Klasör bir git reposuysa `.env*` satırını `.gitignore`'a ekle.
   - Anahtarlar apify.com (Settings → API & Integrations) ve wiro.ai (Projects → API keys) panellerinden alınır.
5. Test (anahtarlar girildikten sonra). `<skill>` = kurulu plugin içindeki `skills/urun-yol-haritasi` klasörü:
   - `python <skill>/scripts/wiro.py ara "kling"` → model listesi gelmeli.
   - `python <skill>/scripts/apify.py apify~instagram-profile-scraper '{"usernames": ["instagram"]}' test.json` → "1 kayıt" yazmalı.
6. Kullanıcıya kısa bir özet ver: skill adı `urun-yol-haritasi`, elle çağırma `/organik-playbook:urun-yol-haritasi`, başlamak için "Yeni ürüne giriyoruz: <ürün>, rakipler: <linkler>" demesi yeterli.

### Elle kurulum: Claude Code (terminal)
```bash
claude plugin marketplace add ferhatsli/organik-playbook
claude plugin install organik-playbook@organik-playbook
```

### Elle kurulum: Claude masaüstü uygulaması / Cowork
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
