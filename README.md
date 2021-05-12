# mediapipe_jetson_nano
Running mediapipe on Jetson Nano


Ref: https://github.com/jiuqiant/mediapipe_python_aarch64


1.
git clone https://github.com/google/mediapipe.git

2.
sudo apt install -y python3-dev
sudo apt install -y cmake


3.
sudo apt install -y protobuf-compiler
sudo apt install libprotobuf-dev.

Modified 2 files 
./mediapipe/calculators/tensor/image_to_tensor_converter_opencv.cc and ./mediapipe/calculators/tensor/image_to_tensor_converter_gl_buffer.cc. Code below:  
          return tensor;  
replace with:  
          return absl::StatusOr<mediapipe::Tensor> ( mediapipe::Tensor(std::move(tensor)) );  


4.
cd ~/mediapipe  

4.1   
sed -i -e "/\"imgcodecs\"/d;/\"calib3d\"/d;/\"features2d\"/d;/\"highgui\"/d;/\"video\"/d;/\"videoio\"/d" third_party/BUILD  

4.2  
sed -i -e "/-ljpeg/d;/-lpng/d;/-ltiff/d;/-lImath/d;/-lIlmImf/d;/-lHalf/d;/-lIex/d;/-lIlmThread/d;/-lrt/d;/-ldc1394/d;/-lavcodec/d;/-lavformat/d;/-lavutil/d;/-lswscale/d;/-lavresample/d" third_party/BUILD  

4.3  
diff --git a/third_party/BUILD b/third_party/BUILD  
index ef408e4..51e1104 100644  
--- a/third_party/BUILD  
+++ b/third_party/BUILD  
@@ -110,6 +104,8 @@ cmake_external(  
   "WITH_ITT": "OFF",  
   "WITH_JASPER": "OFF",  
   "WITH_WEBP": "OFF",  
   "ENABLE_NEON": "OFF",  <--add this    
   "WITH_TENGINE": "OFF",  <--add this  
  
5. pip3 install ./dist/mediapipe-0.8-cp36-cp36m-linux_aarch64.whl

6. 
nano ~/.bashrc  
add following to bottom:  
export OPENBLAS_CORETYPE=ARMV8

7. reboot

8. Run demo:
python3 facemesh_demo.py
