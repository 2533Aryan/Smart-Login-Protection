def send():
    import email, smtplib, ssl

    from email import encoders
    from email.mime.base import MIMEBase
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText

    subject = "Unauthorized Access To Computer"
    body = "Sir, I found a unauthorized person using your computer. Here are some images of that person"

#################################################################################################################
#################################################################################################################
#################################################################################################################
    
    sender_email = "user@gmail.com"
    receiver_email = "receiver@gmail.com"
    password = "****"
    
#################################################################################################################
#################################################################################################################
#################################################################################################################
    
    # Create a multipart message and set headers
    message = MIMEMultipart()
    message["From"] = sender_email
    message["To"] = receiver_email
    message["Subject"] = subject

    # Add body to email
    message.attach(MIMEText(body, "plain"))
    print("hello world")

    try:
        
        filename = "opencv9.png"  # In same directory as script

        # Open PDF file in binary mode
        with open(filename, "rb") as attachment:
            # Add file as application/octet-stream
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename}",
        )
        message.attach(part)
    except:
        pass
        
    # Add attachment to message and convert message to string
    text = message.as_string()

    ###############################################################################

    ## Add body to email

    try:
        
        filename1 = "opencv10.png"  # In same directory as script

        ## Open PDF file in binary mode
        with open(filename1, "rb") as attachment:
            # Add file as application/octet-stream
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        ## Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        ## Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename1}",
        )
        message.attach(part)
    except:
        pass
    
    ## Add attachment to message and convert message to string
    
    text = message.as_string()
    ##############################################################################

    ### Add body to email

    try:
        
        filename2 = "opencv11.png"  # In same directory as script

        # Open PDF file in binary mode
        with open(filename2, "rb") as attachment:
            # Add file as application/octet-stream
            part = MIMEBase("application", "octet-stream")
            part.set_payload(attachment.read())

        # Encode file in ASCII characters to send by email    
        encoders.encode_base64(part)

        # Add header as key/value pair to attachment part
        part.add_header(
            "Content-Disposition",
            f"attachment; filename= {filename2}",
        )
        message.attach(part)
    except:
        pass
    
    # Add attachment to message and convert message to string
    
    text = message.as_string()


    # Log in to server using secure context and send email
    context = ssl.create_default_context()
    with smtplib.SMTP_SSL("smtp.gmail.com", 465, context=context) as server:
        server.login(sender_email, password)
        server.sendmail(sender_email, receiver_email, text)
send()
