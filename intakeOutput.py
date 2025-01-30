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

    # intakeOutput

    df = pd.read_csv(f"{inputpath}/intakeOutput.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"IntakeOutput{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.IntakeOutput))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasIntakeOutput, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasIntakeOutputOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasIntakeTotal"], Literal(row[cols[3]], datatype=XSD.float)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasOutputTotal"], Literal(row[cols[4]], datatype=XSD.float)))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasDialysisTotal"], Literal(row[cols[5]], datatype=XSD.float)))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasNetTotal"], Literal(row[cols[6]], datatype=XSD.float)))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasIntakeOutputEntryOffset"], Literal(row[cols[7]], datatype=XSD.integer)))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasCellPath"], row[cols[8]]))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasCellLabel"], row[cols[9]]))
        if pd.notnull(row[cols[10]]):
            g.add((uid, eicu["hasCellValue"], Literal(row[cols[10]], datatype=XSD.float)))

    g.serialize("result/intakeOutput.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])