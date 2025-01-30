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

    # hospital
    df = pd.read_csv(f"{inputpath}/hospital.csv")
    cols = df.columns
    mapper = {
        '<100' : [0, 99],
        '100 - 249': [100, 249],
        '>= 500': [500, 1000],
        '250 - 499': [250, 499],
    }
    for _, row in df.iterrows():
        uid = ex[f"Hospital{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.Hospital))
        if pd.notnull(row[cols[1]]):
            g.add((uid, eicu["hasMinNumBedCategory"], mapper[row[cols[1]]][0]))
            g.add((uid, eicu["hasMaxNumBedCategory"], mapper[row[cols[1]]][1]))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasTeachingStatus"], row[cols[2]]))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasRegion"], row[cols[3]]))

    g.serialize("result/hospital.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])