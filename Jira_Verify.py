import subprocess
import re
import sys
#import requests
import os

def update_jira_ticket(jira_url="", jira_username="", 
                       jira_api_token="", 
                       jira_id_pattern=r'\b[A-Z]+-\d+\b', commit_msg="SCRUM-1-123-first Jira"):
    match = re.search (jira_id_pattern, commit_msg)
    print(match)
    jira_id=match.group()
    print(jira_id)


if __name__ == "__main__":
   print("In Main")
   update_jira_ticket()