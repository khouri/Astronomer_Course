from datetime import datetime

from airflow import DAG
from airflow.operators.python import PythonOperator
from airflow.utils.helpers import chain


def print_a():
	print('a')
pass

def print_b():
	print('b')
pass

def print_c():
	print('c')
pass

def print_d():
	print('d')
pass

def print_e():
	print('e')
pass


default_args = {
    'retries': 3,
}

with DAG("my_dag2",
		start_date = datetime(2023, 1, 1),
		schedule = "@daily",
		default_args = default_args,
		description = "A simple tutorial dag",
		tags = ["tutorial", "my first dag", "hello world"],
		catchup = False ) as dag:

	task_a = PythonOperator(task_id = 'task_a',
							python_callable = print_a)

	task_b = PythonOperator(task_id='task_b',
							python_callable=print_b)

	task_c = PythonOperator(task_id='task_c',
							python_callable=print_c)

	task_d = PythonOperator(task_id='task_d',
							python_callable=print_d)

	task_e = PythonOperator(task_id='task_e',
							python_callable=print_e)

	# task a is the upstream task from task b
	#task_a >> [task_b, task_c, task_d] >> task_e
	chain(task_a, [task_b, task_c], [task_d, task_e])
pass