
def start(name):
    print(f"Starting, {name}")

def watch_videos(name):
    print(f"Watching videos of {name} course")

def finish_course(name, duration):
    print(f"Finished {name} course after {duration}")

name = input("Enter the course: ") 

duration = input("Enter the duration: ") + " weeks"

start(name)
watch_videos(name)
finish_course(name, duration)
