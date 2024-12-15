# AutomatedOutreach

AutomatedOutreach is a Python script designed to simplify and streamline the process of emailing multiple company employees for job opportunities. The script generates personalized emails based on user inputs, supports attachments (e.g., resumes), and tries multiple email patterns to ensure delivery.

## Features
- **Dynamic Email Pattern Matching**: Automatically generates multiple possible email addresses for a recipient based on their name and company domain.
- **Personalized Email Content**: Customizable email body tailored to your university, applied roles, and company.
- **Attachment Support**: Allows adding a resume or other files to emails.
- **Error Handling**: Tracks and reports failed email attempts.

---

## Requirements
Ensure you have the following before running the script:

1. Python 3.7 or above
2. Required Python packages:
    - `smtplib`
    - `email`
    - `os`
3. A valid Gmail account with App Passwords enabled ([Learn how to create an app password](https://support.google.com/accounts/answer/185833?hl=en))
4. A PDF file named `Resume.pdf` in the same directory as the script

---

## Setup
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/AutomatedOutreach.git
   cd AutomatedOutreach
   ```

2. Install dependencies (if applicable):
   ```bash
   pip install -r requirements.txt
   ```

3. Edit the script to include your email credentials:
   ```python
   FROM = 'your-email@gmail.com'
   PASSWORD = 'your-app-password'
   ```

---

## How to Use
1. Run the script:
   ```bash
   python automated_outreach.py
   ```

2. Follow the prompts to:
   - Enter the company name and domain.
   - Input recipient names.
   - Specify your university name.
   - List roles you've applied for (optional).

3. The script will:
   - Generate personalized emails.
   - Attempt to send emails to all specified recipients using common email patterns.

4. View the output for a summary of successful and failed attempts.

---

## Example
### Input
```
Company: Acme Corp
Domain (e.g., company.com): acme.com
First name: John
Last name: Doe
First name: 
Your University Name: University of Example
Have you applied to specific positions? (yes/no): yes
Role applied (e.g., DevOps Engineer): Software Engineer
Link to the job application: https://acme.com/careers/software-engineer
```

### Output
```
Sending Emails...
Email sent to john.doe@acme.com
Email sent to j.doe@acme.com
Failed to send emails to the following names:

```  

---

## Disclaimer
- This script is intended for ethical use only. Do not use it for spamming or unsolicited communication.
- Ensure compliance with the company’s communication policies before sending emails.

---

## Contributions
Feel free to contribute to this project by submitting issues or pull requests.

---

## License
This project is licensed under the [MIT License](LICENSE).
