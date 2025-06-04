# import smtplib

# smtp_server = 'smtp.gmail.com'
# smtp_port = 587
# email = 'admin@freedomrun.co.in'
# password = 'tfwr rjuc sfkz qelt'  # your app password, **without spaces**

# try:
#     server = smtplib.SMTP(smtp_server, smtp_port)
#     server.ehlo()
#     server.starttls()
#     server.login(email, password)
#     print("SMTP login successful!")
#     server.quit()
# except Exception as e:
#     print(f"SMTP login failed: {e}")


import yagmail

sender = 'admin@freedomrun.co.in'
app_password = 'tfwrrjucsfkzqelt'  # No spaces
recipient = 'inbarepute@gmail.com'

try:
    yag = yagmail.SMTP(user=sender, password=app_password)
    yag.send(
        to=recipient,
        subject='Test Email via yagmail',
        contents='This is a test email sent via yagmail and Gmail SMTP.'
    )
    print("Email sent successfully!")
except Exception as e:
    print(f"Failed to send email: {e}")

