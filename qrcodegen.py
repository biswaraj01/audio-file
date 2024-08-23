import qrcode

features = qrcode.QRCode(version = 1, box_size = 30, border = 3)

features.add_data("https://github.com/biswaraj01/audio-file/raw/main/voice2.mp3")
features.make(fit=True)
generate_image = features.make_image(fill_color = 'black', bg = 'white')
generate_image.save('qrcode.png')
