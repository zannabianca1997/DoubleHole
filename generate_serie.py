s = """[Physical]
t_bar = 0.5
lambda = 2.1
start_path = CENTRE

[Simulation]
seed = {seed}
n = 100
repeats = 10
delta = 0.08
samples = 500000"""
for i in range(20):
    with open(f"Sims\Serie\Serie{i}.ini","w") as out:
        out.write(s.format(seed=i))
