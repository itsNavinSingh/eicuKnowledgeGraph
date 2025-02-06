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

    df = pd.read_csv(f"{inputpath}/nurseCharting.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"NursingChart{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.NursingChart))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasNursingChart, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasNursingChartOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasNursingChartEntryOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasNursingChartCellTypeCat"], Literal(row[cols[4]])))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasNursingChartCellTypeValLabel"], Literal(row[cols[5]])))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasNursingChartCellTypeValName"], Literal(row[cols[6]])))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasNursingChartValue"], Literal(row[cols[7]])))

    g.serialize("result/nurseCharting.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])