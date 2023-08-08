from soundboard import Soundboard

SB_RST = 18
uart_id=0
sound = Soundboard("XB", rst_pin=SB_RST, vol=0.5, debug=True, alt_get_files=True)

# Play track 0
sound.play(0)

# Play the test file that comes with the sound board
sound.play("T00     OGG")
