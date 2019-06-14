#!python3
import code
import sys

class LoggingRepl(code.InteractiveConsole):
    def __init__(self, fname, tab_chars='    ', *args, **kwargs):
        self.fname = fname
        self.log_file = None
        self.tab_chars = tab_chars
        super(LoggingRepl, self).__init__(locals=globals(), *args, **kwargs)
        
    def __enter__(self):
        self.log_file = open(self.fname, 'a+t')
        return self
        
    def __exit__(self, *args, **kwargs):
        self.log_file.write('#ending session\n\n')
        self.log_file.__exit__(*args, **kwargs)

    def raw_input(self, prompt=''):
        s = code.InteractiveConsole.raw_input(self, prompt=prompt)
        self.log_file.write(s.replace('\t', self.tab_chars) + '\n')
        return s

def interact(fname):
    #code.InteractiveConsole(locals=globals()).interact()
    with open(fname, 'a+t') as log:
        def read_and_log(x):
            print(x, end='')
            s = sys.stdin.readline()
            log.write(s)
            return s
        code.interact(local=globals(), readfunc=read_and_log)

def interact2(fname):
    #code.InteractiveConsole(locals=globals()).interact()
    with LoggingRepl(fname) as repl:
        repl.interact()

if __name__ == "__main__":
    interact2('py_history.log')
