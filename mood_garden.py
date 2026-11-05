import random

plants = {
    "happy": [
        "      ☀️\n   \\  |  /\n    \\ | /\n     \\|/\n      🌱"
    ],
    "calm": [
        "       .\n      / \\\n     /   \\\n       |\n      🌿"
    ],
    "tired": [
        "      z Z\n     (   )\n      \\ /\n       |\n      🌱"
    ],
    "excited": [
        "    ✨  ✨\n  🌼  🌱  🌼\n       |"
    ],
}

print("Welcome to Mood Garden 🌷")
mood = input("How are you feeling today? ").strip().lower()

if mood in plants:
    print("\nYour garden says:\n")
    print(random.choice(plants[mood]))
else:
    print("\nI don't know that mood yet—but your garden is still growing 🌱")