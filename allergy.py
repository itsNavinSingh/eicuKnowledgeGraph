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

    # allergy
    df = pd.read_csv(f"{inputpath}/allergy.csv")
    for _, row in df.iterrows():
        allergy_uri = ex[f"Allergy{row['allergyid']}"]
        
        g.add((allergy_uri, RDF.type, eicu.Allergy))
        g.add((ex[f"PatientUnitStay{row['patientunitstayid']}"], eicu.hasAllergy, allergy_uri))
        g.add((allergy_uri, eicu.hasAllergyOffset, Literal(row['allergyoffset'], datatype=XSD.integer)))
        g.add((allergy_uri, eicu.hasAllergyEnteredOffset, Literal(row['allergyenteredoffset'], datatype=XSD.integer)))
        g.add((allergy_uri, eicu.hasAllergyNoteType, Literal(row['allergynotetype'], datatype=XSD.string)))
        g.add((allergy_uri, eicu.hasSpecialtyType, Literal(row['specialtytype'], datatype=XSD.string)))
        g.add((allergy_uri, eicu.hasUserType, Literal(row['usertype'], datatype=XSD.string)))
        g.add((allergy_uri, eicu.hasRxIncluded, Literal(row['rxincluded'], datatype=XSD.boolean)))
        g.add((allergy_uri, eicu.wasWrittenIneICU, Literal(row['writtenineicu'], datatype=XSD.boolean)))
        
        if pd.notnull(row['drugname']):
            g.add((allergy_uri, eicu.hasDrugName, Literal(row['drugname'], datatype=XSD.string)))
        if pd.notnull(row['allergytype']):
            g.add((allergy_uri, eicu.hasAllergyType, Literal(row['allergytype'], datatype=XSD.string)))
        if pd.notnull(row['allergyname']):
            g.add((allergy_uri, eicu.hasAllergyName, Literal(row['allergyname'], datatype=XSD.string)))
        if pd.notnull(row['drughiclseqno']):
            g.add((allergy_uri, eicu.hasDrugHiclSeqno, Literal(row['drughiclseqno'], datatype=XSD.integer)))

    g.serialize("result/allergy.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])