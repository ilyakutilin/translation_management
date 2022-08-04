ACTIVITY_CHOICES = [
    ('PRP', 'Preparation'),
    ('TRN', 'Translation'),
    ('PRF', 'Proofreading'),
    ('VRF', 'Verification'),
    ('FNL', 'Finalization'),
]

STATUS_CHOICES = [
    ('NRQ', 'Not Required'),
    ('PND', 'Pending'),
    ('ONT', 'On Time'),
    ('ERL', 'Early'),
    ('LTE', 'Late'),
]

LANGUAGES = [
    ('EN', 'English'),
    ('RU', 'Russian'),
    ('TR', 'Turkish'),
    ('IT', 'Italian'),
    ('FR', 'French'),
    ('LT', 'Lithuanian'),
    ('UZ', 'Uzbek'),
]

FILE_TYPES = [
    ('DOC', 'MS Word Document'),
    ('XLS', 'MS Excel Spreadsheet'),
    ('PDF', 'PDF'),
    ('DWG', 'AutoCAD Drawing'),
    ('PPT', 'MS PowerPoint Presentation'),
    ('MSG', 'Outlook Email message'),
    ('PIC', 'Picture'),
]

AGENCY_CHOICES = [
    ('MTA', 'MTA'),
]

AGENCY_STATUS_CHOICES = [
    ('REQ', 'Required'),
    ('ONG', 'Ongoing'),
    ('DNE', 'Done'),
]
