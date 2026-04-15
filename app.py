import streamlit as st
import time
import os
import random
import base64
import streamlit.components.v1 as components

AUDIO_PATH = "OpenAI试听.mp3"
COVER_PATH = "cover.jpeg"

st.set_page_config(page_title="热点播客 AI 自动化引擎", layout="wide", page_icon="🎙️")

st.title("🎙️ 热点播客 AI 自动化引擎")
st.markdown("#### 每早7点，精读一条全球热点事件。")

st.divider()

st.subheader("🔄 自动化工作流程图")
st.caption("🚀 通过多 Agent 协同打通从热点输入到音频发布的自动化工作流。")

# 使用列布局来模拟步骤图
col1, col2, col3, col4 = st.columns(4)

with col1:
    st.info("#### 1. IP agent热点初稿\n\n*自然语言提需，配置个性化skill*")
with col2:
    st.success("#### 2. cursor内容总监精修\n\n*消除幻觉，优化听觉体验*")
with col3:
    st.warning("#### 3. cursor知识库复利\n\n*学习AI大神卡帕西的obsidian知识库管理法*")
with col4:
    st.error("#### 4. 音剪自动化制作\n\n*喜千烽录制*")

col_v1, col_v2, col_v3, col_v4 = st.columns(4)

with col_v1:
    if os.path.exists("demo_clip.mp4"):
        st.video("demo_clip.mp4", autoplay=True, muted=True, loop=True)
with col_v2:
    if os.path.exists("opus_refining_demo.webp"):
        st.image("opus_refining_demo.webp", use_container_width=True)
with col_v3:
    if os.path.exists("kb_sliding_demo.mp4"):
        st.video("kb_sliding_demo.mp4", autoplay=True, muted=True, loop=True)
    elif os.path.exists("bitter_lesson_demo.webp"):
        st.image("bitter_lesson_demo.webp", use_container_width=True)
    elif os.path.exists("knowledge_base_demo.webp"):
        st.image("knowledge_base_demo.webp", use_container_width=True)
with col_v4:
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

def build_audio_player_html(audio_path, cover_path):
    with open(audio_path, "rb") as f:
        audio_b64 = base64.b64encode(f.read()).decode()
    with open(cover_path, "rb") as f:
        cover_b64 = base64.b64encode(f.read()).decode()
    return f"""
    <style>
      body {{ margin: 0; }}
      .player-wrap {{
        display: flex;
        flex-direction: column;
        align-items: center;
        padding: 28px 20px 22px;
        background: linear-gradient(145deg, #1a1a2e 0%, #16213e 55%, #0f3460 100%);
        border-radius: 20px;
        box-shadow: 0 8px 32px rgba(0,0,0,0.45);
        font-family: -apple-system, BlinkMacSystemFont, "PingFang SC", sans-serif;
      }}
      .disc {{
        width: 190px;
        height: 190px;
        border-radius: 50%;
        overflow: hidden;
        border: 3px solid rgba(255,255,255,0.18);
        box-shadow: 0 0 0 10px rgba(255,255,255,0.04),
                    0 0 40px rgba(229,46,113,0.35);
        margin-bottom: 18px;
        transition: box-shadow 0.5s ease;
        flex-shrink: 0;
      }}
      .disc.spinning {{
        animation: spin 10s linear infinite;
        box-shadow: 0 0 0 10px rgba(255,255,255,0.04),
                    0 0 60px rgba(229,46,113,0.65),
                    0 0 110px rgba(255,138,0,0.25);
      }}
      @keyframes spin {{
        from {{ transform: rotate(0deg); }}
        to   {{ transform: rotate(360deg); }}
      }}
      .disc img {{ width: 100%; height: 100%; object-fit: cover; display: block; }}
      .track-title {{
        font-size: 14px; font-weight: 700; color: #fff;
        text-align: center; margin-bottom: 4px; letter-spacing: .3px;
      }}
      .track-sub {{
        font-size: 11px; color: rgba(255,255,255,0.45);
        text-align: center; margin-bottom: 16px;
      }}
      audio {{ width: 100%; border-radius: 8px; outline: none; }}
    </style>
    <div class="player-wrap">
      <div class="disc" id="disc">
        <img src="data:image/jpeg;base64,{cover_b64}" alt="封面" />
      </div>
      <div class="track-title">Anthropic 首季收入反超 OpenAI</div>
      <div class="track-sub">热点播客 · 每早 7 点 · AI 深度解析</div>
      <audio id="ap" controls>
        <source src="data:audio/mpeg;base64,{audio_b64}" type="audio/mpeg">
      </audio>
    </div>
    <script>
      var ap   = document.getElementById('ap');
      var disc = document.getElementById('disc');
      ap.addEventListener('play',  function(){{ disc.classList.add('spinning'); }});
      ap.addEventListener('pause', function(){{ disc.classList.remove('spinning'); }});
      ap.addEventListener('ended', function(){{ disc.classList.remove('spinning'); }});
    </script>
    """

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

    col_left, col_right = st.columns([3, 2])

    with col_left:
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

    with col_right:
        if os.path.exists(AUDIO_PATH) and os.path.exists(COVER_PATH):
            player_html = build_audio_player_html(AUDIO_PATH, COVER_PATH)
            components.html(player_html, height=400)
        else:
            st.warning("音频或封面文件未找到，请检查路径。")

