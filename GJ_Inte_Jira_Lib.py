import subprocess
import re
import sys
import requests
import os 
from jira import JIRA
#from atlassian import Jira
import json

def update_jira_ticket(jira_id_pattern=r'\b[A-Z]+-\d+\b'):

    commit_msg = "SCRUM-10 Test GJ Integration v1"
    COMMENT_TEXT = "Hello"
    jira_api_token= os.getenv("jira_api_token")
    print("Commit Message fom Github Repo-", commit_msg )
    match = re.search (jira_id_pattern, commit_msg)
    print(match)
    jira_id=match.group()
    print("JIRA ID-",jira_id)

    try :
       jiraOptions = {'server': "https://dhananjayvd1.atlassian.net"}
       jira = JIRA(options=jiraOptions, basic_auth=("dhananjayvd1@gmail.com", jira_api_token ))
           #Display All Project which are accessible 
       print("*******************Project Details**********************")
       for project in jira.projects(): print(project.key)
    except Exception as e:
       print(f"Failed to connect to Jira: {e}")
       exit()




   # for singleIssue in jira.search_issues(jql_str='project = SCRUM'): print('{}: {}:{}'.format(singleIssue.key, singleIssue.fields.summary, singleIssue.fields.reporter.displayName))
    
    #Extract exact issue/Story Details
    try:
       print("********************Issue Details*********************")
       issue = jira.issue(jira_id)
       Issue_Key= issue.key
       print(f"Issue Key: {issue.key}")
       print(f"Status: {issue.fields.status.name}")
    except Exception as e:
       print(f"Failed to Search Issue: {e}")
       exit()


    try:
       jira.add_comment(Issue_Key, COMMENT_TEXT)
       print(f"Comment successfully added to Jira issue: {jira_id}")
    except Exception as e:
       print(f"Failed to add comment to issue {issue_key}: {e}")
       exit()


    
    

if __name__ == "__main__":
   print("In Main")
   update_jira_ticket()