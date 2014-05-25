import sublime, sublime_plugin, re

class SpecifyCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        for region in self.view.sel():
            if not region.empty():
                    # init the vars
                    dependencies = []
                    specs = []
                    # get the selected text
                    s = self.view.substr(region)
                    # split the text in lines
                    lines = s.splitlines()
                    newLines = ''
                    for line in lines:
                        line = line.strip() 
                        # if it is a dependency statement
                        if re.search("^given\\s+.*", line, re.I):
                            # store the dependency
                            dependencies.append(re.sub("^given\\s+?(.*?)$", "\\1", line, re.I))
                            continue
                        # if it's not a spec line ignore and continue
                        if  not re.search("^[a-zA-Z0-9\\s]*?$", line):
                            continue;
                        # if here then it's a spec line
                        specs.append( re.sub("\\s+", "_", line))
                    # consume the spec lines and create pending specs
                    newLines = []
                    for spec in specs:
                        specLine = '\nfunction '
                        # function it_should_do_something
                        specLine += spec + '('
                        # add each dependency
                        specLine += ', '.join(dependencies);
                        specLine += ')\n{\n'
                        # add the pending statement
                        specLine += '}\n'
                        newLines.append(specLine)
                    # replace the lines
                    newLines = ''.join(newLines)
                    self.view.replace(edit, region, newLines)
                    # reindent output
                    self.view.run_command('reindent')
