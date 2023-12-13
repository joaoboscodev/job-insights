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
        salaries = []
        for job in self.jobs_list:
            min_salary = job.get("min_salary")
            if min_salary.isdigit():
                salaries.append(int(min_salary))

        min_salary = min(salaries)
        return min_salary

    def matches_salary_range(self, job: Dict, salary: Union[int, str]) -> bool:
        min_salary = job.get('min_salary')
        max_salary = job.get('max_salary')

        if not (
            isinstance(salary, (int, float)) or
            (isinstance(salary, str) and salary.isdigit())
        ):
            raise ValueError("Salary não numérico")
        if max_salary is None or min_salary is None:
            raise ValueError("Valor nulo")
        if not (str(max_salary).isdigit() and str(min_salary).isdigit()):
            raise ValueError("Valores não numéricos")
        if int(min_salary) > int(max_salary):
            raise ValueError("min_salary > max_salary")

        return int(min_salary) <= int(salary) <= int(max_salary)

    def filter_by_salary_range(
        self, jobs: List[dict], salary: Union[str, int]
    ) -> List[Dict]:
        filtered_data = []

        for job in jobs:
            min_salary = job.get('min_salary')
            max_salary = job.get('max_salary')

            if (
                isinstance(salary, (int, float)) or
                (isinstance(salary, str) and salary.isdigit())
            ) and max_salary is not None and min_salary is not None and (
                str(max_salary).isdigit() and str(min_salary).isdigit()
            ) and int(min_salary) <= int(max_salary):

                if int(min_salary) <= int(salary) <= int(max_salary):
                    filtered_data.append(job)

        return filtered_data
