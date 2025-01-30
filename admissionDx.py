import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD
import sys

# admissionDx
def main(inputpath):
    g = Graph()
    ex = Namespace("http://schema.org/eicu")
    eicu = Namespace("http://www.eicu.org/ontologies#")
    g.bind("ex", ex)
    g.bind("eicu", eicu)
    df = pd.read_csv(f'{inputpath}/admissiondx.csv')
    for _, row in df.iterrows():
        dx_uri = ex[f"AdmissionDx{row['admissiondxid']}"]
        
        g.add((dx_uri, RDF.type, eicu.AdmissionDx))
        g.add((ex[f"PatientUnitStay{row['patientunitstayid']}"], eicu.hasAdmitDx, dx_uri))
        g.add((dx_uri, eicu.hasAdmitDxEnteredOffset, Literal(row['admitdxenteredoffset'], datatype=XSD.integer)))
        g.add((dx_uri, eicu.hasAdmitDxPath, Literal(row['admitdxpath'], datatype=XSD.string)))
        if pd.notnull(row['admitdxname']):
            g.add((dx_uri, eicu.hasAdmitDxName, Literal(row['admitdxname'], datatype=XSD.string)))
        if pd.notnull(row['admitdxtext']):
            g.add((dx_uri, eicu.hasAdmitDxText, Literal(row['admitdxtext'], datatype=XSD.string)))

    g.serialize("result/admissiondx.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])