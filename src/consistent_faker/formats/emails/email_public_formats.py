"""
Email Public formats
-----------------------------
[TODO PLACEHOLDER]
"""
from consistent_faker.formats.emails.email_work_formats import WORK_FORMATS

PUBLIC_FORMATS = set(
    [x for x in WORK_FORMATS]
    + ([x.replace("@{domain}", "{randomint}@{domain}") for x in WORK_FORMATS])
    + ["{pseudonym}@{domain}"]
)
