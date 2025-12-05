#!/usr/bin/env python3
"""
Code Wiki - 專案搜尋工具
快速查找函式、類別、API 文檔
"""

import json
import re
import argparse
from pathlib import Path
from typing import List, Dict, Optional

class CodeWikiSearch:
    def __init__(self, project_root: Path):
        self.project_root = project_root
        self.wiki_dir = project_root / "wiki"
        self.index_file = self.wiki_dir / "index.json"
        self.index_data = self._load_index()

    def _load_index(self) -> Dict:
        """載入 Wiki 索引"""
        if self.index_file.exists():
            with open(self.index_file, 'r', encoding='utf-8') as f:
                return json.load(f)
        return {"functions": [], "classes": [], "apis": []}

    def search(
        self,
        query: str,
        file_type: Optional[str] = None,
        use_regex: bool = False,
        limit: int = 20,
        show_context: bool = True
    ) -> List[Dict]:
        """
        搜尋函式、類別或 API

        Args:
            query: 搜尋關鍵字
            file_type: 檔案類型篩選 (md, ts, py, js)
            use_regex: 是否使用正則表達式
            limit: 結果數量限制
            show_context: 是否顯示上下文

        Returns:
            搜尋結果列表
        """
        results = []

        # 搜尋索引
        for category in ["functions", "classes", "apis"]:
            for item in self.index_data.get(category, []):
                if self._match(item, query, use_regex):
                    if file_type is None or item.get("file_type") == file_type:
                        results.append({
                            "category": category,
                            "name": item.get("name"),
                            "file": item.get("file"),
                            "line": item.get("line"),
                            "description": item.get("description", ""),
                            "context": item.get("context", "") if show_context else ""
                        })

        # 搜尋檔案內容
        if len(results) < limit:
            results.extend(self._search_files(query, file_type, use_regex, limit - len(results)))

        return results[:limit]

    def _match(self, item: Dict, query: str, use_regex: bool) -> bool:
        """判斷項目是否匹配查詢"""
        name = item.get("name", "")
        description = item.get("description", "")

        if use_regex:
            pattern = re.compile(query, re.IGNORECASE)
            return bool(pattern.search(name) or pattern.search(description))
        else:
            query_lower = query.lower()
            return query_lower in name.lower() or query_lower in description.lower()

    def _search_files(
        self,
        query: str,
        file_type: Optional[str],
        use_regex: bool,
        limit: int
    ) -> List[Dict]:
        """在專案檔案中搜尋"""
        results = []
        search_dirs = [
            self.project_root / "src",
            self.project_root / "lib",
            self.project_root / "wiki"
        ]

        extensions = {
            "md": [".md"],
            "ts": [".ts", ".tsx"],
            "py": [".py"],
            "js": [".js", ".jsx"]
        }

        search_extensions = extensions.get(file_type, [".md", ".ts", ".tsx", ".py", ".js", ".jsx"]) if file_type else [".md", ".ts", ".tsx", ".py", ".js", ".jsx"]

        for search_dir in search_dirs:
            if not search_dir.exists():
                continue

            for file_path in search_dir.rglob("*"):
                if file_path.suffix in search_extensions:
                    results.extend(self._search_in_file(file_path, query, use_regex, limit))
                    if len(results) >= limit:
                        break

        return results[:limit]

    def _search_in_file(
        self,
        file_path: Path,
        query: str,
        use_regex: bool,
        limit: int
    ) -> List[Dict]:
        """在單一檔案中搜尋"""
        results = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                lines = f.readlines()

            for line_num, line in enumerate(lines, start=1):
                if use_regex:
                    pattern = re.compile(query, re.IGNORECASE)
                    if pattern.search(line):
                        results.append({
                            "category": "file_content",
                            "name": query,
                            "file": str(file_path.relative_to(self.project_root)),
                            "line": line_num,
                            "context": line.strip()
                        })
                else:
                    if query.lower() in line.lower():
                        results.append({
                            "category": "file_content",
                            "name": query,
                            "file": str(file_path.relative_to(self.project_root)),
                            "line": line_num,
                            "context": line.strip()
                        })

                if len(results) >= limit:
                    break

        except Exception as e:
            print(f"Error reading {file_path}: {e}")

        return results

    def display_results(self, results: List[Dict], show_context: bool = True):
        """顯示搜尋結果"""
        if not results:
            print("❌ 未找到匹配結果")
            return

        print(f"\n✅ 找到 {len(results)} 個結果:\n")

        for i, result in enumerate(results, start=1):
            category_emoji = {
                "functions": "🔧",
                "classes": "📦",
                "apis": "🌐",
                "file_content": "📄"
            }

            emoji = category_emoji.get(result["category"], "📄")
            print(f"{emoji} [{i}] {result['name']}")
            print(f"   📁 {result['file']}:{result['line']}")

            if show_context and result.get("context"):
                print(f"   💬 {result['context'][:100]}...")

            if result.get("description"):
                print(f"   ℹ️  {result['description']}")

            print()


def main():
    parser = argparse.ArgumentParser(
        description="Code Wiki - 專案搜尋工具",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
範例:
  python code-wiki.py "calculateHandlingTime"
  python code-wiki.py "動態處理時間"
  python code-wiki.py "function.*Allocation" --regex
  python code-wiki.py "Routes API" --type md
  python code-wiki.py "CONFIG" --limit 100 --no-context
        """
    )

    parser.add_argument("query", help="搜尋關鍵字")
    parser.add_argument("--type", choices=["md", "ts", "py", "js"], help="限定檔案類型")
    parser.add_argument("--regex", action="store_true", help="使用正則表達式")
    parser.add_argument("--limit", type=int, default=20, help="結果數量限制 (預設: 20)")
    parser.add_argument("--no-context", action="store_true", help="不顯示上下文")
    parser.add_argument("--version", help="限定版本 (暫未實作)")

    args = parser.parse_args()

    # 取得專案根目錄
    project_root = Path(__file__).parent.parent

    # 建立搜尋器
    searcher = CodeWikiSearch(project_root)

    # 執行搜尋
    results = searcher.search(
        query=args.query,
        file_type=args.type,
        use_regex=args.regex,
        limit=args.limit,
        show_context=not args.no_context
    )

    # 顯示結果
    searcher.display_results(results, show_context=not args.no_context)


if __name__ == "__main__":
    main()
