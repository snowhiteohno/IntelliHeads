import os

# Data for Testimonials
academic_customers = [
    "A K G Engineering College, Ghaziabad", "IILM Academy Of Higher Learning, Gr. Noida",
    "ABES Engineering College, Ghaziabad", "IIMT Group of colleges, Meerut",
    "Al-Falah School Of Engg & Tech., Faridabad", "International College of Girls, Jaipur",
    "Amarapali Institute, Nainital", "IMS College Of Engg. & Tech., Ghaziabad",
    "Ambala college of Engg. & Apllied Sciences,Ambala", "Indian Institute Of Technology, New Delhi",
    "Ambedkar Institute Of Technology, New Delhi", "Indian Institute Of Technology, Pawai, Mumbai",
    "Amity University, Noida", "Indraprastha Engg. College, Ghaziabad",
    "Anand Engineering College, Agra", "ITM University, Gurgoan, Haryana",
    "Apeejay College Of Engg., Sohna, Faridabad", "ITS, Gr. Noida",
    "B R Nahta College Of Pharmacy, MP", "Jaipur National University, Jaipur",
    "Bhilai Institute of technology, Durg (C.G.)", "Jamia Milia Islamia, New Delhi",
    "BMAS Engg. College, Agra", "Jamia Hamdarad University, New Delhi",
    "B. M. S. College of Engineering, Bangalore", "JP Institute Of Engg & Technology, Meerut",
    "Babu Banarsi Das Institute Of Tech., Ghaziabad", "K N G D Modi Engg College, Modinagar",
    "Bhagwan Parshuram College Of Engg., Gohna", "KIET, Ghaziabad",
    "Bhagwan Parshuram Institute of technology ,New Delhi", "Krishna Engineering College, Ghaziabad",
    "BITS, Bhiwani", "Lingaya's University, Faridabad",
    "Career Institute Of Tech. & Mgt., Faridabad", "Lord Krishna Inst. Of Technology, Ghaziabad",
    "College of Science & technology, Jhansi", "Makina institute of technology,Mumbai",
    "Deenbandhu Chhotu Ram Univ., Murthal", "Manav Rachna International University, Faridabad",
    "Delhi College of Engineering, Delhi", "Meerut Institute Of Engg. & Technology, Meerut",
    "D J College Of Engg. & Technology, Modinagar", "Meerut Institute Of Technology, Meerut",
    "DIT School of Engg. Greater Noida", "Modinagar Institute of technology,Modinagar",
    "Deharadun Institute Of Technology, Deharadun", "MIT, Moradabad",
    "Dev Bhomi Institute Of Technology, Deharadun", "Nalanda Medical College, Patna",
    "Electronics Services & Training Center, Nainital", "National Institute Of Technology, Kurushetra",
    "Institute of Engg. & Tech, Agra Univ., Khandari", "National Institute Of Fashion Tech, New Delhi",
    "G B Pant Engineering College, New Delhi", "National Institute Of Fashion Tech, Rai Barelly",
    "G L Bajaj Institute Of Tech. & Mgt., Gr. Noida", "National Institute Of Gems & Jewelry Design, Delhi",
    "Galgotia College Of Engg. & Tech., Gr. Noida", "National Institute of Rock machines,Karnataka",
    "Gold Field Institute Of Tech. & Mgt. Faridabad", "Nirma University, Ahmedabad",
    "Greater Noida Institute of Technology, Gr. Noida", "Noida Institute Of Engg. & Tech., Gr. Noida",
    "GNIT Girls Institute of technology, Greater Noida", "Northern India Engg. College, New Delhi",
    "Guru Gobind Singh Indraprastha University, Delhi", "NSIT, New Delhi",
    "Guru Jumbeshwar University, Hissar", "PD Institute , Jaipur",
    "H R Institute Of Technology, Ghaziabad", "PDM College Of Engineering, Bahadurgarh, Haryana",
    "HIET, Kaithal, Haryana", "PERL Academy of fashion, Jaipur",
    "Hi-Tech Institute Of Technology, Ghaziabad", "Punjab College Of Engg. & Tech., Mohali",
    "IEC College Of Engineering, Gr. Noida", "Punjab Govt. College Of Physical Edn., Punjab",
    "Satya College of Engg. Technology, Palwal", "R.D. Engg College, Ghaziabad",
    "Saraswati Institute of Engg. & Tech., Ghaziabad", "R.D. Foundation Group of Institute, Modinagar",
    "Sh. Udham Singh College Of Engg. & Tech.,Punjab", "Vivekanand Institute of Technology, Ghaziabad",
    "Sherwood Institute Of Technology, Lucknow", "VIET, Dadri, Ghaziabad",
    "Shri Ganpati Institute Of Tech., Ghaziabad", "West Bangal Univ. Of Technology., Kolkata",
    "Skyline Institute Of Engg. & Tech., Gr. Noida", "Thapar Institute Of Technology, Patiyala",
    "Sunderdeep Engg College , Ghaziabad", "Uttarakhand Dual Trust Educational Society,Roorkee",
    "Swami vivekanand subharti university, Meerut", "Univ. Institute Of Engg. & Tech., Chandigarh",
    "TITS, Bhiwani", "Universal Institute of technology,Hisar",
    "TERI Univeristy, New Delhi", "Vaish College Of Engg., Rohtak, Haryana",
    "NITTTR, Chandigarh", "Venketshwara Institute Of Technology, Meerut"
]

