# AI

AI 開発ツール、MCP サーバー、Vibe Coding などの最新 AI 技術を探求します。

## Vibe Coding ツール

AI を活用した次世代の開発ツールを 5 つのカテゴリに分類します。

### 1. AI 統合 IDE 型

AI が開発プロセスを支援する統合開発環境です。

**代表ツール**:

- **Cursor**: AI ファーストの IDE
- **Windsurf**: コード生成とリファクタリング
- **Trae**: インテリジェントなコード補完

### 2. コード支援型

既存の IDE にプラグインとして追加します。

**代表ツール**:

- **GitHub Copilot**: AI ペアプログラミング
- **Cody (Sourcegraph)**: コンテキスト理解型支援
- **JetBrains AI**: IntelliJ 統合
- **Gemini Code Assist**: Google の AI アシスタント

### 3. アプリ生成型

UI・DB・デプロイまですべて自動構築します。

**代表ツール**:

- **Replit Agent**: フルスタック自動生成
- [**Bolt.new**](http://Bolt.new): Web アプリの即時作成
- **Lazy AI**: ノーコード AI 開発
- **Tempo**: 高速プロトタイピング
- **Lovable**: デザインから実装まで
- **v0**: Vercel の AI デザイナー

### 4. エージェント実行型

チケットから PR まで自動で実行します。

**代表ツール**:

- **Devin**: 完全自律型 AI エンジニア
- **Sweep**: GitHub Issues から自動実装
- [**Fine.dev**](http://Fine.dev): タスクの自動処理
- **Copilot Workspace**: エンドツーエンド開発
- **Cline**: CLI ベースのエージェント

### 5. CLI エージェント型

ターミナル上でコード生成や編集を行います。

**代表ツール**:

- **Claude Code**: Anthropic の CLI ツール
- **Codex CLI**: OpenAI の CLI
- **Aider**: Git 統合型 AI ペアプログラミング

## 6. MCP (Model Context Protocol) Server

AI モデルとアプリケーションを接続するプロトコルです。

### MCP サーバーの作成

### TypeScript

```tsx
import { Server, Tool } from "@modelcontextprotocol/typescript-server-sdk";

const server = new Server({
  port: 3000,
  name: "Example MCP Server",
  version: "1.0.0"
});

server.registerTool({
  name: "calculator",
  description: "Performs basic calculations",
  parameters: {
    expression: {
      type: "string",
      description: "The math expression to evaluate"
    }
  },
  handler: async (params) => {
    const result = eval(params.expression);
    return { result };
  }
});

server.start();
```

### Python

```python
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("Demo")

@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers"""
    return a + b

@mcp.resource("greeting://{name}")
def get_greeting(name: str) -> str:
    """Get a personalized greeting"""
    return f"Hello, {name}!"
```

### 実行方法

```bash
# TypeScript
npx @modelcontextprotocol/inspector node build/index.js

# Python
mcp run [server.py](http://server.py)
```

## AI 開発のベストプラクティス

### プロンプトエンジニアリング

**効果的なプロンプトの書き方**:

1. **明確な指示**: 何をしてほしいか具体的に
2. **コンテキストの提供**: 背景情報を含める
3. **例の提示**: Few-shot learning の活用
4. **制約の明示**: やってほしくないことも伝える

### コードレビュー

AI 生成コードのチェックポイント：

- [ ]  セキュリティリスクの確認
- [ ]  パフォーマンスの検証
- [ ]  エッジケースの処理
- [ ]  テストコードの作成
- [ ]  ドキュメントの整備

## 参考リソース

- [MCP Beginner Guide (Microsoft)](https://github.com/microsoft/mcp-beginner-guide)
- [How I Use Claude Code](https://spiess.dev/blog/how-i-use-claude-code)
- [Cursor で議事録を要件定義書にまとめる](https://qiita.com/WdknWdkn/items/79980f4201c8cf9145bf)

## 今後の展望

- **マルチエージェントシステム**: 複数の AI が協調作業
- **コンテキスト理解の向上**: より正確なコード生成
- **カスタマイズ性の向上**: プロジェクト固有の学習
- **セキュリティの強化**: 安全な AI 利用