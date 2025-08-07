import smtplib
from email.message import EmailMessage
import gspread
from oauth2client.service_account import ServiceAccountCredentials

# Another thing it's using Goolge Sheets API and Drive API - Free
# Which are can be accessible from Google Cloud Console
# need to create service account and download the json file of the creds
# then need to give access of the Sheet (from which email, sub, body will be taken) to the service account that will be created from Google Cloud Console

# 1. Google Sheets Setup
def get_sheet_data():
    scope = ["https://spreadsheets.google.com/feeds",
             "https://www.googleapis.com/auth/drive"]
    
    creds = ServiceAccountCredentials.from_json_keyfile_name("msnewproject_creds.json", scope)
    client = gspread.authorize(creds)

    #sheet = client.open("Your Sheet Name").sheet1  # Change if needed
    spreadsheet = client.open_by_key("spreadsheet_unique_id_enter_here")
    sheet = spreadsheet.worksheet("sheet_name")
    data = sheet.get_all_values()
    return data[1:]  # Skip header row

# 2. Email Sending Setup
def send_email(to_email, subject, body):
    msg = EmailMessage()
    msg['Subject'] = subject
    msg['From'] = 'xyz@domain.com' #the email id from which mail should go
    msg['To'] = to_email
    msg.set_content(body)

    with smtplib.SMTP_SSL('smtp.hostinger.com', 465) as smtp: # this could be different from different email hosting service
        smtp.login('email_from_which_mail_will_go', 'password_of_the_email')  # Replace with your password
        smtp.send_message(msg)

# 3. Combine: Read from Sheet & Send Emails
def main():
    rows = get_sheet_data()
    for row in rows:
        time.sleep(2)  # 2 seconds delay
        to_email = row[0]
        subject = row[1]
        message = row[2]
        if to_email and subject and message:
            try:
                send_email(to_email, subject, message)
                print(f"Sent to {to_email}")
            except Exception as e:
                print(f"Failed to send to {to_email}: {e}")

if __name__ == "__main__":
    main()


