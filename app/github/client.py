import os

from dotenv import load_dotenv
from github import Github


class GitHubClient:
    """
    Creates authenticated GitHub API clients.
    """

    def __init__(self):

        load_dotenv()

        token = os.getenv("GITHUB_TOKEN")

        if not token:
            raise RuntimeError("GITHUB_TOKEN not found in environment.")

        self.client = Github(token)

    def get_client(self) -> Github:
        return self.client
