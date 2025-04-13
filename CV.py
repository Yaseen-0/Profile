import streamlit as st
from streamlit_option_menu import option_menu # Install: pip install streamlit-option-menu

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Yaseen Elsedawy | Cybersecurity Portfolio",
    page_icon="🛡️",
    layout="wide"
)

# --- IMAGE HANDLING ---
image_path = "Yaseen.png"

# --- HEADER ---
with st.container():
    col1, col2 = st.columns([3, 1], gap="medium")
    with col1:
        st.title("👋 Hello, I'm Yaseen Elsedawy")
        st.subheader("💼 Cybersecurity Engineer | 🚀 Tech Enthusiast | 📍 Nasr City, Cairo, Egypt")
        st.write("""
        I'm a **dedicated and versatile Cybersecurity Engineer** with **about 2 years** of hands-on experience in implementing, configuring, and managing a variety of security solutions in enterprise environments.

        Currently working at **Intercom Enterprises** as a **Technical Security Engineer**, where I design secure architectures, provide technical support and training, and maintain robust cybersecurity infrastructure.

        Certified across multiple domains and always learning, I focus on **automation**, **endpoint protection**, **SIEM**, and **vulnerability management** to enhance security operations.
        """)

    with col2:
        st.image(image_path, width=200, caption="Yaseen Elsedawy")

st.write("---")

# --- NAVIGATION TABS ---
selected_tab = option_menu(
    menu_title=None,
    options=["About", "Experience & Skills", "Client Engagements", "Contact"],
    icons=["person-badge", "briefcase", "building", "envelope-at"],
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"},
    }
)

# --- ABOUT TAB ---
if selected_tab == "About":
    st.info("Navigate through the tabs above to learn more about my experience, skills, projects, and how to get in touch.", icon="ℹ️")
    st.markdown("### My Focus Areas:")
    st.markdown("""
    *   🛡️ **Security Architecture & Implementation:** Designing and deploying robust security solutions (Endpoint, SIEM, Cloud Security).
    *   ⚙️ **Automation:** Leveraging Python, Bash, and PowerShell to streamline security operations and tasks.
    *   🔍 **Vulnerability Management:** Identifying and remediating security weaknesses using tools like Tenable Nessus and SC+.
    *   ☁️ **Cloud Security:** Experience with securing hybrid cloud environments (Kaspersky Hybrid Cloud).
    *   🤝 **Collaboration & Training:** Effectively communicating technical concepts and providing knowledge transfer.
    """)


# --- EXPERIENCE & SKILLS TAB ---
if selected_tab == "Experience & Skills":
    st.subheader("💼 Work Experience")

    with st.expander("🔧 **Technical Security Engineer — Intercom Enterprises** (Dec 2023 – Present)"):
        st.markdown("""
        *   Deployed, configured, and monitored network and security solutions (Trend Micro, Fortinet, Tenable, etc.).
        *   Delivered customer knowledge transfer sessions and on-the-job training for security products.
        *   Maintained and troubleshooted IT security infrastructure across diverse client environments.
        *   Designed security architectures tailored to customer requirements.
        *   Provided Level 2/3 technical support for implemented solutions.
        """)

    with st.expander("🧭 **SOC L1 — Security Meter** (Sep 2023 – Dec 2023)"):
        st.markdown("""
        *   Monitored Security Operations Center (SOC) alerts using SIEM tools.
        *   Analyzed netflow data, system logs, alerts, and firewall events to detect potential threats.
        *   Escalated unresolved security incidents to L2/L3 analysts according to defined procedures.
        *   Generated daily, weekly, and monthly security reports summarizing key events and trends.
        """)

    st.divider()

    st.subheader("🛠️ Technical Skills")

    col1, col2 = st.columns(2, gap="medium")

    with col1:
        st.markdown("#### Security Platforms & Tools")
        st.markdown("""
        *   **Endpoint Security:** Trend Micro (Apex One, Deep Security), Kaspersky (EDR, KSC, Hybrid Cloud)
        *   **SIEM:** Fortinet FortiSIEM
        *   **Vulnerability Management:** Tenable (Nessus Pro, Security Center/SC+,Nessus Manager)
        *   **Email Security:** Symantec Email Security.cloud
        *   **Network Security:** F5 LTM (Load Balancing), Basic Firewall Concepts (Palo Alto, FortiGate - *exposure via migration project*)
        *   **Patch Management:** Ivanti Security Controls (Patch Management), Ivanti Xtraction
        *   **Sandboxing:** Trend Micro Deep Discovery Analyzer (DDAN)
        """)

    with col2:
        st.markdown("#### Automation & Scripting")
        st.markdown("""
        *   **Languages:** Python, Bash, PowerShell
        *   **Use Cases:** Excel Automation (Data Comparison, Deduplication, Extraction), Configuration Migration (Testing Phase), Task Automation (Patching Integration), Scan Orchestration
        """)
        st.markdown("#### Infrastructure & OS")
        st.markdown("""
        *   **Virtualization:** VMware vSphere/ESXi
        *   **Operating Systems:** Windows Server, Linux (Ubuntu, CentOS)
        """)
   
    st.divider()
    st.subheader("🎓 Education")
    st.markdown("""
    *   **Master's Degree** — Tanta University (Ongoing)
    *   **Bachelor's Degree in Communications & Electronics Engineering** — Thebes Academy
    *   **Cybersecurity Diploma** — National Telecommunications Institute (NTI)
    """)

