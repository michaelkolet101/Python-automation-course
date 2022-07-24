
class BusinessInfo:

    def __init__(self, business_name: str, business_id: str):
        self._business_name = business_name
        self._business_id = business_id

    def get_business_id(self) -> str:
        """
        :return: business_id
        """
        return self._business_id