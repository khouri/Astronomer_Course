from airflow.decorators import dag, task
from airflow.models import Variable
from datetime import datetime


@task
def start():
	print('start')


@task
def print_variable():
	print(Variable.get("my_var"))


@dag(start_date=datetime(2003, 1, 1), catchup = False)
def my_dag():
	start() >> print_variable()

my_dag()