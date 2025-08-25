import subprocess
import re
import sys
import requests
import os 
from jira.client import JIRA
from atlassian import Jira
import json

def update_jira_ticket(jira_id_pattern=r'\b[A-Z]+-\d+\b'):
    jira_url = os.getenv("jira_url")
    jira_username = os.getenv("jira_username")
    jira_api_token = os.getenv("jira_api_token")
    commit_msg = os.getenv("commit_msg")
    print("Commit Message fom Github Repo-", commit_msg )
    match = re.search (jira_id_pattern, commit_msg)
    print(match)
    jira_id=match.group()
    print("JIRA ID-",jira_id)
   
   
    #jira_api_url = f"{jira_url}/rest/api/3/issue/{jira_id}"
    #https://dhananjayvd1.atlassian.net/browse/SCRUM-1
    jira_api_url = f"{jira_url}/browse/{jira_id}"
    print(jira_api_url)
    #response_verify = requests.get(jira_api_url, auth=("dhananjayvd1@gmail.com","Jan_2025"))
    response_verify = requests.get(jira_api_url, auth=(jira_username,jira_api_token) )
    print(response_verify.json)
    print(response_verify.status_code)

    #https://dhananjayvd1.atlassian.net/rest/api/3/issue/SCRUM-1/comment

    #jira_comment_url = f"{jira_url}/browse/{jira_id}/comments"
    jira_comment_url = f"{jira_url}/rest/api/3/issue/{jira_id}/comment"
    print(jira_comment_url)
    headers = { "Content-Type": "application/json" }
    payload = { "body": commit_msg }
    response_comment = requests.post(jira_comment_url, auth=(jira_username,jira_api_token), headers=headers, data=json.dumps(payload) )
    print(response_comment.status_code)
    

if __name__ == "__main__":
   print("In Main")
   update_jira_ticket()