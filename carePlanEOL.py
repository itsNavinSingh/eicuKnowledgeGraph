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

    # carePlanEOL

    df = pd.read_csv(f"{inputpath}/carePlanEOL.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"CarePlanEol{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.CarePlanEol))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasCarePlanEol, uid))
        g.add((uid, eicu["hasCarePlanEolSaveOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        g.add((uid, eicu["hasCarePlanEolDiscussionOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        g.add((uid, eicu["hasActiveUponDischarge"], Literal(row[cols[4]], datatype=XSD.boolean)))
        
    g.serialize("result/carePlanEOL.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])