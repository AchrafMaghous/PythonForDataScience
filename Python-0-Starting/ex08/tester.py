from time import sleep
from tqdm import tqdm
from Loading import ft_tqdm

for elem in ft_tqdm(range(0, 999, 9)):
    sleep(0.005)
print()
for elem in tqdm(range(0, 999, 9)):
    sleep(0.005)
print()
