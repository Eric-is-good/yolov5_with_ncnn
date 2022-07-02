import numpy as np
import onnxruntime
import torch

def to_numpy(tensor):
    return tensor.detach().cpu().numpy() if tensor.requires_grad else tensor.cpu().numpy()



if __name__ == '__main__':
    x = torch.randn(1, 3, 320, 320, requires_grad=True)
    ort_session = onnxruntime.InferenceSession("yolov5n.onnx")


    # compute ONNX Runtime output prediction
    ort_inputs = {ort_session.get_inputs()[0].name: to_numpy(x)}
    ort_outs = ort_session.run(None, ort_inputs)
    print(ort_outs)
