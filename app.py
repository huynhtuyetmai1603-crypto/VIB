import streamlit as st
import os

# ==========================================
# 1. CẤU HÌNH TRANG STREAMLIT
# ==========================================
st.set_page_config(
    page_title="VIB - Hệ thống Tư vấn Vay vốn",
    page_icon="🏦",
    layout="wide",
    initial_sidebar_state="expanded"
)

# ==========================================
# 2. TÙY CHỈNH GIAO DIỆN CHUẨN THƯƠNG HIỆU VIB (CSS)
# ==========================================
st.markdown("""
    <style>
    /* Nền Sidebar VIB */
    [data-testid="stSidebar"] {
        background-color: #002D62 !important;
    }
    
    [data-testid="stSidebar"] * {
        color: #FFFFFF !important;
    }

    [data-testid="stSidebar"] hr {
        border-color: rgba(255, 255, 255, 0.15);
    }

    /* Banner chính VIB */
    .vib-banner {
        background: linear-gradient(135deg, #002D62 0%, #004080 100%);
        color: white;
        padding: 22px 28px;
        border-radius: 12px;
        border-left: 8px solid #F37021;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.08);
        margin-bottom: 25px;
        position: relative;
    }

    .vib-banner-tag {
        position: absolute;
        top: 22px;
        right: 25px;
        background-color: rgba(243, 112, 33, 0.2);
        border: 1px solid #F37021;
        color: #FF8C42;
        padding: 6px 16px;
        border-radius: 20px;
        font-size: 13px;
        font-weight: 600;
    }

    /* Thẻ thông số Bảng tính */
    .calc-card {
        background-color: #FFFFFF;
        border-radius: 10px;
        padding: 18px 20px;
        border: 1px solid #E2E8F0;
        box-shadow: 0px 2px 8px rgba(0, 0, 0, 0.04);
        text-align: left;
    }

    .calc-card .title {
        font-size: 13px;
        color: #64748B;
        font-weight: 600;
        margin-bottom: 6px;
    }

    .calc-card .value {
        font-size: 22px;
        color: #002D62;
        font-weight: 700;
    }

    /* Nút bấm Cam VIB */
    div.stButton > button {
        background-color: #F37021 !important;
        color: white !important;
        border: none !important;
        font-weight: 600 !important;
    }
    
    div.stButton > button:hover {
        background-color: #D95D12 !important;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. THANH DIỀU HƯỚNG SIDEBAR (NƠI HIỂN THỊ LOGO)
# ==========================================
with st.sidebar:
    
    # ----------------------------------------------------
    # ĐOẠN CODE THÊM LOGO
    # ----------------------------------------------------
    LOCAL_LOGO_PATH = "vib_logo.png" # File logo tải về lưu cùng thư mục
    ONLINE_LOGO_URL = "https://www.vib.com.vn/wps/wcm/connect/vib-assets/logo.png" # Link logo dự phòng online

    # Kiểm tra nếu có file logo trong thư mục thì load, không thì lấy từ link online
    if os.path.exists(LOCAL_LOGO_PATH):
        st.image(LOCAL_LOGO_PATH, use_container_width=True)
    else:
        st.image(ONLINE_LOGO_URL, use_container_width=True)
    # ----------------------------------------------------

    st.markdown("<h3 style='text-align: center; font-size: 18px; margin-top: 10px;'>QUẢN LÝ KHÁCH HÀNG</h3>", unsafe_allow_html=True)
    st.markdown("<p style='text-align: center; font-size: 12px; color: #A0B2C6;'>KHỐI NGÂN HÀNG BÁN LẺ</p>", unsafe_allow_html=True)
    st.markdown("---")

    st.markdown("**ĐIỀU HƯỚNG BẢNG ĐIỀU KHIỂN**")
    
    selected_page = st.radio(
        label="Điều hướng",
        options=[
            "📝 Đăng ký nhu cầu vay",
            "🧮 Bảng tính trả góp",
            "🔐 Quản trị Admin"
        ],
        label_visibility="collapsed"
    )

    st.markdown("<br><br><br>", unsafe_allow_html=True)
    st.caption("HỆ THỐNG ĐĂNG KÝ VAY VỐN & QUẢN LÝ KHÁCH HÀNG • PHÁT TRIỂN BỞI KHỐI KHCN VIB")

# ==========================================
# 4. CHÂN TRANG & BANNER CHUNG
# ==========================================
st.markdown("""
    <div class="vib-banner">
        <h2 style='margin:0; font-size:24px; color:white;'>🏛️ VIB - HỆ THỐNG PHÁT TRIỂN KHÁCH HÀNG</h2>
        <p style='margin-top:6px; color:#D1D5DB; font-size:14px;'>Giải pháp thu thập & phân tích nhu cầu vay vốn tài chính cao cấp</p>
        <div class="vib-banner-tag">DỰ ÁN TÀI CHÍNH 2026</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 5. XỬ LÝ GIAO DIỆN CÁC TRANG
# ==========================================

# ------------------------------------------
# TRANG 1: ĐĂNG KÝ NHU CẦU VAY
# ------------------------------------------
if selected_page == "📝 Đăng ký nhu cầu vay":
    st.caption("DỊCH VỤ TÀI CHÍNH CÁ NHÂN")
    st.markdown("## 💳 ĐĂNG KÝ TƯ VẤN VAY VỐN")
    st.write("Khách hàng vui lòng điền đầy đủ thông tin bên dưới để Chuyên viên VIB hỗ trợ gói vay tối ưu nhất.")
    
    st.markdown("---")
    st.markdown("### 📋 Thông tin hồ sơ vay")
    st.caption("Điền thông tin chính xác để chuyên viên thẩm định liên hệ nhanh nhất")

    with st.form("loan_registration_form"):
        col1, col2 = st.columns(2)

        with col1:
            ho_ten = st.text_input("👤 Họ và tên khách hàng (*)", placeholder="Ví dụ: Trần Văn B")
            sdt = st.text_input("📱 Số điện thoại liên hệ (*)", placeholder="Ví dụ: 0987654321")
            tinh_thanh = st.text_input("📍 Tỉnh / Thành phố sinh sống", placeholder="Ví dụ: TP. Hồ Chí Minh, Hà Nội, Đà Nẵng")

        with col2:
            nhu_cau = st.selectbox(
                "📌 Nhu cầu sản phẩm vay (*)",
                [
                    "Vay Mua Ô tô (VIB Auto Loan)",
                    "Vay Mua Nhà / Bất Động Sản",
                    "Vay Tín Chấp Theo Lương",
                    "Vay Kinh Doanh Bổ Sung Vốn Lưu Động"
                ]
            )
            
            so_tien_vay = st.number_input(
                "💰 Số tiền đề xuất vay (VNĐ) (*)", 
                value=350000000, 
                step=10000000, 
                format="%d"
            )
            
            thoi_han_vay = st.selectbox(
                "⏱️ Thời hạn vay mong muốn",
                ["12 tháng", "24 tháng", "36 tháng", "48 tháng", "60 tháng", "84 tháng"],
                index=2
            )

        submit_btn = st.form_submit_button("🚀 Gửi thông tin đăng ký")
        
        if submit_btn:
            if ho_ten and sdt:
                st.success(f"✅ Đăng ký thành công! Chuyên viên VIB sẽ liên hệ tới SĐT {sdt} trong vòng 15 phút.")
            else:
                st.error("⚠️ Vui lòng điền đầy đủ các thông tin bắt buộc (*).")

# ------------------------------------------
# TRANG 2: BẢNG TÍNH LÃI VÀ GỐC TRẢ GÓP
# ------------------------------------------
elif selected_page == "🧮 Bảng tính trả góp":
    st.caption("CÔNG CỤ HỖ TRỢ TÀI CHÍNH")
    st.markdown("## 🧮 BẢNG TÍNH LÃI VÀ GỐC TRẢ GÓP")
    st.write("Công cụ tính toán khoản vay theo dư nợ giảm dần do VIB phát triển.")

    st.markdown("---")

    col_input1, col_input2, col_input3 = st.columns(3)

    with col_input1:
        so_tien = st.number_input("Số tiền vay (VNĐ)", value=500000000, step=10000000, format="%d")

    with col_input2:
        lai_suat = st.number_input("Lãi suất (%/năm)", value=7.9, step=0.1, format="%.2f")

    with col_input3:
        thoi_gian = st.slider("Thời gian vay (Tháng)", min_value=6, max_value=120, value=48, step=6)

    # Tính toán
    goc_co_dinh_thang = so_tien / thoi_gian
    lai_thang_dau = so_tien * (lai_suat / 100) / 12
    tong_tra_thang_dau = goc_co_dinh_thang + lai_thang_dau

    st.markdown("<br>", unsafe_allow_html=True)

    c1, c2, c3 = st.columns(3)

    with c1:
        st.markdown(f"""
            <div class="calc-card">
                <div class="title">📌 Gốc cố định hàng tháng</div>
                <div class="value">{goc_co_dinh_thang:,.0f} VNĐ</div>
            </div>
        """, unsafe_allow_html=True)

    with c2:
        st.markdown(f"""
            <div class="calc-card">
                <div class="title">💸 Lãi tháng đầu tiên</div>
                <div class="value">{lai_thang_dau:,.0f} VNĐ</div>
            </div>
        """, unsafe_allow_html=True)

    with c3:
        st.markdown(f"""
            <div class="calc-card">
                <div class="title">🔥 Tổng trả tháng đầu</div>
                <div class="value" style="color:#F37021;">{tong_tra_thang_dau:,.0f} VNĐ</div>
            </div>
        """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("⚡ *Bảng tính mang tính chất tham khảo. Chi tiết sẽ được Chuyên viên VIB phê duyệt chính xác theo từng hồ sơ cụ thể.*")

# ------------------------------------------
# TRANG 3: QUẢN TRỊ ADMIN
# ------------------------------------------
elif selected_page == "🔐 Quản trị Admin":
    st.markdown("## 🔐 Quản trị Hệ thống VIB")
    st.warning("Vui lòng đăng nhập tài khoản cán bộ VIB để truy cập danh sách hồ sơ.")