# --- CLIENT ENGAGEMENTS TAB ---
if selected_tab == "Client Engagements":
    st.subheader("🏢 Select Client Engagements")
    st.write("I've had the privilege to work with these notable organizations on security implementations:")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        - 🏦 CIB Bank
        - 🏦 Attijariwafa Bank Egypt
        - 🏦 Egyptian Arab Land Bank
        - 🏦 QNB Bank
        - 🗳️ National Election Authority (NEA)
        """)
    
    with col2:
        st.markdown("""
        - 🛢️ Oil & Gas Sector Projects (9 companies)
        - 🏢 Misr Insurance Holding Company
        - 🏭 United Gas Derivatives Company
        - 🚇 Cairo Metro
        - 🏛️ Presidency
        - 📧 VALU
        """)
    
    st.divider()
    st.subheader("⚙️ Technical Projects & Automation")
    st.write("Key technical implementations and automation solutions developed for clients:")
    
    with st.expander("📊 **Excel Automation Tool** - Data Processing"):
        st.markdown("""
        *   **Technology:** Python
        *   **Functionality:** Created a script to automatically compare data across different Excel sheets, highlight duplicate entries, and extract unique records.
        *   **Benefit:** Significantly streamlined data validation processes and reduced manual comparison effort.
        """)

    with st.expander("🔄 **Palo Alto ➡️ FortiGate Migration Tool** - Configuration Conversion (Testing)"):
        st.markdown("""
        *   **Technology:** Scripting (Python/Bash/PowerShell)
        *   **Functionality:** Developed a proof-of-concept tool to automate the conversion of specific Palo Alto firewall configurations (NAT, Policies, Objects) into a format potentially compatible with FortiGate.
        *   **Benefit:** Explored methods to accelerate firewall migration validation and reduce manual reconfiguration errors during testing phases.
        """)

    with st.expander("🔍 **Tenable + Ivanti Patch Automation** - Vulnerability Remediation"):
        st.markdown("""
        *   **Technologies:** Tenable Nessus/SC+ API, Ivanti Security Controls API/CLI
        *   **Functionality:** Created automation scripts to correlate vulnerability data from Tenable scans with patching capabilities in Ivanti.
        *   **Benefit:** Aimed to automate the patching lifecycle for identified vulnerabilities, reducing remediation time and improving security compliance posture.
        """)

    with st.expander("⏲️ **Tenable Scan Initiation & Monitoring**"):
        st.markdown("""
        *   **Technology:** Scripting (e.g., Python using Tenable API)
        *   **Functionality:** Developed a script to programmatically trigger vulnerability scans in Tenable (Nessus/SC+) and monitor their completion status.
        *   **Benefit:** Enables scheduled or on-demand scanning outside the Tenable UI and integrates scan status into automated workflows.
        """)
        
# --- CONTACT TAB ---
if selected_tab == "Contact":
    st.subheader("📬 Get In Touch")
    st.write("Feel free to reach out via email, phone, or connect with me online!")

    col1, col2 = st.columns([1, 2])

    with col1:
        st.image(image_path, width=150)

    with col2:
        st.markdown("### 📧 Email")
        st.markdown("[yaseen.elsedawy@intercom.com.eg](mailto:yaseen.elsedawy@intercom.com.eg)")

        st.markdown("### 📞 Phone")
        st.markdown("[+20 1011505081](tel:+201011505081)")

        st.markdown("### 💼 LinkedIn")
        st.markdown("[linkedin.com/in/yaseen-elsedawy](https://www.linkedin.com/in/yaseen-elsedawy-622425147/)")

        st.markdown("### 💻 GitHub")
        st.markdown("[github.com/Yaseen-0](https://github.com/Yaseen-0)")


# --- FOOTER ---
st.markdown("---")
st.markdown("""
<div style='text-align: center; font-size: 0.85rem;'>
    © 2025 Yaseen Elsedawy
</div>
""", unsafe_allow_html=True)
