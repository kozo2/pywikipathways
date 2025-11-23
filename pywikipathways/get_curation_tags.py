from .utilities import *

def get_curation_status(pathway):
    """Get Curation Status

    Retrieve curation status information for a pathway.

    Args:
        pathway (str): The pathway identifier, e.g., 'WP554'

    Returns:
        pandas.DataFrame: A dataframe of curation status information

    Examples:
        >>> get_curation_status('WP554')
    """
    if pathway is None:
        raise ValueError("Must provide a pathway identifier, e.g., WP554")

    url = f"https://www.wikipathways.org/wikipathways-collection/reports/{pathway}.json"
    res = requests.get(url)
    res.raise_for_status()
    data = res.json()
    return pandas.DataFrame([data])

def get_curation_tags(pathway):
    res = wikipathways_get('getCurationTags', {'pwId': pathway, 'format': 'json'})
    return pandas.DataFrame(res['tags'])

def get_curation_tag_names(pathway):
    res = get_curation_tags(pathway)
    return res['name']

def get_every_curation_tag(tag):
    res = wikipathways_get('getCurationTagsByName', {'tagName': tag, 'format': 'json'})
    return pandas.DataFrame(res['tags'])

def get_pathways_by_curation_tag(tag):
    res = wikipathways_get('getCurationTagsByName', {'tagName': tag, 'format': 'json'})
    return pandas.DataFrame([i['pathway'] for i in res['tags']])

def get_pathway_ids_by_curation_tag(tag):
    res = get_pathways_by_curation_tag(tag)
    return res['id']
