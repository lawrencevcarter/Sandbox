import unittest
import gps

class TestGPS(unittest.TestCase):

    def test_km_to_nm_pos(self):
        nm = gps.km_to_nm(33)
        self.AssertEqual(nm, 17.8186)
 
    def test_km_to_nm_neg(self):
        nm = gps.km_to_nm(-18.7)
        self.AssertEqual(nm, -10.09719)

    def test_nm_to_km_pos(self):
        km = gps.nm_to_km(56)
        self.AssertEqual(km, 103.712)

    def test_nm_to_km_neg(self):
        km = gps.nm_to_km(-12)
        self.AssertEqual(km,- 22.224)