commercial_customers = [
    "Amoliq Jewelers, New Delhi", "Gmk Exim Pvt. Ltd., Mumbai", "Vision Gems Pvt. Ltd., Jaipur",
    "A K Gems & Jewellers , Jaipur", "Sangini Diamond Jewellery (SDJ), Mumbai", "Gold Sukh, Jaipur",
    "Lurgi India Pvt. Ltd., Delhi", "2PKM Architects, Mangalore", "Bhumi Builders, Chennai",
    "JP Sports International Limited, Gr. Noida", "CPWD, Ghaziabad", "Bechtal International, Bangalore",
    "Jacobs International, Mumbai", "Honeywell International, Gurgaon", "Foster Wheeler Ltd., Mumbai",
    "Alstom Projects India Ltd, Mumbai", "CHD Developers Ltd, New Delhi", "HB Estate Developers Ltd., Gurgaon",
    "Aiprakash Associates Limited, Noida", "Sobha Developers Ltd., Bangalore", "L & T Limited, Chennai",
    "Ananat Builders, Ahemadabad", "Geo Informatics & Consultants, Noida", "A K Systems, Bangalore",
    "United Spirit Limited, Bangalore", "Corus India Limited, Gurgoan", "Godfrey Philliphs India Limited, Mumbai",
    "VELDEL Engineers & Construcation Limited.", "Stryker Global Technology Center, Gurgaon", "Softcell Technologies, Bangalore",
    "Vista Tech Solution P. Ltd., New Delhi", "Samsung India Limited, Bangalore", "Chicco, Hyderabad",
    "Peg-Perego, Ahamdbad", "Magneti Marelli Motherson Auto Sys Ltd., Pune", "Hero Motors, Gurgaon",
    "Mahindra & Mahindra, Faridabad", "Bajaj Auto, Mumbai"
]

international_customers = [
    "AFLO trading company Ltd, Baghdad-Iraq", "Aspen Multi-System Corp, Philippines 1500",
    "B & B Trading Concern (P) Ltd.,Kathmandu Nepal", "Bio Medical Science Estb, Riyad, KSA",
    "INTERLAB sarl, Lebanon", "Iraqi Biotechnology Co. Ltd. Baghdad, Iraq",
    "Khaled Badran Trading Est. Riyadh, Saudi Arabia", "KRIJON shpk, ALBANIA",
    "Medical Scientific and Chemicals Corp., Jordan", "Misan University , Emara, Iraq",
    "University of Anbar , Iraq", "INTECK NIG LIMITED, Nigeria"
]

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Update navbar
if '<li><a href="testimonials.html">Testimonials</a></li>' not in content:
    content = content.replace('<li><a href="#events">Events</a></li>', '<li><a href="testimonials.html">Testimonials</a></li>\n      <li><a href="#events">Events</a></li>')
    content = content.replace('<li><a href="index.html#events">Events</a></li>', '<li><a href="testimonials.html">Testimonials</a></li>\n      <li><a href="index.html#events">Events</a></li>')

# Extract header and footer
head_split = content.split('<section id="hero">')
header = head_split[0]
footer = "<footer>" + content.split('<footer>')[1]

