"""
Email work formats
-----------------------------
[TODO PLACEHOLDER]
"""
WORK_FORMATS = set(
    [
        "{FirstNameCapital}{LastName}@{domain}",
        "{FirstName}{LastName}@{domain}",
        "{FirstName}.{LastName}@{domain}",
        "{FirstName}_{LastName}@{domain}",
        "{LastName}@{domain}",
        "{FirstNameCapital}_{LastName}@{domain}",
        "{LastName}{FirstNameCapital}@{domain}",
        "{FirstName}@{domain}",
    ]
)
