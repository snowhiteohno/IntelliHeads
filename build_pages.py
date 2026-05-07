import os

# Read index.html lines
with open('index.html', 'r', encoding='utf-8') as f:
    lines = f.readlines()

# Extract header (lines 1-460) and footer (lines 828-end)
header = "".join(lines[:460])
footer = "".join(lines[827:])

# Data for the 6 pages
pages = {
    'digsilent-powerfactory.html': {
        'title': 'DIgSILENT PowerFactory',
        'subtitle': 'The standard software for power system analysis',
        'sections': [
            {
                'title': 'Advanced Power System Analysis',
                'text': 'PowerFactory is a leading power system analysis software application for use in analysing generation, transmission, distribution and industrial systems. It covers the full range of functionality from standard features to highly sophisticated and advanced applications including wind power, distributed generation, real-time simulation and performance monitoring for system testing and supervision.',
                'image': 'img-powerfactory.png'
            },
            {
                'title': 'Comprehensive Software Solution',
                'text': 'PowerFactory is easy to use, fully Windows compatible and combines reliable and flexible system modelling capabilities with state-of-the-art algorithms and a unique database concept. Also, with its comprehensive features for project management, data handling and team working, PowerFactory provides a comprehensive solution for power system engineering and operation.',
                'image': 'feat-software.png'
            }
        ]
    },
    'digsilent-applications.html': {
        'title': 'PowerFactory Applications',
        'subtitle': 'Versatile solutions for diverse power grids',
        'sections': [
            {
                'title': 'Transmission & Distribution',
                'text': 'PowerFactory offers a complete suite of functions for studying large-scale transmission networks and integrating new generation. For distribution, it includes comprehensive tools for voltage profile optimization, network reinforcement, and integration of distributed energy resources.',
                'image': 'feat-api.png'
            },
            {
                'title': 'Industrial Grids & Renewables',
                'text': 'PowerFactory is perfectly suited to the analysis of industrial networks, from steady-state to electromagnetic transients. It also provides comprehensive models for all types of renewable energy sources, supporting the transition to a sustainable energy future.',
                'image': 'feat-durable.png'
            }
        ]
    },
    'digsilent-features.html': {
        'title': 'PowerFactory Features',
        'subtitle': 'State-of-the-art algorithms and modelling',
        'sections': [
            {
                'title': 'Load Flow & Stability',
                'text': 'The software includes highly robust load flow algorithms for AC and DC networks. The stability analysis module offers full time-domain simulation capabilities for transient and dynamic stability studies, including RMS and EMT simulations.',
                'image': 'feat-loadflow.png'
            },
            {
                'title': 'Harmonics & Power Quality',
                'text': 'PowerFactory provides advanced tools for harmonics analysis, filter sizing, and power quality assessment. It accurately models non-linear devices and frequency-dependent components to ensure grid compliance.',
                'image': 'feat-harmonics.png'
            }
        ]
    },
    'target3001-main.html': {
        'title': 'TARGET 3001!',
        'subtitle': 'PCB Design Software for Engineering Professionals',
        'sections': [
            {
                'title': 'End-to-End PCB Design',
                'text': 'TARGET 3001! is an integrated EDA software for PCB design. It combines schematic capture, PCB layout, mixed-mode simulation, and 3D view in a single project file. No complex data conversions between schematic and layout are required.',
                'image': 'img-target3001.png'
            },
            {
                'title': 'Efficient Workflow',
                'text': 'Designed for efficiency, TARGET 3001! offers a seamless workflow from initial idea to manufacturing data. Its intuitive interface and powerful features make it the ideal choice for both rapid prototyping and complex industrial PCB designs.',
                'image': 'ref-basic.jpg'
            }
        ]
    },
    'target3001-applications.html': {
        'title': 'TARGET 3001! Applications',
        'subtitle': 'From schematics to 3D and front panels',
        'sections': [
            {
                'title': 'PCB Layout & Simulation',
                'text': 'Create professional PCB layouts with advanced routing tools. The integrated mixed-mode simulation allows you to test your circuits before committing to hardware, saving time and reducing prototype iterations.',
                'image': 'ref-layout.svg'
            },
            {
                'title': 'Front Panel Design',
                'text': 'TARGET 3001! is not just for PCBs. It includes a dedicated module for designing custom front panels, allowing you to seamlessly integrate your electronics into professional enclosures with perfectly aligned controls.',
                'image': 'ref-frontpanel.svg'
            }
        ]
    },
    'target3001-features.html': {
        'title': 'TARGET 3001! Features',
        'subtitle': 'Powerful tools for complex designs',
        'sections': [
            {
                'title': 'Schematic Capture & Autorouter',
                'text': 'Draw complex schematics with an extensive component library. The powerful built-in autorouter handles complex routing tasks automatically, optimizing trace paths for single, double, and multi-layer boards.',
                'image': 'ref-schematic.svg'
            },
            {
                'title': '3D View & Export',
                'text': 'Visualize your PCB in true 3D to verify component clearances and mechanical integration. Export your 3D models in standard formats like STEP for seamless integration into your mechanical CAD workflow.',
                'image': 'ref-3d.svg'
            }
        ]
    }
}

# Generate each page
for filename, data in pages.items():
    content = header
    
    # Add hero section
    content += f"""
<section id="hero" style="padding: 60px 0 40px; background: var(--ink); color: var(--white); text-align: center;">
  <div class="container">
    <h1 style="font-family: var(--ff-display); font-size: 42px; margin-bottom: 10px;">{data['title']}</h1>
    <p style="color: #8a9fb8; font-size: 18px;">{data['subtitle']}</p>
  </div>
</section>
<section id="features" style="padding: 80px 0; background: var(--slate);">
  <div class="container">
"""
    
    # Add alternating sections
    for i, section in enumerate(data['sections']):
        # If odd index (1, 3, etc.), it will be reversed by the CSS .feature-row:nth-child(even)
        content += f"""
    <div class="feature-row">
      <div class="feature-text">
        <h2>{section['title']}</h2>
        <p>{section['text']}</p>
      </div>
      <div class="feature-image">
        <img src="{section['image']}" alt="{section['title']}">
      </div>
    </div>
"""
        
    content += """
  </div>
</section>
"""
    content += footer

    with open(filename, 'w', encoding='utf-8') as out_f:
        out_f.write(content)

print("Generated 6 HTML pages successfully.")
