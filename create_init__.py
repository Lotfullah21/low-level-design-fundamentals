import os
for root, dirs, files in os.walk("."):
    for d in dirs:
        path = os.path.join(root, d, "__init__.py")
        if not os.path.exists(path):
            with open(path, "w") as f:
                pass  # create empty file
            print("Created:", path)
