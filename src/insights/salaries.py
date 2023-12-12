from typing import Union, List, Dict
from src.insights.jobs import ProcessJobs


class ProcessSalaries(ProcessJobs):
    def __init__(self):
        super().__init__()

    def get_max_salary(self):
        salaries = []
        for job in self.jobs_list:
            max_salary = job.get("max_salary")
            if max_salary.isdigit():
                salaries.append(int(max_salary))

        max_salary = max(salaries)
        return max_salary

    def get_min_salary(self) -> int:
        pass

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        pass

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        pass
