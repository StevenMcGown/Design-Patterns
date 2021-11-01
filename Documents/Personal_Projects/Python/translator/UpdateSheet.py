from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ["https://www.googleapis.com/auth/spreadsheets"]
SERVICE_ACCOUNT_FILE = 'creds/sheets.json'

creds = None
creds = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES
)

SPREADSHEET_ID = "1nYFE3dxMDk9nL6Rbd0rJ8S2yYQOFiOyVUgzqK2U82Jg"

service = build('sheets', 'v4', credentials=creds)

sheet = service.spreadsheets()


def removeDuplicates(words):
    return list(set([i for i in words]))

def getSpreadsheet():
    return sheet.values().get(spreadsheetId=SPREADSHEET_ID, range="Flashcards").execute()


def updateSpreadsheet(words):
    print("Length of words array before removing duplicates: " + str(len(words)))
    words = removeDuplicates(words)
    print("Length of words array after removing duplicates: " + str(len(words)))
    sheet.values().update(spreadsheetId=SPREADSHEET_ID, range="Flashcards!A2",
                          valueInputOption="USER_ENTERED", body={"values": words}).execute()
