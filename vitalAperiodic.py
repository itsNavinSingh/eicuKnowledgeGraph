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

    # vitalAperiodic

    df = pd.read_csv(f"{inputpath}/vitalAperiodic.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"VitalAperiodic{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.VitalAperiodic))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasVitalAperiodic, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasObservationOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasNonInvasiveSystolic"], Literal(row[cols[3]], datatype=XSD.float)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasNonInvasiveDiastolic"], Literal(row[cols[4]], datatype=XSD.float)))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasNonInvasiveMean"], Literal(row[cols[5]], datatype=XSD.float)))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasPaop"], Literal(row[cols[6]], datatype=XSD.float)))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasCardiacOutput"], Literal(row[cols[7]], datatype=XSD.float)))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasCardiacInput"], Literal(row[cols[8]], datatype=XSD.float)))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasSvr"], Literal(row[cols[9]], datatype=XSD.float)))
        if pd.notnull(row[cols[10]]):
            g.add((uid, eicu["hasSvri"], Literal(row[cols[10]], datatype=XSD.float)))
        if pd.notnull(row[cols[11]]):
            g.add((uid, eicu["hasPvr"], Literal(row[cols[11]], datatype=XSD.float)))
        if pd.notnull(row[cols[12]]):
            g.add((uid, eicu["hasPvri"], Literal(row[cols[12]], datatype=XSD.float)))

    g.serialize("result/vitalAperiodic.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])