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

    # carePlanCareProvider
    df = pd.read_csv(f"{inputpath}/carePlanCareProvider.csv")
    cols = df.columns
    for _, row in df.iterrows():
        uid = ex[f"CarePlanCareProvider{row[cols[0]]}"]
        g.add((uid, RDF.type, eicu.CarePlanCareProvider))
        g.add((ex[f"PatientUnitStay{row[cols[1]]}"], eicu.hasCarePlanCareProvider, uid))
        g.add((uid, eicu["hasCareProviderSaveOffset"], Literal(row[cols[2]], datatype=XSD.integer)))
        if pd.notnull(row[cols[3]]):
            g.add((uid, eicu["hasProviderType"], Literal(row[cols[3]])))
        if pd.notnull(row[cols[4]]):
            g.add((uid, eicu["hasSpecialty"], Literal(row[cols[4]])))
        if pd.notnull(row[cols[5]]):
            g.add((uid, eicu["hasInterventionCategory"], Literal(row[cols[5]])))
        if pd.notnull(row[cols[6]]):
            g.add((uid, eicu["hasManagingPhysician"], Literal(row[cols[6]])))
        if pd.notnull(row[cols[7]]):
            g.add((uid, eicu["hasActiveUponDischarge"], Literal(row[cols[7]], datatype=XSD.boolean)))
        
    g.serialize("result/carePlanCareProvider.ttl", format="turtle")
    return

if __name__ == "__main__":
    main(sys.argv[1])