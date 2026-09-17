import streamlit as st

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
# 2. CẤU HÌNH GIAO DIỆN & MÀU SẮC (CSS)
# ==========================================
st.markdown("""
    <style>
    /* Nền ứng dụng màu xám/xanh nhạt sạch sẽ */
    .stApp {
        background-color: #F8FAFC;
    }

    /* Sidebar sáng chuẩn nhận diện VIB */
    [data-testid="stSidebar"] {
        background-color: #FFFFFF;
        border-right: 1px solid #E2E8F0;
    }

    /* Header Banner màu xanh VIB (#002D62) với bo góc và badge */
    .vib-banner {
        background: linear-gradient(135deg, #002D62 0%, #004080 100%);
        color: white;
        padding: 20px 25px;
        border-radius: 12px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        margin-bottom: 25px;
        box-shadow: 0px 4px 12px rgba(0, 0, 0, 0.05);
    }

    .vib-banner-title {
        font-size: 20px;
        font-weight: 700;
        margin: 0;
        letter-spacing: 0.5px;
    }

    .vib-banner-sub {
        font-size: 13px;
        color: #D1D5DB;
        margin-top: 4px;
    }

    .vib-badge {
        background-color: rgba(255, 255, 255, 0.15);
        border: 1px solid rgba(255, 255, 255, 0.3);
        padding: 6px 14px;
        border-radius: 20px;
        font-size: 12px;
        font-weight: 600;
        color: #FFFFFF;
    }

    /* Khung Metric Thống kê Bảng tính trả góp */
    .metric-card {
        background-color: #FFFFFF;
        padding: 18px 20px;
        border-radius: 10px;
        border: 1px solid #E2E8F0;
        box-shadow: 0px 2px 4px rgba(0,0,0,0.02);
    }
    
    .metric-label {
        font-size: 13px;
        color: #64748B;
        font-weight: 600;
        margin-bottom: 6px;
    }

    .metric-value {
        font-size: 22px;
        font-weight: 700;
        color: #002D62;
    }
    </style>
""", unsafe_allow_html=True)

