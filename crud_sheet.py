import os.path

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

from dotenv import load_dotenv

# 載入 .env
load_dotenv()


# google sheet api的使用範圍
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

# 要crud的google sheet ID
SAMPLE_SPREADSHEET_ID = os.getenv("GOOGLE_SHEET_ID")
TAB_SHEET_NAME = os.getenv("TAB_SHEET_NAME")
STUDENT_AMOUNT = int(os.getenv("STUDENT_AMOUNT"))


def load_to_google_sheet():
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())
    try:
        service = build('sheets', 'v4', credentials=creds)
        # 呼叫 Sheets API
        sheet = service.spreadsheets()
        return sheet
        
        # result = sheet.values().get(spreadsheetId=SAMPLE_SPREADSHEET_ID,
        #                             range=SAMPLE_RANGE_NAME).execute()
        # values = result.get('values', [])

        # if not values:
        #     print('No data found.')
        #     return
        # print(values)
    except HttpError as err:
        print(err)

def create_basic_data():
    sheet = load_to_google_sheet()
    try:
        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{TAB_SHEET_NAME}!A1",
                              valueInputOption="USER_ENTERED", body={"values": [["座號\考試"]]}).execute()
        for student_number in range(1, STUDENT_AMOUNT+1):
            sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{TAB_SHEET_NAME}!A{student_number+1}",
                                  valueInputOption="USER_ENTERED", body={"values": [[student_number]]}).execute()
        print("success")
    except:
        print("fail")


def register_grades(test_name, student_number, score):
    sheet = load_to_google_sheet()
    try:
        # sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{TAB_SHEET_NAME}!B1",
        #                       valueInputOption="USER_ENTERED", body={"values": [[f"{test_name}"]]}).execute()
        sheet.values().update(spreadsheetId=SAMPLE_SPREADSHEET_ID, range=f"{TAB_SHEET_NAME}!B{student_number+1}",
                                  valueInputOption="USER_ENTERED", body={"values": [[score]]}).execute()
    except:
        print("成績輸入錯誤")


if __name__ == '__main__':
    register_grades("常春藤w1", 13, 98)