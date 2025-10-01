def nim_game(heaps): #ChatGPT
    """
    Normal Play Nim game
    heaps: list of integers representing heap sizes
    """
    player = 1
    while True:
        print("\nCurrent heaps:", heaps)
        if all(h == 0 for h in heaps):
            print(f"Player {3 - player} wins!")  # the other player wins
            break
        
        # Nim sum
        nim_sum = 0
        for i in range(len(heaps)):
            nim_sum ^= heaps[i]
            print(f"heap{i:<15}: {bin(heaps[i])[2:]:>20}")
        print(f"Decimal Nim-sum: {nim_sum},\nBinary Nim-sum: {bin(nim_sum)[2:]:>25}")

        # Player move
        print(f"Player {player}'s turn")
        heap_index = int(input("Choose heap index (0-based): "))
        remove = int(input("How many objects to remove: "))

        if heap_index < 0 or heap_index >= len(heaps) or remove <= 0 or remove > heaps[heap_index]:
            print("Invalid move! Try again.")
            continue

        heaps[heap_index] -= remove
        player = 3 - player  # switch player


# Example: 3 heaps of sizes 3, 4, 5
nim_game([3,4,5])
nim_game([332, 441, 555])
