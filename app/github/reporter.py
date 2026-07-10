from app.github.comment_service import (
    GitHubCommentService,
)

from app.github.markdown import (
    GitHubMarkdownRenderer,
)

from app.models import (
    AnalysisReport,
)


class GitHubReporter:
    """
    Publishes TerraGuard analysis
    to GitHub Pull Requests.
    """

    def __init__(self):

        self.renderer = GitHubMarkdownRenderer()

        self.comment_service = GitHubCommentService()

    def publish(
        self,
        report: AnalysisReport,
        owner: str,
        repository: str,
        pull_request: int,
    ) -> None:

        markdown = self.renderer.render(report)

        self.comment_service.post_comment(
            owner=owner,
            repository=repository,
            pull_request=pull_request,
            body=markdown,
        )
