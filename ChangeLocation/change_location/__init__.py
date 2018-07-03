from fman import DirectoryPaneCommand
from fman.url import as_human_readable

class ChangeLocation(DirectoryPaneCommand):
	def __call__(self):
		location = as_human_readable(self.pane.get_path())
		self.pane.run_command('go_to', args={'query': location})