# RGB-To-Hex-Python
A Simple Python Model for the convertion of HEX to RGB and reverse.

## Functionality demonstration

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