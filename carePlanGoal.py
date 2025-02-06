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

    # carePlanGoal

    df = pd.read_csv(f"{inputpath}/carePlanGoal.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"CarePlanGoal{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.CarePlanGoal))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hascarePlanGoal, uid))
        g.add((uid, eicu["hasCarePlanGoalOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        g.add((uid, eicu["hasCarePlanGoalCategory"], Literal(row[cols[3]])))
        g.add((uid, eicu["hasCarePlanGoalValue"], Literal(row[cols[4]])))
        g.add((uid, eicu["hasCarePlanGoalStatus"], Literal(row[cols[5]])))
        g.add((uid, eicu["hasActiveUponDischarge"], Literal(row[cols[6]], datatype=XSD.boolean)))
        
    g.serialize("result/carePlanGoal.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])