import iedb, math
import pandas as pd

def NetMHCIIPan4(peptides, threshold = 0.5, allele = ["HLA-DRB1*03:01","HLA-DRB1*07:01","HLA-DRB1*15:01","HLA-DRB3*01:01","HLA-DRB3*02:02","HLA-DRB4*01:01","HLA-DRB5*01:01"]):

    '''
    Query IC50 values for MHC class II peptide binding of set of peptides to an MHC class II molecule. Sends POST
    request to IEDB API.

    Parameters:
        peptides ([str]): list of peptides
        threshold (float): threshold for good or poor binder
        allele ([str]): list of alleles covered in NetMHCIIPan4.0

    Returns:
            dataframe (pandas.DataFrame): Tabular results formatted as pandas.DataFrame
    '''
    lengthList = [len(p) for p in peptides]
    sequence = ""
    for p in peptides:
        sequence += '\n'+ p
    sequence = [sequence[1:]]
    print("Querying IDEB for ",len(peptides)," peptides and ",len(allele)," alleles.....")
    mhcii_res = iedb.query_mhcii_binding(method="netmhciipan-4.0", sequence=sequence, allele=allele, length=lengthList)
    mhcii_res = mhcii_res[['allele','peptide','ic50']]
    df = pd.DataFrame(columns=allele,index=peptides)

    for a in allele:
        for p in peptides:
            idx = (mhcii_res[(mhcii_res['allele']  == a) & (mhcii_res['peptide'] == p)].index.to_list())
            if round(1-math.log(float(mhcii_res.loc[idx[0],'ic50']))/math.log(50000), 4) >= threshold:
                df.loc[p,a] = 1
            else:
                df.loc[p,a] = 0
    return df
