"""Sending email"""

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
from pathlib import Path
from string import Template

script_dir = Path(__file__).parent
template_path = script_dir / "template.html"
image_path = script_dir / "profile.jpg"
template = Template(Path(template_path).read_text())

message = MIMEMultipart()
message["from"] = "hashirnouman76@gmail.com"
message["to"] = "hashirnouman@gmail.com"
message["subject"] = "Test Email123"
body = template.substitute({"name": "nouman"})
message.attach(MIMEText(body, "html"))
message.attach(MIMEImage(Path(image_path).read_bytes()))

# Use Gmail's SMTP server (smtp.gmail.com) on port 587 with TLS
with smtplib.SMTP("smtp.gmail.com", 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    # Use your Gmail credentials
    smtp.login("hashirnouman76@gmail.com", "lmcy aswp ycxg cafc")
    smtp.send_message(message)
    print("Email sent successfully!")
