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

    # nurseAssessment

    df = pd.read_csv(f"{inputpath}/nurseAssessment.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"NurseAssessment{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.NurseAssessment))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasNurseAssessment, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasNurseAssessOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasNurseAssessEntryOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasCellAttributePath"], row[cols[4]]))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasCellLabel"], row[cols[5]]))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasCellAttribute"], row[cols[6]]))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasCellAttributeValue"], row[cols[7]]))
    g.serialize("result/nurseAssessment.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])