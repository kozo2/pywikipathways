"""Functions for reading GMT (Gene Matrix Transposed) files."""

import pandas


def read_gmt(file):
    """Read GMT File

    Reads any generic GMT file to produce a data frame of term-gene associations
    useful in enrichment analyses.

    Args:
        file (str): Path to the GMT file

    Returns:
        pandas.DataFrame: A dataframe with columns 'term' and 'gene'

    Details:
        GMT files are tab-delimited text files where each line represents a gene set.
        The first column is the term/gene set name, the second is a description,
        and remaining columns are the genes in the set.

    Examples:
        >>> read_gmt('pathways.gmt')
    """
    with open(file, 'r') as f:
        lines = f.readlines()

    term_gene_list = []
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) < 3:
            continue
        term = parts[0]
        # Skip the description (parts[1])
        genes = parts[2:]  # All remaining columns are genes
        for gene in genes:
            if gene:  # Skip empty strings
                term_gene_list.append({'term': term, 'gene': gene})

    return pandas.DataFrame(term_gene_list)


def read_gmt_names(file):
    """Read GMT File Names

    Reads any generic GMT file to produce a data frame of term-name associations.

    Args:
        file (str): Path to the GMT file

    Returns:
        pandas.DataFrame: A dataframe with columns 'term' and 'name'

    Details:
        This function extracts the term identifiers and their descriptive names
        from a GMT file. The first column becomes 'term' and the second column
        becomes 'name'.

    Examples:
        >>> read_gmt_names('pathways.gmt')
    """
    with open(file, 'r') as f:
        lines = f.readlines()

    term_name_list = []
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) < 2:
            continue
        term = parts[0]
        name = parts[1]
        term_name_list.append({'term': term, 'name': name})

    return pandas.DataFrame(term_name_list)
