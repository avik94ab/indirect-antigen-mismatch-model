import iedb, math
from mhctools import NetMHCIIpan4_BA
import pandas as pd
from bioservices import UniProt

def bindingScore(peptides, alleles = ["HLA-DRA1*01:01-DRB1*03:01", "HLA-DRA1*01:01-DRB1*07:01"]):
    protein_sequences = {}
    i = 0
    for p in peptides:
        protein_sequences[i] = p
        i += 1
    predictor = NetMHCIIpan4_BA(alleles = alleles)
    mhcii_res = predictor.predict_subsequences(protein_sequences, peptide_lengths = [15]).to_dataframe()

    df = pd.DataFrame(columns = alleles, index = peptides)
    for a in alleles:
        for p in peptides:
            idx = (mhcii_res[(mhcii_res['allele']  == a) & (mhcii_res['peptide'] == p)].index.to_list())
            df.loc[p,a] = mhcii_res.loc[idx[0],'score']
    return df


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


def fetchSequence(query):

    '''
    Paramters:
        query (str): a valid UniProt identifier
    Returns:
        seq (str): protein-sequence corresponding to UniProt identifier
    '''
    # Make a link to the UniProt webservice (UniProt())
    service = UniProt()

    # Send the query to UniProt, and catch the search result in a variable (service.search())
    fileContent = service.search(query, frmt="fasta")
    seq = "".join(fileContent.splitlines()[1:])

    # Inspect the result
    return seq


def generatePeptides(seq, size = 15, shift = 5):

    '''
    Paramters:
        seq (str): protein-sequence
        size (int): size of each peptide
        shift (int): shifting window
    Returns:
        peptides ([str]): list of peptides
    '''
    peptides = []
    k = 0
    i = 0
    while(k<len(seq)-(size-shift)):
        if len(seq[i:(k+size)]) == size:
            peptides.append(seq[i:(k+size)])
        i += shift
        k += shift
    return peptides
