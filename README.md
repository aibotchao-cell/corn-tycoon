# 🌽 玉米罐頭大亨 (Corn Tycoon)

手機放置經營小遊戲：**種玉米 → 裝罐廠做成罐頭 → 攤位上架 → 客人自己來買**。
買了三段自動化之後，站別之間會長出**輸送帶**，機器人會自己收成／裝罐／運送。

## 玩

👉 **https://aibotchao-cell.github.io/corn-tycoon/**

手機可以直接「加到主畫面」，會用全螢幕開啟（像 App 一樣）。

## 玩法

- 走到**玉米田**裡自動收成（背包滿了會提示）
- 走到**裝罐廠**把玉米壓成罐頭
- 走到**攤位**把罐頭上架，客人會自己來買
- 錢拿去**雜貨店**升級（容量、速度、價格、工人／自動化、開分店）

## 更新流程

```bash
bash /c/Users/YO/gh-pages/corn-tycoon/deploy.sh
```

（把最新的 `farm.html` 複製成 `index.html` 後 push；約 30~60 秒生效）

圖示重畫：`uv run --with pillow python make_icon.py`
