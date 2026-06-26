from typing import Callable


class RetryPolicy:
    def __init__(self, attempts: int, backoff: int) -> None:
        self.attempts = attempts
        self.backoff = backoff

    async def execute(self, func: Callable, *args, **kwargs):
        # TODO: implement retry logic for transient failures
        raise NotImplementedError
