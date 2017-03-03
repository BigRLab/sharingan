Sharingan
=========

Sharingan is a tool built on Python 3.6 using OpenCV 3.2 to extract news
content as text from newspaper’s photo and perform news context extraction.

How it works?
=============

<p align="center">
    <b>Capture Image</b>
</p>
![Alt](http://oi68.tinypic.com/2qiwz2o.jpg "original")

<p align="center">
    <b>Canny Edge Detection</b>
</p>
![Alt](http://oi66.tinypic.com/34fg0hy.jpg "edged")

<p align="center">
    <b>Dilation</b>
</p>
![Alt](http://oi67.tinypic.com/2lw52lz.jpg "dilated")

<p align="center">
    <b>Contour Detection</b>
</p>
![Alt](http://oi63.tinypic.com/2pouoow.jpg "contours")

<p align="center">
    <b>Contour Approximation and Bound Box</b>
</p>
![Alt](https://i.imgur.com/LSR98LW.jpg "bb")

Manual Mode
-----------

![Alt](https://cdn-images-1.medium.com/max/1600/1*6KKm4wGknXonl54dUD6tjQ.gif "drag")

![Alt](https://cdn-images-1.medium.com/max/1600/1*_pOvzvVLvHvcgrpxQL9XeA.gif "thresh")

Context Extraction
------------------

The segmentation done above gives the following result after context extraction:

        [‘residential terraces’, ‘busy markets’, ‘Puppies’, ‘inhumane conditions’, ‘popular e-commerce sites’, ‘Sriramapuram’, ‘Russell Market’, ‘issue licences’,
        ‘meeting conditions’, ‘positive impact’, ‘pet owners’, ‘R. Shantha Kumar’, ‘welfare ofﬁcer’, ‘Animal Welfare Board’, ‘India’]
        [‘Kittie’]
        [‘Compassion Unlimited’]
        [‘public spaces’, ‘Animal’, ‘rights activists’, ‘civic body’, ‘Bengaluru’],
        [‘BENGALURU’, ‘Bruhat Bengaluru Mahanagar Palike’, ‘Dane’, ‘English Mastiff’, ‘Bulldog’, ‘Boxer’, ‘Rottweiler’, ‘Bernard’, ‘Shepherd’, ‘Retriever’,
        ‘draft guidelines’, ‘sterilisation’, ‘pet dogs ’, ‘Owners’]


Installation
============

Installing OpenCV 3.2 from source Python 3.6
--------------------------------------------

* `wget https://github.com/Itseez/opencv/archive/3.2.0.zip`
* `unzip 3.2.0.zip`
* `cd opencv-3.2.0`
* `mkdir release && cd release`

        cmake -DBUILD_TIFF=ON \
            -DBUILD_opencv_java=OFF \
            -DWITH_CUDA=OFF \
            -DENABLE_AVX=ON \
            -DWITH_OPENGL=ON \
            -DWITH_OPENCL=ON \
            -DWITH_IPP=OFF \
            -DWITH_TBB=ON \
            -DWITH_EIGEN=ON \
            -DWITH_V4L=ON \
            -DWITH_VTK=OFF \
            -DBUILD_TESTS=OFF \
            -DBUILD_PERF_TESTS=OFF \
            -DCMAKE_BUILD_TYPE=RELEASE \
            -DBUILD_opencv_python2=OFF \
            -DCMAKE_INSTALL_PREFIX=$(python3.6 -c "import sys; print(sys.prefix)") \
            -DPYTHON3_EXECUTABLE=$(which python3.6) \
            -DPYTHON3_INCLUDE_DIR=$(python3.6 -c "from distutils.sysconfig import get_python_inc; print(get_python_inc())") \
            -DPYTHON3_PACKAGES_PATH=$(python3.6 -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())") ..

* You will be similar to this: [output](https://gist.github.com/vipul-sharma20/d57a779619f22b2254b66c89c957faf2)
* `make -j4`
* make install

Setting up Sharingan
--------------------

* `git clone git@github.com:vipul-sharma20/sharingan.git`
* `pip install -r requirements.txt`

**IMPORTANT:** You will require some corpora and trained models
for the code to run. You can refer to: [http://www.nltk.org/data.html](http://www.nltk.org/data.html)

* Interactive Method:

        In [1]: import nltk

        In [2]: nltk.download()

Docker
======

Try out the code on Jupyter Notebook

* `docker build -t sharingan-docker .`
* `docker run -p 8888:8888 -it sharingan-docker`

