FROM public.ecr.aws/dataminded/spark-k8s-glue:v3.1.2-hadoop-3.3.1

WORKDIR  /app
USER 0
COPY requirements.txt requirements.txt
RUN python3 -m pip install  -r requirements.txt

COPY eve.py snowflake.py main.py ./
ENV AWS_DEFAUT_REGION=
ENV AWS_ACCCESS_KEY_ID=
ENV AWS_SECRET_ACCESS_KEY=
ENV PYSPARK_PYTHON python3
CMD ["python3", "main.py"]

EXPOSE 8080
