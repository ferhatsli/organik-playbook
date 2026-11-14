"""Wiro API istemcisi (görsel ve video üretimi).

Anahtar: WIRO_API_KEY (isteğe bağlı WIRO_API_SECRET) ortam değişkeni ya da çalışma klasöründe .env.wiro dosyası.
Anahtarlar ekrana basılmaz.

Kullanım:
    python wiro.py ara "kling"
    python wiro.py detay klingai kling-v4-reference
    python wiro.py calistir google nano-banana-2-1 p.json cikti/ ref1.png [ref2.png ...]
    python wiro.py calistir klingai kling-v4-reference p.json cikti/ inputVideoBase=rakip.mp4 inputImageReference=urun.png
    python wiro.py indir <taskid> cikti/
Referans "alan=yol" biçimindeyse o alana, değilse varsayılan alana (inputImage) gider.
"""
import os
import hashlib
import hmac
import json
import mimetypes
import sys
import time
import urllib.request
import uuid
from pathlib import Path

API = "https://api.wiro.ai/v1"
UA = "organik-playbook/1.0"


def anahtarlar():
    v = {k: os.environ[k] for k in ("WIRO_API_KEY", "WIRO_API_SECRET") if os.environ.get(k)}
    dosya = Path.cwd() / ".env.wiro"
    if "WIRO_API_KEY" not in v and dosya.exists():
        for satir in dosya.read_text(encoding="utf-8-sig").splitlines():
            satir = satir.strip()
            if satir and not satir.startswith("#") and "=" in satir:
                k, x = satir.split("=", 1)
                v[k.strip()] = x.strip().strip('"').strip("'")
    if "WIRO_API_KEY" not in v:
        sys.exit("WIRO_API_KEY bulunamadı: ortam değişkeni olarak ayarla ya da çalışma klasörüne .env.wiro koy.")
    return v


def basliklar():
    v = anahtarlar()
    # Wiro'nun önündeki Cloudflare, urllib'in varsayılan User-Agent'ını engelliyor (1010).
    h = {"x-api-key": v["WIRO_API_KEY"], "User-Agent": UA, "Accept": "application/json"}
    if v.get("WIRO_API_SECRET"):
        nonce = str(int(time.time()))
        h["x-nonce"] = nonce
        h["x-signature"] = hmac.new(
            v["WIRO_API_KEY"].encode(), (v["WIRO_API_SECRET"] + nonce).encode(), hashlib.sha256
        ).hexdigest()
    return h


def istek(yol, govde=None, dosyalar=None):
    h = basliklar()
    if dosyalar:
        sinir = uuid.uuid4().hex
        parcalar = []
        for k, deger in (govde or {}).items():
            degerler = deger if isinstance(deger, list) else [deger]
            for d in degerler:
                parcalar.append(f'--{sinir}\r\nContent-Disposition: form-data; name="{k}"\r\n\r\n{d}\r\n'.encode())
        for alan, yol_ in dosyalar:
            p = Path(yol_)
            tip = mimetypes.guess_type(p.name)[0] or "application/octet-stream"
            parcalar.append(
                f'--{sinir}\r\nContent-Disposition: form-data; name="{alan}"; filename="{p.name}"\r\nContent-Type: {tip}\r\n\r\n'.encode()
                + p.read_bytes() + b"\r\n"
            )
        parcalar.append(f"--{sinir}--\r\n".encode())
        veri = b"".join(parcalar)
        h["Content-Type"] = f"multipart/form-data; boundary={sinir}"
    else:
        veri = json.dumps(govde or {}).encode()
        h["Content-Type"] = "application/json"
    try:
        with urllib.request.urlopen(urllib.request.Request(API + yol, data=veri, headers=h), timeout=300) as r:
            return json.load(r)
    except urllib.error.HTTPError as e:
        return {"result": False, "http": e.code, "hata": e.read()[:500].decode("utf-8", "replace")}


def ara(sorgu):
    r = istek("/Tool/List", {"search": sorgu, "limit": "30", "hideworkflows": True, "summary": True})
    for t in r.get("tool", []):
        print(t["cleanslugowner"], t["cleanslugproject"], "|", t["title"], "|", ",".join(t.get("categories") or [])[:80], "|", (t.get("dynamicprice") or "")[:120])
    if not r.get("tool"):
        print(json.dumps(r, ensure_ascii=False)[:600])


def detay(sahip, model):
    r = istek("/Tool/Detail", {"slugowner": sahip, "slugproject": model})
    print(json.dumps(r, ensure_ascii=False, indent=1)[:6000])


def calistir(sahip, model, param_dosya, cikti, refler=()):
    param = json.loads(Path(param_dosya).read_text(encoding="utf-8"))
    # Referans "alan=yol" biçimindeyse o alana, değilse varsayılan alana gider (ör. inputImageLast=son.png).
    varsayilan = param.pop("_dosya_alani", "inputImage")
    dosyalar = [tuple(r.split("=", 1)) if "=" in r else (varsayilan, r) for r in refler]
    r = istek(f"/Run/{sahip}/{model}", param, dosyalar or None)
    if not r.get("result"):
        print(json.dumps(r, ensure_ascii=False)[:800])
        return
    print("gorev:", r.get("taskid"))
    bitis = time.time() + 900
    while time.time() < bitis:
        time.sleep(5)
        d = istek("/Task/Detail", {"taskid": r["taskid"]})
        gorev = (d.get("tasklist") or [{}])[0]
        if gorev.get("status") in ("task_postprocess_end", "task_cancel"):
            break
    else:
        print("zaman asimi, son durum:", gorev.get("status"))
        return
    if gorev.get("pexit") != "0":
        print("hata:", json.dumps(gorev, ensure_ascii=False)[:1500])
        return
    indir_gorev(gorev, cikti)


def indir_gorev(gorev, cikti):
    Path(cikti).mkdir(parents=True, exist_ok=True)
    for i, o in enumerate(gorev.get("outputs", [])):
        url = o.get("url")
        if not url:
            continue
        hedef = Path(cikti) / (o.get("name") or f"cikti_{i}.png")
        for deneme in range(4):
            try:
                req = urllib.request.Request(url, headers={"User-Agent": UA})
                with urllib.request.urlopen(req, timeout=300) as yanit:
                    hedef.write_bytes(yanit.read())
                print(hedef)
                break
            except (TimeoutError, OSError) as e:
                print("indirme tekrar:", deneme + 1, e)
                time.sleep(5)


def indir(taskid, cikti):
    gorev = (istek("/Task/Detail", {"taskid": taskid}).get("tasklist") or [{}])[0]
    print("durum:", gorev.get("status"), "pexit:", gorev.get("pexit"))
    indir_gorev(gorev, cikti)


if __name__ == "__main__":
    komut = sys.argv[1]
    if komut == "ara":
        ara(" ".join(sys.argv[2:]))
    elif komut == "detay":
        detay(sys.argv[2], sys.argv[3])
    elif komut == "calistir":
        calistir(sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6:])
    elif komut == "indir":
        indir(sys.argv[2], sys.argv[3])
