"""__init__.py under a package
all other file is a sub module of 'mymodule' in this case
"""
#if __all__ var exists in this file, only the module in the list can be use
# for example:
#from mymodule.bars import simplebar

#__all__=[simplebar,]