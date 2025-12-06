# even if we do not use get_info, the whole file1 codes will be executed
from file1 import get_info

print(f"__name__ in file2: {__name__}") 
print("From File 1")
get_info("hello")