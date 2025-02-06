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

    # lab
    df = pd.read_csv(f"{inputpath}/lab.csv")
    cols = df.columns
    i=0
    for _, row in df.iterrows():
        uid = ex[f"Lab{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.Lab))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasLab, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasLabResultOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasLabTypeId"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasLabName"], Literal(row[cols[4]])))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasLabResult"], Literal(row[cols[5]], datatype=XSD.float)))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasLabMeasureNameSystem"], Literal(row[cols[7]])))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasLabMeasureNameInterface"], Literal(row[cols[8]])))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasLabResultRevisedOffset"], Literal(row[cols[9]], datatype=XSD.integer)))
        if(i==100):
            print("Done")
            return
        i += 1

    g.serialize("result/lab.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])