import subprocess
import re
import sys
#import requests
import os

def update_jira_ticket(jira_id_pattern=r'\b[A-Z]+-\d+\b'):
    jira_url = os.getenv("jira_url")
    jira_username = os.getenv("jira_username")
    jira_api_token = os.getenv("jira_api_token")
    commit_msg = os.getenv("commit_msg")
    print("Commit Message fom Github Repo-", commit_msg )
    match = re.search (jira_id_pattern, commit_msg)
    print(match)
    jira_id=match.group()
    print(" JIRA ID- {jira_id} ")
    print(jira_url)
    print(commit_msg)



if __name__ == "__main__":
   print("In Main")
   update_jira_ticket()