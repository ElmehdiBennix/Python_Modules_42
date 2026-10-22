from S1E7 import Baratheon, Lannister


class King(Baratheon, Lannister):
    """Summary."""

    def __init__(self, first_name: str):
        """
        Summary.

        Args:
            first_name (str): Description.
            is_alive (bool): Description, optional (default: True).
            family_name (str): Description, optional (default: "baratheon").
            eyes (str): Description, optional (default: "brown").
            hairs (str): Description, optional (default: "dark").
        Raises:
            TypeError: if type doesn't match class attribute.
        """
        super().__init__(first_name)

    def get_eyes(self):
        """
        .

        Return:
            Hair color string.
        """
        return self.eyes

    def get_hairs(self):
        """
        .

        Return:
            Hair color string.
        """
        return self.hairs

    def set_eyes(self, eyes: str):
        """
        Summary.

        Args:
            eyes (str): Description.
        Raises:
            TypeError: Description.
        Return:
            str: The updated eyes string.
        """
        if not isinstance(eyes, str):
            raise TypeError("eyes must be a string type.")

        self.eyes = eyes
        return self.eyes

    def set_hairs(self, hairs: str):
        """
        Summary.

        Args:
            hairs (str): Description.
        Raises:
            TypeError: Description.
        Return:
            str: The updated hairs string.
        """
        if not isinstance(hairs, str):
            raise TypeError("hairs must be a string type.")

        self.hairs = hairs
        return self.hairs