# Make header colorful gradient CSS
custom_css = """
<style>
.gradient-text {
  background: linear-gradient(90deg, var(--teal) 0%, var(--copper) 100%);
  -webkit-background-clip: text;
  -webkit-text-fill-color: transparent;
  display: inline-block;
}
.text-only-section {
  padding: 40px;
  background: var(--ink-mid);
  border-radius: 12px;
  margin-bottom: 30px;
  border-left: 4px solid var(--teal);
  box-shadow: 0 4px 20px rgba(0,0,0,0.3);
}
.text-only-section h2 {
  font-size: 28px;
  margin-bottom: 20px;
  color: var(--white);
}
.text-only-section p {
  color: #8a9fb8;
  font-size: 16px;
  line-height: 1.8;
}
</style>
"""
if "gradient-text" not in header:
    header = header.replace('</head>', custom_css + '\n</head>')

pages = {
    'digsilent-powerfactory.html': {
        'title': 'DIgSILENT <span class="gradient-text">PowerFactory</span>',
        'subtitle': 'The standard software for power system analysis',
        'type': 'mixed',
        'sections': [
            {'title': 'Advanced Power System Analysis', 'text': 'PowerFactory is a leading power system analysis software application for use in analysing generation, transmission, distribution and industrial systems.', 'image': 'img-powerfactory.png'},
            {'title': 'Comprehensive Software Solution', 'text': 'PowerFactory is easy to use, fully Windows compatible and combines reliable and flexible system modelling capabilities with state-of-the-art algorithms.', 'image': 'feat-software.png'}
        ]
    },
    'digsilent-applications.html': {
        'title': 'PowerFactory <span class="gradient-text">Applications</span>',
        'subtitle': 'Versatile solutions for diverse power grids',
        'type': 'text',
        'sections': [
            {'title': 'Transmission & Distribution Networks', 'text': 'PowerFactory offers a complete suite of functions for studying large-scale transmission networks and integrating new generation. It includes advanced tools for optimal power flow, contingency analysis, and dynamic security assessment. For distribution networks, it includes comprehensive tools for voltage profile optimization, network reinforcement, protection coordination, and the seamless integration of distributed energy resources like rooftop solar and electric vehicle charging infrastructure.'},
            {'title': 'Industrial Grids & Renewables', 'text': 'PowerFactory is perfectly suited to the analysis of complex industrial networks, from steady-state load flow to highly detailed electromagnetic transients. It assists in motor starting analysis, short-circuit calculations, and arc flash hazard assessment. Furthermore, it provides comprehensive models for all types of renewable energy sources, supporting the transition to a sustainable energy future through detailed grid compliance studies and hybrid energy system modeling.'}
        ]
    },
    'digsilent-features.html': {
        'title': 'PowerFactory <span class="gradient-text">Features</span>',
        'subtitle': 'State-of-the-art algorithms and modelling',
        'type': 'mixed',
        'sections': [
            {'title': '<span class="gradient-text">Load Flow & Stability</span>', 'text': 'The software includes highly robust load flow algorithms for AC and DC networks. The stability analysis module offers full time-domain simulation capabilities for transient and dynamic stability studies, including RMS and EMT simulations.', 'image': 'feat-loadflow.png'},
            {'title': '<span class="gradient-text">Harmonics & Power Quality</span>', 'text': 'PowerFactory provides advanced tools for harmonics analysis, filter sizing, and power quality assessment. It accurately models non-linear devices and frequency-dependent components to ensure grid compliance.', 'image': 'feat-harmonics.png'},
            {'title': '<span class="gradient-text">Electromagnetic Transients (EMT)</span>', 'text': 'Perform precise time-domain simulations of electromagnetic transients. Analyze lightning strikes, switching overvoltages, and sub-synchronous resonance with highly detailed component models and accelerated simulation engines.', 'image': 'feat-emt.png'},
            {'title': '<span class="gradient-text">Protection Modeling</span>', 'text': 'Comprehensive protection modeling tools including time-current characteristic curves on logarithmic grids, relay coordination, and automated protection sweep functionality to ensure the highest safety and reliability of your network.', 'image': 'feat-protection.png'},
            {'title': '<span class="gradient-text">Renewable Energy Integration</span>', 'text': 'Advanced capabilities for modeling wind farms, solar PV arrays, and battery energy storage systems. Perform steady-state, dynamic, and transient analysis to ensure seamless grid integration and code compliance.', 'image': 'feat-renewables.png'}
        ]
    },
    'target3001-main.html': {
        'title': 'TARGET <span class="gradient-text">3001!</span>',
        'subtitle': 'PCB Design Software for Engineering Professionals',
        'type': 'mixed',
        'sections': [
            {'title': 'End-to-End PCB Design', 'text': 'TARGET 3001! is an integrated EDA software for PCB design. It combines schematic capture, PCB layout, mixed-mode simulation, and 3D view in a single project file.', 'image': 'img-target3001.png'},
            {'title': 'Efficient Workflow', 'text': 'Designed for efficiency, TARGET 3001! offers a seamless workflow from initial idea to manufacturing data. Its intuitive interface and powerful features make it the ideal choice.', 'image': 'ref-basic.jpg'}
        ]
    },
    'target3001-applications.html': {
        'title': 'TARGET 3001! <span class="gradient-text">Applications</span>',
        'subtitle': 'From schematics to 3D and front panels',
        'type': 'text',
        'sections': [
            {'title': 'PCB Layout & Rapid Prototyping', 'text': 'Create professional PCB layouts with advanced routing tools. The software streamlines the transition from schematic to board, supporting complex multi-layer designs, precise trace width calculations, and strict design rule checks (DRC). By eliminating data conversion steps, you can rapidly iterate on prototypes, saving valuable time and reducing the risk of errors between design phases.'},
            {'title': 'Simulation & Enclosure Integration', 'text': 'The integrated mixed-mode simulation allows you to thoroughly test your analog and digital circuits before committing to hardware production, ensuring functionality and performance. Beyond the PCB itself, TARGET 3001! includes a dedicated module for designing custom front panels and exploring true 3D visualizations, allowing you to seamlessly integrate your electronics into professional enclosures with perfectly aligned mechanical controls and connectors.'}
        ]
    },
    'target3001-features.html': {
        'title': 'TARGET 3001! <span class="gradient-text">Features</span>',
        'subtitle': 'Powerful tools for complex designs',
        'type': 'mixed',
        'sections': [
            {'title': '<span class="gradient-text">Schematic Capture & Autorouter</span>', 'text': 'Draw complex schematics with an extensive component library. The powerful built-in autorouter handles complex routing tasks automatically, optimizing trace paths for single, double, and multi-layer boards.', 'image': 'ref-schematic.svg'},
            {'title': '<span class="gradient-text">3D View & Export</span>', 'text': 'Visualize your PCB in true 3D to verify component clearances and mechanical integration. Export your 3D models in standard formats like STEP for seamless integration into your mechanical CAD workflow.', 'image': 'ref-3d.svg'},
            {'title': '<span class="gradient-text">Component Database & Creation</span>', 'text': 'Access a vast, searchable database of electronic components. Easily create custom symbols and footprints using the intuitive component editor, complete with precise 3D model assignments for accurate visualization.', 'image': 'feat-components.png'},
            {'title': '<span class="gradient-text">Mixed-Mode Simulation</span>', 'text': 'Validate your designs with powerful mixed-mode circuit simulation. Display schematic diagrams alongside a virtual oscilloscope view to analyze analog waveforms and digital logic signals before manufacturing.', 'image': 'feat-simulation.png'},
            {'title': '<span class="gradient-text">EMC Analysis</span>', 'text': 'Ensure electromagnetic compatibility with built-in EMC analysis tools. Utilize 3D heatmap overlays on PCB traces to identify potential signal integrity issues and emissions, minimizing costly redesigns.', 'image': 'feat-emc.png'}
        ]
    }
}

