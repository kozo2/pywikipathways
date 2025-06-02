import pytest
from pywikipathways.list_pathways import *

def test_list_pathways():
    """Test that pathways are found when calling list_pathways()"""
    pathways = list_pathways()
    assert len(pathways) > 0

def test_list_pathways_anopheles_gambiae():
    """Test that Anopheles gambiae pathways are found"""
    pathways = list_pathways(organism="Anopheles gambiae")
    assert len(pathways) > 0

def test_list_pathway_ids():
    """Test that pathway IDs are returned"""
    pathway_ids = list_pathway_ids()
    assert len(pathway_ids) > 0

def test_list_pathway_ids_with_organism():
    """Test that pathway IDs are returned for specific organism"""
    pathway_ids = list_pathway_ids(organism="Anopheles gambiae")
    assert len(pathway_ids) > 0

def test_list_pathway_names():
    """Test that pathway names are returned"""
    pathway_names = list_pathway_names()
    assert len(pathway_names) > 0

def test_list_pathway_names_with_organism():
    """Test that pathway names are returned for specific organism"""
    pathway_names = list_pathway_names(organism="Anopheles gambiae")
    assert len(pathway_names) > 0

def test_list_pathway_urls():
    """Test that pathway URLs are returned"""
    pathway_urls = list_pathway_urls()
    assert len(pathway_urls) > 0

def test_list_pathway_urls_with_organism():
    """Test that pathway URLs are returned for specific organism"""
    pathway_urls = list_pathway_urls(organism="Anopheles gambiae")
    assert len(pathway_urls) > 0