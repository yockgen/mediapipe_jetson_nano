# mediapipe_jetson_nano
Running mediapipe on Jetson Nano

1.
[git clone https://github.com/google/mediapipe.git]

2.
sudo apt install -y python3-dev
sudo apt install -y cmake


3.
sudo apt install -y protobuf-compiler  
sudo apt install libprotobuf-dev  

If you see a missing any.proto error later, which means the protoc might be too old, you can download the latest protoc-3.x.x-linux-aarch_64.zip from GitHub and copy the "bin" and "include/google" directories to the system libraries. Then, modify mediapipe/setup.py like the following:  

diff --git a/setup.py b/setup.py  
index 61848de..462d91d 100644  
--- a/setup.py
+++ b/setup.py
@@ -208,7 +208,7 @@ class GeneratePyProtos(setuptools.Command):
         sys.stderr.write('cannot find required file: %s\n' % source)
         sys.exit(-1)

-      protoc_command = [self._protoc, '-I.', '--python_out=.', source]  
+      protoc_command = [self._protoc, '-I.', '-I/usr/local/include', '--python_out=.', source]  
       if subprocess.call(protoc_command) != 0:
         sys.exit(-1)

4.  


Modified 2 files 
./mediapipe/calculators/tensor/image_to_tensor_converter_opencv.cc and ./mediapipe/calculators/tensor/image_to_tensor_converter_gl_buffer.cc. Code below:  
          return tensor;  
replace with:  
          return absl::StatusOr<mediapipe::Tensor> ( mediapipe::Tensor(std::move(tensor)) );  


5.  


5.1   
sed -i -e "/\"imgcodecs\"/d;/\"calib3d\"/d;/\"features2d\"/d;/\"highgui\"/d;/\"video\"/d;/\"videoio\"/d" third_party/BUILD  

5.2  
sed -i -e "/-ljpeg/d;/-lpng/d;/-ltiff/d;/-lImath/d;/-lIlmImf/d;/-lHalf/d;/-lIex/d;/-lIlmThread/d;/-lrt/d;/-ldc1394/d;/-lavcodec/d;/-lavformat/d;/-lavutil/d;/-lswscale/d;/-lavresample/d" third_party/BUILD  

5.3  
modified mediapipe/third_party/BUILD b/third_party/BUILD:    
   "WITH_ITT": "OFF",   
   "WITH_JASPER": "OFF",    
   "WITH_WEBP": "OFF",    
   "ENABLE_NEON": "OFF",  <--add this      
   "WITH_TENGINE": "OFF",  <--add this    

5.4
python3 mediapipe/setup.py gen_protos && python3 mediapipe/setup.py bdist_wheel  


6. pip3 install mediapipe/dist/mediapipe-0.8-cp36-cp36m-linux_aarch64.whl

7. 
nano ~/.bashrc  
add following to bottom:  
export OPENBLAS_CORETYPE=ARMV8

8. reboot

9. Run demo:
python3 facemesh_demo.py



Ref: https://github.com/jiuqiant/mediapipe_python_aarch64
