def on_received_number(receivedNumber):
    if receivedNumber == 1:
        music.play_melody("C5 C5 B B C5 C5 B B ", 240)
        basic.show_string("oi")
    else:
        if receivedNumber == 2:
            music.play_melody("D C D C D C D C ", 300)
            basic.show_string("sos")
radio.on_received_number(on_received_number)

def on_button_pressed_a():
    radio.send_number(1)
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    radio.send_number(2)
input.on_button_pressed(Button.B, on_button_pressed_b)
