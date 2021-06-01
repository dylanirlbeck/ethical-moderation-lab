import jupytext

src = jupytext.read('notebook-prototype.py')
jupytext.write(src, 'lab-output.ipynb', fmt='percent')