st.divider()

st.markdown("##### 👥 团队成员")
st.markdown("**夏文彦 &nbsp;|&nbsp; 覃君洋 &nbsp;|&nbsp; 王佳鸣 &nbsp;|&nbsp; 张慧敏 &nbsp;|&nbsp; 钱妤雯**")
st.markdown('<h2>💰✨ <span style="background: linear-gradient(90deg, #ff8a00, #e52e71); -webkit-background-clip: text; -webkit-text-fill-color: transparent;">请为我们爆金币呀！！！</span> 🎉🥳</h2>', unsafe_allow_html=True)

st.divider()

with open("quotes.txt", encoding="utf-8") as _f:
    quotes = [line.strip() for line in _f if line.strip()]

st.write("") # Spacer
col_cb1, col_cb2, col_cb3 = st.columns([1, 2, 1])
with col_cb2:
    if st.button("🎁 投票后，领取你的AI彩蛋～", type="secondary", use_container_width=True):
        st.balloons()
        st.success(random.choice(quotes), icon="🌟")
        components.html("""
        <script>
        (function() {
            try {
                const ctx = new (window.AudioContext || window.webkitAudioContext)();
                const now = ctx.currentTime;
                // 小气泡 pop
                const pop = ctx.createOscillator();
                const popG = ctx.createGain();
                pop.connect(popG); popG.connect(ctx.destination);
                pop.frequency.setValueAtTime(900, now);
                pop.frequency.exponentialRampToValueAtTime(350, now + 0.12);
                pop.type = 'sine';
                popG.gain.setValueAtTime(0.35, now);
                popG.gain.exponentialRampToValueAtTime(0.001, now + 0.14);
                pop.start(now); pop.stop(now + 0.15);
                // 上升星星音阶
                [523, 659, 784, 1047, 1319].forEach(function(hz, i) {
                    const o = ctx.createOscillator();
                    const g = ctx.createGain();
                    o.connect(g); g.connect(ctx.destination);
                    o.frequency.value = hz;
                    o.type = 'sine';
                    const t = now + 0.08 + i * 0.09;
                    g.gain.setValueAtTime(0, t);
                    g.gain.linearRampToValueAtTime(0.18, t + 0.04);
                    g.gain.exponentialRampToValueAtTime(0.001, t + 0.3);
                    o.start(t); o.stop(t + 0.31);
                });
            } catch(e) {}
        })();
        </script>
        """, height=0)
