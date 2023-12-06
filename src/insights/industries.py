from src.insights.jobs import ProcessJobs
from typing import List


class ProcessIndustries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_unique_industries(self) -> List[str]:
        unique_industrie = set()
        for job in self.jobs_list:
            industry = job.get("industry")
            if industry:
                unique_industrie.add(industry)
        return list(unique_industrie)
