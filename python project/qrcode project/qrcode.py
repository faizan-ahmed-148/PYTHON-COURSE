import qrcode as qr

qr.add_data('https://www.instagram.com/faizu_ahmed.849/')
 
qr.make(fit = True)
img = qr.make_image(fill_color = 'red',
                    back_color = 'white')
            
img.save('faizan_instagram.png')