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

    # microLab

    df = pd.read_csv(f"{inputpath}/microLab.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"MicroLab{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.MicroLab))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasMicroLab, uid))
        g.add((uid, eicu["hasCultureTakenOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasCultureSite"], row[cols[3]]))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasOrganism"], row[cols[4]]))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasAntibiotic"], row[cols[5]]))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasSensitivityLevel"], row[cols[6]]))

    g.serialize("result/microLab.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])