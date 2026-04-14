import streamlit as st
import time
import os
import random

st.set_page_config(page_title="热点播客 AI 自动化引擎", layout="wide", page_icon="🎙️")

st.title("🎙️ 热点播客 AI 自动化引擎")
st.markdown("#### 每早7点，精读一条全球热点事件。")

st.divider()

st.subheader("🔄 自动化工作流程图")
st.caption("🚀 通过多 Agent 协同打通从热点输入到音频发布的自动化工作流。")

# 使用列布局来模拟步骤图
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("#### 1. IP agent热点初稿")
    if os.path.exists("demo_clip.mp4"):
        st.video("demo_clip.mp4", autoplay=True, muted=True, loop=True)
with col2:
    st.success("#### 2. cursor内容总监精修")
    if os.path.exists("opus_refining_demo.webp"):
        st.image("opus_refining_demo.webp", use_container_width=True)
with col3:
    st.warning("#### 3. cursor知识库复利")
    if os.path.exists("knowledge_base_demo.webp"):
        st.image("knowledge_base_demo.webp", use_container_width=True)
with col4:
    st.error("#### 4. 音剪自动化制作")
    if os.path.exists("audio_clip.mp4"):
        st.video("audio_clip.mp4", autoplay=True, muted=True, loop=True)

st.divider()

st.subheader("⚙️ 模拟器：消除幻觉、交付认知增量")

hot_topic = st.text_input("🔗 输入热点资讯标题或链接：", value="anthropic第一季度收入为何反超open AI")

def mock_generate_script():
    with st.spinner('第一步：Ip agent 正在处理热点资讯，产出初稿...'):
        time.sleep(1.0)
    with st.spinner('第二步：Opus 深度精修中 (检查风险、提取认知、优化体验)...'):
        time.sleep(1.5)
    with st.spinner('第三步：Agent 正在评估定稿，并归档至作品库...'):
        time.sleep(1.0)
    with st.spinner('第四步：准备推送至音剪平台进行音频转换...'):
        time.sleep(0.5)
        
    md_path = "demo_article.md"
    try:
        with open(md_path, "r", encoding="utf-8") as f:
            return f.read()
    except Exception as e:
        return f"处理出错，无法生成文稿：{e}"

st.write("")
if "generated_script" not in st.session_state:
    st.session_state.generated_script = None
if "show_full_script" not in st.session_state:
    st.session_state.show_full_script = False

if st.button("👇 自动生成文稿 🪄", type="primary", use_container_width=True):
    st.session_state.generated_script = None
    st.info(f"正在处理热点输入：**{hot_topic}**")
    st.session_state.generated_script = mock_generate_script()
    st.session_state.show_full_script = False
    st.balloons()
    st.success("✅ 播客深度推演完毕，您想要的定稿与核心认知已成功提炼！", icon="🎉")

if st.session_state.generated_script:
    lines = st.session_state.generated_script.split('\n')
    preview_text = '\n'.join(lines[:10])
    
    st.info("**👀 【正文自动预览】（前 10 行）**")
    st.markdown(preview_text)
    st.markdown("<span style='color:gray;'>...（此处省略其余部分）...</span>", unsafe_allow_html=True)
    
    if st.session_state.show_full_script:
        st.divider()
        st.markdown("### 📄 完整播客终稿全文")
        st.markdown(st.session_state.generated_script)
        
        with st.sidebar:
            st.markdown("### 📖 沉浸阅读模式")
            st.success("您正在阅读完整播客终稿。")
            if st.button("🔼 阅毕，收起文稿", use_container_width=True, type="primary"):
                st.session_state.show_full_script = False
                st.rerun()
    else:
        if st.button("🔽 展开阅读完整全文"):
            st.session_state.show_full_script = True
            st.rerun()

st.divider()

st.markdown("##### 👥 团队成员")
st.markdown("**夏文彦 &nbsp;|&nbsp; 覃君洋 &nbsp;|&nbsp; 王佳鸣 &nbsp;|&nbsp; 张慧敏 &nbsp;|&nbsp; 钱妤雯**")
st.markdown('<h2>💰✨ <span style="background: linear-gradient(90deg, #ff8a00, #e52e71); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">请为我们爆金币呀！！！</span> 🎉🥳</h2>', unsafe_allow_html=True)

st.divider()

quotes = [
    "“人工智能不是要取代人类，而是要让人类变得更加具有创造力。” —— **李飞飞 (斯坦福跨学科人工智能研究所所长)**",
    "“在不久的将来，熟练地与AI对话并编程提示词，将成为一种全新的通用语言。” —— **萨姆·奥特曼 (OpenAI 创始人)**",
    "“未来的文盲不再是那些不识字的人，而是那些不知道如何与人工智能协作的人。” —— **吴恩达 (Coursera 创始人, AI先驱)**",
    "“我们将像看待电一样看待人工智能：起初你惊叹它，后来你发现它已无声无息地隐入日常。” —— **桑达尔·皮查伊 (Google CEO)**",
    "“机器没有欲望，只有目的；人的伟大之处不仅在于思考，更在于拥有不可计算的‘热爱’。” —— **艾伦·图灵 (计算机科学之父)**",
    "“别问智能机器能不能替你思考，问问它能如何帮你拓展思维的边界。” —— **大卫·银 (DeepMind 核心科学家)**"
]

st.write("") # Spacer
col_cb1, col_cb2, col_cb3 = st.columns([1, 2, 1])
with col_cb2:
    if st.button("🎁 投票后，领取你的AI彩蛋～", type="secondary", use_container_width=True):
        st.balloons()
        st.success(random.choice(quotes), icon="🌟")
