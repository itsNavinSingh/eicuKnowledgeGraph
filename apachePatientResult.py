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

    # apachePatientResult
    df = pd.read_csv(f"{inputpath}/apachePatientResult.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"ApachePatientResult{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.ApachePatientResult))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasApachePatientResult, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasPhysicianSpeciality"], row[cols[2]]))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasPhysicianInterventionCategory"], row[cols[3]]))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasAcutePhysiologyScore"], Literal(row[cols[4]], datatype=XSD.integer)))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasApacheScore"], Literal(row[cols[5]], datatype=XSD.integer)))
        g.add((uid, eicu["hasApacheVersion"], Literal(row[cols[6]], datatype=XSD.integer)))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasPredictedIcuMortality"], row[cols[7]]))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasActualIcuMortality"], row[cols[8]]))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasPredictedIcuLos"], Literal(row[cols[9]], datatype=XSD.float)))
        if pd.notnull(row[cols[10]]):
            g.add((uid, eicu["hasActualIcuLos"], Literal(row[cols[10]], datatype=XSD.float)))
        if pd.notnull(row[cols[11]]):
            g.add((uid, eicu["hasPredictedHospitalMortality"], row[cols[12]]))
        if pd.notnull(row[cols[12]]):
            g.add((uid, eicu["hasActualHospitalMortality"], row[cols[12]]))
        if  pd.notnull(row[cols[13]]):
            g.add((uid, eicu["hasPredictedHospitalLos"], Literal(row[cols[13]], datatype=XSD.float)))
        if pd.notnull(row[cols[14]]):
            g.add((uid, eicu["hasActualHospitalLos"], Literal(row[cols[14]], datatype=XSD.float)))
        if pd.notnull(row[cols[15]]):
            g.add((uid, eicu["hasPreopMi"], Literal(row[cols[15]], datatype=XSD.integer)))
        if pd.notnull(row[cols[16]]):
            g.add((uid, eicu["hasPreopCardiacCath"], Literal(row[cols[16]], datatype=XSD.integer)))
        if pd.notnull(row[cols[17]]):
            g.add((uid, eicu["hasPtcaWithin24h"], Literal(row[cols[17]], datatype=XSD.integer)))
        if pd.notnull(row[cols[18]]):
            g.add((uid, eicu["hasUnbridgedUnitLos"], Literal(row[cols[18]], datatype=XSD.float)))
        if pd.notnull(row[cols[19]]):
            g.add((uid, eicu["hasUnbridgedHospLos"], Literal(row[cols[19]], datatype=XSD.float)))
        if pd.notnull(row[cols[20]]):
            g.add((uid, eicu["hasActualVentDays"], Literal(row[cols[20]], datatype=XSD.float)))
        if pd.notnull(row[cols[21]]):
            g.add((uid, eicu["hasPredVentDays"], Literal(row[cols[21]], datatype=XSD.float)))
        if pd.notnull(row[cols[22]]):
            g.add((uid, eicu["hasUnbridgedActualVentDays"], Literal(row[cols[22]], datatype=XSD.float)))
        
    g.serialize("result/apachePatientResult.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])