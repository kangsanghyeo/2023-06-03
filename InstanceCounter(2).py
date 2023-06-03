class InstanceCounter:
    count = 0
    def __init__(self):
        InstanceCounter.count += 1


    @classmethod
    def print_instance_count(cls):
        print(cls.count)
