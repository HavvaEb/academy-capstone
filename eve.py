"""
import libraries.
"""
import pyspark
import datetime
from pyspark.sql import SparkSession, DataFrame
from pyspark.sql.types import IntegerType, StringType, StructField, StructType
from pyspark import SparkConf
from pyspark.sql.functions import to_timestamp

def flatten_df(df: pyspark.sql.DataFrame):
    flat_cols = [colname for colname, datatype in df.dtypes if not datatype.startswith('struct')]
    nested_cols = [colname for colname, datatype in df.dtypes if datatype.startswith('struct')]
    return df.select(*flat_cols, *[c + ".*" for c in nested_cols])

def get_spark():
    conf = SparkConf()
    conf.set('fs.s3a.aws.credentials.provider', 'com.amazonaws.auth.DefaultAWSCredentialsProviderChain')
    conf.set("fs.s3.impl", "org.apache.hadoop.fs.s3a.S3AFileSystem")
    conf.set("fs.s3a.endpoint", "s3.amazonaws.com")
    paks = [ 'org.apache.hadoop:hadoop-aws:3.1.2',
             'net.snowflake:snowflake-jdbc:3.13.14',
             'net.snowflake:spark-snowflake_2.12:2.10.0-spark_3.2']
    conf.set('spark.jars.packages',",".join(paks))

    return SparkSession.builder.config(conf=conf).getOrCreate()

def transform_for_exercises(frame: DataFrame) -> DataFrame:

    data = flatten_df(frame)

    #data.select(data.colName("data.*"))


    data2 = data.withColumn('date_local', to_timestamp('local', format="yyyy-MM-dd'T'HH:mm:ssXXX"))
    return data2.withColumn('date_utc', to_timestamp('utc', format="yyyy-MM-dd'T'HH:mm:ssXXX"))

