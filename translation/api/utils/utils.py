from string import printable


def company_name_is_correct(text):
    entity_forms = ['LLC', 'SPA', 'GMBH']
    for entity_form in entity_forms:
        if entity_form not in text:
            return (text.isupper()
                    and not bool(set(text) - set(printable)))
    return False
