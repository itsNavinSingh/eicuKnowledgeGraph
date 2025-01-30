import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD
import sys
def main(inputpath):
    g = Graph()
    ex = Namespace("http://schema.org/eicu")
    eicu = Namespace("http://www.eicu.org/ontologies#")
    g.bind("ex", ex)
    g.bind("eicu", eicu)

    # diagnosis
    df = pd.read_csv(f"{inputpath}/diagnosis.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"Diagnosis{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.Diagnosis))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasDiagnosis, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasActiveUponDischarge"], Literal(row[cols[2]], datatype=XSD.boolean)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasDiagnosisOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasDiagnosisString"], row[cols[4]]))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasIcd9Code"], row[cols[5]]))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasDiagnosisPriority"], row[cols[6]]))
        
    g.serialize("result/diagnosis.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])