for filename, data in pages.items():
    page_content = header
    
    # Hero section
    page_content += f"""
<section id="hero" style="padding: 60px 0 40px; background: var(--ink); color: var(--white); text-align: center;">
  <div class="container">
    <h1 style="font-family: var(--ff-display); font-size: 42px; margin-bottom: 10px;">{data['title']}</h1>
    <p style="color: #8a9fb8; font-size: 18px;">{data['subtitle']}</p>
  </div>
</section>
<section id="features" style="padding: 80px 0; background: var(--slate);">
  <div class="container">
"""
    
    if data['type'] == 'mixed':
        for i, section in enumerate(data['sections']):
            page_content += f"""
        <div class="feature-row">
          <div class="feature-text">
            <h2>{section['title']}</h2>
            <p>{section['text']}</p>
          </div>
          <div class="feature-image">
            <img src="{section['image']}" alt="{section.get('title').replace('<span class="gradient-text">', '').replace('</span>', '')}">
          </div>
        </div>
"""
    elif data['type'] == 'text':
        for section in data['sections']:
            page_content += f"""
        <div class="text-only-section">
            <h2>{section['title']}</h2>
            <p>{section['text']}</p>
        </div>
"""
        
    page_content += """
  </div>
</section>
"""
    
    # Fix links if they are subpages
    page_content = page_content.replace('href="#hero"', 'href="index.html#hero"')
    page_content = page_content.replace('href="#about"', 'href="index.html#about"')
    page_content = page_content.replace('href="#services"', 'href="index.html#services"')
    page_content = page_content.replace('href="#events"', 'href="index.html#events"')
    page_content = page_content.replace('href="#contact"', 'href="index.html#contact"')
    
    page_content += footer
    
    with open(filename, 'w', encoding='utf-8') as out_f:
        out_f.write(page_content)


