import streamlit as st
from streamlit_option_menu import option_menu # Install: pip install streamlit-option-menu

# --- PAGE CONFIG ---
st.set_page_config(
    page_title="Yaseen Elsedawy | Cybersecurity Portfolio",
    page_icon="🛡️", # Add a relevant emoji/icon
    layout="wide"
)

# --- IMAGE HANDLING ---
# IMPORTANT: Replace this placeholder URL with the actual URL where your image is hosted online
# OR place 'Yaseen.png' in the same folder as your script and use image_path = "Yaseen.png"
image_path = "Yaseen.png" # Replace with your actual image URL or local path if run locally
# Example using a local path (if Yaseen.png is in the same folder):
# image_path = "Yaseen.png"
# Example using a local path (if Yaseen.png is in an 'images' subfolder):
# image_path = "images/Yaseen.png"

# --- HEADER ---
with st.container():
    col1, col2 = st.columns([3, 1], gap="medium")
    with col1:
        st.title("👋 Hello, I'm Yaseen Elsedawy")
        st.subheader("💼 Cybersecurity Engineer | 🚀 Tech Enthusiast | 📍 Nasr City, Cairo, Egypt")
        st.write("""
        I’m a **dedicated and versatile Cybersecurity Engineer** with **1 year and a half** of hands-on experience in implementing, configuring, and managing a variety of security solutions in enterprise environments.

        Currently working at **Intercom Enterprises** as a **Technical Security Engineer**, where I design secure architectures, provide technical support and training, and maintain robust cybersecurity infrastructure.

        Certified across multiple domains and always learning, I focus on **automation**, **endpoint protection**, **SIEM**, and **vulnerability management** to enhance security operations.
        """)

    with col2:
        st.image(image_path, width=200, caption="Yaseen Elsedawy") # Added caption

st.write("---") # Divider

