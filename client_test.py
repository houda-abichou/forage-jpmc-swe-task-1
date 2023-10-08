import unittest
from client3 import getDataPoint, getRatio


class ClientTest(unittest.TestCase):
  def test_getDataPoint_calculatePrice(self):
    quotes = [
      {'top_ask': {'price': 121.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ("ABC", 120.48, 121.2, 120.84))
    self.assertEqual(getDataPoint(quotes[1]), ("DEF", 117.87, 121.68, 119.775))

  def test_getDataPoint_calculatePriceBidGreaterThanAsk(self):
    quotes = [
      {'top_ask': {'price': 119.2, 'size': 36}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 120.48, 'size': 109}, 'id': '0.109974697771', 'stock': 'ABC'},
      {'top_ask': {'price': 121.68, 'size': 4}, 'timestamp': '2019-02-11 22:06:30.572453', 'top_bid': {'price': 117.87, 'size': 81}, 'id': '0.109974697771', 'stock': 'DEF'}
    ]
    """ ------------ Add the assertion below ------------ """
    self.assertEqual(getDataPoint(quotes[0]), ("ABC", 120.48, 119.2, 119.84))
    self.assertEqual(getDataPoint(quotes[1]), ("DEF", 117.87, 121.68, 119.775))

  def test_getRatio_calculatedRatio(self):
    price_a = 119.2
    price_b = 125
    self.assertEqual(getRatio(price_a, price_b), 0.9536)

  def test_getRatio_calculatedRatioWhenPriceBIsZero(self):
    price_a = 123
    price_b = 0
    self.assertEqual(getRatio(price_a, price_b), None)

  def test_getRatio_calculatedRatioWhenPriceAIsZero(self):
    price_a = 0
    price_b = 123
    self.assertEqual(getRatio(price_a, price_b), 0)


if __name__ == '__main__':
    unittest.main()
