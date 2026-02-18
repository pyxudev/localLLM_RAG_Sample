# AWS セキュリティ基礎

AWS 環境におけるセキュリティの基本概念と実践を学びます。

## 共有責任モデル

AWS とユーザーでセキュリティ責任を分担します。

**AWS の責任** (Security OF the Cloud):

- 物理インフラストラクチャ
- ハードウェア・ソフトウェア
- ネットワークインフラ
- 施設のセキュリティ

**ユーザーの責任** (Security IN the Cloud):

- データの暗号化
- アクセス管理 (IAM)
- OS・アプリケーションのパッチ適用
- ファイアウォール設定
- ネットワーク構成

## セキュリティのベストプラクティス

### IAM (Identity and Access Management)

**原則**:

1. **最小権限の原則**: 必要最小限の権限のみ付与
2. **ルートユーザーを使わない**: 日常業務では IAM ユーザーを使用
3. **MFA の有効化**: 多要素認証を必ず設定
4. **定期的な認証情報のローテーション**: アクセスキーの定期更新
5. **IAM ロールの活用**: アクセスキーの代わりにロールを使用

### S3 バケットのセキュリティ

**よくある脆弱性**:

- パブリック読み取りアクセスの誤設定
- アクセスポリシーの不適切な設定
- 暗号化の未設定

**対策**:

```json
{
  "Version": "2012-10-17",
  "Statement": [
    {
      "Effect": "Deny",
      "Principal": "*",
      "Action": "s3:*",
      "Resource": [
        "arn:aws:s3:::my-bucket/*",
        "arn:aws:s3:::my-bucket"
      ],
      "Condition": {
        "Bool": {
          "aws:SecureTransport": "false"
        }
      }
    }
  ]
}
```

### EC2 セキュリティ

**ベストプラクティス**:

1. **セキュリティグループの適切な設定**
    - 必要なポートのみ開放
    - 送信元 IP の制限
2. **IMDSv2 の使用**
    - メタデータサービスの保護
    - SSRF 攻撃の防止
3. **Systems Manager Session Manager**
    - SSH ポートを開けずに接続
    - 操作ログの記録

## 実践的セキュリティ演習

### S3 バケットの脆弱性

**攻撃シナリオ**:

1. 公開されている S3 バケットの発見
2. バケットのディレクトリ構造の列挙
3. 機密ファイルのダウンロード

**対策**:

- バケットポリシーの見直し
- パブリックアクセスブロックの有効化
- CloudTrail によるアクセスログ記録

### SSRF (Server-Side Request Forgery)

**攻撃シナリオ**:

```bash
# EC2 メタデータサービスへのアクセス
curl [http://169.254.169.254/latest/meta-data/](http://169.254.169.254/latest/meta-data/)

# IAM クレデンシャルの取得
curl [http://169.254.169.254/latest/meta-data/iam/security-credentials/](http://169.254.169.254/latest/meta-data/iam/security-credentials/)
```

**対策**:

- IMDSv2 の強制使用
- アプリケーションレベルでの URL 検証
- ネットワークセグメンテーション

### 認証情報の漏洩

**危険な例**:

```bash
# コードに直接記述 (NG)
aws_access_key_id = "AKIAIOSFODNN7EXAMPLE"
aws_secret_access_key = "wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY"
```

**安全な方法**:

1. **環境変数の使用**
2. **AWS Secrets Manager**
3. **IAM ロールの使用** (推奨)
4. **Systems Manager Parameter Store**

## セキュリティツール

### AWS セキュリティサービス

- **AWS CloudTrail**: API 呼び出しのログ記録
- **Amazon GuardDuty**: 脅威検知
- **AWS Security Hub**: セキュリティ状況の一元管理
- **AWS Config**: リソース設定の監視
- **Amazon Inspector**: 脆弱性スキャン

### 監視とアラート

```yaml
# CloudWatch Alarm の例
AlarmName: UnauthorizedAPICallsAlarm
MetricName: UnauthorizedAPICalls
Threshold: 1
Period: 300
EvaluationPeriods: 1
ComparisonOperator: GreaterThanThreshold
```

## インシデント対応

### 対応手順

1. **検知**: 異常なアクティビティの発見
2. **封じ込め**: 被害の拡大防止
3. **根絶**: 脅威の除去
4. **復旧**: 正常な状態への回復
5. **事後分析**: 原因究明と改善

### チェックリスト

- [ ]  影響範囲の特定
- [ ]  侵害されたクレデンシャルの無効化
- [ ]  セキュリティグループの見直し
- [ ]  ログの保全
- [ ]  フォレンジック調査
- [ ]  再発防止策の実施