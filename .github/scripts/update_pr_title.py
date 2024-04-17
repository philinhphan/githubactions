import sys
import openai
from github import Github

def generate_new_title(pr_description):
    # Using OpenAI's API to generate a new title based on the PR description
    response = openai.Completion.create(
        engine="text-davinci-002",  # Adjust as per the current best model
        prompt=f"Generate a concise and informative title for a pull request based on the following description: {pr_description}",
        max_tokens=60
    )
    return response.choices[0].text.strip()

def update_pr_title(repo_name, pr_number, pr_description, token):
    g = Github(token)
    repo = g.get_repo(repo_name)
    pr = repo.get_pull(pr_number)
    new_title = generate_new_title(pr_description)
    pr.edit(title=new_title)

if __name__ == "__main__":
    repo_name = 'philinhphan/githubactions'  # Replace with actual repo name
    pr_number = int(sys.argv[1])
    pr_description = sys.argv[2]  
    token = sys.argv[3]
    update_pr_title(repo_name, pr_number, pr_description, token)
