#!/usr/bin/python3
if __name__ == "__main__":
    module_path = 'hidden_4.pyc'
    print_module_names(module_path)
     for name in sorted(names):
        if not name.startswith("__"):
            print(name)
