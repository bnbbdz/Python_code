from dagster import repository

from first_project.jobs.say_hello import say_hello_job
from first_project.schedules.my_hourly_schedule import my_hourly_schedule
from first_project.sensors.my_sensor import my_sensor


@repository
def first_project():
    """
    The repository definition for this first_project Dagster repository.

    For hints on building your Dagster repository, see our documentation overview on Repositories:
    https://docs.dagster.io/overview/repositories-workspaces/repositories
    """
    jobs = [say_hello_job]
    schedules = [my_hourly_schedule]
    sensors = [my_sensor]

    return jobs + schedules + sensors
