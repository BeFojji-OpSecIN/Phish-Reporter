import requests
import json
import whois
import smtplib
from email.mime.text import MIMEText

DOMAIN = input("Enter the domain to check: ")
EMAIL = input("Enter your email address: ")
PASSWORD = input("Enter your email password: ")
REGISTRAR_EMAIL = input("Enter the email address of the domain registrar: ")

# WHOIS lookup to get registrar email
w = whois.whois(DOMAIN)
registrar_email = w.emails[0]

# Check if domain is associated with phishing
url = "checkdomainurl"
headers = {"Content-Type": "application/json"}
data = {"url": DOMAIN}
response = requests.post(url, headers=headers, data=json.dumps(data))
result = response.json()["result"]
is_phishing = result["is_phishing"]
phishing_score = result["phishing_score"]
if is_phishing:
    print(f"[!] {DOMAIN} is a phishing website with a phishing score of {phishing_score}. Sending email to registrar...")
    # Email message
    message = MIMEText(f"{DOMAIN} has been identified as a phishing website with a phishing score of {phishing_score}. Please take action to investigate and remove this website from your domain.")
    message['Subject'] = f"Phishing website report for {DOMAIN}"
    message['From'] = EMAIL
    message['To'] = REGISTRAR_EMAIL
    # Connect to email server and send message
    with smtplib.SMTP_SSL("smtp.gmail.com", 465) as server:
        server.login(EMAIL, PASSWORD)
        server.sendmail(EMAIL, REGISTRAR_EMAIL, message.as_string())
    print("[+] Email sent!")
else:
    print(f"[+] {DOMAIN} is not a phishing website.")
