import requests
import json
import smtplib
from email.mime.text import MIMEText

# Azure DevOps organization URL
organization_url = "https://dev.azure.com/janranjani450"

# Personal access token (PAT) with appropriate permissions
personal_access_token = "cxkhy5rf2rgz5hzkyxw3s67kszsq6upxto5qhmydhcng4scxomg"

# Project ID or name
project = "registrationform"

# API version
api_version = "7.0"

# SMTP server configuration
smtp_server = "smtp.gmail.com"
smtp_port = 587
smtp_username = "janaranjani.venkatesan@isteer.com"
smtp_password = "byxdaebckqugidrr"

# Email configuration
sender_email = "janaranjani.venkatesan@isteer.com"
receiver_email = "janaranjani.venkatesan@isteer.coml"
email_subject = "New Work Item Created"

# Create a work item
def create_work_item(title, description):
    url = f"{organization_url}/{project}/_apis/wit/workitems/$Task?api-version={api_version}"

    headers = {
        "Authorization": "Bearer " + personal_access_token,
        "Content-Type": "application/json-patch+json"
    }

    payload = [
        {
            "op": "add",
            "path": "/fields/System.Title",
            "value": title
        },
        {
            "op": "add",
            "path": "/fields/System.Description",
            "value": description
        }
    ]

    response = requests.patch(url, headers=headers, data=json.dumps(payload))

    if response.status_code == 200:
        print("Work item created successfully.")
        send_email(title, description)
    else:
        print("Failed to create work item. Error:", response.text)

# Send email with work item details
def send_email(title, description):
    message = f"Title: {title}\nDescription: {description}"

    msg = MIMEText(message)
    msg['Subject'] = email_subject
    msg['From'] = sender_email
    msg['To'] = receiver_email

    try:
        server = smtplib.SMTP(smtp_server, smtp_port)
        server.starttls()
        server.login(smtp_username, smtp_password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
        server.quit()
        print("Email sent successfully.")
    except Exception as e:
        print("Failed to send email. Error:", str(e))

# Usage example
title = "Sample Task"
description = "This is a sample task created via REST API."

create_work_item(title, description)
