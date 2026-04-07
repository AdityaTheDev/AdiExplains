import time

def task(task_id):
    print(f"Task {task_id} started")
    time.sleep(2)
    print(f"Task {task_id} completed")


start=time.time()
task(1)
task(2)
end=time.time()
print(f"Total time taken: {end-start} seconds")