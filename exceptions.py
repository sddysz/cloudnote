"""
    DyszCloud.exceptions
    ~~~~~~~~~~~~~~~~~~

    Exceptions implemented by cloudnote.
"""
from werkzeug.exceptions import HTTPException, Forbidden


class CloudNoteError(HTTPException):
    "Root exception for CloudNote"
    description = "An internal error has occured"


class AuthorizationRequired(CloudNoteError, Forbidden):
    description = "Authorization is required to access this area."


class AuthenticationError(CloudNoteError):
    description = "Invalid username and password combination."
