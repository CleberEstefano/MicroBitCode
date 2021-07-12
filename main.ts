radio.onReceivedNumber(function (receivedNumber) {
    if (receivedNumber == 1) {
        music.playMelody("C5 C5 B B C5 C5 B B ", 240)
        basic.showString("oi")
    } else if (receivedNumber == 2) {
        music.playMelody("D C D C D C D C ", 300)
        basic.showString("sos")
    }
})
input.onButtonPressed(Button.A, function () {
    radio.sendNumber(1)
})
input.onButtonPressed(Button.B, function () {
    radio.sendNumber(2)
})
