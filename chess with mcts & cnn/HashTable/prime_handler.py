from random import randint


class PrimeHandler:
    @staticmethod
    def calculate_modular_exponent(base: int, exponent: int, modulus: int) -> int:
       
        result = 1  # Initialize result
        base = base % modulus  # Update x if it is more than or equal to p
        while exponent > 0:
            if exponent & 1:
                result = (result * base) % modulus
            exponent = exponent >> 1  # Equivalent to exponent = exponent / 2
            base = (base * base) % modulus
        return result

    def perform_miller_rabin_test(self, reduced_n_minus_one: int, number: int) -> bool:
       
        witness = 2 + randint(1, number - 4)  # A random number in [2, number-2]
        x = self.calculate_modular_exponent(witness, reduced_n_minus_one, number)
        if x == 1 or x == number - 1:
            return True
        while reduced_n_minus_one != number - 1:
            x = (x * x) % number
            reduced_n_minus_one *= 2
            if x == 1:
                return False
            if x == number - 1:
                return True
        return False

    def is_prime(self, number: int, iterations: int = 10) -> bool:
       
        if number <= 1:
            return False
        if number <= 3:
            return True
        if number % 2 == 0:
            return False

        reduced_n_minus_one = number - 1
        while reduced_n_minus_one % 2 == 0:
            reduced_n_minus_one //= 2

        for _ in range(iterations):
            if not self.perform_miller_rabin_test(reduced_n_minus_one, number):
                return False
        return True

    def generate_prime(self, starting_point: int):
        if starting_point % 2 == 0:
            starting_point += 1

        while True:
            if self.is_prime(starting_point):
                return starting_point
            starting_point += 2