from github.GithubException import GithubException

from app.github.client import GitHubClient


class GitHubCommentService:
    """
    Posts comments to GitHub Pull Requests.
    """

    def __init__(self):

        self.client = GitHubClient().get_client()

    def post_comment(
        self,
        owner: str,
        repository: str,
        pull_request: int,
        body: str,
    ) -> None:

        try:

            repo = self.client.get_repo(f"{owner}/{repository}")

            pr = repo.get_pull(pull_request)

            pr.create_issue_comment(body)

            print()

            print("Comment posted successfully.")

        except GithubException as error:

            print()

            print("GitHub API Error")

            print(error)
