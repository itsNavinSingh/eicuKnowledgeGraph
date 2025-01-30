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

    # patient
    df = pd.read_csv(f"{inputpath}/patient.csv")
    for _, row in df.iterrows():
        patient_uri = ex[f"PatientUnitStay{row['patientunitstayid']}"]
        
        g.add((patient_uri, RDF.type, eicu.Patient))
        g.add((patient_uri, eicu.hasPatientHealthSystemStay, ex[f"HealthSystemStay{row['patienthealthsystemstayid']}"]))
        g.add((patient_uri, eicu.hasGender, Literal(row['gender'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasAge, Literal(row['age'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasEthnicity, Literal(row['ethnicity'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasHospital, ex[f"Hospital{row['hospitalid']}"]))
        g.add((patient_uri, eicu.hasWard, ex[f"Ward{row['wardid']}"]))
        g.add((patient_uri, eicu.hasApacheAdmissionDx, Literal(row['apacheadmissiondx'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasAdmissionHeight, Literal(row['admissionheight'], datatype=XSD.decimal)))
        g.add((patient_uri, eicu.hasHospitalAdmitTime, Literal(str(row['hospitaladmittime24']), datatype=XSD.time)))
        g.add((patient_uri, eicu.hasHospitalAdmitOffset, Literal(row['hospitaladmitoffset'], datatype=XSD.integer)))
        g.add((patient_uri, eicu.hasHospitalAdmitSource, Literal(row['hospitaladmitsource'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasHospitalDischargeYear, Literal(row['hospitaldischargeyear'], datatype=XSD.gYear)))
        g.add((patient_uri, eicu.hasHospitalDischargeTime, Literal(str(row['hospitaldischargetime24']), datatype=XSD.time)))
        g.add((patient_uri, eicu.hasHospitalDischargeOffset, Literal(row['hospitaldischargeoffset'], datatype=XSD.integer)))
        g.add((patient_uri, eicu.hasHospitalDischargeLocation, Literal(row['hospitaldischargelocation'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasHospitalDischargeStatus, Literal(row['hospitaldischargestatus'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasUnitType, Literal(row['unittype'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasUnitAdmitTime, Literal(str(row['unitadmittime24']), datatype=XSD.time)))
        g.add((patient_uri, eicu.hasUnitAdmitSource, Literal(row['unitadmitsource'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasUnitVisitNumber, Literal(row['unitvisitnumber'], datatype=XSD.integer)))
        g.add((patient_uri, eicu.hasUnitStayType, Literal(row['unitstaytype'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasAdmissionWeight, Literal(row['admissionweight'], datatype=XSD.decimal)))
        g.add((patient_uri, eicu.hasDischargeWeight, Literal(row['dischargeweight'], datatype=XSD.decimal)))
        g.add((patient_uri, eicu.hasUnitDischargeTime, Literal(str(row['unitdischargetime24']), datatype=XSD.time)))
        g.add((patient_uri, eicu.hasUnitDischargeOffset, Literal(row['unitdischargeoffset'], datatype=XSD.integer)))
        g.add((patient_uri, eicu.hasUnitDischargeLocation, Literal(row['unitdischargelocation'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasUnitDischargeStatus, Literal(row['unitdischargestatus'], datatype=XSD.string)))
        g.add((patient_uri, eicu.hasUniquePID, Literal(row['uniquepid'], datatype=XSD.string)))
    g.serialize("result/patient.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])