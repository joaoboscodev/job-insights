import csv
from typing import List, Dict


class ProcessJobs:
    def __init__(self) -> None:
        self.jobs_list = list()

    def read(self, path: str) -> List[Dict]:
        with open(path, newline='', encoding='utf-8') as csvfile:
            reader = csv.DictReader(csvfile)
            self.jobs_list = list(reader)
        return self.jobs_list

    def get_unique_job_types(self) -> List[str]:
        unique_job_types = set()
        for job in self.jobs_list:
            unique_job_types.add(job["job_type"])
        return list(unique_job_types)

    def filter_by_multiple_criteria(self, jobs, filter_criteria) -> List[dict]:
        if not isinstance(filter_criteria, dict):
            raise TypeError("Filtro precisa ser um dicionário")

        filtered_jobs = []

        for job in jobs:
            if all(
                job.get(key) == value
                for key, value in filter_criteria.items()
            ):
                filtered_jobs.append(job)

        return filtered_jobs
