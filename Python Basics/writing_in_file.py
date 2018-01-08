import tkintr.filedialog
tkinter.filedialog.askopenfilename()
from_filename = tkinter.filedialog.askopenfilename()

to_filename = tkinter.filedialog.asksaveasfilename()
to_filename

from_file = open(from_filename, 'r')
contents = from_file.read()
from_file.close()
contents

to_file = open(to_filename, 'w')
to_file.write("Copy\n")
to_file.write(contents)
to_file.close()
