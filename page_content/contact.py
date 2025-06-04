import streamlit as st

def contact_page():
    # 设置页面标题
    st.title("Contact Me")
    
    # 使用卡片式容器增强层次感
    with st.container():
        st.markdown("""
        <div style="background-color: #f8f9fa; padding: 1.5rem; border-radius: 0.5rem; box-shadow: 0 2px 4px rgba(0,0,0,0.1);">
            <p style="margin-bottom: 0.5rem;">I'd love to hear from you! Connect with me through 😊:</p>
        </div>
        """, unsafe_allow_html=True)
        
        # 使用多列布局分隔联系方式
        col1, col2 = st.columns(2)
        
        with col1:
            st.subheader("Direct Contact 💬")
            st.markdown("""
            - **Email**: [linhan_fu@163.com](mailto:linhan_fu@163.com)
            - **Phone**: +86 18850637133
            """)
        
        with col2:
            st.subheader("Social Media 💞")
            st.markdown("""
            - **Wechat**: -Rhiannon-
            - **Xiaohongshu**: @Isla
            """)
    
    # 使用分隔线和空间增强层次感
    st.write("")
    st.markdown("---")
    st.write("")
    
    # Send Me a Message部分（使用您提供的代码）
    st.markdown("### Send Me a Message")
    
    # ===================== Google Forms 嵌入 =====================
    st.markdown("""
    <iframe 
        src="https://docs.google.com/forms/d/e/1FAIpQLSefp0Bru1FpBmpjh0VyNqD64nmsv08UJtqBz2SScUYkptpjZg/viewform?embedded=true" 
        width="100%" 
        height="800" 
        frameborder="0" 
        marginheight="0" 
        marginwidth="0"
        style="border: none;"
    >
        Loading...
    </iframe>
    """, unsafe_allow_html=True)
    
    # 原本地表单代码（已注释，作为备选）
    """
    with st.form("contact_form"):
        col1, col2 = st.columns(2)
        
        with col1:
            name = st.text_input("Name")
            email = st.text_input("Email")
            
        with col2:
            subject = st.text_input("Subject")
            
        message = st.text_area("Message", height=150)
        
        submitted = st.form_submit_button("Send Message")
        
        if submitted:
            st.success("Thanks for your message! I'll get back to you soon.")
    """
    
    # 页脚区域
    st.write("")
    st.markdown("---")
    
    with st.container():
        st.markdown("""
        <div style="text-align: center; color: #6c757d; font-size: 0.9rem;">
            <p>© 2025 All Rights Reserved</p>
        </div>
        """, unsafe_allow_html=True)

if __name__ == "__main__":
    contact_page()