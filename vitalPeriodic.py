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

    # vitalPeriodic

    df = pd.read_csv(f"{inputpath}/vitalPeriodic.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"VitalPeriodic{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.VitalPeriodic))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasVitalPeriodic, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasObservationOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasTemprature"], Literal(row[cols[3]], datatype=XSD.float)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasSao2"], Literal(row[cols[4]], datatype=XSD.integer)))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasHeartRate"], Literal(row[cols[5]], datatype=XSD.integer)))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasRespiration"], Literal(row[cols[6]], datatype=XSD.integer)))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasCvp"], Literal(row[cols[7]], datatype=XSD.integer)))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasEtCo2"], Literal(row[cols[8]], datatype=XSD.integer)))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasSystemicSystolic"], Literal(row[cols[9]], datatype=XSD.integer)))
        if pd.notnull(row[cols[10]]):
            g.add((uid, eicu["hasSystemicDiastolic"], Literal(row[cols[10]], datatype=XSD.integer)))
        if pd.notnull(row[cols[11]]):
            g.add((uid, eicu["hasSystemicMean"], Literal(row[cols[11]], datatype=XSD.integer)))
        if pd.notnull(row[cols[12]]):
            g.add((uid, eicu["hasPaSystolic"], Literal(row[cols[12]], datatype=XSD.integer)))
        if pd.notnull(row[cols[13]]):
            g.add((uid, eicu["hasPaDiastolic"], Literal(row[cols[13]], datatype=XSD.integer)))
        if pd.notnull(row[cols[14]]):
            g.add((uid, eicu["hasPaMean"], Literal(row[cols[14]], datatype=XSD.integer)))
        if pd.notnull(row[cols[15]]):
            g.add((uid, eicu["hasSt1"], Literal(row[cols[15]], datatype=XSD.float)))
        if pd.notnull(row[cols[16]]):
            g.add((uid, eicu["hasSt2"], Literal(row[cols[16]], datatype=XSD.float)))
        if pd.notnull(row[cols[17]]):
            g.add((uid, eicu["hasSt3"], Literal(row[cols[17]], datatype=XSD.float)))
        if pd.notnull(row[cols[18]]):
            g.add((uid, eicu["hasIcp"], Literal(row[cols[18]], datatype=XSD.integer)))

    g.serialize("result/vitalPeriodic.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])