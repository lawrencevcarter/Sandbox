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

    def test_nm_to_ddeg_pos(self)
        ddeg = nm_to_ddeg(500)
        self.AssertEqual(ddeg, 0.1453)

    def test_nm_to_ddeg_neg(self)
        ddeg = nm_to_ddeg(-767)
        self.AssertEqual(ddeg, -0.223)

    def test_ddeg_to_dms_pos(self):
        dms = gps.ddeg_to_dms(45.333)
        self.AssertEqual(dms[0], 45)
        self.AssertEqual(dms[0], 19)
        self.AssertEqual(dms[0], 58.8)

    def test_ddeg_to_dms_neg(self):
        dms = gps.ddeg_to_dms(-210.5)
        self.AssertEqual(dms[0], 210)
        self.AssertEqual(dms[0], 30)
        self.AssertEqual(dms[0], 0)

    def test_dms_to_ddeg_pos(self):
        ddeg = ddeg_to_dms(30, 2, 9)
        self.AssertEqual(ddeg, 30.03583)

    def test_dms_to_ddeg_neg(self):
        ddeg = ddeg_to_dms(-359, 1, 5)
        self.AssertEqual(ddeg, -359.0181)

    def test_latlon_to_dms_invalid(self):
        [lat, lon] = latlon_to_ddeg([-50, 185])
        self.AssertEqual(lat[0], None)
        self.AssertEqual(lat[1], None)
        self.AssertEqual(lat[2], None)
        self.AssertEqual(lat[3], None)
        self.AssertEqual(lon[0], None)
        self.AssertEqual(lon[1], None)
        self.AssertEqual(lon[2], None)
        self.AssertEqual(lon[3], None)
 
    def test_latlon_to_dms_lat_pos(self):
        [lat, lon] = latlon_to_ddeg([45.6, 120.333])
        self.AssertEqual(lat[0], 45)
        self.AssertEqual(lat[1], 36)
        self.AssertEqual(lat[2], 0)
        self.AssertEqual(lat[3], 'N')
        self.AssertEqual(lon[0], 120)
        self.AssertEqual(lon[1], 19)
        self.AssertEqual(lon[2], 58.7994)
        self.AssertEqual(lon[3], 'E')
 
    def test_latlon_to_dms_lat_neg(self):
        [lat, lon] = latlon_to_ddeg([-45.755, 120.333])
        self.AssertEqual(lat[0], 45)
        self.AssertEqual(lat[1], 45)
        self.AssertEqual(lat[2], 18)
        self.AssertEqual(lat[3], 'S')
        self.AssertEqual(lon[0], 120)
        self.AssertEqual(lon[1], 19)
        self.AssertEqual(lon[2], 58.7994)
        self.AssertEqual(lon[3], 'E')
  
    def test_latlon_to_dms_lon_pos(self):
        [lat, lon] = latlon_to_ddeg([60.5, 19.25])
        self.AssertEqual(lat[0], 60)
        self.AssertEqual(lat[1], 30)
        self.AssertEqual(lat[2], 0)
        self.AssertEqual(lat[3], 'N')
        self.AssertEqual(lon[0], 19)
        self.AssertEqual(lon[1], 15)
        self.AssertEqual(lon[2], 0)
        self.AssertEqual(lon[3], 'E')
 
    def test_latlon_to_dms_lon_neg(self):
        [lat, lon] = latlon_to_ddeg([60.45, -120.9])
        self.AssertEqual(lat[0], 60)
        self.AssertEqual(lat[1], 27)
        self.AssertEqual(lat[2], 0)
        self.AssertEqual(lat[3], 'N')
        self.AssertEqual(lon[0], 120)
        self.AssertEqual(lon[1], 54)
        self.AssertEqual(lon[2], 0)
        self.AssertEqual(lon[3], 'W')       self.AssertEqual(lon[3], None)
