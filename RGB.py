class RGB:
    """
        Type model to define an RGB data type.

        It has a built in hex to RGB converter to convert an RGB_hex to RGB.

        And it has a built in rgb to hex converter,
        which converts the RGB values into an RGB_hex_code.

    """

    def __init__(self, red: int, green: int, blue: int):
        #_DataValidation.checkRGBData(red, green, blue) # Validates Parameters

        self.red = red
        self.green = green
        self.blue = blue

    def __str__(self):
        return f"RGB({self.red}, {self.green}, {self.blue})"

    def __repr__(self):
        return f"RGB({self.red}, {self.green}, {self.blue})"

    def toHex(self):
        # Converts rgb_values into hex_code
        #
        # Takes rgb_values from Type RGB
        #                                                           red  blue
        #                                                            __  __
        # Returns a 8 digit hex_code string as followed example: 0xfff44336
        #                                                          ^^  ^^
        #                                           fixed_alpha_value  green
        # Digit 1 & 2 = fixed_alpha_value (255)
        # Digit 3 & 4 = red_value
        # Digit 5 & 6 = green_value
        # Digit 7 & 8 = blue_value

        hex_parts = []  # List to store sub_hex_codes
        hex_code = "0x"  # Basis for final hex_code

        hex_parts.append(hex(self.red))  # Appends sub_hex_code from red (int) value to hex_parts
        hex_parts.append(hex(self.green))  # Appends sub_hex_code from green (int) value to hex_parts
        hex_parts.append(hex(self.blue))  # Appends sub_hex_code from blue (int) value to hex_parts

        for i in range(len(hex_parts)):

            # Appends sub_hex_codes to hex_code excluding '0x'
            hex_code += hex_parts[i][2:] if len(hex_parts[i]) == 4 else f"0{hex_parts[i][2:]}"

        return hex_code

    @staticmethod
    def toRGB(hex_code: str):
        # Converts a hex_code to int_values from 0 to 255 and groups them as RGB Type
        #
        #                                                    red  blue
        #                                                     __  __
        # Takes a 8 digit hex_code string as followed example: 0xfff44336
        #                                                   ^^  ^^
        #                                    fixed_alpha_value  green
        # Digit 1 & 2 = fixed_alpha_value (255)
        # Digit 3 & 4 = red_value
        # Digit 5 & 6 = green_value
        # Digit 7 & 8 = blue_value
        # Converts 2 digits into one int_value
        # Excludes the first 2 digits from converting
        # Returns rgb_values from Type RGB

        # Validates [hex_code].
        #
        # Checks if it has the right format, size and type.
        #_DataValidation.checkHexString(hexString=hex_code)

        # Splits [hex_code] apart using [_splitHexCode].
        hex_parts = RGB._splitHexCode(hex_code)

        red_value = int(hex_parts[0], 0)  # Converts hex_code to int_value
        green_value = int(hex_parts[1], 0)  # Converts hex_code to int_value
        blue_value = int(hex_parts[2], 0)  # Converts hex_code to int_value

        return RGB(red_value, green_value, blue_value)

    @staticmethod
    def _splitHexCode(hex_code: str):
        # Splits hex_code in sub hex codes
        #
        # Takes 6 digit hex_code string as followed example: 0xf44336

        modified_hex_code = hex_code[2:]  # Cut off "0x" from hex code
        hex_parts = []  # List to store sub_hex_codes
        hex_part = "0x"  # String to make sub_hex_codes

        for i in range(len(modified_hex_code)):
            # Check if i is not uneven, add hexPart to hexParts list and reset hexPart
            if (i != 0 and not i % 2) or (i == len(modified_hex_code) - 1):
                hex_parts.append(hex_part)
                hex_part = "0x"

            hex_part += modified_hex_code[i]  # Add value from i to hex_part to combine 2 values

        return hex_parts
