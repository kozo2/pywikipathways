from pywikipathways.get_pathway import get_pathway

def test_get_pathway():
    res = get_pathway("WP4")
    assert len(res) > 0
