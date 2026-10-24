"""Independent finite-dimensional test of the standard inverse-spectral energy bound.
Run: python -m unittest discover -s tests -v
No string-theory theorem is claimed.
"""
import unittest
from fractions import Fraction


def inverse_energy(eigenvalues, amplitudes):
    assert len(eigenvalues) == len(amplitudes) and len(eigenvalues) > 0
    assert all(x > 0 for x in eigenvalues)
    return sum((Fraction(a) ** 2 / Fraction(l) for l, a in zip(eigenvalues, amplitudes)), Fraction(0))

class SpectralEnergyTests(unittest.TestCase):
    def test_bound_and_equality(self):
        lam = [1, 4, 9]
        for amps in [[0, 0, 0], [1, 0, 0], [1, 2, 3], [0, 3, 0]]:
            energy = inverse_energy(lam, amps)
            bound = sum((Fraction(a)**2 for a in amps), Fraction(0)) / min(lam)
            self.assertLessEqual(energy, bound)
        self.assertEqual(inverse_energy(lam, [2, 0, 0]), Fraction(4))
    def test_larger_eigenvalue_lowers_energy(self):
        self.assertEqual(inverse_energy([4], [2]), Fraction(1))
        self.assertEqual(inverse_energy([16], [2]), Fraction(1, 4))

if __name__ == '__main__': unittest.main()
