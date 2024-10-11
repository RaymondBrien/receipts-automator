import calendar
import pprint

from datetime import datetime
from typing import TypedDict

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError



# If modifying these scopes, delete the file token.json.
SCOPES = ["https://www.googleapis.com/auth/gmail.readonly"]
TAXI_LABEL_ID = 'Label_8621806233538209042'
PROVIDER = {"Royal Cars": 1, "Uber": 2}

# Add trip dictionary type safety
class trip(TypedDict):
        date: datetime
        time: str
        amount: float
        transaction_id: str
        pickup_location: str
        dropoff_location: str
        time_completed: datetime # TODO handle/transform to date later? confirm correct date handling
        provider: object # PROVIDER


class getReceipts():
    def __init__(self):

        self.request_time = datetime.now()  # log time of request
        print('class initialized')

        # call functions
        self.service = self.call_gmail_api()  # initialise service


    def call_gmail_api(self):

        try:
            # Load credentials from file
            creds = Credentials.from_authorized_user_file('token.json')
            # Call the Gmail API
            service = build('gmail', 'v1', credentials=creds)
            print('Got credentials')

        except HttpError as error:
            # TODO(developer) - Handle errors from gmail API.
            print(f"An error occurred: {error}")

        return service



    def get_message_ids_with_taxi_label(self, year: datetime.year, month: datetime.month):
        print(f"Getting messages with taxi label for {month} {year}" )
        def check_service():
            if self.service == None:
                print(f"An error occurred: {error}")
                print("Calling API again")
                self.service = self.call_gmail_api()
            if self.service == None:
                print("Could not get service")
                return  # exit early

        # Get all emails from the 'taxi' label within specified month
        messages = self.service.users().messages().list(
            userId='me',
            labelIds=[TAXI_LABEL_ID],
            q=f"after:{year}/{month}/01 before:{year}/{month + 1}/01"
        ).execute()
        # me = authenticated user

        # print(messsages.length())

        # avoid message duplicates
        return set([message['id'] for message in messages['messages']])




r_date = [datetime.year, datetime.month]
r_date[0] = 2024
r_date[1] = 9

all_messages = getReceipts().get_message_ids_with_taxi_label(r_date[0], r_date[1])

