import sublime
import sublime_plugin


class Extract_methodCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        view = self.view
        window = view.window()
        sel = view.sel()

        if (len(sel) != 1):
            sublime.message_dialog("[Refactr] Multiline is not supported yet.")
            return

        new_method_name = "New method name:"
        window.show_input_panel(new_method_name, "", self.on_done, None, None)

    def on_done(self, user_input):
        if (len(user_input) <= 0):
            sublime.message_dialog("[Refactr] Please enter a method name.")
            return

        view = self.view
        window = view.window()

        line_nums = self.get_line_numbers()

        startLine = (line_nums[0] + 1)
        startLineStr = str(startLine)

        endLine = (startLine + len(line_nums) - 1)
        endLineStr = str(endLine)

        refactor_command = self.build_refactor_command(
            startLineStr, endLineStr, user_input)

        if (refactor_command == ''):
            return

        self.run_shell_command(window, refactor_command)
        sublime.set_timeout(self.reload_all_views, 500)

    def build_refactor_command(self, startLine, endLine, newMethod):
        view = self.view
        userSettings = view.settings()
        refactoring_browser = userSettings.get('refactor_browser_file')

        if (refactoring_browser is None):
            settings = sublime.load_settings("Default.sublime-settings")
            refactoring_browser = settings.get('refactor_browser_file')

            if (refactoring_browser is None):
                sublime.message_dialog("[Refactr] Please review your Refactr-Settings.")
                return

        begin = "php "+refactoring_browser+" extract-method"
        #print(refactoring_browser)

        file_name = str(view.file_name())

        lines = startLine + "-" + endLine
        applyPatch = "|patch -p1"

        return ' '.join([begin, file_name, lines, newMethod, applyPatch])

    def run_shell_command(self, window, cmd):
        window.run_command('exec', {'cmd': cmd, 'shell': True})

    def get_line_numbers(self):
        view = self.view
        sel = view.sel()
        return [view.rowcol(line.a)[0] for line in view.lines(sel[0])]

    def reload_all_views(self):
        view = self.view
        window = view.window()
        current_view = window.active_view()
        gr_number = window.num_groups()

        for i in range(0, gr_number):
            window.focus_group(i)
            views_in_i = window.views_in_group(i)
            for inner_view in views_in_i:
                window.focus_view(inner_view)

        window.focus_view(current_view)
