import smtplib

user = 'pythoncamp'
password = 'haslo'

sent_from = "pythonbootcamp@wp.pl"
to = ["rkorzen@wp.pl"]
subject = 'Try this'
body = "To jest tresc"

email_txt = f"""
From: {sent_from}
to: {', '.join(to)}
Subject: {subject}

{body}
"""

try server = smtplib.SMTP_SSL("smtp.wp.pl", 465)
    server.ehlo()
    server.login(user, password)
    server.sendmail(sent_from, to, email_txt)
    