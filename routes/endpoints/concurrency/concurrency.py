from fastapi import APIRouter, Request, Response, Depends
import concurrent.futures
import time


concurrency_api = APIRouter()

# Function to simulate a task that takes some time to complete
def task(num):
    # print(f"Task {num} started")
    time.sleep(3)  # Simulate some work
    # print(f"Task {num} completed")
    return f"Result of Task {num}"


# Create a ThreadPoolExecutor with maximum 3 worker threads
@concurrency_api.get("/testConcurrent", tags=["Sample"])
async def getAllUsers():
    with concurrent.futures.ThreadPoolExecutor(max_workers=2) as executor:
        # Submit tasks to the executor
        tasks = [executor.submit(task, i) for i in range(1, 6)]

        # Check if all tasks are finished
        all_tasks_finished = False
        while(not all_tasks_finished):
            time.sleep(3)  # Simulate some work
            all_tasks_finished = all(task.done() for task in tasks)
            if all_tasks_finished:
                print("All tasks finished")
                # False
            else:
                print("Some tasks are still running")
                # True

        # Wait for the tasks to complete and get the results
        for future in concurrent.futures.as_completed(tasks):
            result = future.result()
            # print(future.result()
            print(result)