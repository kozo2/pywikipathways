"""Function for writing GMT (Gene Matrix Transposed) files."""

import pandas


def write_gmt(df, outfile):
    """Write GMT File

    Writes a data frame to a GMT file.

    Args:
        df (pandas.DataFrame): A dataframe with at least two columns.
            The first column(s) will be used as identifiers, and the last
            column should contain genes or gene products.
        outfile (str): The file path where the GMT output will be saved.

    Details:
        The function handles dataframes with different numbers of columns:

        - 2 columns: The first column is used as both identifier and description,
          the second column contains genes.
        - 3 columns: The first column is the identifier, second is description,
          third contains genes.
        - More than 3 columns: The first n columns (where n = total columns - 2)
          are concatenated with '%' separators to form the identifier. The
          second-to-last column is used as description, and the last column
          contains genes.

    Examples:
        >>> # Two column dataframe
        >>> df = pandas.DataFrame({'pathway': ['WP554', 'WP554', 'WP619'],
        ...                        'gene': ['Gene1', 'Gene2', 'Gene3']})
        >>> write_gmt(df, 'output.gmt')
        >>>
        >>> # Three column dataframe
        >>> df = pandas.DataFrame({'pathway': ['WP554', 'WP554'],
        ...                        'description': ['ACE2 pathway', 'ACE2 pathway'],
        ...                        'gene': ['Gene1', 'Gene2']})
        >>> write_gmt(df, 'output.gmt')
    """
    df = df.copy()  # Avoid modifying the original dataframe
    df_len = len(df.columns)

    if df_len < 2:
        raise ValueError("The input data frame must include at least two columns.")
    elif df_len == 2:
        # Duplicate first column as description
        col_names = list(df.columns)
        df['desc'] = df.iloc[:, 0]
        df = df[[col_names[0], 'desc', col_names[1]]]
    elif df_len > 3:
        # Concatenate first n-2 columns with % separator
        id_cols = list(df.columns[0:df_len-2])
        print(f"Concatenating the following columns to use as Identifiers: {', '.join(id_cols)}")

        # Create concatenated identifier
        df['concat_id'] = df[id_cols].apply(lambda row: '%'.join(row.astype(str)), axis=1)

        # Get the last two columns (description and genes)
        desc_col = df.columns[df_len-2]
        gene_col = df.columns[df_len-1]

        # Reorder: concat_id, description, genes
        df = df[['concat_id', desc_col, gene_col]]

    # At this point, df should have exactly 3 columns: ID, description, genes
    col_names = list(df.columns)
    id_col = col_names[0]
    desc_col = col_names[1]
    gene_col = col_names[2]

    # Group genes by identifier
    grouped = df.groupby([id_col, desc_col], sort=False)[gene_col].apply(lambda x: '\t'.join(x.astype(str))).reset_index()

    # Write to file
    with open(outfile, 'w') as f:
        for _, row in grouped.iterrows():
            line = f"{row[id_col]}\t{row[desc_col]}\t{row[gene_col]}\n"
            f.write(line)
