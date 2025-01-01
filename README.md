# YouTube Live Chat Bot

This Python script allows you to send messages to a YouTube live chat during a stream using the YouTube Data API v3. It authenticates using OAuth2, stores the credentials in a local pickle file for reuse, and sends messages to the live chat of a YouTube live stream.

## Prerequisites

- Python 3.x
- Google Cloud Project with YouTube Data API v3 enabled
- `credentials.json` file (OAuth 2.0 credentials)
- Required Python libraries:
  - `google-auth-oauthlib`
  - `google-api-python-client`
  - `pickle` (part of the Python standard library)

### Steps to Set Up

1. **Create a Google Cloud Project**
   - Go to the [Google Cloud Console](https://console.cloud.google.com/).
   - Create a new project or use an existing one.
   - Enable the **YouTube Data API v3**.
   - Create OAuth 2.0 credentials for a desktop application.
   - Download the credentials JSON file and save it as `credentials.json` in the same directory as this script.

2. **Install Dependencies**
   You can install the required libraries using `pip`:

   ```bash
   pip install google-auth-oauthlib google-api-python-client
