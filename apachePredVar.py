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

    # apachePredVar

    df = pd.read_csv(f"{inputpath}/apachePredVar.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"ApachePredVar{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.ApachePredVar))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasApachePredVar, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasSicDay"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasSaps3Day1"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasSaps3Today"], Literal(row[cols[4]], datatype=XSD.integer)))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasSaps3Yesterday"], Literal(row[cols[5]], datatype=XSD.integer)))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasGender"], Literal(row[cols[6]], datatype=XSD.integer)))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasTechType"], Literal(row[cols[7]], datatype=XSD.integer)))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasRegion"], Literal(row[cols[8]], datatype=XSD.integer)))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasBedCount"], Literal(row[cols[9]], datatype=XSD.integer)))
        if pd.notnull(row[cols[10]]):
            g.add((uid, eicu["hasAdmitSource"], Literal(row[cols[10]], datatype=XSD.integer)))
        if pd.notnull(row[cols[11]]):
            g.add((uid, eicu["hasGraftCount"], Literal(row[cols[11]], datatype=XSD.integer)))
        if pd.notnull(row[cols[12]]):
            g.add((uid, eicu["hasMeds"], Literal(row[cols[12]], datatype=XSD.integer)))
        if pd.notnull(row[cols[13]]):
            g.add((uid, eicu["hasVerbal"], Literal(row[cols[13]], datatype=XSD.integer)))
        if pd.notnull(row[cols[14]]):
            g.add((uid, eicu["hasMotor"], Literal(row[cols[14]], datatype=XSD.integer)))
        if pd.notnull(row[cols[15]]):
            g.add((uid, eicu["hasEyes"], Literal(row[cols[15]], datatype=XSD.integer)))
        if pd.notnull(row[cols[16]]):
            g.add((uid, eicu["hasAge"], Literal(row[cols[16]], datatype=XSD.integer)))
        if pd.notnull(row[cols[17]]):
            g.add((uid, eicu["hasAdmitDiagnosis"], Literal(row[cols[17]])))
        if pd.notnull(row[cols[18]]):
            g.add((uid, eicu["hasThrombolytics"], Literal(row[cols[18]], datatype=XSD.integer)))
        if pd.notnull(row[cols[19]]):
            g.add((uid, eicu["hasDiedInHospital"], Literal(row[cols[19]], datatype=XSD.integer)))
        if pd.notnull(row[cols[20]]):
            g.add((uid, eicu["hasAids"], Literal(row[cols[20]], datatype=XSD.integer)))
        if pd.notnull(row[cols[21]]):
            g.add((uid, eicu["hasHepticFailure"], Literal(row[cols[21]], datatype=XSD.integer)))
        if pd.notnull(row[cols[22]]):
            g.add((uid, eicu["hasLymphoma"], Literal(row[cols[22]], datatype=XSD.integer)))
        if pd.notnull(row[cols[23]]):
            g.add((uid, eicu["hasMetastaticCancer"], Literal(row[cols[23]], datatype=XSD.integer)))
        if pd.notnull(row[cols[24]]):
            g.add((uid, eicu["hasLeukemia"], Literal(row[cols[24]], datatype=XSD.integer)))
        if pd.notnull(row[cols[25]]):
            g.add((uid, eicu["hasImmunosupperession"], Literal(row[cols[25]], datatype=XSD.integer)))
        if pd.notnull(row[cols[26]]):
            g.add((uid, eicu["hasCirrhosis"], Literal(row[cols[26]], datatype=XSD.integer)))
        if pd.notnull(row[cols[27]]):
            g.add((uid, eicu["hasElectiveSurgery"], Literal(row[cols[27]], datatype=XSD.integer)))
        if pd.notnull(row[cols[28]]):
            g.add((uid, eicu["hasActiveTx"], Literal(row[cols[28]], datatype=XSD.integer)))
        if pd.notnull(row[cols[29]]):
            g.add((uid, eicu["hasReadmit"], Literal(row[cols[29]], datatype=XSD.integer)))
        if pd.notnull(row[cols[30]]):
            g.add((uid, eicu["hasIma"], Literal(row[cols[30]], datatype=XSD.integer)))
        if pd.notnull(row[cols[31]]):
            g.add((uid, eicu["hasMidur"], Literal(row[cols[31]], datatype=XSD.integer)))
        if pd.notnull(row[cols[32]]):
            g.add((uid, eicu["hasVentDay1"], Literal(row[cols[32]], datatype=XSD.integer)))
        if pd.notnull(row[cols[33]]):
            g.add((uid, eicu["hasOobVentDay1"], Literal(row[cols[33]], datatype=XSD.integer)))
        if pd.notnull(row[cols[34]]):
            g.add((uid, eicu["hasOobIntubDay1"], Literal(row[cols[34]], datatype=XSD.integer)))
        if pd.notnull(row[cols[35]]):
            g.add((uid, eicu["hasDiabetes"], Literal(row[cols[35]], datatype=XSD.integer)))
        if pd.notnull(row[cols[36]]):
            g.add((uid, eicu["hasManagementSystem"], Literal(row[cols[36]], datatype=XSD.integer)))
        if pd.notnull(row[cols[37]]):
            g.add((uid, eicu["hasVar03HsXlos"], Literal(row[cols[37]], datatype=XSD.float)))
        if pd.notnull(row[cols[38]]):
            g.add((uid, eicu["hasPao2"], Literal(row[cols[38]], datatype=XSD.float)))
        if pd.notnull(row[cols[39]]):
            g.add((uid, eicu["hasFio2"], Literal(row[cols[39]], datatype=XSD.float)))
        if pd.notnull(row[cols[40]]):
            g.add((uid, eicu["hasEjectFx"], Literal(row[cols[40]], datatype=XSD.float)))
        if pd.notnull(row[cols[41]]):
            g.add((uid, eicu["hasCreatinine"], Literal(row[cols[41]], datatype=XSD.float)))
        if pd.notnull(row[cols[42]]):
            g.add((uid, eicu["hasDischargeLocation"], Literal(row[cols[42]], datatype=XSD.integer)))
        if pd.notnull(row[cols[43]]):
            g.add((uid, eicu["hasVisitNumber"], Literal(row[cols[43]], datatype=XSD.integer)))
        if pd.notnull(row[cols[44]]):
            g.add((uid, eicu["hasAmiLocation"], Literal(row[cols[44]], datatype=XSD.integer)))
        if pd.notnull(row[cols[45]]):
            g.add((uid, eicu["hasDay1Meds"], Literal(row[cols[45]], datatype=XSD.integer)))
        if pd.notnull(row[cols[46]]):
            g.add((uid, eicu["hasDay1Verbal"], Literal(row[cols[46]], datatype=XSD.integer)))
        if pd.notnull(row[cols[47]]):
            g.add((uid, eicu["hasDay1Motor"], Literal(row[cols[47]], datatype=XSD.integer)))
        if pd.notnull(row[cols[48]]):
            g.add((uid, eicu["hasDay1Eyes"], Literal(row[cols[48]], datatype=XSD.integer)))
        if pd.notnull(row[cols[49]]):
            g.add((uid, eicu["hasDay1Pao2"], Literal(row[cols[49]], datatype=XSD.float)))
        if pd.notnull(row[cols[50]]):
            g.add((uid, eicu["hasDay1Fio2"], Literal(row[cols[50]], datatype=XSD.float)))
        
    g.serialize("result/apachePredVar.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])