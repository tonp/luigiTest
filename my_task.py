import luigi

class Hello(luigi.Task): 

	def requires(self): 
		return None

	def run(self): 

		with self.output().open('w') as file: 
			file.write('Luigiii\n')


	def output(self): 
		return luigi.LocalTarget('helloworld.txt')

if __name__ == '__main__':

    # since we are setting MySecondTask to be the main task,
    # it will check for the requirements first, then run
    luigi.run(["--local-scheduler"], main_task_cls=Hello)