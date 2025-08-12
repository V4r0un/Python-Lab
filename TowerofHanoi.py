def towerOfHanoi(num, source, helper, destination):
    if num == 1:
        print(f"Move from {source} to {destination}")
        return
    towerOfHanoi(num-1, source, helper, destination)
    print(f"Move disk {num} from {source} to {destination}")
    towerOfHanoi(num-1, source, helper, destination)

n = 3
towerOfHanoi(n, "A", 'B', 'C')