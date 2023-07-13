from pyspark.context import SparkContext
from pyspark.sql.session import SparkSession
from helpers.load_csv import load_csv

sc = SparkContext("local")
sc.setLogLevel("WARN")
spark = SparkSession(sc)

df = load_csv("data/world-data-2023.csv", spark)
df.show(truncate=False)