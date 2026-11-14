# 4 · Video üretimi

Sıfırdan AI video üretimi genelde "yapay" duruyor. En gerçekçi sonuç, **rakibin viral reelini düzenlemekten** geliyor: hareket, ışık ve kurgu korunur; kişi, mekân ve ürün bizimkiyle değişir.

## Akış
1. **Storyboard** (`video-XX-<ad>/STORYBOARD.md` + `storyboard.jpg`): saniye tablosu (görüntü / değişen), üst sırada rakip kareler, alt sırada bizim kareler. Ekran yazısı, ses, caption ve sabit yorum da bu dosyaya yazılır.
2. **Anahtar kareler:** Rakip kareyi (`kare/orijinal/tX.png`) Nano Banana ile düzenle (1K test). Referans olarak ürün fotoğrafı ve logo ver. Aynı kişi birden fazla karede görünecekse, önceki üretilen kareyi de referans ver.
3. **Kling düzenleme** (Wiro `klingai kling-v4-reference`):
   - `inputVideoBase` = rakip reel (ya da bir parçası), `inputImageReference` = bizim kare ya da ürün fotoğrafı.
   - Prompt'ta `@video_1`, `@image_1` ile atıf yapılır.
   - Prompt yapısı: "Keep EXACTLY the same: ... (kurgu, kamera, hareket, kıyafet, ışık). Change only: 1) ... 2) ...". Ürünü tarif ederken şekil, renk ve detayları tek tek yaz. İstenmeyen şeyi açıkça yasakla ("No pink pig anywhere").
   - Parametreler: `{"duration": "11", "resolution": "720p", "ratio": "9:16", "watermark": "false"}`. Test 720p, final 1080p. Yaklaşık maliyet: 10 sn 720p ≈ 2 $.
   - Komut: `python scripts/wiro.py calistir klingai kling-v4-reference p.json cikti/ inputVideoBase=rakip.mp4 inputImageReference=urun.png`
4. **Kanca + kalan:** Genelde yalnız ilk 3–5 sn (kanca) yeniden üretilir, rakibin kalan kısmı düzenlenerek kullanılır. ffmpeg ile birleştir:
   ```
   ffmpeg -i kanca.mp4 -i kalan.mp4 -i rakip.mp4 -filter_complex "[0:v]scale=720:1280,fps=30,setsar=1[a];[1:v]scale=720:1280,fps=30,setsar=1[b];[a][b]concat=n=2:v=1:a=0[v]" -map "[v]" -map 2:a? -shortest -c:v libx264 -crf 20 -pix_fmt yuv420p -c:a aac cikti.mp4
   ```
5. **Kare kare kontrol:** `fps=2,tile=6x4` şeridiyle bütün videoyu incele. Bak: şekil değiştiren nesne, kaybolan/beliren parçalar, yanlış model, kalan rakip yazısı ya da logo, el/parmak bozukluğu. Bozukluk varsa yalnız o parçayı yeniden üret.

## Bilinen tuzaklar
- **Yalnız "yazıyı kaldır" istemi işe yaramaz:** Kling, videoyu değiştirmeden geri döndürüyor (para gidiyor). Yazı kaldırmayı, görünür başka bir değişiklikle birlikte iste (kişiyi ya da ürünü değiştir).
- **Kamera yaklaşması ile aksiyon ayrı klip olmalı:** Yaklaşmanın son karesini önceki karenin kırpılıp büyütülmesiyle hazırla; yoksa model kamerayı değil kişiyi hareket ettirir.
- **Kişi değişimi:** "completely different person" demezsen orijinal kişiye benzer çıkar.
- **Ses:** Kling v4 reference videoyu düzenlerken ses de üretir. Konuşma gerekiyorsa `inputAll`'a 5–30 sn ses örneği verip prompt'ta `@voice_1` kullan. Bazen İngilizce konuşur; o zaman repliği TTS ile değiştir.
- **Eşzamanlı görev sınırı:** Wiro bakiyesi düşükken aynı anda tek görev çalışır (`code 96`). Üretimleri sırayla yap ya da hata alınca dakikada bir yeniden dene.

## Ekran yazısı ve ses
- Ekran yazısı videoya **basılmaz**; Instagram'da paylaşırken eklenir. Metinler saniyeleriyle birlikte `PAYLASIM-*.md` dosyasına yazılır.
- Ses Instagram'ın trend seslerinden seçilir. Özel ses gerekiyorsa ElevenLabs ile üretilip -16 LUFS'a getirilir.

## Görsel üretim notları (Nano Banana)
- Stüdyo ürün fotoğrafı: "Clean product photo of ONE ... from IMAGE 1, exactly the same product design: ... on a seamless <renk> studio background. NO text, NO logo, NO hands."
- İkon/kapak: logoyu referans ver, "in exactly the same style as IMAGE 1 ... NO text".
- Yazı içeren görselleri (hikâye, kapak yazısı) modelle değil Python/PIL ile bas: font kontrolü ve Türkçe karakterler doğru olur.
