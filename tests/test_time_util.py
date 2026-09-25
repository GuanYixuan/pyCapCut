import unittest

from pycapcut import SEC, Timerange, trange, trange_seconds


class TrangeSecondsTest(unittest.TestCase):
    def test_end_and_duration_match_on_fractional_boundaries(self):
        bar = 60 / 136 * 4
        by_end = trange_seconds(4 * bar, end=5 * bar)
        by_duration = trange_seconds(4 * bar, duration=bar)
        following = trange_seconds(5 * bar, end=6 * bar)

        self.assertEqual(by_end, by_duration)
        self.assertEqual(by_end, Timerange(7_058_824, 1_764_705))
        self.assertEqual(by_end.end, following.start)
        self.assertFalse(by_end.overlaps(following))

    def test_units_and_existing_trange_semantics(self):
        self.assertEqual(trange_seconds(-1, end=0), Timerange(-SEC, SEC))
        self.assertEqual(trange_seconds(1, duration=0), Timerange(SEC, 0))
        self.assertEqual(trange("1s", "2s"), Timerange(SEC, 2 * SEC))

    def test_invalid_inputs(self):
        for kwargs in ({}, {"end": 1, "duration": 1}, {"end": 0}):
            with self.subTest(kwargs=kwargs):
                with self.assertRaises(ValueError):
                    trange_seconds(1, **kwargs)
        for start, kwargs in ((True, {"end": 1}), ("1s", {"end": 2})):
            with self.subTest(start=start):
                with self.assertRaises(TypeError):
                    trange_seconds(start, **kwargs)
        for start, kwargs in ((float("nan"), {"end": 1}), (0, {"duration": float("inf")}),
                              (1e307, {"duration": 0})):
            with self.subTest(start=start, kwargs=kwargs):
                with self.assertRaises(ValueError):
                    trange_seconds(start, **kwargs)


if __name__ == "__main__":
    unittest.main()
