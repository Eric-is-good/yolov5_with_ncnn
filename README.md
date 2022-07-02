# yolov5_with_ncnn



### 网上这个东西的教程很多，但是他们往往不说版本对应关系，这使得有许多细节需要更改，对于小白，这相当于没有教程，因为解决细节需要你有一定的功底，我这里直接提供了一套配套的文件。



## 拓展部分（可以跳过，与本工程无关）

1. 如何 [onnx 模型可视化](https://netron.app/)。
2. pytorch 到 ncnn，有些网络层没有对应的 c++ 底层实现，怎么自己 [手撸 ncnn](https://zhuanlan.zhihu.com/p/275989233?utm_source=qq) ，或者 修改 .param 文件。
3. 认识无法转化的 crop 层。



### 使用yolov5和ncnn，将其部署到移动端，我提供了精心挑选的相互匹配的版本，不会报错，为您节省了许多时间



## 如何安装

1. 直接下载 yolov5 和 安卓文件，进入到 ncnn-android-yolov5/app/src/main/ ，解压 jni.zip。



## 训练模型

1. 在 yolov5/models/pts/ 下提供了两个官方的预训练模型。

2. 参照 [yolov5](https://github.com/ultralytics/yolov5) 官方教程即可，在训练结果中得到 best.pt 文件。

3. 使用 export.py 到处 onnx 格式，**注意**，必须要 带有 --train ，例如

   ```python
   python export.py --train
   ```

3. 使用 模型剪枝工具转化 onnx 文件

   ```python
   pip install onnx coremltools onnx-simplifier
   
   python -m onnxsim best.onnx best-sim.onnx
   ```

4. 转化为 ncnn 文件用于部署，在 [这里](https://convertmodel.com/) 转换。

   pic

5. 将 .param 和 .bin 替换 安卓工程的 ncnn-android-yolov5/app/src/main/assets/ 即可

6. 更改  .param 文件，参照 [这里](https://blog.csdn.net/angelsweet/article/details/124625456) 即可



## 开始享受吧