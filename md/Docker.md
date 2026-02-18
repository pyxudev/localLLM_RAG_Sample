# Docker

Docker の基礎から実践的なコンテナ化手法まで、1週間の集中学習プランです。

## Docker とは

Docker は、アプリケーションを開発、配布、実行するためのオープンプラットフォームです。

**特徴**:

- アプリケーションをインフラから分離
- コードを迅速に本番環境にデリバリー
- 開発環境と本番環境の一貫性

## VM との違い

### Docker コンテナ

- ホスト OS のカーネルを共有
- 軽量で起動が速い
- リソース使用量が少ない
- ポータビリティが高い

### 仮想マシン

- 完全なゲスト OS を必要とする
- 起動時間が長い
- リソース消費が大きい
- 強固な隔離

## 基本コマンド

### イメージ管理

```bash
# イメージの取得
docker pull ubuntu

# イメージ一覧
docker images

# イメージの削除
docker rmi イメージID
```

### コンテナ管理

```bash
# コンテナ起動
docker run -d -p 8080:80 --name my-nginx nginx

# コンテナ一覧
docker ps
docker ps -a  # 停止中も含む

# コンテナ停止
docker stop コンテナID

# コンテナ削除
docker rm コンテナID

# コンテナに入る
docker exec -it コンテナID /bin/bash
```

## Dockerfile

### 基本構文

```docker
# ベースイメージ
FROM node:20-alpine

# 作業ディレクトリ
WORKDIR /app

# 依存関係のコピーとインストール
COPY package*.json ./
RUN npm install

# ソースコードのコピー
COPY . .

# ビルド
RUN npm run build

# ポート公開
EXPOSE 3000

# 起動コマンド
CMD ["npm", "start"]
```

### Multi-stage Build

イメージを軽量化するテクニックです。

```docker
# ビルドステージ
FROM node:20 AS builder
WORKDIR /app
COPY package*.json ./
RUN npm install
COPY . .
RUN npm run build

# 実行ステージ
FROM node:20-slim AS runner
WORKDIR /app
COPY --from=builder /app/package*.json ./
RUN npm install --omit=dev
COPY --from=builder /app/.next ./.next
EXPOSE 3000
CMD ["npm", "start"]
```

## Docker Compose

複数のコンテナをまとめて管理します。

```yaml
version: "3.9"

services:
  web:
    build: ./app
    ports:
      - "3000:3000"
    environment:
      - DB_HOST=db
    depends_on:
      - db

  db:
    image: mysql:8
    environment:
      - MYSQL_ROOT_PASSWORD=pass123
      - MYSQL_DATABASE=mydb
    volumes:
      - mysql_data:/var/lib/mysql

volumes:
  mysql_data:
```

### コマンド

```bash
# 起動
docker-compose up -d

# 停止・削除
docker-compose down

# ログ確認
docker-compose logs -f

# 再ビルド
docker-compose up -d --build
```

## ベストプラクティス

1. **Alpine ベースイメージ**: 軽量化
2. **Multi-stage Build**: 本番イメージの最小化
3. **.dockerignore**: 不要ファイルの除外
4. **レイヤーキャッシュ**: ビルド高速化
5. **ボリュームマウント**: データ永続化