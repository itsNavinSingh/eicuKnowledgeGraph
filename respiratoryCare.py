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

    # respiratoryCare

    df = pd.read_csv(f"{inputpath}/respiratoryCare.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"RespiratoryCare{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.RespiratoryCare))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasRespiratoryCare, uid))
        if pd.notnull(row[cols[2]]):
            g.add((uid, eicu["hasRespCareStatusOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasCurrentHistorySeqNum"], Literal(row[cols[3]], datatype=XSD.integer)))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasAirwayType"], Literal(row[cols[4]])))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasAirwaySize"], Literal(row[cols[5]])))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasAirwayPosition"], Literal(row[cols[6]])))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasCuffPressure"], Literal(row[cols[7]], datatype=XSD.float)))
        if pd.notnull(row[cols[8]]):
            g.add((uid, eicu["hasVentStartOffset"], Literal(row[cols[8]], datatype=XSD.integer)))
        if pd.notnull(row[cols[9]]):
            g.add((uid, eicu["hasVentEndOffset"], Literal(row[cols[9]], datatype=XSD.integer)))
        if pd.notnull(row[cols[10]]):
            g.add((uid, eicu["hasPriorVentStartOffset"], Literal(row[cols[10]], datatype=XSD.integer)))
        if pd.notnull(row[cols[11]]):
            g.add((uid, eicu["hasPriorVentEndOffset"], Literal(row[cols[11]], datatype=XSD.integer)))
        if pd.notnull(row[cols[12]]):
            g.add((uid, eicu["hasApneaParams"], Literal(row[cols[12]])))
        if pd.notnull(row[cols[13]]):
            g.add((uid, eicu["hasLowExhMvLimit"], Literal(row[cols[13]], datatype=XSD.float)))
        if pd.notnull(row[cols[14]]):
            g.add((uid, eicu["hasHiExhMvLimit"], Literal(row[cols[14]], datatype=XSD.float)))
        if pd.notnull(row[cols[15]]):
            g.add((uid, eicu["hasLowExhTvLimit"], Literal(row[cols[15]], datatype=XSD.float)))
        if pd.notnull(row[cols[16]]):
            g.add((uid, eicu["hasHiPeakPresLimit"], Literal(row[cols[16]], datatype=XSD.float)))
        if pd.notnull(row[cols[17]]):
            g.add((uid, eicu["hasLowPeakPresLimit"], Literal(row[cols[17]], datatype=XSD.float)))
        if pd.notnull(row[cols[18]]):
            g.add((uid, eicu["hasHiRespRateLimit"], Literal(row[cols[18]], datatype=XSD.float)))
        if pd.notnull(row[cols[19]]):
            g.add((uid, eicu["hasLowRespRateLimit"], Literal(row[cols[19]], datatype=XSD.float)))
        if pd.notnull(row[cols[20]]):
            g.add((uid, eicu["hasSighPresLimit"], Literal(row[cols[20]], datatype=XSD.float)))
        if pd.notnull(row[cols[21]]):
            g.add((uid, eicu["hasLowIronOxLimit"], Literal(row[cols[21]], datatype=XSD.float)))
        if pd.notnull(row[cols[22]]):
            g.add((uid, eicu["hasHighIronOxLimit"], Literal(row[cols[22]], datatype=XSD.float)))
        if pd.notnull(row[cols[23]]):
            g.add((uid, eicu["hasMeanAirwayPresLimit"], Literal(row[cols[23]], datatype=XSD.float)))
        if pd.notnull(row[cols[24]]):
            g.add((uid, eicu["hasPeepLimit"], Literal(row[cols[24]], datatype=XSD.float)))
        if pd.notnull(row[cols[25]]):
            g.add((uid, eicu["hasCpapLimit"], Literal(row[cols[24]], datatype=XSD.float)))
        if pd.notnull(row[cols[26]]):
            g.add((uid, eicu["hasSetApneaInterval"], Literal(row[cols[26]])))
        if pd.notnull(row[cols[27]]):
            g.add((uid, eicu["hasSetApneaTv"], Literal(row[cols[27]])))
        if pd.notnull(row[cols[28]]):
            g.add((uid, eicu["hasSetApnealPpeepHigh"], Literal(row[cols[28]])))
        if pd.notnull(row[cols[29]]):
            g.add((uid, eicu["hasSetApneaRr"], Literal(row[cols[29]], datatype=XSD.float)))
        if pd.notnull(row[cols[30]]):
            g.add((uid, eicu["hasSetApneaPeakFlow"], Literal(row[cols[30]])))
        if pd.notnull(row[cols[31]]):
            g.add((uid, eicu["hasSetApneaInspTime"], Literal(row[cols[31]])))
        if pd.notnull(row[cols[32]]):
            g.add((uid, eicu["hasSetApneaIe"], Literal(row[cols[32]])))
        if pd.notnull(row[cols[33]]):
            g.add((uid, eicu["hasSetApneaFio2"], Literal(row[cols[33]])))

    g.serialize("result/respiratoryCare.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])