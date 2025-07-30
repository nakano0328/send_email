import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import datetime

def create_email_content():
    """
    メールの件名と本文(HTML)を生成する関数。
    ★★この関数の中身を、あなたの送りたい内容に合わせて書き換えてください★★
    """
    print("メール内容の作成を開始します...")

    # --- ▼▼▼ ここを自由にカスタマイズ ▼▼▼ ---

    # メール件名
    today_str = datetime.date.today().strftime("%Y/%m/%d")
    subject = f"{today_str}の定例通知"
    
    # メール本文 (HTML形式で自由に記述できます)
    html_content = """
    <html>
    <body>
        <h1>おはようございます！</h1>
        <p>今日のタスクリストです。</p>
        <ul>
            <li>タスクA：資料作成</li>
            <li>タスクB：メール返信</li>
            <li>タスクC：会議準備</li>
        </ul>
        <p>今日も一日頑張りましょう！</p>
    </body>
    </html>
    """
    
    # --- ▲▲▲ ここまでカスタマイズ ▲▲▲ ---
    
    print("メール内容の作成が完了しました。")
    return subject, html_content

def send_email(subject, html_content):
    """メールを送信する関数 (この関数は変更不要です)"""
    smtp_server = os.environ.get('SMTP_SERVER')
    smtp_port = os.environ.get('SMTP_PORT')
    smtp_username = os.environ.get('SMTP_USERNAME')
    smtp_password = os.environ.get('SMTP_PASSWORD')
    recipient_email = os.environ.get('RECIPIENT_EMAIL')

    if not all([smtp_server, smtp_port, smtp_username, smtp_password, recipient_email]):
        print("エラー: メール送信に必要な環境変数が設定されていません。")
        return

    msg = MIMEMultipart('alternative')
    msg['Subject'] = subject
    msg['From'] = smtp_username
    msg['To'] = recipient_email
    msg.attach(MIMEText(html_content, 'html', 'utf-8'))

    try:
        with smtplib.SMTP(smtp_server, int(smtp_port)) as server:
            server.starttls()
            server.login(smtp_username, smtp_password)
            server.send_message(msg)
        print("メールを正常に送信しました。")
    except Exception as e:
        print(f"メールの送信に失敗しました: {e}")

if __name__ == '__main__':
    mail_subject, mail_body = create_email_content()
    send_email(mail_subject, mail_body)