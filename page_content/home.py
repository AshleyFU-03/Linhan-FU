import streamlit as st
from PIL import Image
import os

def home_page():
    # 设置页面配置（新增position-title样式）
    st.markdown("""
    <style>
        /* 导入外部字体 */
        @import url('https://fonts.googleapis.com/css2?family=Inter:wght@300;400;500;600;700&display=swap');
        
        /* 全局样式 */
        body {
            font-family: 'Inter', sans-serif;
        }
        
        /* 自定义容器样式 */
        .custom-container {
            background-color: #F5F5F5;  /* 浅灰色背景 */
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .custom-container:hover {
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }
        
        /* 标题样式 */
        .title {
            color: #8B8378;  /* 莫兰迪浅棕色 */
            font-weight: 600;
            margin-bottom: 10px;
        }
        
        /* 职位标题样式（新增） */
        .position-title {
            color: #696969;  /* 深灰色 */
            font-weight: 500;
            font-style: italic;
            font-size: 1.1em;  /* 增大字体 */
            margin-bottom: 15px;
        }
        
        /* 文本样式 */
        .text {
            color: #555555;  /* 中灰色 */
            font-size: 0.9em;  /* 减小地址字体 */
        }
        
        /* 强调文本 */
        .highlight {
            color: #8B8378;  /* 莫兰迪浅棕色 */
            font-weight: 500;
        }
        
        /* 链接样式 */
        a {
            color: #8B8378;  /* 莫兰迪浅棕色 */
            text-decoration: none;
            transition: all 0.2s ease;
        }
        
        a:hover {
            color: #696969;  /* 深灰色 */
            text-decoration: underline;
        }
        
        /* 分隔线样式 */
        .divider {
            border-top: 1px solid #A9A9A9;  /* 莫兰迪深灰色 */
            margin: 25px 0;
        }
        
        /* 图标样式 */
        .icon {
            margin-right: 8px;
            color: #8B8378;  /* 莫兰迪浅棕色 */
        }
        
        /* 自定义expander标题样式 */
        .streamlit-expanderHeader {
            font-size: 1.5em;  /* 增大字体 */
            color: #8B8378;   /* 使用莫兰迪浅棕色 */
            font-weight: 600;  /* 增加字体粗细 */
        }
        
        .streamlit-expanderHeader:hover {
            color: #696969;   /* 悬停时颜色变深 */
        }
        
        /* 展开后的标题样式 */
        .streamlit-expander[expanded] .streamlit-expanderHeader {
            font-size: 1.2em;  /* 展开后稍微缩小 */
        }
        
        /* 技能标签样式 */
        .skill-tag {
            display: inline-block;
            background-color: #E8E4E0;  /* 莫兰迪浅棕色背景 */
            color: #696969;  /* 深灰色文字 */
            border-radius: 5px;
            padding: 3px 8px;
            margin: 2px 5px 2px 0;
            font-size: 0.9em;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)

    # 顶部信息卡片
    with st.container():
        col1, col2 = st.columns([3, 1])

        with col1:
            st.markdown(
                """
                <div class="custom-container">
                    <h1 class="title" style="margin-bottom: 5px;">Linhan FU</h1>
                    <p class="position-title">Recent Master's Graduate in Marketing</p>  <!-- 使用新样式 -->
                    <p class="text">
                        <i class="icon fa fa-university"></i>The Chinese University of Hong Kong<br>
                        <i class="icon fa fa-map-marker"></i>12 Chak Cheung St., Ma Liu Shui, HKSAR<br>
                        <i class="icon fa fa-envelope"></i><a href="mailto:linhan_fu@163.com">linhan_fu@163.com</a>
                    </p>
                </div>
                """,
                unsafe_allow_html=True
            )

        with col2:
            image_path = os.path.join("static", "images", "FU, Linhan.jpeg")
            if os.path.exists(image_path):
                image = Image.open(image_path)
                st.image(image, use_container_width=True)
            else:
                st.warning("Profile image not found")

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)


    # 关于我部分 - 使用可折叠面板
    with st.expander("About Me 💗", expanded=True):
        st.markdown(
            """
            <div class="custom-container">
                <h2 class="title" style="font-size: 1.8em; margin-bottom: 15px; border-bottom: 2px solid #8B8378; padding-bottom: 5px;">About Me</h2>
                <p class="text">
                    Hi, I'm Linhan FU, a Master's student in <span class="highlight">Big Data Marketing</span> at The Chinese University of Hong Kong, 
                    with a Finance background from Shanghai University of Finance and Economics.
                </p>
                <p class="text">
                    I've worked across projects involving segmentation, experimentation, and predictive modeling — 
                    turning data into strategies that resonate with real consumer behavior.
                </p>
                <p class="text">
                    Beyond analytics, I care deeply about understanding people — what they value, how they decide, and why they connect. 
                    I believe effective marketing is not just persuasive, but significant.
                </p>
                <p class="text">
                    Curious by nature and collaborative at heart, I'm always open to new ideas, diverse minds, and purposeful conversations.
                </p>
            </div>
            """,
            unsafe_allow_html=True
        )

    # 个人信条部分 - 增大字体并加粗
    st.markdown(
        """
        <div class="custom-container" style="text-align: center; background-color: #DCD0C8; color: #555555;">
            <p style="font-size: 1.3em; font-weight: 600; font-style: italic;">
                "Starting is always more meaningful than longing 🦋"
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)

    # 技能和兴趣部分 - 使用标签页
    tab1, tab2 = st.tabs(["Skills", "Interests"])
    
    with tab1:
        st.markdown(
            """
            <div class="custom-container">
                <h3 class="title">Professional Skills</h3>
                <div class="text">
                    <p><span class="skill-tag">Data Analysis</span> Python, R, Machine Learning, SQL, Excel</p>
                    <p><span class="skill-tag">Marketing</span> Customer Analytics, Social Media Analytics, Marketing Research, Predictive Modeling</p>
                    <p><span class="skill-tag">Languages</span> Mandarin (Native), English (Fluent)</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )
    
    with tab2:
        st.markdown(
            """
            <div class="custom-container">
                <h3 class="title">Personal Interests</h3>
                <div class="text">
                    <p><i class="icon fa fa-book"></i><span class="skill-tag">Reading</span> Marketing Strategy, Economics, Psychology, Poems</p>
                    <p><i class="icon fa fa-plane"></i><span class="skill-tag">Travel</span> Embracing cultural diversity and human connections</p>
                    <p><i class="icon fa fa-paint-brush"></i><span class="skill-tag">Art</span> Channeling life's emotions through piano melodies and artistic expression</p>
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )