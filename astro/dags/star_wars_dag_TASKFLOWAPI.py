from airflow.decorators import dag, task
import pendulum
import requests


@dag(
   'star_wars_dag_TASKFLOWAPI',
   start_date = pendulum.datetime(2023,3,1),
   schedule = None,
   catchup = False
)
@task
def _transform():

	resp = requests.get(f'https://swapi.dev/api/people/1').json()
	print(resp)
	my_character = {}
	my_character["height"] = int(resp["height"]) - 20
	my_character["mass"] = int(resp["mass"]) - 13
	my_character["hair_color"] = "black" if resp["hair_color"] == "blond" else "blond"
	my_character["eye_color"] = "hazel" if resp["eye_color"] == "blue" else "blue"
	my_character["gender"] = "female" if resp["gender"] == "male" else "female"
	return my_character


@task
def _load(character_info: str):
	print(character_info)


_load(_transform())
