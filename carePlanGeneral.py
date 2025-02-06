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

    # carePlanGeneral

    df = pd.read_csv(f"{inputpath}/carePlanGeneral.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"CarePlanGeneral{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.CarePlanGeneral))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hascarePlanGeneral, uid))
        g.add((uid, eicu["hasActiveUponDischarge"], Literal(row[cols[2]], datatype=XSD.boolean)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasCarePlanGeneralItemOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasCarePlanGeneralGroup"], Literal(row[cols[4]])))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasCarePlanGeneralItemValue"], Literal(row[cols[5]])))
        
    g.serialize("result/carePlanGeneral.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])