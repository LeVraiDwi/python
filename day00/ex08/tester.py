from Loading import ft_tqdm
from time import sleep
from tqdm import tqdm   


def main():
    for i in ft_tqdm(range(int(0))):
        sleep(0.00001)
    for i in tqdm(range(int(9223372036854775808))):
        sleep(0.00001)


if __name__ == "__main__":
    main()
