#  my_module/main.py

import first
import second

print("=== Math Functions ===")
print("5 + 3 =", first.add(5, 3))
print("10 - 4 =", first.subtract(10, 4))
print("6 * 7 =", first.multiply(6, 7))

#  Lets us the function in the second.py file
print("\n=== Strint Function ===")
print(second.greet("Ridwan"))
print("reverse of 'python' =", second.reverse_string("Python"))
print("character count in sentence =", second.count_words("Python modules are powerful"))
print("Word count in sentence =", second.count_words("Pyhton modules are powerful"))
