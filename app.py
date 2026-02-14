def rail_fence_encrypt(text, rails):
    text = text.replace(" ", "")
    fence = [[] for _ in range(rails)]

    row = 0
    direction = 1

    for char in text:
        fence[row].append(char)
        row += direction

        if row == 0 or row == rails - 1:
            direction *= -1

    return "".join("".join(r) for r in fence)


def rail_fence_decrypt(cipher, rails):
    pattern = [[] for _ in range(rails)]
    row = 0
    direction = 1

    # Marking positions
    for char in cipher:
        pattern[row].append("*")
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    # Filling characters
    index = 0
    for r in range(rails):
        for c in range(len(pattern[r])):
            pattern[r][c] = cipher[index]
            index += 1

    # Reading zigzag
    result = []
    row = 0
    direction = 1

    for _ in cipher:
        result.append(pattern[row].pop(0))
        row += direction
        if row == 0 or row == rails - 1:
            direction *= -1

    return "".join(result)


print("\n--- Rail Fence Cipher ---\n")

choice = input("Encrypt or Decrypt (E/D): ").upper()
message = input("Enter message: ")
rails = int(input("Enter number of rails: "))

if choice == "E":
    print("Encrypted message:", rail_fence_encrypt(message, rails))
elif choice == "D":
    print("Decrypted message:", rail_fence_decrypt(message, rails))
else:
    print("Invalid choice!")
