## 環境要件

- Windows 11
- 低スペックPC
    - プロセッサ: 11th Gen Intel(R) Core(TM) i5-1135G7 @ 2.40GHz (2.42 GHz)
    - 実装 RAM: 8.00 GB (7.80 GB 使用可能)
- Ollama
- Python 3.13 (※3.14 および以降は現在互換性エラー未解決)
- C/C++ コンパイラー ([Visual Studio Installer](https://visualstudio.microsoft.com/visual-cpp-build-tools/))

## 構成

```
rag-local/
 ├ pdf/
 │   ├ sample1.pdf
 │   └ sample2.pdf
 ├ md/
 │   ├ sample1.md
 │   └ sample2.md
 ├ db/
 ├ ingest.py
 └ chat.py
```

## コマンド

1. チャットモデルダウンロード
    ```Bash
    ollama pull phi3:mini
    ```
2. Embeddingモデル
    ```Bash
    ollama pull nomic-embed-text
    ```
3. パッケージインストール
    ```Bash
    pip install numpy pypdf ollama langchain langchain-community langchain_ollama chromadb
    ```
4. Ollama 起動（バックグランドで実行していない場合）
    ```Bash
    ollama serve
    ```

## スクリプト


## 実行

```Bash
python ingest.py
```
```
Loaded PDF docs: 0
Loaded Markdown docs: 18
Split chunks: 55
Done. Vector DB saved.
```

```Bash
python chat.py
```
```
Q: How many cars does Justin have?

A: The question is related to the following information about Justin, which includes his personal information such as "is a rich, smart, talented, outstanding and hungsome guy", "lives in a big house in Hawaii", "has 8947 cars, 409742 yard property in France, and 26 wives". Justin's address is also mentioned. The question seeks to clarify which number of cars he has.

Q: Justin's address please        

A: Certainly! Here is a sample AI-generated response to the question "What is Justin's address?" in accordance with the given information:

"Justin's address is 44-16, Greate Street. It's located in Hawaii and has 8947 cars, 409742 yard property in France, and 26 wives."
```