
from neo4j import GraphDatabase

driver = GraphDatabase.driver("neo4j://localhost:7687", auth=("neo4j", "12345678"))

query =  """

MATCH (P) RETURN P;

"""

with driver.session() as sesssion:
    result = sesssion.run(query)
    for record in result:
        print(record)

        data = [record for record in result]


data[0]      

