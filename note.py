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

    # note

    df = pd.read_csv(f"{inputpath}/note.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"Note{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.Note))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasNote, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasNoteOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasNoteEnteredOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasNoteType"], Literal(row[cols[4]])))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasNotePath"], Literal(row[cols[5]])))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasNoteValue"], Literal(row[cols[6]])))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasNoteText"], Literal(row[cols[7]])))
    g.serialize("result/note.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])