# RGB-To-Hex-Python
A Simple Python Model for the convertion of HEX to RGB and reverse

A Python example Object for converting color codes.

## Examples

```
# Hex code.
original_hex_code = "0xf44336"
print(original_hex_code)  # Output: 0xf44336

# Converts hex code to RGB.
rgb_value = RGB.toRGB(hex_code=original_hex_code)
print(rgb_value)  # Output: RGB(244, 67, 3)

# Converts RGB back to hex code.
new_hex_code = rgb_value.toHex()
print(new_hex_code)  # Output: 0xf44303

# New RGB object with red, green, blue as parameters.
rgb = RGB(250, 70, 30)
print(rgb)  # Output: RGB(250, 70, 30)

# Converts RGB object to hex code.
hex_code = rgb.toHex()
print(hex_code)  # Output: 0xfa461e
```

## Errors
```
rgb = RGB(280, 40, 50)  # Error: ValueTooLargeError.
# One or more RGB values are higher than 255.

rgb = RGB(-10, 50, 240)  # Error: ValueTooSmallError.
# One or more RGB values are smaller than 0.

rgb = RGB("60", 50, 240)  # Error: ExpectsIntError.
# One or more RGB values aren't integers.

rgb = RGB.toRGB(hex_code=0xf44336)  # Error: ExpectsStringError.
# Hex code isn't a string.

rgb = RGB.toRGB(hex_code="f44336")  # Error: HexStringFormatError.
# Hex code has not the right format: Is missing "0x".

rgb = RGB.toRGB(hex_code="0xf443")  # Error: HexStringTooShortError.
# Overall hex string length is shorter than 8.

rgb = RGB.toRGB(hex_code="0xf44336ff")  # Error: HexStringTooLongError.
# Overall hex string length is longer than 8.
```