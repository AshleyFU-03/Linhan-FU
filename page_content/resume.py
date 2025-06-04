import streamlit as st
import os
import base64

def resume_page():
    # 设置页面配置（与其他页面保持一致）
    st.markdown("""
    <style>
        /* 莫兰迪色系配色方案 */
        :root {
            --morandi-light-brown: #8B8378;  /* 浅棕色 */
            --morandi-dark-gray: #696969;    /* 深灰色 */
            --morandi-medium-gray: #555555;  /* 中灰色 */
            --morandi-light-gray: #777777;   /* 浅灰色 */
            --morandi-bg: #F5F5F5;           /* 背景色 */
            --morandi-title-bg: #E8E4E0;     /* 标题背景色 */
            --morandi-cream-dark: #EDE0C8;   /* 深米白色 */
        }
        
        /* 标题卡片 */
        .title-card {
            background-color: var(--morandi-title-bg);
            border-radius: 10px;
            padding: 15px 20px;
            margin-bottom: 20px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
        }
        
        /* 内容卡片 */
        .content-card {
            background-color: var(--morandi-bg);
            border-radius: 10px;
            padding: 20px;
            margin-bottom: 20px;
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
            transition: all 0.3s ease;
        }
        
        .content-card:hover {
            box-shadow: 0 8px 12px rgba(0, 0, 0, 0.15);
            transform: translateY(-2px);
        }
        
        /* 标题样式 */
        .card-subtitle {
            color: var(--morandi-dark-gray);
            font-weight: 500;
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        
        /* 文本样式 */
        .text {
            color: var(--morandi-medium-gray);
            font-size: 0.9em;
        }
        
        .time-text {
            color: var(--morandi-light-gray);
            font-size: 0.9em;
        }
        
        /* 分隔线 */
        .divider {
            border-top: 1px solid var(--morandi-light-brown);
            margin: 25px 0;
        }
        
        /* 技能标签 */
        .skill-tag {
            display: inline-block;
            background-color: var(--morandi-title-bg);
            color: var(--morandi-dark-gray);
            border-radius: 5px;
            padding: 3px 8px;
            margin: 2px;
            font-size: 0.8em;
        }
        
        /* 按钮样式 - 深米白色 */
        .resume-button {
            background-color: var(--morandi-cream-dark);  /* 深米白色 */
            color: var(--morandi-dark-gray);  /* 深灰色文字 */
            border-radius: 5px;
            padding: 10px 15px;
            text-align: center;
            text-decoration: none;
            display: inline-block;
            font-size: 1em;
            margin: 4px 2px;
            cursor: pointer;
            transition: all 0.3s ease;
        }
        
        .resume-button:hover {
            background-color: var(--morandi-title-bg);  /* 悬停时变浅棕色 */
        }
        
        /* 自定义展开器样式 */
        .custom-expander .streamlit-expanderHeader {
            background-color: var(--morandi-bg);
            border-radius: 10px;
            padding: 15px;
            margin-bottom: 10px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.08);
            transition: all 0.3s ease;
        }
        
        .custom-expander .streamlit-expanderHeader:hover {
            box-shadow: 0 4px 6px rgba(0, 0, 0, 0.1);
        }
        
        .custom-expander .streamlit-expanderContent {
            padding: 0 15px 15px 15px;
            margin-top: -5px;
        }
        
        /* 联系信息强调标签 */
        .contact-tag {
            display: inline-block;
            background-color: var(--morandi-title-bg);
            color: var(--morandi-dark-gray);
            border-radius: 3px;
            padding: 1px 5px;
            margin-right: 5px;
            font-size: 0.9em;
            font-weight: 500;
        }
        
        /* 按钮容器 */
        .button-container {
            text-align: right;
            margin-bottom: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    pdf_file_path = os.path.join("static", "docs", "FU Linhan_CUHK_Big Data Marketing.pdf")

    if os.path.exists(pdf_file_path):
        with open(pdf_file_path, "rb") as pdf_file:
            PDFbyte = pdf_file.read()

        # 使用深米白色按钮并调整位置到右侧
        st.markdown("""
        <div class="button-container">
            <a href="javascript:void(0);" class="resume-button" onclick="document.getElementById('download-resume').click()">
                Unfold My Story 🔍
            </a>
            <input type="file" id="download-resume" style="display:none;" />
        </div>
        """, unsafe_allow_html=True)
        
        # 添加JavaScript下载功能
        st.markdown(f"""
        <script>
            document.querySelector('.resume-button').addEventListener('click', function() {{
                var link = document.createElement('a');
                link.href = 'data:application/pdf;base64,{base64.b64encode(PDFbyte).decode()}';
                link.download = 'Linhan_FU_Resume.pdf';
                link.click();
            }});
        </script>
        """, unsafe_allow_html=True)
    else:
        st.warning("Resume PDF file not found")

    # 联系方式卡片 - 添加颜色底框（删除名字卡片后直接显示联系方式）
    st.markdown("""
    <div class="content-card">
        <h3 class="card-subtitle">Where to Find Me</h3>
        <ul class="text">
            <li><span class="contact-tag">Email</span> <a href="mailto:linhan_fu@163.com">linhan_fu@163.com</a></li>
            <li><span class="contact-tag">Phone</span> +86 18850637133</li>
            <li><span class="contact-tag">Address</span> 12 Chak Cheung St., Ma Liu Shui, HKSAR</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    # 专业概述卡片
    st.markdown("""
    <div class="content-card">
        <h3 class="card-subtitle">Professional Summary</h3>
        <p class="text">
            Master's in Marketing (CUHK) with finance roots. Proven in product management (Midea), growth campaigns (+150% GMV at Dewu), and data analytics (SQL, Python). Led teams to top-tier case competitions (KPMG Top 3%). Passionate about merging insights with action.
        </p>
    </div>
    """, unsafe_allow_html=True)

    # 项目经验部分
    st.markdown("""
    <div class="title-card">
        <h2 class="card-title">Projects with Demonstrated Impact</h2>
    </div>
    """, unsafe_allow_html=True)

    # 项目1 - 使用折叠器
    st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
    with st.expander("Travel Cosmetic Bags Campaign for Dewu", expanded=True):
        st.markdown("""
        <div class="content-card">
            <p class="time-text">April 2023</p>
            <ul class="text">
                <li>Met the huge demand for beauty travel kits.</li>
                <li>Listed over 150 SPUs in the first month.</li>
                <li>Achieved a 150% increase in orders and 120% growth in GMV week-over-week.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 项目2 - 使用折叠器
    st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
    with st.expander("Shanghai Municipal Undergraduate Innovation and Entrepreneurship Project “LianlianYoucai”", expanded=False):
        st.markdown("""
        <div class="content-card">
            <p class="time-text">October 2021 - June 2024</p>
            <ul class="text">
                <li>Innovated “One-Week CP” activities like "1+X," "Matchmaker," and "Task Pool".</li>
                <li>Enhanced engagement & user experience and amassed over 1,000 active followers.</li>
                <li>Secured sponsorships from Juneyao Airlines, Nichang Tea Dance, Sensation Bar, and other brands, raising over 10,000 RMB in funding.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

    # 项目3 - 使用折叠器
    st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
    with st.expander("KPMG ESG Case Analysis Competition", expanded=False):
        st.markdown("""
        <div class="content-card">
            <p class="time-text">September 2022 - October 2022</p>
            <ul class="text">
                <li>Analyzed consumption characteristics, price sensitivity, and demand pain points of African BOP populations.</li>
                <li>Developed localized marketing strategies tailored to BOP populations, such as "One Place, One Person".</li>
                <li>Formulated the "Star Plan", including a "semi-localization" strategy to establish a sustainable business model.</li>
                <li>Built the "Star Lighting-Empowering BOP Populations" interactive platform, integrating social welfare resources and blending corporate social responsibility with business operations.</li>
                <li>Led the team to elite top-3%.</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)