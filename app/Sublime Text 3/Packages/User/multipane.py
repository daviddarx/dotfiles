import sublime, sublime_plugin

# sublime.log_commands(True)

class XpaneCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        self.view.insert(edit, 0, "Hello, World!")
        self.view.window().views()

