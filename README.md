# mediapipe_jetson_nano
Running mediapipe on Jetson Nano

git clone https://github.com/JetsonHacksNano/installSwapfile.git     
cd installSwapfile/   
./installSwapfile.sh       
  
sudo apt-get update  
sudo apt-get install python3-pip       
sudo pip3 install -U pip testresources setuptools==49.6.0    
sudo apt-get install libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip libjpeg8-dev liblapack-dev libblas-dev gfortran     
sudo pip3 install -U --no-deps numpy==1.19.4 future==0.18.2 mock==3.0.5 keras_preprocessing==1.1.2 keras_applications==1.0.8 gast==0.4.0 protobuf pybind11 cython pkgconfig      
  
  
env H5PY_SETUP_REQUIRES=0 pip3 install -U h5py==3.1.0     
sudo apt-get install python3-opencv      
  
git clone https://github.com/google/mediapipe.git     
cd mediapipe/        
sudo apt-get install -y libopencv-core-dev  libopencv-highgui-dev libopencv-calib3d-dev libopencv-features2d-dev libopencv-imgproc-dev libopencv-video-dev          
./setup_opencv.sh         
chmod +x ./setup_opencv.sh       
./setup_opencv.sh    
sudo pip3 install opencv_contrib_python       
  
git clone https://github.com/PINTO0309/mediapipe-bin       
cd mediapipe-bin/  
sudo apt install curl    
unzip v0.8.5.zip 
pip3 install ./v0.8.5/numpy119x/py36/mediapipe-0.8.5_cuda102-cp36-cp36m-linux_aarch64.whl 

git clone 
cd mediapipe_jetson_nano/  
python3 facemesh_demo.py    