# --- NAVIGATION TABS ---
selected_tab = option_menu(
    menu_title=None, # Hides the default menu title
    options=["About", "Experience & Skills", "Projects", "Contact"],
    icons=["person-badge", "briefcase", "code-slash", "envelope-at"], # Bootstrap Icons
    orientation="horizontal",
    styles={
        "container": {"padding": "0!important", "background-color": "#fafafa"},
        "icon": {"color": "orange", "font-size": "18px"},
        "nav-link": {"font-size": "18px", "text-align": "center", "margin":"0px", "--hover-color": "#eee"},
        "nav-link-selected": {"background-color": "#02ab21"}, # Green accent for selected tab
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
        """) # Using markdown bullet points

    with st.expander("🧭 **SOC L1 — Security Meter** (Sep 2023 – Dec 2023)"):
        st.markdown("""
        *   Monitored Security Operations Center (SOC) alerts using SIEM tools.
        *   Analyzed netflow data, system logs, alerts, and firewall events to detect potential threats.
        *   Escalated unresolved security incidents to L2/L3 analysts according to defined procedures.
        *   Generated daily, weekly, and monthly security reports summarizing key events and trends.
        """) # Using markdown bullet points

    st.divider() # Visual separator

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
        """) # Added Scan Orchestration to Use Cases
        st.markdown("#### Infrastructure & OS")
        st.markdown("""
        *   **Virtualization:** VMware vSphere/ESXi
        *   **Operating Systems:** Windows Server, Linux (Ubuntu, CentOS)
        """)
   
    # --- EDUCATION SECTION ---
    st.divider() # Add divider before Education
    st.subheader("🎓 Education")
    st.markdown("""
    *   **Master's Degree** — Tanta University (Ongoing)
        *   _Tanta, Egypt_
    *   **Bachelor’s Degree in Communications & Electronics Engineering** — Thebes Academy
        *   _Cairo, Egypt_
    *   **Cybersecurity Diploma** — National Telecommunications Institute (NTI)
        *   _Cairo, Egypt_
    """)

# --- PROJECTS TAB ---
if selected_tab == "Projects":
    st.subheader("🚀 Major Deployment & Consultation Projects")
    st.write("Hands-on experience implementing and configuring security solutions for diverse clients.")

    with st.expander("🏦 **CIB Bank** - Tenable Support"):
        st.markdown("""
        *   **Focus:** Post-deployment support and optimization.
        *   **Key Activities:** Provided expert technical support and troubleshooting for the bank's Tenable SC+ deployment.
        """)

    with st.expander("🏦 **Attijariwafa Bank Egypt** - Tenable Support"):
        st.markdown("""
        *   **Technologies:** Tenable Security Center
        *   **Key Activities:** Delivered post-deployment support and technical assistance for Tenable SC, ensuring smooth vulnerability management operations.
        """)

    with st.expander("🏦 **Egyptian Arab Land Bank** - Endpoint Security Support"):
        st.markdown("""
        *   **Technologies:** Kaspersky Security Center
        *   **Key Activities:** Provided ongoing support and optimization for Kaspersky endpoint protection platform.
        """)

    with st.expander("🏦 **QNB Bank** - Patch Management Enhancement"):
        st.markdown("""
        *   **Technologies:** Ivanti Patch Management
        *   **Key Activities:** Enhanced and supported patching cycles, helping improve overall security posture through effective Ivanti deployment.
        """)

    with st.expander("🗳️ **National Election Authority (NEA)** - Vulnerability Management Setup"):
        st.markdown("""
        *   **Technologies:** Tenable Security Center Plus (SC+), Tenable Nessus Scanners, Tenable Nessus Manager
        *   **Key Activities:** Installed and configured the complete Tenable VM suite for infrastructure scanning and management.
        """)

    with st.expander("🛢️ **Oil & Gas Sector Projects (Multiple Companies)** - Patching & Network"):
        st.markdown("""
        *   **Technologies:** Ivanti Patch Management, Ivanti Xtraction, Tenable Nessus Pro, F5 LTM
        *   **Scope:** Delivered solutions across **8 different companies** in the sector.
        *   **Key Activities:** Configured patch management and reporting tools, deployed Nessus Pro for vulnerability scanning, implemented F5 Load Balancers for **2 organizations**.
        """)

    with st.expander("🏢 **Misr Insurance Holding Company** - Endpoint & Network Consultation"):
        st.markdown("""
        *   **Technologies:** Kaspersky Endpoint Security, Kaspersky Hybrid Cloud, F5 LTM
        *   **Key Activities:** Provided expert consultation and configuration services for endpoint security (including hybrid cloud) and network load balancing.
        """)

    with st.expander("🏭 **United Gas Derivatives Company** - Advanced Threat Detection"):
        st.markdown("""
        *   **Technologies:** Trend Micro Deep Discovery Analyzer (DDAN) Sandbox
        *   **Key Activities:** Deployed and configured the DDAN sandbox solution for in-depth analysis of potentially malicious files and URLs.
        """)

    with st.expander("🔐 **Cairo Metro** - Endpoint Security Implementation"):
        st.markdown("""
        *   **Technologies:** Trend Micro Apex One, Apex Central, Deep Security Manager
        *   **Key Activities:** Full installation & configuration, database migration, license activation, agent troubleshooting, policy deployment, health checks.
        """)

    with st.expander("🛡️ **Presidency HA Project** - F5 High Availability Implementation"):
        st.markdown("""
        *   **Focus:** Ensuring business continuity for critical security infrastructure using F5 solutions.
        *   **Key Activities:** Designed and implemented F5 High Availability (HA) configurations, performed rigorous failover testing, created comprehensive documentation.
        """)


    with st.expander("📧 **VALU** -Email Security.cloud"):
        st.markdown("""
        *   **Technologies:** Symantec Email Security.cloud, Office 365
        *   **Key Activities:** Integrated cloud email security with O365, configured mail flow rules, implemented Data Loss Prevention (DLP) policies, enhanced anti-spam effectiveness.
        """)


    st.divider()
    st.subheader("⚙️ Automation Projects")
    st.write("Utilizing scripting to improve efficiency and integrate security tools.")

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

    # --- NEWLY ADDED PROJECT ---
    with st.expander("⏲️ **Tenable Scan Initiation & Monitoring**"): # Added icon
        st.markdown("""
        *   **Technology:** Scripting (e.g., Python using Tenable API)
        *   **Functionality:** Developed a script to programmatically trigger vulnerability scans in Tenable (Nessus/SC+) and monitor their completion status.
        *   **Benefit:** Enables scheduled or on-demand scanning outside the Tenable UI and integrates scan status into automated workflows.
        """)
    # --- END OF NEW PROJECT ---

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
