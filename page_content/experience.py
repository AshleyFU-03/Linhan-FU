import streamlit as st
from components.interactive import display_interactive_chart

def experience_page():
    # 设置页面配置（与教育页面保持一致）
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
        .card-title {
            color: var(--morandi-light-brown);
            font-weight: 600;
            margin-bottom: 0;
            font-size: 1.5em;
        }
        
        .card-subtitle {
            color: var(--morandi-dark-gray);
            font-weight: 500;
            margin-bottom: 10px;
            font-size: 1.2em;
        }
        
        .position-title {
            color: var(--morandi-dark-gray);
            font-weight: 500;
            margin-bottom: 5px;
            font-size: 1.1em;
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
        
        /* 列表样式 */
        .content-list {
            margin-top: 0;
            margin-bottom: 0;
            padding-left: 20px;
        }
    </style>
    """, unsafe_allow_html=True)

    # 专业经验部分
    st.markdown("""
    <div class="title-card">
        <h2 class="card-title">Internship Experience</h2>
    </div>
    """, unsafe_allow_html=True)
    
    experiences = [
        {
            "title": "Global Funding Digital Platform Product Manager Intern",
            "company": "Midea Group Co., Ltd.",
            "time": "January 2024 - May 2024",
            "description": """
            Product Strategy: Defined 5+ PRDs from user insights
            Design & Iteration: Prototyped 3 versions (Axure), driving efficiency gains
            """
        },
        {
            "title": "Investment Business Intern",
            "company": "China Cinda Asset Management Co., Ltd.",
            "time": "October 2023 - December 2023",
            "description": """
            Data Insights: Extracted key insights from AI firms' financials & strategies to guide investments
            Portfolio Oversight: Tracked company performance & risks for stable returns
            """
        },
        {
            "title": "Beauty & Personal Care Merchant Operations Intern",
            "company": "Shanghai Shizhuang Information Technology Co., Ltd. (Dewu)",
            "time": "February 2023 - May 2023",
            "description": """
            Precision Operations: Managed 2K+ SPUs for KA sellers, optimizing selection & pricing
            Marketing Projects: Launched "Travel Cosmetic Bags" (150+ SPUs), driving 150% order growth
            Product Iteration: Delivered user-requested features to enhance UX
            Data-Driven Optimization: Used SQL insights to lift KA sellers' GMV 30%
            """
        },
        {
            "title": "Industry Research Intern, Overseas TMT Group",
            "company": "TF Securities",
            "time": "August 2022 - November 2022",
            "description": """
            Industry Insights: Analyzed Alibaba's competitive edge in e-commerce, delivering 60-page strategic report
            Competitive Benchmarking: Compared Taobao vs rivals on GMV/ROI for beauty & fashion
            Market Analysis: Produced weekly stock reports (U.S./HK) using Wind/Bloomberg data
            """
        }
    ]
    
    # 使用展开器展示专业经验
    for i, exp in enumerate(experiences):
        st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
        with st.expander(f"{exp['title']} @ {exp['company']}", expanded=i==0):
            # 将描述文本按行分割并转换为HTML列表
            lines = exp["description"].strip().split('\n')
            html_list = '<ul class="content-list">'
            for line in lines:
                if line.strip():  # 跳过空行
                    html_list += f'<li class="text">{line.strip()}</li>'
            html_list += '</ul>'
            
            st.markdown(f"""
            <div class="content-card">
                <p class="time-text">{exp["time"]}</p>
                {html_list}
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # 项目部分
    st.markdown("""
    <div class="title-card">
        <h2 class="card-title">Projects</h2>
    </div>
    """, unsafe_allow_html=True)
    
    projects = [
        {
            "title": "Customer Analysis & Behavior Prediction",
            "description": "Developed a predictive model using XGBoost to identify high-value customers and applied K-means clustering for user segmentation.",
            "skills": ["Python", "scikit-learn", "RFM Analysis", "MBA Analysis", "Matplotlib", "Seaborn"],
            "outcome": "Created 4 distinct user personas and implemented targeted marketing strategies, improving campaign conversion rates by 20%."
        },
        {
            "title": "Natural Language Processing for Social Media Analysis",
            "description": "Analyzed 10K+ Douyin videos/comments using NLP and statistical modeling to compare Luckin Coffee and Mixue Bingcheng's IP marketing strategies.",
            "skills": ["Web Scraping", "API Integration", "Sentiment Analysis", "Competitive Benchmarking"],
            "outcome": "Identified 3 engagement pattern differences and recommended optimizations that boosted brand sentiment by 25%."
        }
    ]
    
    for i, project in enumerate(projects):
        st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
        with st.expander(f"{project['title']}", expanded=i==0):
            st.markdown(f"""
            <div class="content-card">
                <p class="text"><strong>Description:</strong> {project['description']}</p>
                <p class="text"><strong>Skills Used:</strong> {' '.join([f'<span class="skill-tag">{skill}</span>' for skill in project['skills']])}</p>
                <p class="text"><strong>Outcome:</strong> {project['outcome']}</p>
            </div>
            """, unsafe_allow_html=True)
        st.markdown('</div>', unsafe_allow_html=True)
    
    # 交互式可视化演示
    st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
    with st.expander("Interactive Data Visualization Techniques", expanded=False):
        st.markdown("""
        <div class="content-card">
            <p class="text"><strong>Description:</strong> An interactive demonstration of various data visualization techniques.</p>
        </div>
        """, unsafe_allow_html=True)
        display_interactive_chart()
    st.markdown('</div>', unsafe_allow_html=True)
    
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    
    # 专业技能部分
    st.markdown("""
    <div class="title-card">
        <h2 class="card-title">Professional Skills</h2>
    </div>
    """, unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        <div class="content-card">
            <h3 class="card-subtitle">Technical Skills</h3>
            <ul class="text">
                <li><strong>Programming Languages:</strong> Python, R, SQL</li>
                <li><strong>Machine Learning:</strong> XGBoost, Random Forest, Neural Network</li>
                <li><strong>Natural Language Processing:</strong> NLTK, spaCy</li>
                <li><strong>Marketing Modeling:</strong> sBG Model, Markov Chain Model </li>
                <li><strong>Data Analysis:</strong> Corhort Analysis, MBA Analysis</li>
                <li><strong>Visualization:</strong> Matplotlib, Seaborn, Tableau</li>
                <li><strong>Web Development:</strong> Streamlit, Flask</li>
                <li><strong>Prototype Design:</strong> Axure</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown("""
        <div class="content-card">
            <h3 class="card-subtitle">Soft Skills</h3>
            <ul class="text">
                <li><strong>Strategic Thinking:</strong> Ability to translate data insights into actionable marketing strategies</li>
                <li><strong>Analytical Mindset:</strong> Critical evaluation of marketing performance metrics</li>
                <li><strong>Communication:</strong> Presenting technical findings to non-technical stakeholders</li>
                <li><strong>Adaptability:</strong> Embracing new measurement methodologies and technologies</li>
                <li><strong>Leadership:</strong> Securing executive buy-in for data-informed marketing investments</li>
            </ul>
        </div>
        """, unsafe_allow_html=True)