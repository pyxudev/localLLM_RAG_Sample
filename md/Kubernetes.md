# Kubernetes

Kubernetes によるコンテナオーケストレーションの基礎と実践を学びます。

## なぜ Kubernetes を使うのか

Kubernetes は、データセンターのサーバー群を抽象化するレイヤーを提供します。

**メリット**:

- **アプリケーションとサーバーの疎結合**: 独立した開発・運用が可能
- **自動スケーリング**: 負荷に応じた自動調整
- **自己修復**: 障害からの自動回復
- **宣言的設定**: あるべき状態を定義

## 主要コンセプト

### Pod

Kubernetes のデプロイ可能な最小単位です。

**特徴**:

- 1つ以上のコンテナをまとめたもの
- 同じ Pod 内のコンテナは同じノードに配置
- IP アドレスを共有

```yaml
apiVersion: v1
kind: Pod
metadata:
  name: my-first-pod
  labels:
    component: nginx
spec:
  containers:
  - name: nginx
    image: nginx:latest
```

### Service

Pod へのアクセスを提供する安定したエンドポイントです。

**特徴**:

- ラベルセレクタで Pod を選択
- TCP レベルのロードバランシング
- クラスタ内 DNS 名で通信可能

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-first-service
spec:
  selector:
    component: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
```

### ReplicaSet

指定した数の Pod レプリカを維持します。

**機能**:

- Pod の自動作成・削除
- 希望する数のレプリカを維持
- Pod の障害時に自動復旧

### Deployment

ReplicaSet を管理し、ローリングアップデートを実現します。

```yaml
apiVersion: apps/v1
kind: Deployment
metadata:
  name: nginx-deployment
spec:
  replicas: 3
  selector:
    matchLabels:
      component: nginx
  template:
    metadata:
      labels:
        component: nginx
    spec:
      containers:
      - name: nginx
        image: nginx:1.21
```

## 基本操作

### kubectl コマンド

```bash
# リソースの作成
kubectl apply -f nginx-deployment.yaml

# Pod の一覧
kubectl get pod

# Pod の詳細
kubectl describe pod my-first-pod

# コンテナに入る
kubectl exec -it my-first-pod -- bash

# ログ確認
kubectl logs my-first-pod
kubectl logs -f my-first-pod  # リアルタイム

# ポートフォワード
kubectl port-forward deployment/nginx-deployment 8080:80

# リソースの削除
kubectl delete -f nginx-deployment.yaml
```

## ローリングアップデート

Deployment を使った無停止更新の流れ：

1. 新バージョンの Pod を1つ追加
2. 旧バージョンの Pod を1つ削除
3. 上記を繰り返して全 Pod を更新

```bash
# イメージを更新
kubectl set image deployment/nginx-deployment nginx=nginx:1.22

# ロールアウト状態の確認
kubectl rollout status deployment/nginx-deployment

# ロールバック
kubectl rollout undo deployment/nginx-deployment
```

## ネットワーク

### Service の種類

1. **ClusterIP** (デフォルト): クラスタ内部のみアクセス可能
2. **NodePort**: ノードの特定ポート経由でアクセス可能
3. **LoadBalancer**: 外部ロードバランサーを使用

```yaml
apiVersion: v1
kind: Service
metadata:
  name: my-service
spec:
  type: NodePort
  selector:
    component: nginx
  ports:
  - protocol: TCP
    port: 80
    targetPort: 80
    nodePort: 30000
```

## ベストプラクティス

1. **Deployment を使う**: Pod を直接作成しない
2. **リソース制限**: CPU・メモリの上限設定
3. **Health Check**: Liveness/Readiness Probe の設定
4. **ConfigMap/Secret**: 設定と機密情報の分離
5. **Namespace**: リソースの論理的分離