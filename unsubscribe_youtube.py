import os
import google.oauth2.credentials
import google_auth_oauthlib.flow
import googleapiclient.discovery
import googleapiclient.errors

# Replace with the path to your client_secret.json file
CLIENT_SECRET_FILE = 'client_secret.json'
SCOPES = ['https://www.googleapis.com/auth/youtube.force-ssl']

def authenticate_youtube_api():
    # Get credentials and create an API client
    flow = google_auth_oauthlib.flow.InstalledAppFlow.from_client_secrets_file(
        CLIENT_SECRET_FILE, SCOPES)
    credentials = flow.run_local_server(port=8080)  # Ensure this port matches the URI you added
    youtube = googleapiclient.discovery.build('youtube', 'v3', credentials=credentials)
    return youtube

def list_subscriptions(youtube):
    # List all subscriptions
    request = youtube.subscriptions().list(
        part="snippet",
        mine=True,
        maxResults=50
    )
    response = request.execute()
    return response.get('items', [])

def remove_subscription(youtube, subscription_id):
    # Remove a subscription
    request = youtube.subscriptions().delete(id=subscription_id)
    request.execute()

def main():
    youtube = authenticate_youtube_api()
    
    subscriptions = list_subscriptions(youtube)
    while subscriptions:
        for subscription in subscriptions:
            print(f"Unsubscribing from: {subscription['snippet']['title']}")
            remove_subscription(youtube, subscription['id'])
        
        # Check if there are more subscriptions to process
        subscriptions = list_subscriptions(youtube)

    print("Unsubscribed from all channels.")

if __name__ == "__main__":
    main()
