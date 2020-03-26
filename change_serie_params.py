import common

DRY_RUN = False  # if this script will actually change anything

new_repeats = 10

if __name__ == "__main__":

    for file, data in common.find_all("Sims/Serie/"):
        assert data is not None
        setup, _ = common.load(file, data)
        print(f"Simulation {file}")
        repeats = setup.getint("Simulation", "repeats")
        print(f"Correcting old N {repeats} with new {new_repeats}")
        if not DRY_RUN:
            setup.set("Simulation", "repeats", str(new_repeats))  # changing data in memory...
            with open(file, "w") as out:
                setup.write(out)