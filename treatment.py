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

    # treatment

    df = pd.read_csv(f"{inputpath}/treatment.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"Treatment{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.Treatment))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasTreatment, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasTreatmentOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasTreatmentString"], Literal(row[cols[3]])))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasActiveUponDischarge"], Literal(row[cols[4]], datatype=XSD.boolean)))

    g.serialize("result/treatment.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])