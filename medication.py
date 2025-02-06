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

    # medication

    df = pd.read_csv(f"{inputpath}/medication.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"Medication{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.Medication))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasMedication, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasDrugOrderOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasDrugStartOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasDrugIVAdmixture"], Literal(row[cols[4]].lower()=="yes", datatype=XSD.boolean)))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasDrugOrderCancelled"], Literal(row[cols[5]].lower()=="yes", datatype=XSD.boolean)))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasDrugName"], Literal(row[cols[6]])))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasDrugHiclSeqno"], Literal(row[cols[7]], datatype=XSD.float)))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasDosage"], Literal(row[cols[8]])))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasRouteAdmin"], Literal(row[cols[9]])))
        if pd.notnull(row[cols[10]]):
            g.add((uid, eicu["hasFrequency"], Literal(row[cols[10]])))
        if pd.notnull(row[cols[11]]):
            g.add((uid, eicu["hasLoadingDose"], Literal(row[cols[11]])))
        if pd.notnull(row[cols[12]]):
            g.add((uid, eicu["hasPnr"], Literal(row[cols[12]].lower()=='yes', datatype=XSD.boolean)))
        if pd.notnull(row[cols[13]]):
            g.add((uid, eicu["hasDrugStopOffset"], Literal(row[cols[13]], datatype=XSD.integer)))
        if pd.notnull(row[cols[14]]):
            g.add((uid, eicu["hasGtc"], Literal(row[cols[14]], datatype=XSD.integer)))

    g.serialize("result/medication.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])