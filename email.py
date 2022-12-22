import smtplib
frommail = "senderemail"
tomail = "receiveremail"

sub = "This is the subject"
msg = "This is the message body"

server = smtplib.SMTP('smtp.example.com')
server.login("username", "password")
server.sendmail(frommail, tomail, f"Subject: {sub}\n\n{msg}")
server.quit()