# ==========================================
# 3. THANH ĐIỀU HƯỚNG (SIDEBAR)
# ==========================================
with st.sidebar:
    # Logo & Tiêu đề khối
    st.markdown("""
        <div style="text-align: center; padding: 10px 0;">
            <div style="width: 45px; height: 45px; background-color: #002D62; color: #F37021; 
                        display: inline-flex; align-items: center; justify-content: center; 
                        transform: rotate(45deg); border-radius: 6px; font-weight: bold; font-size: 20px;">
                <span style="transform: rotate(-45deg);">%</span>
            </div>
            <h3 style="margin-top: 15px; margin-bottom: 0; color: #0f172a; font-size: 18px;">QUẢN LÝ KHÁCH HÀNG</h3>
            <p style="color: #64748b; font-size: 12px; margin-top: 2px;">NHÓM CHIẾN LƯỢC</p>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("<br>", unsafe_allow_html=True)
    st.caption("ĐIỀU HƯỚNG BẢNG ĐIỀU KHIỂN")

    # Chọn Tab chức năng
    selected_page = st.radio(
        label="Menu Navigation",
        options=["💳 Đăng ký nhu cầu vay", "🧮 Bảng tính trả góp", "⚙️ Quản trị Admin"],
        label_visibility="collapsed"
    )

# ==========================================
# 4. BANNER TIÊU ĐỀ CHUNG
# ==========================================
st.markdown("""
    <div class="vib-banner">
        <div>
            <div class="vib-banner-title">🏛️ NHÓM CHIẾN LƯỢC - HỆ THỐNG PHÁT TRIỂN KHÁCH HÀNG</div>
            <div class="vib-banner-sub">Giải pháp thu thập & phân tích nhu cầu vay vốn tài chính cao cấp</div>
        </div>
        <div class="vib-badge">DỰ ÁN TÀI CHÍNH 2026</div>
    </div>
""", unsafe_allow_html=True)

# ==========================================
# 5. NỘI DUNG TỪNG TRANG
# ==========================================

# ------------------------------------------
# TRANG 1: ĐĂNG KÝ NHU CẦU VAY
# ------------------------------------------
if selected_page == "💳 Đăng ký nhu cầu vay":
    st.caption("DỊCH VỤ TÀI CHÍNH CÁ NHÂN")
    st.title("💳 ĐĂNG KÝ TƯ VẤN VAY VỐN")
    st.write("Khách hàng vui lòng điền đầy đủ thông tin bên dưới để Nhóm Chiến Lược hỗ trợ gói vay tối ưu nhất.")
    
    st.markdown("---")
    st.subheader("📋 Thông tin hồ sơ vay")
    st.caption("Điền thông tin chính xác để chuyên viên thẩm định liên hệ nhanh nhất")

    with st.form("loan_registration_form"):
        col1, col2 = st.columns(2)

        with col1:
            name = st.text_input("👤 Họ và tên khách hàng (*)", placeholder="Nguyễn Văn A")
            phone = st.text_input("📱 Số điện thoại liên hệ (*)", placeholder="0901234567")
            city = st.text_input("📍 Tỉnh / Thành phố sinh sống", placeholder="Ví dụ: Hà Nội, TP.HCM")

        with col2:
            product = st.selectbox(
                "🏷️ Nhu cầu sản phẩm vay (*)",
                ["Vay Tín Chấp Theo Lương", "Vay Mua Ô Tô (VIB Auto Loan)", "Vay Mua Nhà / Bất Động Sản", "Vay Sửa Chữa Nhà", "Vay Kinh Doanh"]
            )
            amount = st.number_input("💰 Số tiền đề xuất vay (VNĐ) (*)", min_value=10000000, value=100000000, step=10000000)
            term = st.selectbox("⏰ Thời hạn vay mong muốn", ["12 tháng", "24 tháng", "36 tháng", "48 tháng", "60 tháng", "120 tháng"])

        submit_btn = st.form_submit_button("🚀 Gửi đăng ký tư vấn")

        if submit_btn:
            if not name or not phone:
                st.error("Vui lòng nhập đầy đủ Họ tên và Số điện thoại!")
            else:
                st.success(f"Cảm ơn ông/bà **{name}**! Thông tin đăng ký vay **{amount:,.0f} VNĐ** đã được gửi thành công.")

# ------------------------------------------
# TRANG 2: BẢNG TÍNH TRẢ GÓP
# ------------------------------------------
elif selected_page == "🧮 Bảng tính trả góp":
    st.caption("CÔNG CỤ HỖ TRỢ TÀI CHÍNH")
    st.title("🧮 BẢNG TÍNH LÃI VÀ GỐC TRẢ GÓP")
    st.write("Công cụ tính khoản vay theo dư nợ giảm dần do Nhóm Chiến Lược phát triển.")

    st.markdown("---")

    # Nhập thông số tính toán
    col_a, col_b, col_c = st.columns([1.5, 1.5, 2])

    with col_a:
        loan_amount = st.number_input("Số tiền vay (VNĐ)", min_value=10000000, value=200000000, step=10000000)
    with col_b:
        interest_rate = st.number_input("Lãi suất (%/năm)", min_value=1.0, max_value=25.0, value=8.5, step=0.1)
    with col_c:
        months = st.slider("Thời gian vay (Tháng)", min_value=6, max_value=120, value=36, step=6)

    # Tính toán công thức dư nợ giảm dần
    goc_co_dinh = loan_amount / months
    lai_thang_dau = loan_amount * (interest_rate / 100) / 12
    tong_thang_dau = goc_co_dinh + lai_thang_dau

    st.markdown("<br>", unsafe_allow_html=True)

    # Hiển thị 3 ô Metric kết quả
    m1, m2, m3 = st.columns(3)

    with m1:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">📌 Gốc cố định hàng tháng</div>
                <div class="metric-value">{goc_co_dinh:,.0f} VNĐ</div>
            </div>
        """, unsafe_allow_html=True)

    with m2:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">💸 Lãi tháng đầu tiên</div>
                <div class="metric-value">{lai_thang_dau:,.0f} VNĐ</div>
            </div>
        """, unsafe_allow_html=True)

    with m3:
        st.markdown(f"""
            <div class="metric-card">
                <div class="metric-label">🔥 Tổng trả tháng đầu</div>
                <div class="metric-value" style="color: #F37021;">{tong_thang_dau:,.0f} VNĐ</div>
            </div>
        """, unsafe_allow_html=True)

    st.caption("<br>⚡ <i>Bảng tính mang tính tham khảo. Chi tiết sẽ được Chuyên viên thẩm định phê duyệt chính xác theo hồ sơ.</i>", unsafe_allow_html=True)

# ------------------------------------------
# TRANG 3: QUẢN TRỊ ADMIN
# ------------------------------------------
else:
    st.title("⚙️ Bảng Quản Trị Admin")
    st.info("Chức năng dành cho Quản lý danh sách Lead vay vốn.")
