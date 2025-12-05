#!/usr/bin/env python3
"""
Wiki 索引生成器
自動掃描專案原始碼，生成函式索引和參考文檔
"""

import json
import re
from pathlib import Path
from typing import List, Dict, Tuple
from datetime import datetime

class WikiIndexGenerator:
    def __init__(self, project_root: Path, verbose: bool = False):
        self.project_root = project_root
        self.verbose = verbose
        self.src_dir = project_root / "src"
        self.lib_dir = project_root / "lib"
        self.wiki_dir = project_root / "wiki"

        # 確保 wiki 目錄存在
        self.wiki_dir.mkdir(exist_ok=True)

    def generate(self):
        """生成完整的 Wiki 索引"""
        print("🔍 開始掃描專案...")

        # 掃描函式、類別和 API
        functions = self._scan_functions()
        classes = self._scan_classes()
        apis = self._scan_apis()

        # 生成 JSON 索引
        index_data = {
            "generated_at": datetime.now().isoformat(),
            "version": "1.0",
            "functions": functions,
            "classes": classes,
            "apis": apis,
            "statistics": {
                "total_functions": len(functions),
                "total_classes": len(classes),
                "total_apis": len(apis)
            }
        }

        # 儲存 JSON 索引
        index_file = self.wiki_dir / "index.json"
        with open(index_file, 'w', encoding='utf-8') as f:
            json.dump(index_data, f, indent=2, ensure_ascii=False)

        print(f"✅ 已生成 JSON 索引: {index_file}")

        # 生成 Markdown 參考文檔
        self._generate_function_reference(functions)
        self._generate_api_reference(apis)

        print(f"\n📊 統計:")
        print(f"   - 函式: {len(functions)}")
        print(f"   - 類別: {len(classes)}")
        print(f"   - APIs: {len(apis)}")

    def _scan_functions(self) -> List[Dict]:
        """掃描所有函式"""
        functions = []

        for dir_path in [self.src_dir, self.lib_dir]:
            if not dir_path.exists():
                continue

            for file_path in dir_path.rglob("*.ts"):
                functions.extend(self._extract_functions_from_file(file_path))

            for file_path in dir_path.rglob("*.tsx"):
                functions.extend(self._extract_functions_from_file(file_path))

        return functions

    def _extract_functions_from_file(self, file_path: Path) -> List[Dict]:
        """從檔案中提取函式"""
        functions = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            # TypeScript 函式模式
            patterns = [
                r'export\s+(?:async\s+)?function\s+(\w+)',  # export function
                r'(?:export\s+)?const\s+(\w+)\s*=\s*(?:async\s+)?\(',  # const func =
                r'(?:public|private|protected)\s+(?:async\s+)?(\w+)\s*\(',  # class methods
            ]

            for line_num, line in enumerate(lines, start=1):
                for pattern in patterns:
                    match = re.search(pattern, line)
                    if match:
                        func_name = match.group(1)

                        # 提取文檔註解
                        doc_comment = self._extract_doc_comment(lines, line_num - 1)

                        functions.append({
                            "name": func_name,
                            "file": str(file_path.relative_to(self.project_root)),
                            "line": line_num,
                            "file_type": file_path.suffix[1:],
                            "description": doc_comment,
                            "context": line.strip()
                        })

                        if self.verbose:
                            print(f"   找到函式: {func_name} @ {file_path.name}:{line_num}")

        except Exception as e:
            print(f"⚠️  讀取檔案錯誤 {file_path}: {e}")

        return functions

    def _extract_doc_comment(self, lines: List[str], line_num: int) -> str:
        """提取文檔註解"""
        doc_lines = []

        # 向上搜尋註解
        for i in range(line_num - 1, max(0, line_num - 10), -1):
            line = lines[i].strip()

            if line.startswith('*') or line.startswith('//'):
                doc_lines.insert(0, line.lstrip('/*').strip())
            elif line.startswith('/**'):
                doc_lines.insert(0, line.lstrip('/**').strip())
                break
            elif line and not line.startswith('*'):
                break

        return ' '.join(doc_lines) if doc_lines else ""

    def _scan_classes(self) -> List[Dict]:
        """掃描所有類別"""
        classes = []

        for dir_path in [self.src_dir, self.lib_dir]:
            if not dir_path.exists():
                continue

            for file_path in dir_path.rglob("*.ts"):
                classes.extend(self._extract_classes_from_file(file_path))

        return classes

    def _extract_classes_from_file(self, file_path: Path) -> List[Dict]:
        """從檔案中提取類別"""
        classes = []

        try:
            with open(file_path, 'r', encoding='utf-8') as f:
                content = f.read()
                lines = content.split('\n')

            # TypeScript 類別模式
            pattern = r'(?:export\s+)?class\s+(\w+)'

            for line_num, line in enumerate(lines, start=1):
                match = re.search(pattern, line)
                if match:
                    class_name = match.group(1)

                    doc_comment = self._extract_doc_comment(lines, line_num - 1)

                    classes.append({
                        "name": class_name,
                        "file": str(file_path.relative_to(self.project_root)),
                        "line": line_num,
                        "file_type": file_path.suffix[1:],
                        "description": doc_comment,
                        "context": line.strip()
                    })

                    if self.verbose:
                        print(f"   找到類別: {class_name} @ {file_path.name}:{line_num}")

        except Exception as e:
            print(f"⚠️  讀取檔案錯誤 {file_path}: {e}")

        return classes

    def _scan_apis(self) -> List[Dict]:
        """掃描 API 端點"""
        # TODO: 實作 API 端點掃描
        # 需要根據實際的路由定義方式來實作
        return []

    def _generate_function_reference(self, functions: List[Dict]):
        """生成函式參考文檔"""
        output_file = self.wiki_dir / "function-reference.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# 函式參考 (Function Reference)\n\n")
            f.write(f"> 自動生成於: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**函式總數**: {len(functions)}\n\n")
            f.write("---\n\n")

            # 依檔案分組
            functions_by_file = {}
            for func in functions:
                file_path = func["file"]
                if file_path not in functions_by_file:
                    functions_by_file[file_path] = []
                functions_by_file[file_path].append(func)

            # 輸出每個檔案的函式
            for file_path in sorted(functions_by_file.keys()):
                f.write(f"## 📁 {file_path}\n\n")

                for func in functions_by_file[file_path]:
                    f.write(f"### `{func['name']}`\n\n")
                    f.write(f"**位置**: {func['file']}:{func['line']}\n\n")

                    if func['description']:
                        f.write(f"**說明**: {func['description']}\n\n")

                    f.write(f"```typescript\n{func['context']}\n```\n\n")
                    f.write("---\n\n")

        print(f"✅ 已生成函式參考: {output_file}")

    def _generate_api_reference(self, apis: List[Dict]):
        """生成 API 參考文檔"""
        output_file = self.wiki_dir / "api-reference.md"

        with open(output_file, 'w', encoding='utf-8') as f:
            f.write("# API 參考 (API Reference)\n\n")
            f.write(f"> 自動生成於: {datetime.now().strftime('%Y-%m-%d %H:%M:%S')}\n\n")
            f.write(f"**API 端點總數**: {len(apis)}\n\n")
            f.write("---\n\n")

            if not apis:
                f.write("⚠️ 尚未定義 API 端點\n")
            else:
                for api in apis:
                    f.write(f"## `{api['method']} {api['path']}`\n\n")
                    f.write(f"**說明**: {api['description']}\n\n")
                    f.write("---\n\n")

        print(f"✅ 已生成 API 參考: {output_file}")


def main():
    import argparse

    parser = argparse.ArgumentParser(description="Wiki 索引生成器")
    parser.add_argument("--verbose", "-v", action="store_true", help="顯示詳細資訊")

    args = parser.parse_args()

    # 取得專案根目錄
    project_root = Path(__file__).parent.parent

    # 建立生成器
    generator = WikiIndexGenerator(project_root, verbose=args.verbose)

    # 生成索引
    generator.generate()


if __name__ == "__main__":
    main()
