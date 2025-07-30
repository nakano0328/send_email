# send_email

GitHub Actionsを用いて定期的にメールを自動送信するスクリプトです。

## 概要

このプロジェクトは、GitHub Actionsのスケジュール機能を使用して、毎日決まった時間に自動的にメールを送信するシステムです。メールの内容は簡単にカスタマイズでき、日次のタスクリマインダーや定期通知などに活用できます。

## まとめ記事

このスクリプトの詳細や利用方法に関して、以下のまとめ記事をご覧ください。

- [Zennの記事](https://zenn.dev/mtk0328/articles/send-email-github)
- [Qiitaの記事](https://qiita.com/nakano0328/items/6deed8e4a83100104802)

## 機能

- **定期実行**: 毎日指定した時間に自動でメール送信
- **手動実行**: GitHub ActionsのUI から手動でワークフローを実行可能
- **カスタマイズ可能**: メールの件名・本文を簡単に変更可能
- **HTML対応**: リッチテキストでのメール送信に対応

## セットアップ

### 1. リポジトリのSecrets設定

GitHubリポジトリの Settings > Secrets and variables > Actions で以下のSecretsを設定してください：

- `SMTP_SERVER`: SMTPサーバーのホスト名
- `SMTP_PORT`: SMTPサーバーのポート番号（通常587）
- `SMTP_USERNAME`: 送信者のメールアドレス
- `SMTP_PASSWORD`: 送信者のメールパスワード（アプリパスワード推奨）
- `RECIPIENT_EMAIL`: 受信者のメールアドレス

### 2. メール内容のカスタマイズ

[main.py](main.py)の`create_email_content()`関数内で、メールの件名と本文を自由に編集できます：

```py
# メール件名
subject = f"{today_str}の定例通知"

# メール本文 (HTML形式)
html_content = """
<html>
<body>
    <h1>おはようございます！</h1>
    <p>今日のタスクリストです。</p>
    <!-- ここを自由に変更 -->
</body>
</html>
"""
```

### 3. 実行スケジュールの変更

[.github/workflows/main.yml](.github/workflows/main.yml)のcron設定で実行時間を変更できます：

```yml
schedule:
  # 毎日午前8時 (JST) に実行 (UTCでは前日の23:00)
  - cron: "0 23 * * *"
```

## 使用方法

### 自動実行
設定したスケジュールに従って自動的に実行されます。

### 手動実行
1. GitHubリポジトリの「Actions」タブを開く
2. 「定期メール自動送信」ワークフローを選択
3. 「Run workflow」ボタンをクリック

## ファイル構成

```
.
├── .github/
│   └── workflows/
│       └── main.yml      # 自動化の指示書
├── main.py               # メインのPythonスクリプト
└── requirements.txt      # (今回は空のファイル)
```

## 主な設定例

### Gmail使用時の設定例
- `SMTP_SERVER`: `smtp.gmail.com`
- `SMTP_PORT`: `587`
- `SMTP_USERNAME`: あなたのGmailアドレス
- `SMTP_PASSWORD`: Gmailのアプリパスワード

## 注意事項

- メール送信にはアプリパスワードの使用を強く推奨します
- cron設定の時刻はUTCで指定する必要があります（JST = UTC + 9時間）
- 無料のGitHubアカウントでは月間の実行時間に制限があります

## トラブルシューティング

### メール送信が失敗する場合
1. Secrets設定が正しいか確認
2. SMTPサーバー・ポート番号が正しいか確認
3. アプリパスワードを使用しているか確認
4. GitHub Actionsのログで詳細なエラーメッセージを確認

### ワークフローが実行されない場合
1. cron設定が正しいか確認
2. リポジトリがプライベートの場合、適切な権限設定がされているか確認# send_email
GitHub Actionsを用いてメールを送るスクリプト
