# ChatGPT-Assistant
Based on streamlit, support below function
- Multi chat box
- Keep chat records
- Preset chat context
- Model parameter adjustment
- Export conversation as a Markdown file
- ChatGPT voice communication

# Setting
## Config API key

- write `apikey = "Openai Key"` to `.streamlit/secrets.toml`
- if you want use proxy, write `apibase = "prox_url"` to `.streamlit/secrets.toml` explanation is as follows：   
  1. use project [openai-forward](https://github.com/beidongjiedeguang/openai-forward) proxy interface - `apibase = "https://api.openai-forward.com/v1"` 
  2. set up yourself ref: [openai-forward](https://github.com/beidongjiedeguang/openai-forward)

# 说明
- 在[custom.py](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/libs/custom.py)文件中可自定义用户名和SVG格式头像[(来源)](https://www.dicebear.com/playground?style=identicon)。
- 在部署的项目源码中编辑[set_context.py](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/libs/set_context.py)，即可增加预设定的上下文选项，会自动同步到应用中。
- 有条件的可以考虑把[helper.py](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/libs/helper.py)中的文件读写逻辑改为云数据库操作，防止历史记录丢失。


# Thanks
- Based on [PierXuY/ChatGPT-Assistant](https://github.com/PierXuY/ChatGPT-Assistant/) thanks
- [context function](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/set_context.py) from [binary-husky/chatgpt_academic](https://github.com/binary-husky/chatgpt_academic) and [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts) thanks
- voice interaction from [talk-to-chatgpt](https://github.com/C-Nedelcu/talk-to-chatgpt) and [Voice Control for ChatGPT](https://chrome.google.com/webstore/detail/voice-control-for-chatgpt/eollffkcakegifhacjnlnegohfdlidhn) thanks
- proxy from [openai-forward](https://github.com/beidongjiedeguang/openai-forward) thanks
