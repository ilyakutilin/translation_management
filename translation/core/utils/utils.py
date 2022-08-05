from string import printable


def company_name_is_correct(text):
    """Checks that the company name is in line with cpy naming rules.

    The rules are:
    - No legal entity forms (LLC etc.)
    - Only Latin alphabet
    - Uppercase.

    To be used together with the appropriate validator.
    """
    entity_forms = ['LLC', 'SPA', 'GMBH']
    for entity_form in entity_forms:
        if entity_form not in text:
            return (text.isupper()
                    and not bool(set(text) - set(printable)))
    return False
