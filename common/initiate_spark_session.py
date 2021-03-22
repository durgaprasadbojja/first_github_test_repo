# sparksession creation
from pyspark.sql import SparkSession


def get_spark_session():
    spark = SparkSession.builder.appName("TestApplication").master("local[*]").getOrCreate()
    return spark
