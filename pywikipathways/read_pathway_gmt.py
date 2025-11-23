"""Function for reading WikiPathways GMT files."""

import pandas


def read_pathway_gmt(file):
    """Read Pathway GMT File

    Reads a WikiPathways GMT file and returns a data frame of pathway-gene
    associations for use in enrichment analyses.

    Args:
        file (str): Path to a GMT format file

    Returns:
        pandas.DataFrame: A dataframe with columns 'name', 'version', 'wpid',
            'org', and 'gene' (NCBI Entrez Gene identifiers)

    Details:
        WikiPathways GMT files have pathway identifiers in the first column
        formatted as 'name%version%wpid%org' where:
        - name: pathway name
        - version: pathway version
        - wpid: WikiPathways identifier (e.g., WP554)
        - org: organism name

        The second column is a description (ignored), and remaining columns
        contain NCBI Entrez Gene IDs.

        Use downloadPathwayArchive to obtain GMT files.

    Examples:
        >>> read_pathway_gmt('wikipathways-20231210-gmt-Homo_sapiens.gmt')
    """
    with open(file, 'r') as f:
        lines = f.readlines()

    pathway_gene_list = []
    for line in lines:
        parts = line.strip().split('\t')
        if len(parts) < 3:
            continue

        pathway_id = parts[0]
        # Skip the description (parts[1])
        genes = parts[2:]  # All remaining columns are genes

        # Parse the pathway identifier: name%version%wpid%org
        pathway_parts = pathway_id.split('%')
        if len(pathway_parts) >= 4:
            name = pathway_parts[0]
            version = pathway_parts[1]
            wpid = pathway_parts[2]
            org = pathway_parts[3]
        else:
            # Handle cases where the format might be different
            name = pathway_id
            version = ''
            wpid = ''
            org = ''

        for gene in genes:
            if gene:  # Skip empty strings
                pathway_gene_list.append({
                    'name': name,
                    'version': version,
                    'wpid': wpid,
                    'org': org,
                    'gene': gene
                })

    return pandas.DataFrame(pathway_gene_list)
