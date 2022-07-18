from oauth2client.service_account import ServiceAccountCredentials
import gspread


def get_first_sheet_data(api_file_name, document_name):
    scope = ["https://spreadsheets.google.com/feeds", "https://www.googleapis.com/auth/spreadsheets",
             "https://www.googleapis.com/auth/drive.file", "https://www.googleapis.com/auth/drive"]
    creds = ServiceAccountCredentials.from_json_keyfile_name(
        api_file_name, scope)
    client = gspread.authorize(creds)
    sheet = client.open(document_name).sheet1
    data = sheet.get_all_records()

    return data


def get_categories():
    return [
        {
            'name': 'Necessary expenses',
            "absoluteAmount": 50
        },
        {
            "name": 'Discretionary expenses',
            "absoluteAmount": 30
        },
        {
            "name": ' Investments',
            "absoluteAmount": 20
        }
    ]
