
from notebook import Note,Notebook

n = Notebook()
n.new_note("hello world")
n.new_note("hello python")
print(n.notes[0].memo)
print(n.notes[0].id)