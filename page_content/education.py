import streamlit as st

def education_page():
    # 设置页面配置
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
            height: 100%;  /* 确保卡片高度一致 */
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
        
        /* 强调标签 */
        .emphasis-tag {
            display: inline-block;
            background-color: var(--morandi-title-bg);
            color: var(--morandi-dark-gray);
            border-radius: 3px;
            padding: 1px 5px;
            margin-right: 5px;
            font-size: 0.9em;
            font-weight: 500;
        }
    </style>
    """, unsafe_allow_html=True)

    # 教育背景部分
    def render_education_section():
        st.markdown("""
        <div class="title-card">
            <h2 class="card-title">Education</h2>
        </div>
        """, unsafe_allow_html=True)
        
        education_entries = [
            {
                "title": "Master of Science in Marketing",
                "school": "The Chinese University of Hong Kong",
                "time": "August 2024 - October 2025",
                "description": """<span class="emphasis-tag">Relevant Coursework</span> Machine Learning in Marketing, Customer Analytics, Big Data Strategy, Digital Marketing, Social Media Analytics, Marketing Research, Buyer Behavior"""
            },
            {
                "title": "Bachelor of Economics in Finance",
                "school": "Shanghai University of Finance and Economics",
                "time": "September 2020 - June 2024",
                "description": """<span class="emphasis-tag">Thesis</span> "Research on the Effect of Internet Consumer Finance Asset Securitization —— A Case Study of Jingdong Baitiao"<br>
<span class="emphasis-tag">Relevant Coursework</span> Corporate Finance, Experiment Finance, Behavioral Finance, Finance Econometrics, International Settlement"""
            }
        ]
        
        for i, entry in enumerate(education_entries):
            st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
            with st.expander(f"{entry['title']} @ {entry['school']}", expanded=i==0):
                st.markdown(f"""
                <div class="content-card">
                    <p class="time-text">{entry['time']}</p>
                    <p class="text">{entry['description']}</p>
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # 证书部分 - 使用三列布局
    def render_certifications_section():
        st.markdown("""
        <div class="title-card">
            <h2 class="card-title">Certifications</h2>
        </div>
        """, unsafe_allow_html=True)
        
        certifications = [
            {
                "title": "GMAT: 720 (top 7%)",
                "issuer": "Pearson VUE",
                "time": "July 2024",
                "description": "Demonstrated strong quantitative and verbal reasoning skills for graduate business studies"
            },
            {
                "title": "PSC: Level 2-A",
                "issuer": "National Language Committee",
                "time": "April 2024",
                "description": "Certified advanced Mandarin proficiency for professional communication and public speaking"
            },
            {
                "title": "NCRE: Level 2",
                "issuer": "China Ministry of Education",
                "time": "March 2023",
                "description": "Validated expertise in advanced office productivity tools and data processing applications."
            }
        ]
        
        col1, col2, col3 = st.columns(3)
        
        for i, cert in enumerate(certifications):
            col = [col1, col2, col3][i % 3]
            with col:
                st.markdown(f"""
                <div class="content-card">
                    <h3 class="card-subtitle">{cert['title']}</h3>
                    <p><strong>{cert['issuer']}</strong> <span class="time-text">| {cert['time']}</span></p>
                    <p class="text">{cert['description']}</p>
                </div>
                """, unsafe_allow_html=True)

    # 学术项目部分
    def render_projects_section():
        st.markdown("""
        <div class="title-card">
            <h2 class="card-title">Academic Projects</h2>
        </div>
        """, unsafe_allow_html=True)
        
        projects = [
            {
                "title": "JD High-End Electronics: User Targeting and Marketing Strategy",
                "description": """
                <ul class="text">
                    <li>Developed an XGBoost-based prediction model to identify high-potential JD electronics consumers from 1M+ user profiles</li>
                    <li>Achieved 90% precision in targeting high-value customers through feature engineering and hyperparameter tuning</li>
                    <li>Optimized AUC-ROC to 0.91 by addressing class imbalance with SMOTE sampling</li>
                    <li>Segmented 50K+ top users into 4 distinct personas using clustering analysis (RFM + K-means)</li>
                    <li>Designed a tiered recommendation system that boosted conversion rates by 20% through personalized marketing strategies</li>
                </ul>
                """
            },
            {
                "title": "Comparative Analysis of IP Marketing Effectiveness on Douyin",
                "description": """
                <ul class="text">
                    <li>Collected and analyzed 10K+ Douyin videos/comments using web scraping and NLP techniques</li>
                    <li>Compared IP marketing effectiveness between Luckin Coffee and Mixue Bingcheng across brand affinity, emotional connection, and customer loyalty metrics</li>
                    <li>Proposed data-driven recommendations that improved brand sentiment scores by 25% in pilot campaigns</li>
                </ul>
                """
            },
            {
                "title": "How does Xiaohongshu win the hearts of Hong Kong users?",
                "description": """
                <ul class="text">
                    <li>Conducted multi-modal analysis on 800+ Hong Kong news articles using NLP to decode public perception of Xiaohongshu</li>
                    <li>Processed 20K+ Xiaohongshu posts with LDA topic modeling and co-occurrence networks, discovering top 5 trending content categories among HK users</li>
                    <li>Designed quadrant analysis frameworks to prioritize content strategies, revealing "cross-border shopping guides" as high-opportunity-low-competition areas</li>
                    <li>Surveyed 400+ local residents to build user personas</li>
                </ul>
                """
            }
        ]
        
        for i, project in enumerate(projects):
            st.markdown('<div class="custom-expander">', unsafe_allow_html=True)
            with st.expander(f"{project['title']}", expanded=i==0):
                st.markdown(f"""
                <div class="content-card">
                    {project['description']}
                </div>
                """, unsafe_allow_html=True)
            st.markdown('</div>', unsafe_allow_html=True)

    # 渲染所有部分
    render_education_section()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    render_certifications_section()
    st.markdown('<div class="divider"></div>', unsafe_allow_html=True)
    render_projects_section()