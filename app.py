import streamlit as st

# ==========================================
# 1. CẤU HÌNH TRANG STREAMLIT
# ==========================================
st.set_page_config(
    page_title="VIB Lead Manager - Nhóm 5",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. TÙY CHỈNH GIAO DIỆN MÀU SẮC (CSS)
# ==========================================
# Màu chủ đạo VIB: Xanh Navy (#002D62) & Cam (#F37021)
st.markdown("""
    <style>
    /* 1. Đổi màu thanh Sidebar bên trái */
    [data-testid="stSidebar"] {
        background-color: #002D62 !important;
    }
    
    /* 2. Đổi chữ trong Sidebar sang màu trắng */
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    /* 3. Đổi màu đường kẻ phân cách trong Sidebar */
    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.2);
    }

    /* 4. Tùy chỉnh Banner Tiêu đề VIB chính */
    .vib-banner {
        background: linear-gradient(135deg, #002D62 0%, #0056B3 100%);
        color: white;
        padding: 24px 30px;
        border-radius: 10px;
        border-left: 8px solid #F37021;
        box-shadow: 0px 4px 10px rgba(0, 0, 0, 0.08);
        margin-bottom: 25px;
    }

    .vib-banner h2 {
        margin: 0;
        font-size: 26px;
        font-weight: 700;
        color: #FFFFFF;
    }

    .vib-banner p {
        margin-top: 5px;
        margin-bottom: 0;
        font-size: 14px;
        color: #E0E6ED;
    }

    /* 5. Tùy chỉnh Khung Thống kê (Metric Cards) */
    [data-testid="stMetric"] {
        background-color: #FFFFFF;
        padding: 15px 20px;
        border-radius: 8px;
        border: 1px solid #E1E6EB;
        box-shadow: 0px 2px 6px rgba(0,0,0,0.03);
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. DỰNG THANH MENU SIDEBAR BÊN TRÁI
# ==========================================
with st.sidebar:
    # Hiển thị Logo VIB (Ưu tiên đọc file nội bộ vib_logo.png)
    try:
        st.image("vib_logo.png", use_container_width=True)
    except:
        # Nếu chưa tải file logo, hệ thống sẽ dùng link logo dự phòng
        st.image("https://www.vib.com.vn/wps/wcm/connect/vib-assets/logo.png", use_container_width=True)

    st.markdown("<p style='text-align: center; font-size: 13px;'>Hệ thống Lead Management</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("**📂 MENU QUẢN LÝ**")
    
    # Danh sách tùy chọn Menu
    selected_menu = st.radio(
        label="Chức năng chính",
        options=[
            "📌 Bảng điều khiển",
            "📋 Danh sách Leads",
            "➕ Thêm Lead mới",
            "📊 Tiến độ xử lý",
            "📈 Báo cáo chỉ số"
        ],
        label_visibility="collapsed"
    )

    # Chân trang Sidebar
    st.markdown("<br><br><br><br>", unsafe_allow_html=True)
    st.markdown("""
        <div style='font-size: 11px; color: #A0B2C6;'>
            <b>VIB Lead Manager - Nhóm 5 v3.0</b><br>
            Phát triển cho Khối KHCN VIB
        </div>
    """, unsafe_allow_html=True)

# ==========================================
# 4. KHU VỰC NỘI DUNG CHÍNH (MAIN PAGE)
# ==========================================

# 1. Banner Tiêu đề
st.markdown("""
    <div class="vib-banner">
        <h2>🏦 VIB LEAD MANAGER - NHÓM 5</h2>
        <p>Hệ thống Quản lý & Phân loại Khách hàng Tiềm năng (Personal Banking Leads)</p>
    </div>
""", unsafe_allow_html=True)

# 2. Xử lý hiển thị nội dung theo trang người dùng chọn
if selected_menu == "📌 Bảng điều khiển":
    
    # Phần 1: Thống kê số lượng Lead
    st.markdown("### 📊 Thống kê lượng Lead hiện tại")
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(label="👥 TỔNG KHÁCH HÀNG", value="0")
    with col2:
        st.metric(label="🔥 KHÁCH HOT", value="0")
    with col3:
        st.metric(label="⚡ KHÁCH WARM", value="0")
    with col4:
        st.metric(label="❄️ KHÁCH COLD", value="0")

    st.markdown("<br>", unsafe_allow_html=True)

    # Phần 2: Danh sách Lead ưu tiên
    st.markdown("### 🔥 Danh sách Lead Ưu tiên (HOT - Điểm cao nhất)")
    st.info("Chưa có dữ liệu khách hàng trong hệ thống.")

elif selected_menu == "➕ Thêm Lead mới":
    st.markdown("### ➕ Thêm Lead Khách hàng mới")
    with st.form("add_lead_form"):
        ho_ten = st.text_input("Họ và tên khách hàng")
        sdt = st.text_input("Số điện thoại")
        san_pham = st.selectbox("Sản phẩm quan tâm", ["Thẻ tín dụng VIB", "Vay tiêu dùng", "Vay mua nhà", "Gửi tiết kiệm"])
        submit = st.form_submit_button("Lưu dữ liệu")
        if submit:
            st.success(f"Đã thêm thành công khách hàng {ho_ten}!")

else:
    st.markdown(f"### {selected_menu}")
    st.write("Nội dung đang trong quá trình cập nhật...")
