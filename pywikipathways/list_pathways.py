from .utilities import *

def list_pathways(organism=""):
    """List Pathways
    
    Retrieve list of pathways per species, including WPID, name,
    species, URL and latest revision number.
    
    Args:
        organism (str): A particular species.
    
    Returns:
        pandas.DataFrame: A dataframe of pathway information.
        
    Examples:
        >>> list_pathways('Mus musculus')
                id                                           url                                               name       species    revision
        0    WP3673  https://www.wikipathways.org/instance/WP3673                  Hfe effect on hepcidin production  Mus musculus  2016-12-13
        1    WP4627  https://www.wikipathways.org/instance/WP4627   Lipids measured in liver metastasis from brea...  Mus musculus  2024-03-27
        2     WP396   https://www.wikipathways.org/instance/WP396                              ACE inhibitor pathway  Mus musculus  2021-05-14
        3     WP175   https://www.wikipathways.org/instance/WP175                            Acetylcholine synthesis  Mus musculus  2021-05-14
        4     WP447   https://www.wikipathways.org/instance/WP447                                 Adipogenesis genes  Mus musculus  2023-04-21
        . .      ...                                           ...                                                ...           ...         ...
        200  WP2904  https://www.wikipathways.org/instance/WP2904   miR302-367 promoting cardiomyocyte proliferation  Mus musculus  2021-05-23
        201  WP2375  https://www.wikipathways.org/instance/WP2375              miRNAs and TFs in iPS Cell Generation  Mus musculus  2019-06-27
        202  WP3979  https://www.wikipathways.org/instance/WP3979        mir-193a and MVP in colon cancer metastasis  Mus musculus  2019-11-29
        203   WP350   https://www.wikipathways.org/instance/WP350                         p38 Mapk signaling pathway  Mus musculus  2021-05-11
        204  WP2902  https://www.wikipathways.org/instance/WP2902                                      p53 signaling  Mus musculus  2016-08-01

        [205 rows x 5 columns]
    """

    # Fetch JSON data from the URL
    url = "https://www.wikipathways.org/json/listPathways.json"
    response = requests.get(url)
    data = response.json()
    
    # Extract pathways from each organism
    # This flattens the list of pathways from each organism into one list
    pathways = [pathway for org in data['organisms'] for pathway in org.get('pathways', [])]
    
    # Create a DataFrame from the list
    df = pandas.DataFrame(pathways)
    
    # If an organism is specified, filter the DataFrame
    if organism:
        df = df[df['species'] == organism]
    
    # Print a message if no results are found
    if df.empty:
        print("No results")
    
    df.reset_index(drop=True, inplace=True)
    return df


def list_pathway_ids(organism=""):
    """List Pathway WPIDs
    
    Retrieve list of pathway WPIDs per species.
    Basically returns a subset of list_pathways result.
    
    Args:
        organism (str): A particular species.
    
    Returns:
        pandas.Series: A series of WPIDs.
        
    Examples:
        >>> list_pathway_ids('Mus musculus')
        0        WP1
        1       WP10
        2      WP103
        3      WP108
        4      WP113
               ...  
        230     WP79
        231     WP85
        232     WP87
        233     WP88
        234     WP93
        Name: id, Length: 235, dtype: object
    """
    res = list_pathways(organism)
    return res['id']

def list_pathway_names(organism=""):
    """List Pathway Names
    
    Retrieve list of pathway names per species.
    Basically returns a subset of list_pathways result.
    
    Args:
        organism (str): A particular species.
    
    Returns:
        pandas.Series: A series of names.
        
    Examples:
        >>> list_pathway_ids('Mus musculus')
        0      WP3673
        1      WP4627
        2       WP396
        3       WP175
        4       WP447
                ...
        200    WP2904
        201    WP2375
        202    WP3979
        203     WP350
        204    WP2902
        Name: id, Length: 205, dtype: object
    """
    res = list_pathways(organism)
    return res['name']

def list_pathway_urls(organism=""):
    """List Pathway URLs
    
    Retrieve list of pathway URLs per species.
    Basically returns a subset of list_pathways result.
    
    Args:
        organism (str): A particular species.
    
    Returns:
        pandas.Series: A series of URLs.
        
    Examples:
        >>> list_pathway_urls('Mus musculus')
        0      https://www.wikipathways.org/instance/WP3673
        1      https://www.wikipathways.org/instance/WP4627
        2       https://www.wikipathways.org/instance/WP396
        3       https://www.wikipathways.org/instance/WP175
        4       https://www.wikipathways.org/instance/WP447
                                ...
        200    https://www.wikipathways.org/instance/WP2904
        201    https://www.wikipathways.org/instance/WP2375
        202    https://www.wikipathways.org/instance/WP3979
        203     https://www.wikipathways.org/instance/WP350
        204    https://www.wikipathways.org/instance/WP2902
        Name: url, Length: 205, dtype: object
    """
    res = list_pathways(organism)
    return res['url']
