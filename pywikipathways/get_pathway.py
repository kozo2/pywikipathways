from .utilities import wikipathways_get

def get_pathway(pathway, revision=0):
    res = wikipathways_get('getPathway', {'pwId': pathway, 'revision': revision, 'format': 'json'})
    return res['pathway']['gpml']
