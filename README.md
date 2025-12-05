# Prompt Library Manager

> 訂閱式、智慧化的 AI Prompt 管理與執行平台

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![TypeScript](https://img.shields.io/badge/TypeScript-5.0-blue.svg)](https://www.typescriptlang.org/)
[![Electron](https://img.shields.io/badge/Electron-Latest-47848F.svg)](https://www.electronjs.org/)

---

## 🎯 專案簡介

Prompt Library Manager 是一個功能強大的桌面應用程式，讓您能夠：

- **📚 訂閱社群 Prompt 庫**: 自動同步 GitHub 上的優質 Prompt 集合 (如 Awesome ChatGPT Prompts)
- **⚙️ 智慧變數系統**: 將靜態 Prompt 轉換為動態表單，一鍵填寫參數
- **🤖 多模型支援**: 整合 OpenAI、Google Gemini、Anthropic Claude、Ollama
- **💾 本地優先**: 資料完全儲存於本地，隱私安全
- **🔍 智慧搜尋**: 快速查找函式、API、Prompt 內容

---

## ✨ 核心功能

### 1. 訂閱系統
自動同步來自 GitHub 的 Prompt 集合，支援：
- Awesome ChatGPT Prompts
- Midjourney Styles Library
- Mr. Ranedeer AI Tutor
- 自訂訂閱源

### 2. 智慧變數引擎
將 Prompt 中的變數自動轉換為互動式表單：

```markdown
Write a {{Tone:Professional|Casual}} blog post about {{Topic}}
with {{WordCount#1000}} words.
```

自動生成：
- 文字輸入欄位
- 下拉選單
- 數值滑桿
- 多選核取方塊

### 3. 一鍵執行
填寫參數後直接發送至您選擇的 AI 模型，支援即時串流輸出。

---

## 🚀 快速開始

### 環境需求

- Node.js 18+
- npm 或 yarn
- Windows / macOS / Linux

### 安裝步驟

```bash
# 克隆專案
git clone https://github.com/kaoru0429/Prompt-Master.git
cd Prompt-Master

# 安裝依賴
npm install

# 啟動開發環境
npm run dev

# 建構應用程式
npm run build
```

### 配置 API 金鑰

1. 開啟應用程式設定
2. 新增您的 AI 服務 API 金鑰：
   - OpenAI API Key
   - Google Gemini API Key
   - Anthropic API Key
   - Ollama URL (本地模型)

---

## 📂 專案結構

```
prompt-library-manager/
├── src/                        # 原始碼
│   ├── components/             # React UI 元件
│   ├── services/               # 業務邏輯服務
│   ├── utils/                  # 工具函式
│   └── types/                  # TypeScript 類型定義
├── scripts/                    # 工具腳本
│   ├── code-wiki.py           # Code Wiki 搜尋工具
│   └── generate-wiki-index.py # Wiki 索引生成器
├── config/                     # 配置檔案
│   └── subscriptions.json     # 訂閱源配置
├── wiki/                       # 專案 Wiki 文檔
│   ├── index.md               # Wiki 主頁
│   ├── function-reference.md  # 函式參考
│   └── api-reference.md       # API 文檔
├── lib/                        # 共用函式庫
├── tests/                      # 測試檔案
│   ├── unit/                  # 單元測試
│   └── integration/           # 整合測試
└── docs/                       # 文檔
    ├── prompt-library-concept.md  # 完整概念設計
    └── codewiki-snapshot.md       # Code Wiki 快照
```

---

## 🛠️ 開發工具整合

### Code Wiki 系統

快速搜尋專案中的函式和 API：

```bash
# 搜尋函式名稱
python scripts/code-wiki.py "calculateHandlingTime"

# 搜尋中文概念
python scripts/code-wiki.py "動態處理時間"

# 使用正則表達式
python scripts/code-wiki.py "function.*Allocation" --regex

# 限定檔案類型
python scripts/code-wiki.py "Routes API" --type md
```

### Gemini CLI 分析

當需要分析大型程式碼庫時，使用 Gemini CLI：

```powershell
# 分析整個原始碼目錄
gemini -p "@src/ 總結此程式碼庫的架構"

# 比對多個檔案
gemini -p "@src/main.ts @src/renderer.ts 分析應用程式流程"

# 功能驗證
gemini -p "@src/ @lib/ 變數引擎是否已實作?顯示相關檔案"
```

---

## 📖 文檔

- [完整概念設計](docs/prompt-library-concept.md) - 詳細的系統架構與功能規劃
- [Wiki 主頁](wiki/index.md) - 專案 Wiki 導航
- [函式參考](wiki/function-reference.md) - 完整的函式文檔
- [API 參考](wiki/api-reference.md) - REST API 端點說明

---

## 🗺️ 開發路線圖

- [x] 專案初始化與架構設計
- [x] 完整概念文檔撰寫
- [ ] MVP UI 原型 (Electron + React)
- [ ] 智慧變數引擎實作
- [ ] OpenAI API 整合
- [ ] GitHub 訂閱系統
- [ ] 多模型支援 (Gemini, Claude, Ollama)
- [ ] 執行歷史與版本控制
- [ ] 雲端同步功能 (Optional)

---

## 🤝 貢獻指南

我們歡迎所有形式的貢獻！

1. Fork 本專案
2. 建立功能分支 (`git checkout -b feature/AmazingFeature`)
3. 提交變更 (`git commit -m 'Add some AmazingFeature'`)
4. 推送至分支 (`git push origin feature/AmazingFeature`)
5. 開啟 Pull Request

### 開發規範

- 使用 TypeScript 嚴格模式
- 遵循 ESLint 規則
- 撰寫單元測試 (覆蓋率 > 80%)
- 更新相關文檔

---

## 📄 授權

本專案採用 MIT 授權條款 - 詳見 [LICENSE](LICENSE) 檔案

---

## 👨‍💻 作者

**TestProject Team**

- GitHub: [@kaoru0429](https://github.com/kaoru0429)

---

## 🙏 致謝

本專案靈感來源與使用的開源資源：

- [Awesome ChatGPT Prompts](https://github.com/f/awesome-chatgpt-prompts)
- [Electron](https://www.electronjs.org/)
- [React](https://react.dev/)
- [shadcn/ui](https://ui.shadcn.com/)
- [Better SQLite3](https://github.com/WiseLibs/better-sqlite3)

---

## 📞 聯絡方式

有任何問題或建議？

- 開啟 [GitHub Issue](https://github.com/kaoru0429/prompt-library-manager/issues)
- 發送 Pull Request
- 聯絡維護者

---

**建構時間**: 2025-12-05
**專案狀態**: 🚧 開發中
**目前版本**: v0.1.0 (Concept Phase)
