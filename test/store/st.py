from pymilvus import utility,connections
from pymilvus import Collection
connections.connect("default", host="8.217.52.63", port="19530")
cc = utility.list_collections()
print(f"list_collections:{cc}")

collection = Collection("web") # Get an existing collection.
print(f"collection.schema:{collection.schema}")             # Return the schema.CollectionSchema of the collection.
print(f"collection.description:{collection.description}")        # Return the description of the collection.
print(f"collection.name:{collection.name}")               # Return the name of the collection.
print(f"collection.is_empty:{collection.is_empty}")           # Return the boolean value that indicates if the collection is empty.
print(f"collection.num_entities:{collection.num_entities}")          # Return the number of entities in the collection.
print(f"collection.primary_field:{collection.primary_field}")         # Return the schema.FieldSchema of the primary key field.
print(f"collection.partitions:{collection.partitions}")            # Return the list[Partition] object.
print(f"collection.indexes:{collection.indexes}")               # Return the list[Index] object.
print(f"collection.properties:{collection.properties}")		# Return the expiration time of data in the collection.
