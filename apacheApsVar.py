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

    # apacheApsVar
    df = pd.read_csv(f"{inputpath}/apacheApsVar.csv")
    cols = df.columns
    for _, row in df.iterrows():
        aps_var_uri = ex[f"ApacheApsVar{row['apacheapsvarid']}"]

        g.add((aps_var_uri, RDF.type, eicu.ApacheApsVar))
        g.add((ex[f"PatientUnitStay{row['patientunitstayid']}"], eicu.hasApacheApsVar, aps_var_uri))
        g.add((aps_var_uri, eicu["hasIntubated"], Literal(row[cols[2]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasVent"], Literal(row[cols[3]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasDialysis"], Literal(row[cols[4]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasEyes"], Literal(row[cols[5]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasMotor"], Literal(row[cols[6]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasVerbal"], Literal(row[cols[7]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasMeds"], Literal(row[cols[8]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasUrine"], Literal(row[cols[9]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasWbc"], Literal(row[cols[10]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasTemprature"], Literal(row[cols[11]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasRespiratoryRate"], Literal(row[cols[12]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasSodium"], Literal(row[cols[13]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasHeartRate"], Literal(row[cols[14]], datatype=XSD.integer)))
        g.add((aps_var_uri, eicu["hasMeanBp"], Literal(row[cols[15]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasPh"], Literal(row[cols[16]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasHematocrit"], Literal(row[cols[17]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasCreatinine"], Literal(row[cols[18]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasAlbumin"], Literal(row[cols[19]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasPao2"], Literal(row[cols[20]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasPco2"], Literal(row[cols[21]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasBun"], Literal(row[cols[22]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasGlucose"], Literal(row[cols[23]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasBilirubin"], Literal(row[cols[24]], datatype=XSD.float)))
        g.add((aps_var_uri, eicu["hasFio2"], Literal(row[cols[25]], datatype=XSD.float)))
        
    g.serialize("result/apacheApsVar.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])