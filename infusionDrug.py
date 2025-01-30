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

    # infusionDrug

    df = pd.read_csv(f"{inputpath}/infusionDrug.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"InfusionDrug{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.InfusionDrug))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasInfusionDrug, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasInfusionOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasDrugName"], row[cols[3]]))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasDrugRate"], row[cols[4]]))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasInfusionRate"], Literal(row[cols[5]], datatype=XSD.float)))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasDrugAmount"], Literal(row[cols[6]], datatype=XSD.float)))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasVolumeOfFluid"], Literal(row[cols[7]], datatype=XSD.float)))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasPatientWeight"], Literal(row[cols[8]], datatype=XSD.float)))

    g.serialize("result/infusionDrug.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])