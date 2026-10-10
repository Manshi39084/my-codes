import qrcode

upi_id = input("Enter your UPI ID ")

phonepay_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
paytm_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'
google_pay_url = f'upi://pay?pa={upi_id}&pn=Recipent%20Name&mc=1234'

#Create QR Codes for each payment app
phonepay_qr = qrcode.make(phonepay_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#save the QR code to image file (optional)
phonepay_qr.save('phonepay_qr.png')
paytm_qr.save('paytm_qr.png')
google_pay_qr.save('google_pay_qr.png')

#Display the Qr codes
phonepay_qr.show()
paytm_qr.show()
google_pay_qr.show()
