# Installation
```bash
git clone https://github.com/chenxi52/test_swift.git
cd test-swift/backend
pip install -e '.[llm]' # install locally
```

# Getting Started
First of all, download the pretrained model from the website to your local machine, and specify the path where you saved the model using the `model_type` parameter.
```bash
# Linux
CUDA_VISIBLE_DEVICES=0 swift deploy --model_type model-type --model_id_or_path path-to-model
e.g.
CUDA_VISIBLE_DEVICES=0 swift deploy --model_type internvl2-1b --model_id_or_path ~/.cache/modelscope/hub/OpenGVLab/InternVL2-1B
```


# TO-DO
- [x] 数据库存储，将累积历史对话形式的api修改为单次对话api
  - [x] 接入数据库
  - [x] 用户登录功能(每个用户维护一个uid，每个对话维护一个chatid)
- [ ] 代码重构
- [ ] 并发问题
