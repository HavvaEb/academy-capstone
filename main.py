from eve   import transform_for_exercises, get_spark
from snowflake import get_snowflake_creds_from_sm, write_df_with_options
import logging

SNOWFLAKE_SOURCE_NAME = "net.snowflake.spark.snowflake"


path = "s3a://dataminded-academy-capstone-resources/raw/open_aq/"
spark = get_spark()
frame = spark.read.json(path)

frame = transform_for_exercises(frame)

options = get_snowflake_creds_from_sm("snowflake/capstone/login")
logging.info(options)
write_df_with_options(frame, format=SNOWFLAKE_SOURCE_NAME, options=options, mode="overwrite")
