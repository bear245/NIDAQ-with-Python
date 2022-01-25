class Module:
    all = []
    def __init__(self, task_configuration):
        # Run valdation to the received arguments
        assert len(task_configuration['dev_name']) > 0, f"Device name couldn't be empty"
        assert len(task_configuration['channel']) > 0, f"Channel couldn't be empty"

        # Assign to self object
        self.dev_name = task_configuration['dev_name']
        self.channel = task_configuration['channel']

        # Actions to execute
        Module.all.append(self)

    def __repr__(self):
        return f"Module('{self.dev_name} : {self.channel}')"

    def Open(self):
        pass

    def Close(self):
        pass

class AnalogReader(Module):
    def __init__(self, task_configuration):
        # Assign to self object
        super().__init__(task_configuration)
        self.samples_per_read = task_configuration['samples_per_read']
        self.min_voltage = task_configuration['min_voltage']
        self.max_voltage = task_configuration['max_voltage']
        self.sample_rate = task_configuration['sample_rate']
        self.sample_clock_source = task_configuration['sample_clock_source']
        self.terminal_configuration = task_configuration['terminal_configuration']



if __name__ == "__main__":
    # Testing purposes
    Module1 = Module(task_configuration={'dev_name':'6255', 'channel':'ai0'})
    Module2 = Module(task_configuration={'dev_name':'6739', 'channel':'ai11'})
    print(Module1)
    print(Module.all)
