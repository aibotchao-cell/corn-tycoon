#!/usr/bin/env bash
# 把最新的遊戲檔推上 GitHub Pages（公開網址）
# 用法：bash /c/Users/YO/gh-pages/corn-tycoon/deploy.sh
set -e
SRC="/c/Users/YO/kidpickup_app/farm.html"
DEST="/c/Users/YO/gh-pages/corn-tycoon"
export PATH="/c/Users/YO/bin/gh/bin:$PATH"
export GH_TOKEN=$(cat ~/.github_token | tr -d '\r\n')

cp "$SRC" "$DEST/index.html"
cd "$DEST"
# 公開版與本機版的 manifest 只有 start_url 不同，這裡確保公開版是 "./"
python - <<'PY'
import re, io
p = "corn-manifest.json"
s = io.open(p, encoding="utf-8").read()
s = re.sub(r'"start_url":\s*"[^"]*"', '"start_url": "./"', s)
io.open(p, "w", encoding="utf-8").write(s)
PY

git add -A
if git diff --cached --quiet; then
  echo "(沒有任何變更)"
else
  git commit -q -m "update: $(date '+%Y-%m-%d %H:%M')"
  git push -q
  echo "已推送 ✓  https://aibotchao-cell.github.io/corn-tycoon/"
  echo "(GitHub Pages 大約 30~60 秒後生效)"
fi
