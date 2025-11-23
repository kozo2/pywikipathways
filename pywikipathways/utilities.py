import requests
import pandas
import urllib.parse

DEFAULT_BASE_URL = 'https://webservice.wikipathways.org'

def wikipathways_get(operation, parameters=None, base_url=DEFAULT_BASE_URL):
    """WikiPathways GET.
    
    FILLME
    FILLME
    
    Args:
        operation (str): operation
        base_url (str): Ignore unless you need to specify a custom domain
    
    Returns:
        str: query result content
    
    Examples:
        >>> wikipathways_get('listOrganisms')
        >>> wikipathways_get('listOrganisms', parameters={'format': 'json'})
    """
    try:
        url = build_url(base_url, operation)
        r = requests.request('GET', url, params=parameters)
        r.raise_for_status()
        try:
            return r.json()
        except ValueError as e:
            return r.text
    except requests.exceptions.RequestException as e:
        print("Error: ", e)

def build_url(base_url=DEFAULT_BASE_URL, operation=None):
    if operation is not None:
        return base_url + "/" + urllib.parse.quote(operation)
    else:
        return base_url

def wikipathways_api():
    """WikiPathways API

    Opens the WikiPathways Swagger API documentation in a web browser.

    Note:
        This function is provided for compatibility with older web services
        and may be deprecated in future releases.

    Examples:
        >>> wikipathways_api()
    """
    import webbrowser
    url = "https://webservice.wikipathways.org/ui"
    webbrowser.open(url)
