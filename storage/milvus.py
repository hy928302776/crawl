from pymilvus import (
    connections,
    utility,
    FieldSchema,
    CollectionSchema,
    DataType,
    Collection,
)
print("start connecting to Milvus")
connections.connect("default", host="8.217.52.63", port="19530")

fields = [
    FieldSchema(name="pk", dtype=DataType.INT64, is_primary=True, auto_id=False),
    FieldSchema(name="code", dtype=DataType.JSON),
    FieldSchema(name="date", dtype=DataType.DOUBLE),
    FieldSchema(name="source", dtype=DataType.DOUBLE),
    FieldSchema(name="link", dtype=DataType.FLOAT_VECTOR, dim=8),
    FieldSchema(name="title", dtype=DataType.FLOAT_VECTOR, dim=8),
    FieldSchema(name="text", dtype=DataType.FLOAT_VECTOR, dim=8),
    FieldSchema(name="createTime", dtype=DataType.FLOAT_VECTOR, dim=8),
]
schema = CollectionSchema(fields, "hello_milvus is the simplest demo to introduce the APIs")
hello_milvus = Collection("hello_milvus", schema)
