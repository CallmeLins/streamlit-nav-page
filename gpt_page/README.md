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

# Custom config
- config avatar and user name in [custom.py](https://github.com/CallmeLins/streamlit-nav-page/blob/main/gpt_page/libs/custom.py)  [(source)](https://www.dicebear.com/playground?style=identicon)。
- add preset context in [setcontext.py](https://github.com/CallmeLins/streamlit-nav-page/blob/main/gpt_page/libs/setcontext.py)


# Thanks
- Based on [PierXuY/ChatGPT-Assistant](https://github.com/PierXuY/ChatGPT-Assistant/), thanks
- [context function](https://github.com/PierXuY/ChatGPT-Assistant/blob/main/set_context.py) from [binary-husky/chatgpt_academic](https://github.com/binary-husky/chatgpt_academic) and [f/awesome-chatgpt-prompts](https://github.com/f/awesome-chatgpt-prompts), thanks
- voice interaction from [talk-to-chatgpt](https://github.com/C-Nedelcu/talk-to-chatgpt) and [Voice Control for ChatGPT](https://chrome.google.com/webstore/detail/voice-control-for-chatgpt/eollffkcakegifhacjnlnegohfdlidhn), thanks
- proxy from [openai-forward](https://github.com/beidongjiedeguang/openai-forward), thanks
