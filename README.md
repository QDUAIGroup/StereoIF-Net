# Stereoscopic-Image-Quality-Assessment-Network

This is a demonstration of the Stereoscopic Image Quality Assessment Network  based binocular interaction and fusion mechanisms (StereoIF-Net). The algorithm is described in:

1. Jianwei Si, Baoxiang Huang, Huan Yang, Weisi Lin and Zhenkuan Pan, "A no-reference stereoscopic image quality assessment network based on binocular interaction and fusion mechanisms".

You can change this program as you like and use it anywhere, but please refer to its original source (cite our paper and our web page at https://github.com/QDUAIGroup/StereoIF-Net, 2021) or cite the citation in your paper as follows:

The citation will be added soon...

## Copyright Notice

Copyright (c) 2021 Qingdao University All rights reserved.

Permission is hereby granted, without written agreement and without license or royalty fees, to use, copy, modify, and distribute this code (the source files) and its documentation for any purpose, provided that the copyright notice in its entirety appear in all copies of this code, and the original source of this code,Computer Science of Technology at Qingdao University (QDU), is acknowledged in any publication that reports research using this code. The research is to be cited in the bibliography as:

1. Jianwei Si, Baoxiang Huang, Huan Yang, Weisi Lin and Zhenkuan Pan, "A no-reference stereoscopic image quality assessment network based on binocular interaction and fusion mechanisms".

IN NO EVENT SHALL QINGDAO UNIVERSITY BE LIABLE TO ANY PARTY FOR DIRECT, INDIRECT, SPECIAL, INCIDENTAL, OR CONSEQUENTIAL DAMAGES ARISING OUT OF THE USE OF THIS DATABASE AND ITS DOCUMENTATION, EVEN IF QINGDAO UNIVERSITY HAS BEEN ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

QINGDAO UNIVERSITY SPECIFICALLY DISCLAIMS ANY WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE. THE DATABASE PROVIDED HEREUNDER IS ON AN "AS IS" BASIS, AND QINGDAO UNIVERSITY HAS NO OBLIGATION TO PROVIDE MAINTENANCE, SUPPORT, UPDATES, ENHANCEMENTS, OR MODIFICATIONS.

## How to Start 

You can use source codes as following instructions.

### Requirements:

- Python 3.6

- TensorFlow 2.0.0 with Keras

- GPU with memory &ge; 12GB

- CUDA 10.0

- Matlab R2017b or later

### Usage:

0. Install the requirements

1. Install Matlab API in python.

   ```python
   cd (root_path_of_matlab)\extern\engines\python\
   python setup.py install
   ```

2. Obtain SIQA prediction results. You need run `test_SIQA_LIVE1.py` and `test_SIQA_LIVE2.py` to obtain predicted stereoscopic image quality scores of StereoIF-Net on LIVE 3D Phase I and LIVE 3D Phase II database, respectively. The predicted scores are in `./LIVE1/preds_LIVE1.mat` and `./LIVE2/preds_LIVE2.mat` 

   ```python
   python test_SIQA_LIVE1.py
   ```

   ```python
   python test_SIQA_LIVE2.py
   ```

3. Compare prediction scores with DMOS to obtain the performance of StereoIF-Net. You need run `compute_test_LIVE1.py` and `compute_test_LIVE.py` to get various performance indexes (PLCC and SROCC) on LIVE 3D Phase I and LIVE 3D Phase II database, respectively 

   ```
   python compute_test_LIVE1.py
   ```

   ```
   python compute_test_LIVE2.py
   ```

### Results

|                  |  PLCC  | SROCC  |
| :--------------: | :----: | :----: |
| LIVE 3D Phase I  | 0.9779 | 0.9656 |
| LIVE 3D Phase II | 0.9717 | 0.9529 |

## Contacts

Author: Jianwei Si 

The authors are with the College of Computer Science and Technology, Qingdao University, Qingdao 266071, China

Kindly report any suggestions or corrections to jianwei_1995@hotmail.com
