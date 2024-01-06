# ChatGPT-Assistant
Based on streamlit, support below function
- Multi chat box
- Keep chat records
- Preset chat context
- Model parameter adjustment
- Export conversation as a Markdown file
- ChatGPT voice communication

# Setting

## Streamlit Cloud部署（推荐）
轻松免费部署，且无须科学上网即可使用，注意设置为私人应用。   
可参考由[@Hannah11111](https://github.com/Hannah11111)提供的[详细步骤](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/Tutorial.md)。
1. `Fork`本项目到个人Github仓库。
2. 注册[Streamlit Cloud账号](https://share.streamlit.io/)，并连接到Github。
3. 开始部署应用，具体可参考[官方教程](https://docs.streamlit.io/streamlit-community-cloud/get-started)。   
4. 在应用的Secrets中配置Openai Key，具体格式参考下图：
<div style="display: flex;">
  <img src="https://github.com/PierXuY/ChatGPT-Assistant/blob/main/Figure/advanced-setting.png" alt="advanced-setting.png" style="flex: 1; width: 40%;"/>
  <img src="https://github.com/PierXuY/ChatGPT-Assistant/blob/main/Figure/set-apikey.png" alt="set-apikey.png" style="flex: 1; width: 40%;" />
</div>   
也可以在部署完成后再进行配置。

## 本地部署
1. 建立虚拟环境（建议）

2. 克隆项目（也可以手动下载到本地）
```bash
git clone https://github.com/PierXuY/ChatGPT-Assistant.git
```

3. 安装依赖
```bash
pip install -r requirements.txt
```

4. 设置API Key;设置API Base（可选）

- 在 `.streamlit/secrets.toml`文件中写入`apikey = "Openai Key"`
- 在 `.streamlit/secrets.toml`文件中写入代理接口即可实现免科学使用，格式为`apibase = "代理接口地址"`，说明如下：   
  1. 可以直接使用项目[openai-forward](https://github.com/beidongjiedeguang/openai-forward)已搭建的代理接口，即`apibase = "https://api.openai-forward.com/v1"` 。
  2. 可参考[openai-forward](https://github.com/beidongjiedeguang/openai-forward)项目自行搭建代理接口并进行设置。

5. 启动应用
```bash
streamlit run app.py
```

# 说明
- 在[custom.py](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/libs/custom.py)文件中可自定义用户名和SVG格式头像[(来源)](https://www.dicebear.com/playground?style=identicon)。
- 在部署的项目源码中编辑[set_context.py](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/libs/set_context.py)，即可增加预设定的上下文选项，会自动同步到应用中。
- 有条件的可以考虑把[helper.py](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/libs/helper.py)中的文件读写逻辑改为云数据库操作，防止历史记录丢失。


# 致谢
- 基于[PierXuY/ChatGPT-Assistant](https://github.com/PierXuY/ChatGPT-Assistant/)项目进行的改造，感谢。
- 预设的[上下文功能](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/set_context.py)参考自[binary-husky/chatgpt_academic](https://github.com/binary-husky/chatgpt_academic)项目和[f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts)项目，感谢。
- 语音交互功能参考了项目[talk-to-chatgpt](https://github.com/C-Nedelcu/talk-to-chatgpt)和[Voice Control for ChatGPT](https://chrome.google.com/webstore/detail/voice-control-for-chatgpt/eollffkcakegifhacjnlnegohfdlidhn)的实现，感谢。
- 本地免科学上网功能可以借助项目[openai-forward](https://github.com/beidongjiedeguang/openai-forward)，感谢。
