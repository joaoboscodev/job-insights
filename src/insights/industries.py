from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industrie = set()
        for job in self.jobs_list:
            unique_industrie.add(job["industry"])
        return list(unique_industrie)
