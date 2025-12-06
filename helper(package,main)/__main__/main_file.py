class Course:
    def __init__(self, name, duration):
        self.name=name
        self.duration = duration

def main():
    python = Course("Python", "3 months")
    ml = Course("Machine learning", "4 months")
    print(python.name)
    print(ml.name)


# this make sure to execute __main__ only if the file is executed directly
if __name__ == "__main__":
    main()