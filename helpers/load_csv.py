from pyspark.sql import DataFrame, SparkSession

def load_csv(path: str, spark: SparkSession) -> DataFrame:
    df = spark.read.option("header",True).csv("data/world-data-2023.csv")
    return df

