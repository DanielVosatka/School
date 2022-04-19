class LYKMC:
    def convert_to_km(value):
        """
        Convert from light years to kilometers
        :param value: The value in light years that you want to convert
        :type value: float
        """
        return value * 9460730472580.8
        
    def convert_to_ly(value):
        """
        Convert from kilometers to light years
        :param value: The value in kilometers that you want to convert
        :type value: float
        """
        return value / 9460730472580.8
