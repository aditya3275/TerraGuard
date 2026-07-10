from github.GithubException import GithubException

from app.github.client import GitHubClient
from app.github.markdown import GitHubMarkdownRenderer


class GitHubCommentService:
    """
    Creates or updates TerraGuard Pull Request comments.
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

            marker = GitHubMarkdownRenderer.REPORT_MARKER

            # Look for an existing TerraGuard comment
            for comment in pr.get_issue_comments():

                if marker in comment.body:

                    comment.edit(body)

                    print()
                    print("Updated existing TerraGuard comment.")

                    return

            # No existing comment found.
            pr.create_issue_comment(body)

            print()
            print("Created new TerraGuard comment.")

        except GithubException as error:

            print()
            print("GitHub API Error")
            print(error)
