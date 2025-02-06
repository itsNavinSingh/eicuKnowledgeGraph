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

    # customLab

    df = pd.read_csv(f"{inputpath}/customLab.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"CustomLab{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.CustomLab))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasCustomLab, uid))
        g.add((uid, eicu["hasCustomLabOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        g.add((uid, eicu["hasCustomLabTypeId"], Literal(row[cols[3]], datatype=XSD.integer)))
        g.add((uid, eicu["hasCustomLabName"], Literal(row[cols[4]])))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasCustomLabResult"], Literal(row[cols[5]], datatype=XSD.float)))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasCustomLabValueText"], Literal(row[cols[6]])))
        
    g.serialize("result/customLab.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])