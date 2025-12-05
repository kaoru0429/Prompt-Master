# Repository 資訊

## GitHub Repository

**Repository URL**: https://github.com/kaoru0429/Prompt-Master

**專案名稱**: Prompt Library Manager (Prompt Master)

**描述**: 訂閱式、智慧化的 AI Prompt 管理與執行平台

## Repository 結構

```
Prompt-Master/
├── .claude/              # Claude Code 配置
├── .git/                 # Git 版本控制
├── config/               # 配置檔案
│   └── subscriptions.json
├── docs/                 # 文檔
│   ├── prompt-library-concept.md  # 完整概念設計
│   └── repository-info.md         # Repository 資訊
├── lib/                  # 共用函式庫
├── scripts/              # 工具腳本
│   ├── code-wiki.py              # Code Wiki 搜尋工具
│   └── generate-wiki-index.py    # Wiki 索引生成器
├── src/                  # 原始碼
│   ├── components/       # React 元件
│   ├── services/         # 業務邏輯
│   ├── types/            # TypeScript 類型
│   └── utils/            # 工具函式
├── tests/                # 測試
│   ├── unit/             # 單元測試
│   └── integration/      # 整合測試
├── wiki/                 # Wiki 文檔
│   └── index.md          # Wiki 主頁
├── .gitignore            # Git 忽略規則
├── CLAUDE.md             # Claude Code 專案配置
├── LICENSE               # MIT License
├── README.md             # 專案說明
├── package.json          # Node.js 依賴
└── tsconfig.json         # TypeScript 配置
```

## 分支策略

- **main**: 主要開發分支
- **feature/***: 功能開發分支
- **bugfix/***: Bug 修復分支
- **release/***: 發布分支

## 提交規範

使用 Conventional Commits 格式：

```
<type>(<scope>): <subject>

<body>

<footer>
```

**Type 類型**:
- `feat`: 新功能
- `fix`: Bug 修復
- `docs`: 文檔更新
- `style`: 程式碼格式化
- `refactor`: 重構
- `test`: 測試
- `chore`: 構建過程或輔助工具的變動

**範例**:
```
feat(parser): 新增變數解析器支援多選語法

- 實作 {{變數:選項1,選項2,選項3}} 語法
- 新增單元測試
- 更新文檔

Closes #123
```

## 標籤（Tags）

- `v0.1.0`: 初始版本（概念設計完成）
- `v0.2.0`: Phase 1 完成（基礎架構）
- `v0.3.0`: Phase 2 完成（CRUD 功能）
- ...
- `v1.0.0`: MVP 發布

## Issues 管理

**標籤分類**:
- `bug`: Bug 回報
- `enhancement`: 功能增強
- `documentation`: 文檔相關
- `question`: 問題討論
- `good first issue`: 適合新手
- `help wanted`: 需要協助

## Pull Request 流程

1. Fork repository
2. 創建 feature 分支
3. 開發並測試
4. 提交 Pull Request
5. Code Review
6. 合併到 main

## 聯絡方式

- **GitHub Issues**: https://github.com/kaoru0429/Prompt-Master/issues
- **Discussions**: https://github.com/kaoru0429/Prompt-Master/discussions
- **維護者**: [@kaoru0429](https://github.com/kaoru0429)

## License

MIT License - 查看 [LICENSE](../LICENSE) 檔案

---

**建立日期**: 2025-12-05
**最後更新**: 2025-12-05
