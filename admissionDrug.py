import pandas as pd
from rdflib import Graph, Literal, Namespace, RDF, URIRef
from rdflib.namespace import XSD
import sys

# admission drug
def main(inputpath):
    g = Graph()
    ex = Namespace("http://schema.org/eicu")
    eicu = Namespace("http://www.eicu.org/ontologies#")
    g.bind("ex", ex)
    g.bind("eicu", eicu)
    df = pd.read_csv(f"{inputpath}/admissiondrug.csv")
    for _, row in df.iterrows():
        drug_uri = ex[f"AdmissionDrug{row['admissiondrugid']}"]
        
        g.add((drug_uri, RDF.type, eicu.AdmissionDrug))
        g.add((ex[f"PatientUnitStay{row['patientunitstayid']}"], eicu.hasAdmissionDrug, drug_uri))
        g.add((drug_uri, eicu.hasDrugOffset, Literal(row['drugoffset'], datatype=XSD.integer)))
        g.add((drug_uri, eicu.hasDrugEnteredOffset, Literal(row['drugenteredoffset'], datatype=XSD.integer)))
        g.add((drug_uri, eicu.hasDrugNoteType, Literal(row['drugnotetype'], datatype=XSD.string)))
        g.add((drug_uri, eicu.hasSpecialtyType, Literal(row['specialtytype'], datatype=XSD.string)))
        g.add((drug_uri, eicu.hasUserType, Literal(row['usertype'], datatype=XSD.string)))
        g.add((drug_uri, eicu.hasRxIncluded, Literal(row['rxincluded'], datatype=XSD.boolean)))
        g.add((drug_uri, eicu.hasWrittenIneICU, Literal(row['writtenineicu'], datatype=XSD.boolean)))
        g.add((drug_uri, eicu.hasDrugName, Literal(row['drugname'], datatype=XSD.string)))
        if pd.notnull(row['drugdosage']):
            g.add((drug_uri, eicu.hasDrugDosage, Literal(row['drugdosage'], datatype=XSD.decimal)))
        if pd.notnull(row['drugunit']):
            g.add((drug_uri, eicu.hasDrugUnit, Literal(row['drugunit'], datatype=XSD.string)))
        if pd.notnull(row['drugadmitfrequency']):
            g.add((drug_uri, eicu.hasDrugAdmitFrequency, Literal(row['drugadmitfrequency'], datatype=XSD.string)))
        if pd.notnull(row['drughiclseqno']):
            g.add((drug_uri, eicu.hasDrugHiclSeqno, Literal(row['drughiclseqno'], datatype=XSD.integer)))

    g.serialize("result/admissionDrug.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])