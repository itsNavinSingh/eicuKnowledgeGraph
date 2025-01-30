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

    # pastHistory

    df = pd.read_csv(f"{inputpath}/pastHistory.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"PastHistory{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.PastHistory))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasPastHistory, uid))
        g.add((uid, eicu["hasPastHistoryOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        g.add((uid, eicu["hasPastHistoryEnteredOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        g.add((uid, eicu["hasPastHistoryNoteType"], row[cols[4]]))
        g.add((uid, eicu["hasPastHistoryPath"], row[cols[5]]))
        g.add((uid, eicu["hasPastHistoryValue"], row[cols[6]]))
        g.add((uid, eicu["hasPastHistoryValueText"], row[cols[7]]))

    g.serialize("result/pastHistory.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])