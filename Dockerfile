FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.2-hadoop-3.3.1

WORKDIR  /app
USER 0
ADD https://repo1.maven.org/maven2/net/snowflake/spark-snowflake_2.12/2.9.0-spark_3.1/spark-snowflake_2.12-2.9.0-spark_3.1.jar /opt/spark/jars/spark-snowflake_2.12-2.9.0-spark_3.1.jar
ADD https://repo1.maven.org/maven2/net/snowflake/snowflake-jdbc/3.13.3/snowflake-jdbc-3.13.3.jar /opt/spark/jars/snowflake-jdbc-3.13.3.jar
RUN chmod a+r /opt/spark/jars/*


COPY requirements.txt requirements.txt
RUN python3 -m pip install  -r requirements.txt

COPY eve.py snowflake.py main.py ./
ENV AWS_DEFAUT_REGION=
ENV AWS_ACCCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
ENV PYSPARK_PYTHON python3
CMD ["python3", "main.py"]

EXPOSE 8080