# --- Build Testimonials Page ---
testimonials_html = header + """
<section id="hero" style="padding: 60px 0 40px; background: var(--ink); color: var(--white); text-align: center;">
  <div class="container">
    <h1 style="font-family: var(--ff-display); font-size: 42px; margin-bottom: 10px;">Our <span class="gradient-text">Clients</span></h1>
    <p style="color: #8a9fb8; font-size: 18px;">Trusted by leading institutions and enterprises worldwide</p>
  </div>
</section>
<section id="testimonials" style="padding: 60px 0; background: var(--slate);">
  <div class="container">
    <div class="tabs" style="display: flex; justify-content: center; gap: 15px; margin-bottom: 40px; flex-wrap: wrap;">
      <button class="btn btn-primary tab-btn active" onclick="showTab('academic')">Academic Customers</button>
      <button class="btn btn-outline tab-btn" onclick="showTab('commercial')">Commercial & Industrial</button>
      <button class="btn btn-outline tab-btn" onclick="showTab('international')">International Customers</button>
    </div>
    
    <style>
      .clients-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(300px, 1fr)); gap: 20px; }
      .client-card { background: var(--ink-mid); border: 1px solid rgba(14,179,200,0.2); border-radius: 8px; padding: 20px; color: var(--white); transition: all 0.3s; display: flex; align-items: center; gap: 15px; }
      .client-card:hover { transform: translateY(-5px); box-shadow: 0 10px 20px rgba(14,179,200,0.15); border-color: var(--teal); }
      .client-icon { width: 40px; height: 40px; border-radius: 50%; background: linear-gradient(135deg, var(--teal), var(--copper)); display: flex; align-items: center; justify-content: center; font-weight: bold; font-size: 18px; color: var(--ink); flex-shrink: 0; }
      .tab-content { display: none; animation: fadeIn 0.5s; }
      .tab-content.active { display: block; }
      @keyframes fadeIn { from { opacity: 0; transform: translateY(10px); } to { opacity: 1; transform: translateY(0); } }
    </style>

    <div id="academic" class="tab-content active">
      <div class="clients-grid">
"""

for client in academic_customers:
    testimonials_html += f"""
        <div class="client-card">
          <div class="client-icon">{client[0]}</div>
          <div class="client-name">{client}</div>
        </div>
"""

testimonials_html += """
      </div>
    </div>
    <div id="commercial" class="tab-content">
      <div class="clients-grid">
"""

for client in commercial_customers:
    testimonials_html += f"""
        <div class="client-card">
          <div class="client-icon">{client[0]}</div>
          <div class="client-name">{client}</div>
        </div>
"""

testimonials_html += """
      </div>
    </div>
    <div id="international" class="tab-content">
      <div class="clients-grid">
"""

for client in international_customers:
    testimonials_html += f"""
        <div class="client-card">
          <div class="client-icon">{client[0]}</div>
          <div class="client-name">{client}</div>
        </div>
"""

testimonials_html += """
      </div>
    </div>
  </div>
</section>

<script>
function showTab(tabId) {
    document.querySelectorAll('.tab-content').forEach(el => el.classList.remove('active'));
    document.querySelectorAll('.tab-btn').forEach(el => {
        el.classList.remove('btn-primary');
        el.classList.add('btn-outline');
    });
    
    document.getElementById(tabId).classList.add('active');
    event.target.classList.remove('btn-outline');
    event.target.classList.add('btn-primary');
}
</script>
"""

testimonials_html = testimonials_html.replace('href="#hero"', 'href="index.html#hero"')
testimonials_html = testimonials_html.replace('href="#about"', 'href="index.html#about"')
testimonials_html = testimonials_html.replace('href="#services"', 'href="index.html#services"')
testimonials_html = testimonials_html.replace('href="#events"', 'href="index.html#events"')
testimonials_html = testimonials_html.replace('href="#contact"', 'href="index.html#contact"')

testimonials_html += footer

with open('testimonials.html', 'w', encoding='utf-8') as f:
    f.write(testimonials_html)

# Update index.html itself with the new navbar
with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Build complete.")
