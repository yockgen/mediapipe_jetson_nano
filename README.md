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
  132  sudo apt-get install python3-opencv
  133  cd ..
  134  git clone https://github.com/google/mediapipe.git
  135  cd mediapipe/
  136  clear
  137  sudo apt-get install -y libopencv-core-dev  libopencv-highgui-dev libopencv-calib3d-dev libopencv-features2d-dev libopencv-imgproc-dev libopencv-video-dev
  138  ./setup_opencv.sh
  139  chmod +x ./setup_opencv.sh
  140  ./setup_opencv.sh
  141  sudo pip3 install opencv_contrib_python
  142  cd ..
  143  git clone https://github.com/PINTO0309/mediapipe-bin
  144  cd mediapipe-bin/
  145  sudo apt install curl
  146  ./v0.8.5/numpy119x/mediapipe-0.8.5_cuda102-cp36-cp36m-linux_aarch64_numpy119x_jetsonnano_L4T32.5.1_download.sh
  147  ls
  148  ls ./v0.8.5/
  149  ls ./v0.8.5/download.sh 
  150  ./v0.8.5/download.sh 
  151  sudo pip3 install numpy-1.19.4-cp36-none-manylinux2014_aarch64.whl
  152  sudo pip3 install mediapipe-0.8.5_cuda102-cp36-none-linux_aarch64.whl
  153  cd ..
  154  git clone https://github.com/yockgen/mediapipe_jetson_nano.git
  155  cd mediapipe_jetson_nano/
  156  ls
  157  python3 facemesh_demo.py 
  158  cd -
  159  cd mediapipe-bin/
  160  ls
  161  ls v0.8.4
  162  unzip
  163  unzip v0.8.5.zip 
  164  ls
  165  ls v0.8.5
  166  ./v0.8.5/numpy119x/mediapipe-0.8.5_cuda102-cp36-cp36m-linux_aarch64_numpy119x_jetsonnano_L4T32.5.1_download.sh
  167  ls ./v0.8.5/numpy119x/
  168  ls ./v0.8.5/numpy119x/py36/
  169  pip3 install ./v0.8.5/numpy119x/py36/mediapipe-0.8.5_cuda102-cp36-cp36m-linux_aarch64.whl 
  170  ls ./v0.8.5/
  171  ls ./v0.8.5/numpy119x/
  172  pip3 install ./v0.8.5/numpy119x/py36/m
  173  pip3 install ./v0.8.5/numpy119x/py36/
  174  ls ./v0.8.5/numpy119x/py36/
  175  cd ..
  176  ls
  177  cd mediapipe_jetson_nano/
  178  python3 facemesh_demo.py 
