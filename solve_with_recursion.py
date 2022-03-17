def solve_tower_of_hanoi_with_recursion(disks, source, destination, auxiliary):
    # Case: No disk
    if disks <= 0:
        pass

    # Case: 1 disk
    elif disks == 1:
        print(f"Move disk {disks} from {source} to {destination}")

    # Case: n disks
    else:
        solve_tower_of_hanoi_with_recursion(disks=disks-1, source=source, destination=auxiliary, auxiliary=destination)
        print(f"Move disk {disks} from {source} to {destination}")
        solve_tower_of_hanoi_with_recursion(disks=disks-1, source=auxiliary, destination=destination, auxiliary=source)


solve_tower_of_hanoi_with_recursion(disks=10, source="Rod A", destination="Rod B", auxiliary="Rod C")
