# YouTube Unsubscribe Script

This Python script allows you to unsubscribe from all the YouTube channels you're subscribed to using the YouTube Data API.

## Prerequisites

Before running the script, ensure you have the following:

- Python 3.x installed on your machine.
- A Google Cloud project with the YouTube Data API v3 enabled.
- OAuth 2.0 credentials (client ID and client secret) configured for a desktop application.

## Setup Instructions

### 1. Set Up Google Cloud Project

1. Go to the [Google Cloud Console](https://console.cloud.google.com/).
2. Create a new project (if you don't have one).
3. Navigate to **APIs & Services** > **Library**.
4. Search for "YouTube Data API v3" and click **Enable** to enable the API for your project.

### 2. Configure OAuth Consent Screen

1. Go to **APIs & Services** > **OAuth consent screen**.
2. Choose **External** if your app will be used by anyone, or **Internal** if only your Google account will use it.
3. Fill out the necessary information (App name, Support email, etc.).
4. Under **Scopes for Google APIs**, ensure the following scope is added:
   - `https://www.googleapis.com/auth/youtube.force-ssl`
5. Save your changes.

### 3. Create OAuth 2.0 Credentials

1. Navigate to **APIs & Services** > **Credentials**.
2. Click **Create Credentials** and select **OAuth 2.0 Client ID**.
3. Choose **Desktop app** as the application type.
4. Name your OAuth 2.0 client (e.g., "YouTube Unsubscribe Script").
5. Download the `client_secret.json` file and save it in the same directory as your Python script.

### 4. Install Required Python Packages

Install the necessary Python packages using pip:

```bash
pip install google-auth google-auth-oauthlib google-auth-httplib2 google-api-python-client
```

## 5. Run the Script

Run the Python script using the following command:

```bash
python unsubscribe_youtube.py
```

## 6. Troubleshooting

### Error 400: `redirect_uri_mismatch`

Ensure that the redirect URI `http://localhost:8080/` is added to the OAuth 2.0 Client ID settings in the Google Cloud Console.

### Error 403: `access_denied`

- Double-check the OAuth consent screen configuration and ensure the correct scope (`https://www.googleapis.com/auth/youtube.force-ssl`) is included.
- Ensure that your Google account is added as a test user if your app is in "Testing" mode.
- Clear any stored credentials (e.g., delete any `token.json` files) and re-run the script to authenticate again.

### General Tips

- Try running the script in an incognito window or using a different browser if you encounter issues during the authentication flow.
- If the problem persists, consider recreating the OAuth client and starting the setup process from scratch.

## License

This script is provided "as-is" without any warranties. Use it at your own risk.


