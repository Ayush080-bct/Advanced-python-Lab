import Module
Module.greet(Name="World")
# (labpython) ayush@Ayush:~/LabPython$ python3 Import.py
# hello  Ayush
# hello  World As you can see when the function inside a module is not called inside a mif __name__="__main__",
#  it will get executed when call in another file
# python import.py
# │
# ├── import.py
# │     __name__ = "__main__"
# │
# └── module.py
#       __name__ = "module"


# so purpose is just that if i write a script like resuable function and
#  i want to check in that script if this function run or not then we use if __name__=="__main__"