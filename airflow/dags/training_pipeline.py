from airflow import DAG
from airflow.operators.python import PythonOperator
from textwrap import dedent
import pendulam 

from src.pipeline.training_pipeline import TrainingPipeline

train_pipeline = TrainingPipeline()

with DAG(
    "pricepredictor_training_pipeline",
    default_args={"retries": 2},
    description="my first airflow DAG",
    schedule="@weekly",
    start_date=pendulam.datetime(2024, 5, 30),
    catchup=False,
    tags=["machine_learning", "regression", "price_prediction"]) as dag:
    
    dag.doc_md = __doc__

    def data_ingestion(**kwargs):
        ti = kwargs["ti"]
        train_path, test_path = TrainingPipeline.start_data_ingestion()
        ti.xcom_push("data_ingestion_artifacts", {"train_path":train_path, "test_path":test_path})

    