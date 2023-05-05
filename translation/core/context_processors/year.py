from datetime import date


def year(request):
    """Adds a variable with the current year."""
    return {"year": date.today().year}
