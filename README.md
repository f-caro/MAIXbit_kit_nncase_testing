# MAIXbit_kit_nncase_testing
MAIXbit kit, built around the Kendryte K210 chip,  comes ready with CGA camera and 640x480 lcd display.


"MaixBit_Attempt1" directory holds first attempt at testing MicroPython code on the MaixBit dev kit.
The code that handles the camera image, that then gets sent to LCD display.  A full explanation is found on the [ MaixPy github ] (https://github.com/sipeed/MaixPy#simple-code)

Searching for better explanation around KPU lib,  led to a quick KModel [face_detection_example](https://github.com/sipeed/MaixPy_scripts/blob/master/machine_vision/face_find/demo_find_face.py)
This forced me to update the firmware,  binaries available from [Sipeed MaixPy downloads page] (https://dl.sipeed.com/shareURL/MAIX/MaixPy/release/master/maixpy_v0.6.2_72_g22a8555b5)
Also in linux, it is recommended to use the binary uploader provided by MaixPy: `pip3 install kflash --user`   and then using  `kflash -p /dev/ttyUSB0 -B maixduino MaixBit_Attempt1/maixpy_v0.6.2_72_g22a8555b5_with_lvgl.bin` worked

The `maixpy_v0.6.2_72_g22a8555b5_with_lvgl.bin` binary by itself will ask for the kmodel file.  That needs to uploaded via kflash : `kflash -p /dev/ttyUSB0 -B maixduino -b 1500000 face_model_at_0x300000.kfpkg`.  Sources [issue explanation](https://github.com/sipeed/MaixPy/issues/361) ;  [Full instructions on howto upload binary and kmodel file / thanks to GarretGross] (https://garrettgoss.com/blog/2019/07/getting-started-with-the-sipeed-maixduino-kit.html)


