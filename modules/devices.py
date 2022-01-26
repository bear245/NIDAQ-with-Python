import numpy as np
import nidaqmx
from nidaqmx.constants import AcquisitionType
from nidaqmx.stream_readers import AnalogSingleChannelReader, AnalogMultiChannelReader
from nidaqmx.constants import TerminalConfiguration

class Module:
    all = []
    def __init__(self, task_configuration):
        # Run valdation to the received arguments
        assert len(task_configuration['dev_name']) > 0, f"Device name couldn't be empty"
        assert len(task_configuration['channels']) > 0, f"Channel couldn't be empty"

        # Assign to self object
        self.dev_name = task_configuration['dev_name']
        self.channels = task_configuration['channels']

        # Actions to execute
        Module.all.append(self)

    def __repr__(self):
        return f"Module('{self.dev_name} : {self.channels}')"


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


    def run(self):
        """
        Read from the DAQmx task which is acquiring at sample_rate.Each loop iteration acquires samples_per_read and
        adds the samples to both the io and ui queues for logging and display. The default timeout is 10 seconds.
        """
        with nidaqmx.Task() as self.reader_task:
            # Create a temp dict to pass multiple arguments more easily
            chan_args = {
                "min_val": self.min_voltage,
                "max_val": self.max_voltage,
                "terminal_config": self.terminal_configuration
            }
            # Build the proper channel name using the device + channels
            channel_names = self.dev_name + "/" + self.channels
            print(channel_names)
            # Add the DAQmx channel to the task
            self.reader_task.ai_channels.add_ai_voltage_chan(channel_names, **chan_args)

            # Configure the timing of the task. Notice we do not specify the samples per channel. As this program only
            # supports continuous acquisitions, samples per channel simply specifies the DAQmx PC buffer size which
            # is usually ignored anyway as the default is sufficient.
            # For more info, see: https://knowledge.ni.com/KnowledgeArticleDetails?id=kA03q000000YHpECAW&l=en-US
            self.reader_task.timing.cfg_samp_clk_timing(rate=self.sample_rate,
                                                        sample_mode=AcquisitionType.FINITE,
                                                        samps_per_chan=self.samples_per_read)
            self.input_data = np.empty(shape=(self.samples_per_read, self.reader_task.number_of_channels))
            print(self.reader_task.number_of_channels)

            # Run the task if it was created successfully
            self.reader_task.start()
            self.reader = AnalogMultiChannelReader(self.reader_task.in_stream)

            while self.reader_task.is_task_done():
                # Read from the DAQmx buffer the required number of samples on the configured channel, waiting,
                # if needed, up to timeout for the requested number_of_samples_per_channel becomes available
                self.reader.read_many_sample(data=self.input_data,
                                             number_of_samples_per_channel=self.samples_per_read,
                                             timeout=10.0)
            print(self.input_data)
            self.reader_task.stop()


if __name__ == "__main__":
    # Testing purposes
    Module1 = AnalogReader(task_configuration={'dev_name':'6255',
                                               'channels':'ai0:3',
                                               'max_voltage':10.0,
                                               'min_voltage':0.0,
                                               'sample_rate': 10,
                                               'sample_clock_source':'OnBoardClock',
                                               'samples_per_read':50,
                                               'terminal_configuration':TerminalConfiguration.DEFAULT
                                               })
    Module1.run()