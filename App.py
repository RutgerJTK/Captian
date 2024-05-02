import streamlit as st

def main():
    # Create a sidebar for navigation
    st.sidebar.title("Navigation 🦪")
    page = st.sidebar.selectbox("Select a page", ["Home 🧭", "About IAS 🐸"])

    # Render the selected page
    if page == "Home 🧭":
        render_home_page()
    elif page == "About IAS 🐸":
        render_about_page()

def render_home_page():
    st.title("Welcome to the Invasive Alien Species App 🧭")
    st.write("This app provides information on invasive alien species.")

    # Add your content here

def render_about_page():
    st.title("About Invasive Alien Species 🐸")
    st.write("""
    **Invasive alien species (IAS), also referred to as non-native or exotic species, are organisms that have been introduced, deliberately or accidentally, into ecosystems where they are not native and whose introduction causes, or is likely to cause, harm to the environment, economy, or human health.** In the European Union (EU), addressing the issue of invasive alien species is a significant concern due to its impact on biodiversity, ecosystems, and various sectors such as agriculture, forestry, and fisheries.
    
    **Here are some general points regarding invasive alien species in accordance with the European Union:**
    
    **Legislation:**
        The European Union has implemented legislation to address the issue of invasive alien species. The most significant piece of legislation is the EU Regulation 1143/2014 on the prevention and management of the introduction and spread of invasive alien species. This regulation provides a framework for preventing the introduction and spread of invasive alien species and for managing their impact within the EU.
    
    **Impact on Biodiversity:**
        Invasive alien species can have a profound impact on biodiversity by outcompeting native species for resources, preying on native species, altering habitats, and disrupting ecosystem functions. This can lead to the decline or extinction of native species, loss of biodiversity, and degradation of ecosystems.
    
    **Economic Impact:**
        Invasive alien species can also have significant economic impacts. They can damage crops, forests, and fisheries, leading to reduced agricultural productivity, increased management costs, and loss of revenue for affected industries. Additionally, control and eradication efforts for invasive species can be costly.
    
    **Vectors of Introduction:**
        Invasive alien species can be introduced through various vectors, including international trade, transport, tourism, and deliberate release. The unintentional introduction of invasive species through these vectors is often associated with global trade and travel.
    
    **Prevention and Control Measures:**
        The EU Regulation on invasive alien species includes measures aimed at preventing the introduction and spread of invasive species, such as risk assessments, surveillance, early detection, and rapid response mechanisms. Additionally, it promotes cooperation between EU Member States and other stakeholders to address the issue effectively.
    
    **List of Invasive Alien Species of Union Concern:**
        The EU maintains a list of invasive alien species of Union concern, which includes species that have significant adverse impacts on biodiversity in the EU. Member States are required to take measures to prevent their introduction and spread, and to manage populations already established. 
    
    **Awareness and Public Engagement:**
        Increasing awareness and engaging the public, stakeholders, and relevant sectors are essential components of addressing the issue of invasive alien species. Education, outreach campaigns, and collaboration between governments, NGOs, research institutions, and the private sector can help raise awareness and promote actions to prevent the introduction and spread of invasive species. Overall, the European Union recognizes the importance of addressing the threat posed by invasive alien species and has taken legislative and strategic measures to prevent their introduction and manage their impacts effectively.""")

    # Add your content here

if __name__ == "__main__":
    main()