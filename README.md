# MAIXbit_kit_nncase_testing
MAIXbit kit, built around the Kendryte K210 chip,  comes ready with CGA camera and 640x480 lcd display.


"MaixBit_Attempt1" directory holds first attempt at testing MicroPython code on the MaixBit dev kit.
The code that handles the camera image, that then gets sent to LCD display.  A full explanation is found on the [ MaixPy github ] (https://github.com/sipeed/MaixPy#simple-code)

Searching for better explanation around KPU lib,  led to a quick KModel [face_detection_example](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/face_find/demo_find_face.py)
This forced me to update the firmware,  binaries available from [Sipeed MaixPy downloads page] (https://dl.sipeed.com/shareURL/MAIX/MaixPy/release/master/maixpy_v0.6.2_72_g22a8555b5)
Also in linux, it is recommended to use the binary uploader provided by MaixPy: `pip3 install kflash --user`   and then using  `kflash -p /dev/ttyUSB0 -B maixduino MaixBit_Attempt1/maixpy_v0.6.2_72_g22a8555b5_with_lvgl.bin` worked

The `maixpy_v0.6.2_72_g22a8555b5_with_lvgl.bin` binary by itself will ask for the kmodel file.  That needs to uploaded via kflash : `kflash -p /dev/ttyUSB0 -B maixduino -b 1500000 face_model_at_0x300000.kfpkg`.  Sources [issue explanation](https://github.com/sipeed/MaixPy/issues/361) ;  
Full instructions on howto upload binary and kmodel file / thanks to GarretGross :: (https://garrettgoss.com/blog/2019/07/getting-started-with-the-sipeed-maixduino-kit.html)

Thonny has a hard time uploading files correctly (error halfway through upload, causes file truncated at awkward file position).  So use ampy instead :  `pip3 install adafruit-ampy --user`  ---> `ampy --port /dev/ttyUSB0 -d 0.5 put face_model_detect_test1.py /flash/face_model_detect_test1.py`

- Face has to be properly lit in order for KPU to detect face.

`demo_scan_qr_code.py`  is a great example of scanning QR code,  ` img = sensor.snapshot()`  then  `res = img.find_qrcodes()`  ---  but the digital camera has no mechanical auto focus, so one has to preset the focal distance to detect printed QR code.  Also room illumination plays a key role in detection.  Should try the RaspberryPi InfraRed camera to see if detects at low lighting scenarios. 
