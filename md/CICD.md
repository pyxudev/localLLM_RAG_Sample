# CI/CD

継続的インテグレーションと継続的デリバリーの実践方法を学びます。

## CI/CD でできること

**継続的インテグレーション (CI)**:

- 自動ビルド
- 自動テスト実行
- コード品質チェック
- 早期のバグ検出

**継続的デリバリー (CD)**:

- 自動デプロイ
- ステージング環境への配信
- 本番環境へのリリース
- ロールバック機能

## CircleCI

クラウドベースの CI/CD プラットフォームです。

**特徴**:

- YAML ベースの設定
- Docker サポート
- 並列実行
- ワークフロー管理

**基本的な設定例**:

```yaml
version: 2.1
jobs:
  build:
    docker:
      - image: circleci/node:14
    steps:
      - checkout
      - run: npm install
      - run: npm test
      - run: npm run build

workflows:
  version: 2
  build-and-test:
    jobs:
      - build
```