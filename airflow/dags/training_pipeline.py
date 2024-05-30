from airflow import DAG
from airflow.operators.python import PythonOperator
from textwrap import dedent
import pendulam 

from src.pipeline.training_pipeline import TrainingPipeline

train_pipeline = TrainingPipeline()

with DAG()

