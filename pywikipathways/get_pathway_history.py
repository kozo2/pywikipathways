import pandas
from .utilities import wikipathways_get

def get_pathway_history(pathway, timestamp):
    res = wikipathways_get('getPathwayHistory', {'pwId': pathway, 'timestamp': timestamp, 'format': 'json'})
    return pandas.DataFrame(res['history']['history'])
