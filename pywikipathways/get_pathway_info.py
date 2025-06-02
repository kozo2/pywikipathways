from .utilities import wikipathways_get

def get_pathway_info(pathway):
    res = wikipathways_get('getPathwayInfo', {'pwId': pathway, 'format': 'json'})
    if res['pathwayInfo']['name'] == "":
        print("No results")
    else:
        return res['pathwayInfo']
