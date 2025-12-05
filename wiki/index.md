# Prompt Library Manager - Wiki 主頁

> 專案文檔導航中心

**更新日期**: 2025-12-05
**Wiki 版本**: v1.0

---

## 📚 快速導航

### 核心文檔

| 文檔 | 說明 | 狀態 |
|------|------|------|
| [函式參考](function-reference.md) | 完整的函式文檔與 API | 🚧 建構中 |
| [API 參考](api-reference.md) | REST API 端點說明 | 🚧 建構中 |
| [版本對比](version-comparison.md) | 版本更新與變更記錄 | 📝 規劃中 |
| [快速參考](quick-reference.md) | 常用命令速查表 | 📝 規劃中 |

### 開發指南

| 文檔 | 說明 | 狀態 |
|------|------|------|
| [架構設計](../docs/prompt-library-concept.md) | 完整的系統架構與技術設計 | ✅ 完成 |
| [開發環境設置](setup-guide.md) | 環境配置與安裝步驟 | 📝 規劃中 |
| [貢獻指南](contributing.md) | 如何為專案貢獻 | 📝 規劃中 |
| [測試指南](testing-guide.md) | 單元測試與整合測試 | 📝 規劃中 |

---

## 🔍 Code Wiki 搜尋工具

### 基本搜尋

快速查找專案中的函式、類別、API：

```bash
# 搜尋函式名稱
python scripts/code-wiki.py "executePrompt"

# 搜尋中文概念
python scripts/code-wiki.py "訂閱系統"

# 使用正則表達式
python scripts/code-wiki.py "function.*Handler" --regex
```

### 進階搜尋

```bash
# 限定檔案類型 (md, ts, py, js)
python scripts/code-wiki.py "PromptAdapter" --type ts

# 限定版本
python scripts/code-wiki.py "performAllocation" --version v2.0

# 顯示更多結果
python scripts/code-wiki.py "CONFIG" --limit 100

# 只顯示檔案和行號（不顯示上下文）
python scripts/code-wiki.py "handleSubscription" --no-context
```

### 更新索引

當修改源代碼後，執行索引生成器：

```bash
# 生成函式索引和參考文檔
python scripts/generate-wiki-index.py

# 顯示詳細資訊
python scripts/generate-wiki-index.py --verbose
```

---

## 🤖 Gemini CLI 深度分析

### 程式碼庫分析

使用 Gemini 的大型 context window 分析整個專案：

```powershell
# 分析整個原始碼目錄
gemini -p "@src/ 總結此程式碼庫的架構"

# 結合多個目錄
gemini -p "@src/ @lib/ 分析共用函式庫的設計模式"

# 包含測試覆蓋率分析
gemini -p "@src/ @tests/ 分析測試覆蓋率並指出未測試的功能"
```

### 功能驗證

檢查特定功能是否已實作：

```powershell
# 驗證訂閱系統
gemini -p "@src/ @config/ 訂閱系統是否已實作?顯示相關檔案"

# 驗證變數引擎
gemini -p "@src/ @lib/ 智慧變數引擎是否已實作?展示解析邏輯"

# 驗證 API 整合
gemini -p "@src/services/ OpenAI、Gemini、Claude 的 API 整合是否完整?"
```

### 深度理解

```powershell
# 追蹤資料流
gemini -p "@src/ 追蹤從訂閱 Prompt 到執行的完整流程"

# 效能分析
gemini -p "@src/ 分析變數引擎的效能瓶頸和優化機會"

# 安全性審查
gemini -p "@src/ 檢查 API 金鑰儲存的安全性實作"
```

---

## 📊 專案統計

### 目前狀態

| 指標 | 數值 | 備註 |
|------|------|------|
| 函式總數 | 0 | 待開發 |
| 測試覆蓋率 | 0% | 待開發 |
| 文檔完整度 | 30% | 概念設計已完成 |
| 程式碼行數 | 0 | 待開發 |

### 開發進度

- ✅ 專案結構建立
- ✅ 完整概念文檔
- ✅ Wiki 系統初始化
- 🚧 MVP UI 開發中
- ⏳ 變數引擎待開發
- ⏳ API 整合待開發

---

## 🎓 學習資源

### TypeScript 開發

- [TypeScript 官方文檔](https://www.typescriptlang.org/docs/)
- [TypeScript Deep Dive](https://basarat.gitbook.io/typescript/)

### Electron 開發

- [Electron 官方文檔](https://www.electronjs.org/docs/latest)
- [Electron Fiddle](https://www.electronjs.org/fiddle)

### React 開發

- [React 官方文檔](https://react.dev/)
- [React Hooks](https://react.dev/reference/react)

### AI API 整合

- [OpenAI API 文檔](https://platform.openai.com/docs)
- [Google Gemini API](https://ai.google.dev/)
- [Anthropic Claude API](https://docs.anthropic.com/)

---

## 🔧 工具與配置

### 開發工具

- **Code Editor**: VS Code (推薦擴充功能: ESLint, Prettier, TypeScript)
- **版本控制**: Git + GitHub
- **套件管理**: npm / yarn
- **測試框架**: Jest + React Testing Library
- **建構工具**: Electron Builder

### 專案配置

```
.
├── .vscode/           # VS Code 設定
├── .github/           # GitHub Actions CI/CD
├── tsconfig.json      # TypeScript 配置
├── package.json       # 專案依賴
└── electron.config.js # Electron 建構配置
```

---

## 📝 版本記錄

### v0.1.0 (2025-12-05)
- ✨ 專案初始化
- 📝 完整概念設計文檔
- 🏗️ 建立專案結構
- 📚 Wiki 系統建置

### Upcoming (v0.2.0)
- 🎨 MVP UI 原型
- ⚙️ 基礎變數引擎
- 🔌 OpenAI API 整合

---

## 🤝 社群與支援

### 取得協助

- 📖 查閱 [完整概念文檔](../docs/prompt-library-concept.md)
- 🐛 回報 [Bug](https://github.com/kaoru0429/prompt-library-manager/issues)
- 💡 提出 [功能建議](https://github.com/kaoru0429/prompt-library-manager/discussions)

### 參與貢獻

- 🍴 Fork 專案並提交 PR
- 📝 改善文檔
- ✅ 撰寫測試
- 🎨 設計 UI/UX

---

## 📞 聯絡方式

**專案維護者**: [@kaoru0429](https://github.com/kaoru0429)

---

**Wiki 系統版本**: v1.0
**最後更新**: 2025-12-05
**維護團隊**: TestProject Team
