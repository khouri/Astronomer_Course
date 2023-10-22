from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain
from airflow.operators.bash import BashOperator


def readfile():
	lambda: print(open('/tmp/dummy', 'rb').read())
	return(None)
pass

default_args = {
    'retries': 3,
}

with DAG("check_dag",
		start_date = datetime(2023, 1, 1),
		schedule = "@daily",
		default_args = default_args,
		description = "Read and write a file",
		tags = ["BashOPerator", "PythonOPerator"],
		catchup = False ) as dag:
	None

	task_create_file = BashOperator(task_id = 'task_create_file',
									bash_command = "echo Hi there! >/tmp/dummy")

	task_check_file = BashOperator(task_id = 'task_read_file',
									bash_command="test -f /tmp/dummy")

	task_readfile = PythonOperator(task_id = 'task_readfile',
									python_callable = readfile)

	task_create_file >> task_check_file >> task_readfile

pass