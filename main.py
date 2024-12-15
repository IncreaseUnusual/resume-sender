import smtplib
from os.path import basename
from email.mime.text import MIMEText
from email.utils import formatdate
from email.mime.multipart import MIMEMultipart
from email.mime.application import MIMEApplication

SERVER = "smtp.gmail.com"
PORT = 587
FROM = ''
PASSWORD = ''

COMPANY = input("Company: ").strip()
DOMAIN = "@" + input("Domain (e.g., company.com): ").strip()

NAMES = []
print('Enter first and last names of employees you want to email (leave blank to finish):')
while True:
    first = input("First name: ").strip()
    if not first:
        break
    last = input("Last name: ").strip()
    NAMES.append((first, last))

UNIVERSITY = input("Your University Name: ").strip()

intro = (
    f"<p>Dear {COMPANY} Team,</p>"
    f"<p>I am a <b>{UNIVERSITY}</b> undergraduate close to graduation, and I am keen on contributing to "
    f"<b>{COMPANY}</b> as a part-time or contract employee. While I couldn't find any open applications on the "
    f"careers page that perfectly align with my profile, I wanted to reach out for future opportunities.</p>"
)

applications = ""
if input("Have you applied to specific positions? (yes/no): ").lower().startswith('y'):
    ROLES = []
    LINKS = []
    while True:
        role = input("Role applied (e.g., DevOps Engineer): ").strip()
        if not role:
            break
        link = input("Link to the job application: ").strip()
        ROLES.append(role)
        LINKS.append(link)

    roles = ", ".join(
        f'<a href="{link}">{role}</a>' for role, link in zip(ROLES, LINKS)
    )
    applications = (
        f"<p>I applied to the following roles: {roles} because I believe my skills and experience match "
        "many of the requirements. I would greatly appreciate it if you could review my application.</p>"
    )

body = (
    "Intro here in HTML format."
)


def send_email(to_email, recipient_name):
    email_content = (
        f"<html><body>"
        f"{intro}"
        f"{applications}"
        f"{body}"
        f"</body></html>"
    )
    message = MIMEMultipart()
    message['From'] = FROM
    message['To'] = to_email
    message['Date'] = formatdate(localtime=True)
    message['Subject'] = "[Junior/Mid-level] Part-Time/Contract Employment Opportunity"

    message.attach(MIMEText(email_content, 'html'))

    try:
        with open("Resume.pdf", "rb") as file:  # Ensure this file exists in the same directory
            part = MIMEApplication(file.read(), Name=basename("Resume.pdf"))
            part['Content-Disposition'] = f'attachment; filename="{basename("Resume.pdf")}"'
            message.attach(part)
    except FileNotFoundError:
        print("Resume.pdf not found. Skipping attachment.")

    try:
        with smtplib.SMTP(SERVER, PORT) as server:
            server.starttls()
            server.login(FROM, PASSWORD)
            server.sendmail(FROM, to_email, message.as_string())
        return True
    except smtplib.SMTPException as e:
        print(f"Failed to send to {to_email}: {e}")
        return False


failed_attempts = []

print("Sending Emails...")
for first, last in NAMES:
    sent = False
    for pattern in [
        f"{first}{last}{DOMAIN}",
        f"{first}.{last}{DOMAIN}",
        f"{first[0]}{last}{DOMAIN}",
        f"{first}{last[0]}{DOMAIN}",
        f"{first}_{last}{DOMAIN}",
        f"{first}-{last}{DOMAIN}",
        f"{last}.{first}{DOMAIN}",
        f"{last}{first}{DOMAIN}",
        f"{last}_{first}{DOMAIN}",
        f"{last}-{first}{DOMAIN}",
        f"{first[0]}.{last}{DOMAIN}",
        f"{first}.{last[0]}{DOMAIN}",
        f"{first[0]}_{last}{DOMAIN}",
        f"{first}_{last[0]}{DOMAIN}",
        f"{first[0]}-{last}{DOMAIN}",
        f"{first}-{last[0]}{DOMAIN}",
        f"{first[0]}{last[0]}{DOMAIN}",
        f"{last}.{first[0]}{DOMAIN}",
        f"{last}{first[0]}{DOMAIN}",
        f"{last[0]}{first}{DOMAIN}",
        f"{last[0]}_{first}{DOMAIN}",
        f"{last[0]}-{first}{DOMAIN}",
        f"{last[0]}{first[0]}{DOMAIN}"
    ]:
        if send_email(pattern, f"{first} {last}"):
            print(f"Email sent to {pattern}")
            sent = True
            break  # Exit after the first successful email
    if not sent:
        failed_attempts.append((first, last))

if failed_attempts:
    print("Failed to send emails to the following names:")
    for first, last in failed_attempts:
        print(f"{first} {last}")