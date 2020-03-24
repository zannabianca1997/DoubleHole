import os
import common

for file, data in common.find_all("Sims"):
    print(f"Found setup file {file}")
    if data is not None:
        if not common.is_modified(file, data):  # simulation already done
            print(f"Found up-to-date data file {data}")
            continue
        print(f"Found old data file {data}")
    else:
        print("No data file found")
        data = os.path.splitext(file)[0] + common.DATA_EXT
    print("Running...")
    common.do_simulation(file, data)