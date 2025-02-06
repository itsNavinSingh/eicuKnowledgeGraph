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

    # carePlanInfectiousDisease

    df = pd.read_csv(f"{inputpath}/carePlanInfectiousDisease.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"CarePlanInfectiousDisease{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.CarePlanInfectiousDisease))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasCarePlanInfectiousDisease, uid))
        g.add((uid, eicu["hasActiveUponDischarge"], Literal(row[cols[2]], datatype=XSD.boolean)))
        g.add((uid, eicu["hascarePlanInfectiousDiseaseOffset"], Literal(row[cols[3]], datatype=XSD.integer)))
        g.add((uid, eicu["hasInfectDiseaseSite"], Literal(row[cols[4]])))
        g.add((uid, eicu["hasInfectDiseaseAssessment"], Literal(row[cols[5]])))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasResponseToTherapy"], Literal(row[cols[6]])))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasTreatment"], Literal(row[cols[7]])))
        
    g.serialize("result/carePlanInfectiousDisease.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])