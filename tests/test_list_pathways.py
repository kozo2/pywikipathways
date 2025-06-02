from pywikipathways.list_pathways import list_pathways

def test_pathways_are_found():
    pathways = list_pathways()
    assert len(pathways) > 0

def test_anopheles_gambiae_pathways_are_found():
    pathways = list_pathways(organism="Anopheles gambiae")
    assert len(pathways) > 0