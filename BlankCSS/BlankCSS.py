import sublime, sublime_plugin
import re

class BlankcssCommand(sublime_plugin.TextCommand):
	def run(self, edit):
		for region in self.view.sel():
			if not region.empty():
				s = self.view.substr(region)
				s = re.findall(r'class="[^"]*"|id="[^"]*"', s)
				a = []
				for x in s:
					if not " " in x:
						if not x in a:
							a.append(x)
					else:
						x = re.sub(r' +', '" class="', x)
						x = x.split(' ')
						for y in x:
							if not " " in y:
								if not y in a:
									a.append(y)
				s = ""
				for x in a:
					x = x.replace(' ', '"class="').replace('class="', ".").replace('id="', "#").replace("\"", " {\n\t\n}\n\n")
					s += x
				s = s[:-2]
				self.view.replace(edit, region, s)