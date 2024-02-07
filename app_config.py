import os

# !MS AUTH
AUTHORITY = os.getenv("AUTHORITY") or "https://login.microsoftonline.com/common"

# Application (client) ID of app registration
CLIENT_ID = os.getenv("CLIENT_ID")
# Application's generated client secret: never check this into source control!
CLIENT_SECRET = os.getenv("CLIENT_SECRET")

REDIRECT_PATH = "/getAToken"  # Used for forming an absolute URL to your redirect URI.
# The absolute URL must match the redirect URI you set
# in the app's registration in the Azure portal.

# You can find more Microsoft Graph API endpoints from Graph Explorer
# https://developer.microsoft.com/en-us/graph/graph-explorer
ENDPOINT = 'https://graph.microsoft.com/v1.0/me/events?$select=subject,body,bodyPreview,organizer,attendees,start,end,location'  # This resource requires no admin consent

# You can find the proper permission names from this document
# https://docs.microsoft.com/en-us/graph/permissions-reference
SCOPE = ["Calendars.Read"]

# !GOOGLE AUTH
# Application (client) ID of app registration
GOOGLE_CLIENT_ID = os.getenv("GOOGLE_CLIENT_ID")
# Application's generated client secret: never check this into source control!
GOOGLE_CLIENT_SECRET = os.getenv("GOOGLE_CLIENT_SECRET")

# Tells the Flask-session extension to store sessions in the filesystem
SESSION_TYPE = "filesystem"
