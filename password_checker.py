import string

password = input("Enter your password: ")

# Length check
if len(password) < 8:
    print("❌ Too short")
else:
    print("✅ Good length")

# Uppercase check
if any(char.isupper() for char in password):
    print("✅ Has uppercase")
else:
    print("❌ No uppercase")

# Number check
if any(char.isdigit() for char in password):
    print("✅ Has number")
else:
    print("❌ No number")

# Special character check
if any(char in string.punctuation for char in password):
    print("✅ Has special character")
else:
    print("❌ No special character")
    score = 0

import string

password = input("Enter your password: ")

# Length check
if len(password) >= 8:
    print("✅ Good length")
else:
    print("❌ Too short")

# Uppercase check
if any(char.isupper() for char in password):
    print("✅ Has uppercase")
else:
    print("❌ No uppercase")

# Number check
if any(char.isdigit() for char in password):
    print("✅ Has number")
else:
    print("❌ No number")

# Special character check
if any(char in string.punctuation for char in password):
    print("✅ Has special character")
else:
    print("❌ No special character")

# ⭐ IMPORTANT: initialize score
score = 0

# Scoring system
if len(password) >= 8:
    score += 1
if any(char.isupper() for char in password):
    score += 1
if any(char.isdigit() for char in password):
    score += 1
if any(char in string.punctuation for char in password):
    score += 1

# Result
print("\nPassword Strength:", end=" ")

if score <= 2:
    print("Weak ❌")
elif score == 3:
    print("Medium ⚠️")
else:
    print("Strong 💪")