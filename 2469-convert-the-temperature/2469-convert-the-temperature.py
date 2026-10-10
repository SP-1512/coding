class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        ll = []
        ll.append(celsius + 273.15)
        ll.append(celsius * 1.8 + 32)
        return ll