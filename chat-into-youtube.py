import os
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors
import pickle

# Replace with your live video ID
live_video_id = "3iRz7_-x4Dk"

# OAuth2 parameters
scopes = ["https://www.googleapis.com/auth/youtube.force-ssl"]

# Load OAuth2 authentication information from JSON file
# Got to Google Cloud Console > Create a project > Activate 'YouTube Data API v3' > create 0Auth 2.0 identification. > put it in a json file (like credentials.json)
# On the first run, it will save the token in a pickle file.

client_secrets_file = "credentials.json"
credentials_file = "token.pickle"

# Function to get an access token via OAuth2
def get_authenticated_service():
    credentials = None

    # If the token file exists, load credentials from this file
    if os.path.exists(credentials_file):
        with open(credentials_file, "rb") as token:
            credentials = pickle.load(token)

    # If credentials are invalid or non-existent, restart OAuth2 authentication
    if not credentials or not credentials.valid:
        if credentials and credentials.expired and credentials.refresh_token:
            credentials.refresh(Request())
        else:
            flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
                client_secrets_file, scopes)
            credentials = flow.run_local_server(port=0)

        # Save credentials for next use
        with open(credentials_file, "wb") as token:
            pickle.dump(credentials, token)

    youtube = googleapiclient.discovery.build("youtube", "v3", credentials=credentials)
    return youtube

# Function to send a message in the live chat
def send_message_to_chat(message, youtube, live_video_id):
    # Retrieve the live chat ID
    request = youtube.videos().list(
        part="liveStreamingDetails",
        id=live_video_id
    )
    response = request.execute()

    if "items" not in response or len(response["items"]) == 0:
        print("No live stream found.")
        return

    live_chat_id = response["items"][0]["liveStreamingDetails"]["activeLiveChatId"]
    
    # Send the message in the live chat
    request = youtube.liveChatMessages().insert(
        part="snippet",
        body={
            "snippet": {
                "type": "textMessageEvent",
                "liveChatId": live_chat_id,
                "textMessageDetails": {
                    "messageText": message
                }
            }
        }
    )
    
    response = request.execute()
    print(f"Message sent: {message}")

# Get the authenticated service
youtube = get_authenticated_service()

# Send a message
send_message_to_chat("Hey B-word, is your mom hot?", youtube, live_video_id)
