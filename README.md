# YouTube-Video-Downloader
Before using my code it is advised to first read README as it would help you to avoid any error.

First of all make sure you have installed pytube3 module. If not install it using "pip install pytube3".
So, This is a python code to download videos from the YouTube easily.
All you have to do is to just copy paste the link from the YouTube. 
Before using code please read the disclaimer carefully and make the changes particularly.

                                                        "DISCLAIMER"
If you get any keyerror like this: 

KeyError: 'cipher'

then you need to make following changes in extract.py by fixing some lines and this file is located in pytube library.

cipher_url = [
                parse_qs(formats[i]["cipher"]) for i, data in enumerate(formats)
            ]



To


cipher_url = [
                parse_qs(formats[i]["signatureCipher"]) for i, data in enumerate(formats)
            ]
            
            
Just change cipher to signatureCipher and you are done.

Thanks
