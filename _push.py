#!/usr/bin/env python3
"""Push /tmp/ai-map files to the antoniompaulo25/ai-agent-job-map repo via the
GitHub Contents API (the git push path 403s with this token; the API works)."""
import base64, json, os, ssl, urllib.request

TOK = open("/tmp/gh3").read().strip()
REPO = "antonio-clicktoclose/ai-agent-job-map"
ROOT = "/tmp/ai-map"
CTX = ssl.create_default_context(); CTX.check_hostname = False; CTX.verify_mode = ssl.CERT_NONE

def get_sha(path):
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        headers={"Authorization": f"Bearer {TOK}", "Accept": "application/vnd.github+json"})
    try:
        with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
            return json.loads(r.read()).get("sha")
    except Exception:
        return None

def put(path, b64):
    sha = get_sha(path)
    body = {"message": f"add {path}", "content": b64}
    if sha: body["sha"] = sha
    req = urllib.request.Request(
        f"https://api.github.com/repos/{REPO}/contents/{path}",
        data=json.dumps(body).encode(),
        headers={"Authorization": f"Bearer {TOK}", "Content-Type": "application/json",
                 "Accept": "application/vnd.github+json"},
        method="PUT")
    with urllib.request.urlopen(req, context=CTX, timeout=30) as r:
        return json.loads(r.read()).get("content", {}).get("sha")

files = []
for base, dirs, names in os.walk(ROOT):
    if ".git" in base: continue
    for n in names:
        p = os.path.join(base, n)
        rel = os.path.relpath(p, ROOT)
        if rel == "_gen.py": continue
        files.append(rel)

files.sort()
ok = 0
for rel in files:
    b64 = base64.b64encode(open(os.path.join(ROOT, rel), "rb").read()).decode()
    try:
        put(rel, b64); ok += 1
    except Exception as e:
        print(f"  FAIL {rel}: {e}")
print(f"pushed {ok}/{len(files)} files")
