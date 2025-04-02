#  Luhn Algorithm Credit Card Validator

This is a simple Python implementation of the Luhn Algorithm, commonly used to validate credit card numbers. The algorithm checks whether a given number passes a checksum formula, identifying typos and invalid card numbers.

---

##  What is the Luhn Algorithm?

The Luhn Algorithm (also known as the "modulus 10" or "mod 10" algorithm) is used to validate identification numbers such as:

- Credit card numbers  
- IMEI numbers  
- Social Insurance Numbers (in some countries)

---

##  How It Works:

1. Start from the **rightmost digit** and move left.  
2. **Double every second digit**. If the result is greater than 9, add the digits together (e.g. `14 → 1 + 4 = 5`).  
3. Sum all the resulting digits.  
4. If the **total modulo 10** is zero, the number is **valid**.
