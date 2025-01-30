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

    # physicalExam
    df = pd.read_csv(f"{inputpath}/physicalExam.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"PhysicalExam{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.PhysicalExam))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasPhysicalExam, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasPhysicalExamOffset"], row[cols[2]]))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasPhysicalExamPath"], row[cols[3]]))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasPhysicalExamValue"], row[cols[4]]))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasPhysicalExamText"], row[cols[5]]))

    g.serialize("result/physicalExam.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])