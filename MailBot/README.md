# 📬 MailBot

**MailBot** is a Python-based automation script that connects Google Sheets with your email service to send personalized emails directly from a spreadsheet.  
It’s perfect for sending updates, newsletters, or notifications - all controlled from an easy-to-edit Google Sheet.

---

## 🚀 Features
- Reads recipient email addresses, subject lines, and message bodies from Google Sheets  
- Sends emails automatically via SMTP  
- Uses Google Sheets API and Google Drive API (free and simple setup)  
- Secure authentication with a Google Cloud **Service Account JSON**  
- Customizable delay between emails to prevent spam filters  
- Works with any SMTP email provider (Gmail, Hostinger, etc.)

---

## 🛠️ Requirements
- Python 3.8+
- A Google Cloud **Service Account**
- Access to Google Sheets and Google Drive APIs (enabled via Google Cloud Console)
- The following Python packages:
  ```bash
  pip install gspread oauth2client
