# Integrating Microsoft Identity Platform with a Python web application

This is a Python web application that uses the Flask framework and the Microsoft identity platform to sign in users and make authenticated calls to the Microsoft Graph API.

# Configuration

## If you are configuring your Microsoft Entra ID app or Microsoft Entra External ID app

To get started with this sample, you have two options:

* Use the Azure portal to create the Azure AD applications and related objects. Follow the steps in
  [Quickstart: Add sign-in with Microsoft to a Python web app](https://docs.microsoft.com/azure/active-directory/develop/web-app-quickstart?pivots=devlang-python).
* Use PowerShell scripts that automatically create the Azure AD applications and related objects (passwords, permissions, dependencies) for you, and then modify the configuration files. Follow the steps in the [App Creation Scripts README](./AppCreationScripts/AppCreationScripts.md).


## Environment file

In the root directory, create the following `.env` file:
```
# Note: If you are using Azure App Service, go to your app's Configuration,
# and then set the following values into your app's "Application settings".
FLASK_DEBUG=True

# The following variables are required for the app to run.
CLIENT_ID=<from_microsoft_app>
CLIENT_SECRET=<from_microsoft_app>
AUTHORITY=<from_microsoft_app>

GOOGLE_CLIENT_ID=<from_google_cloud_app>
GOOGLE_CLIENT_SECRET=<from_google_cloud_app>
```