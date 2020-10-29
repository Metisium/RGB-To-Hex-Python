# RGB-To-Hex-Python
A Simple Python RGB model including built in HEX to RGB and reverse conversion.

Includes data validation. Checks the data, before initialising, for the right types and formats.

Suited for active error handling by providing error raising with custom errors.

## Examples
Initialize RGB object and access rgb values with the instance variables red, green and blue.
```
# RGB object.
rgb_object = RGB(230, 50, 80)

# Red value.
red = rgb_object.red  # Output: 230

# Green value.
green = rgb_object.green  # Output: 50

# Blue value.
blue = rgb_object.blue  # Output: 80

```
Get RGB object from Hex code string.
```
# Hex code.
initial_hex_code = "0xf44336"
print(initial_hex_code)  # Output: 0xf44336

# Converts hex code to RGB.
rgb_object = RGB.toRGB(hex_code=initial_hex_code)
print(rgb_object)  # Output: RGB(244, 67, 3)
```
Get Hex code string from RGB object.
```
# Converts RGB back to hex code.
hex_code = rgb_object.toHex()
print(hex_code)  # Output: 0xf44303
```

## Errors
```
rgb_object = RGB(280, 40, 50)  # Error: ValueTooLargeError.
# One or more RGB values are higher than 255.

rgb_object = RGB(-10, 50, 240)  # Error: ValueTooSmallError.
# One or more RGB values are smaller than 0.

rgb_object = RGB("60", 50, 240)  # Error: ExpectsIntError.
# One or more RGB values aren't integers.

rgb_object = RGB.toRGB(hex_code=0xf44336)  # Error: ExpectsStringError.
# Hex code isn't a string.

rgb_object = RGB.toRGB(hex_code="f44336")  # Error: HexStringFormatError.
# Hex code has not the right format: Is missing "0x".

rgb_object = RGB.toRGB(hex_code="0xf443")  # Error: HexStringTooShortError.
# Overall hex string length is shorter than 8.

rgb_object = RGB.toRGB(hex_code="0xf44336ff")  # Error: HexStringTooLongError.
# Overall hex string length is longer than 8.
```