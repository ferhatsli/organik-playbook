"""Apify actor'ını çalıştırır ve dataset'i JSON olarak kaydeder.

Anahtar: APIFY_TOKEN ortam değişkeni ya da çalışma klasöründe .env.apify (APIFY_TOKEN=...). Ekrana basılmaz.

Kullanım:
    python apify.py apify~instagram-profile-scraper girdi.json cikti.json
    python apify.py apify~instagram-reel-scraper '{"username": ["hesap"], "resultsLimit": 30}' cikti.json
    python apify.py indir cikti.json reels/      (videoUrl alanlarını <kod>.mp4 olarak indirir)
Girdi bir dosya yolu ya da doğrudan JSON metni olabilir.
"""
import json
import os
import sys
import urllib.error
import urllib.request
from pathlib import Path

UA = "organik-playbook/1.0"


def token():
    t = os.environ.get("APIFY_TOKEN")
    dosya = Path.cwd() / ".env.apify"
    if not t and dosya.exists():
        for satir in dosya.read_text(encoding="utf-8-sig").splitlines():
            if "=" in satir and not satir.strip().startswith("#"):
                k, v = satir.split("=", 1)
                if k.strip() in ("APIFY_TOKEN", "APIFY_API_TOKEN"):
                    t = v.strip().strip('"').strip("'")
    if not t:
        sys.exit("APIFY_TOKEN bulunamadı: ortam değişkeni olarak ayarla ya da çalışma klasörüne .env.apify koy.")
    return t


def calistir(actor, girdi, cikti):
    govde = Path(girdi).read_text(encoding="utf-8") if Path(girdi).exists() else girdi
    json.loads(govde)  # geçerli JSON mu
    url = f"https://api.apify.com/v2/acts/{actor}/run-sync-get-dataset-items?timeout=300"
    istek = urllib.request.Request(url, data=govde.encode(), headers={
        "Authorization": f"Bearer {token()}", "Content-Type": "application/json", "User-Agent": UA})
    try:
        with urllib.request.urlopen(istek, timeout=330) as r:
            veri = json.load(r)
    except urllib.error.HTTPError as e:
        sys.exit(f"Apify hatası {e.code}: {e.read()[:400].decode('utf-8', 'replace')}")
    Path(cikti).parent.mkdir(parents=True, exist_ok=True)
    Path(cikti).write_text(json.dumps(veri, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"{len(veri)} kayıt → {cikti}")


def indir(json_yolu, klasor):
    Path(klasor).mkdir(parents=True, exist_ok=True)
    for o in json.loads(Path(json_yolu).read_text(encoding="utf-8")):
        url = o.get("videoUrl")
        if not url:
            continue
        hedef = Path(klasor) / f"{o.get('shortCode') or o.get('id')}.mp4"
        with urllib.request.urlopen(urllib.request.Request(url, headers={"User-Agent": UA}), timeout=300) as r:
            hedef.write_bytes(r.read())
        print(hedef, o.get("videoViewCount") or o.get("videoPlayCount") or "")


if __name__ == "__main__":
    if sys.argv[1] == "indir":
        indir(sys.argv[2], sys.argv[3])
    else:
        calistir(sys.argv[1], sys.argv[2], sys.argv[3])
