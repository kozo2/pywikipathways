import requests

def list_organisms():
    """List Organisms.

    Retrieve the list of organisms supported by WikiPathways

    Returns:
        list: A list of organisms

    Example:
        >>> list_organisms()
        ['Arabidopsis thaliana', 'Hordeum vulgare', 'Bacillus subtilis', ...]
    """
    # Fetch data from JSON API endpoint
    url = "https://www.wikipathways.org/json/listOrganisms.json"
    response = requests.get(url)
    response.raise_for_status()
    
    # Extract and return the list of organisms
    data = response.json()
    return data['organisms']
