import numpy as np
import common

DIMS = (11, 11)
eta_max = 0.02  # the maximum value of eta_0 and eta_d

#generating seeds
np.random.seed(1234)
seeds = np.random.choice(1000000, DIMS, replace=False)
print(seeds)

for i,lambda_ in enumerate(np.logspace(-1,1,DIMS[0])):
    for j, T_bar in enumerate(np.logspace(-1,1,DIMS[1])):
        #calculating N
        N_min = int(1/(eta_max * T_bar * min(1, lambda_))) + 1  # the min value N can take

        with open(f"Sims/Serie/{i}_{j}.ini", "w") as out:
            out.write(
                common.BASE_SETUP.format(
                    T_bar=T_bar,
                    lambda_=lambda_,
                    start_path="RIGHT",  # is simmetrized later
                    SEED=seeds[i, j],
                    N=max(2,N_min),  # the algorithm work only for N > 2
                    repeats=100,
                    delta=0.08,
                    samples=50,
                    samples_spacing=1000
                )
            )
