from otp_service import generate_otp, save_otp, verify_otp

def send_otp_sms(mobile, otp):
    # TEMP: replace with Fast2SMS later
    print(f"OTP for {mobile} is {otp}")

def start_login(conn, mobile):
    otp = generate_otp()
    save_otp(conn, mobile, otp)
    send_otp_sms(mobile, otp)

def confirm_otp(conn, mobile, otp):
    return verify_otp(conn, mobile, otp)
