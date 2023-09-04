import requests

def create_issue():

    # personal authentication credentials
    JIRA_URL = "https://demo-server.atlassian.net"
    USERNAME = "ra5803@srmist.edu.in"
    API_TOKEN = "ATATT3xFfGF0Lo7YO01xcC2CIW34BEFJ_QNbxm3HQzaICk5Q0A1gtrBRBxFFTQFov7QSAgDYjnbQ_Jiczjq7YF1sVePaxnmSF972WwOOoI6nbQhrkPRRcfY5GkpyH8UAJOo8aOU-qS92lkRcz71vjdbYygHQB-CsmA9Vkhw6CYJyobaTsS865rA=F4078428"  # You can generate an API token from your Jira account settings


    PROJECT_KEY = "KAN"
    ISSUE_TYPE = "Task"

    # Construct the API endpoint URL for creating issues
    CREATE_ISSUE_API = f"{JIRA_URL}/rest/api/3/issue/"

    # Set up the API request headers
    # headers = {
    #     "Content-Type": "application/json"
    # }

    headers = {
        "X-Atlassian-Token": "no-check",  # Disable CSRF token check for attachments
    }

    # Define the data for the new issue
    issue_data = {
        "fields": {
            "project": {
                "key": PROJECT_KEY
            },
            "summary": "Issue summary",
            "issuetype": {
                "name": ISSUE_TYPE
            }
        }
    }

    # issue_data2 = {
#     "fields": {
#         "project": {
#             "id": "10233"
#         },
#         "issuetype": {
#             "id": "10004"
#         },
#         "summary": "CFT : Demo 1",
#         "description": {
#             "version": 1,
#             "type": "doc",
#             "content": [
#                 {
#                     "type": "paragraph",
#                     "content": [
#                         {
#                             "type": "text",
#                             "text": "Ignore this issue"
#                         }
#                     ]
#                 }
#             ]
#         },
#         "priority": {
#             "id": "3",
#             "name": "Medium",
#             "iconUrl": "https://tatadigital.atlassian.net/images/icons/priorities/medium.svg"
#         },
#         "fixVersions": [
#             {
#                 "id": "10962"
#             }
#         ],
#         "components": [
#             {
#                 "id": "12354",
#                 "name": "Brand - Westside"
#             }
#         ],
#         "customfield_10040": {
#             "id": "10036",
#             "value": "Functional"
#         },
#         "customfield_10061": {
#             "id": "10880",
#             "value": "CFT"
#         },
#         "customfield_10102": {
#             "id": "10962"
#         },
#         "customfield_10100": {
#             "id": "10406",
#             "value": "Android",
#             "child": {
#                 "id": "10913",
#                 "value": "Samsung Galaxy S21 FE"
#             }
#         },
#         "customfield_10086": "NA",
#         "customfield_10096": [
#             {
#                 "id": "10305",
#                 "value": "Android 12.0"
#             }
#         ],
#         "customfield_10093": [],
#         "customfield_10097": [
#             "CFT_4.0.0"
#         ]
#     },
#     "update": {}
# }

    # Make the API request to create the issue
    response = requests.post(
        CREATE_ISSUE_API,
        headers=headers,
        auth=(USERNAME, API_TOKEN),
        json=issue_data
    )

    # Check the API response
    if response.status_code == 201:
        print("Issue created successfully.")
        issue_key = response.json()["key"]
        print(f"Issue key: {issue_key}")

        # Attach the file to the created issue
        attachment_url = f"{JIRA_URL}/rest/api/2/issue/{issue_key}/attachments"
        files = {'file': ('demo.txt', open('demo.txt', 'rb'))}
        
        attachment_response = requests.post(
            attachment_url,
            headers=headers,
            auth=(USERNAME, API_TOKEN),
            files=files
        )
        
        if attachment_response.status_code == 200:
            print("Attachment added successfully.")
        else:
            print("Attachment addition failed.")
            print("Response:", attachment_response.text)

    else:
        print("Issue creation failed.")
        print("Response:", response.text)
