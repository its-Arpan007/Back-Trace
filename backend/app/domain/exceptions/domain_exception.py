class DomainException(Exception):
    """Base exception for Domain Driven Design rule violations."""

    def __init__(self, message: str, code: str = "DOMAIN_ERROR"):
        self.message = message
        self.code = code
        super().__init__(self.message)
