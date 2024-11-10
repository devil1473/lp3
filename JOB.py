class Job:
    def _init_(self, job_id, deadline, profit):
        self.job_id = job_id
        self.deadline = deadline
        self.profit = profit

def job_sequencing_with_deadlines(jobs):
    jobs.sort(key=lambda x: x.profit, reverse=True)

    max_deadline = max(job.deadline for job in jobs)
    time_slots = [-1] * (max_deadline + 1)

    total_profit = 0
    job_sequence = []

    for job in jobs:
        for t in range(min(max_deadline, job.deadline), 0, -1):
            if time_slots[t] == -1:
                time_slots[t] = job.job_id
                total_profit += job.profit
                job_sequence.append(job.job_id)
                break

    return job_sequence, total_profit

def main():
    n = int(input("Enter the number of jobs: "))

    jobs = []
    for i in range(n):
        job_id = input(f"Enter Job ID for job {i + 1}: ")
        deadline = int(input(f"Enter deadline for job {i + 1}: "))
        profit = int(input(f"Enter profit for job {i + 1}: "))
        jobs.append(Job(job_id, deadline, profit))

    job_sequence, total_profit = job_sequencing_with_deadlines(jobs)
    print(f"Job sequence: {job_sequence}")
    print(f"Total profit: {total_profit}")

if _name_ == "_main_":
    main()
