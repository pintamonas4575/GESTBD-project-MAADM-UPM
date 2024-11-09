import json
import pandas as pd
from elasticsearch import Elasticsearch

es = Elasticsearch("http://localhost:9200")

# CREAR ÍNDICE
index_mapping = {
    "mappings": {
        "properties": {
            "ranking_date": {"type": "date", "format": "yyyy-MM-dd"},
            "pilot_name": {"type": "keyword"},
            "position": {"type": "integer"},
            "pilot_review": {"type": "text"},
            "ranking_link": {"type": "text"},
        }
    }
}

try:
    es.indices.create(index="my_index", body=index_mapping)
except Exception as e:
    print(f"Error: {e}")
    
# es.indices.delete(index='my_index') # borrar índice

# INDEXAR CSV
csv = pd.read_csv("rankings_info.csv")
df = pd.DataFrame(csv)

for index in range(len(df)):
    doc = df.iloc[index].to_dict()
    res_insert = es.index(index="my_index", id=index+1, document=doc)

# print(json.dumps(res_insert.body, indent=3)) # el último insertado
# es.get(index='my_index', id=455) # coger un ejemplo

# CONSULTAS
res = es.search(index='my_index', body={
     'query': {
         'range': {
             'position': {
                 'gte': 1,
                 'lte': 3
             }
         }
     },
     'size': 1
})

# print(json.dumps(res.body["hits"]["hits"][0]["_source"], indent=4))
print(json.dumps(res.body, indent=4))


