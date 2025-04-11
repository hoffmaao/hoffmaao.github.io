---
# Leave the homepage title empty to use the site title
title:
date: 2025-04-10
type: landing

sections:
  - block: markdown
    id: hero
    content:
      title: ""
      text: >
        <div class="video-hero-wrapper">
          <div style="padding:56% 0 0 0;position:relative;"><iframe src="https://player.vimeo.com/video/1074445072?h=91ad82fd50&amp;badge=0&amp;player_id=0&amp;app_id=58479" frameborder="0" style="position:absolute;top:0;left:0;width:100%;height:100%;" 
          allow="autoplay; fullscreen"
          title="EGRIP ground-based UHF radar surveys 2024"></iframe></div>
          <div class="video-overlay-text">
          </div>
        </div>
    design:
      position: center
      size: cover
      text_color_light: true
      css_class: fullscreen
      spacing:
        padding: ["0", "0", "0", "0"]

  - block: markdown
    id: home
    content:
      title: "About Us"
      text: |
         We develop new observational and modeling approaches to understand how ice sheets, oceans, and coastal systems evolve in a changing climate. Our research focuses on remote sensing of ice dynamics, radar imaging of englacial structure, and the use of geophysical observations to improve predictions of sea level rise and coastal vulnerability. We combine radar-based measurements, airborne and satellite remote sensing, and high-performance computing with physical modeling and data assimilation to investigate how englacial properties, basal sliding, subglacial hydrology, and ocean driven melt shape glacier change. These tools allow us to address fundamental questions about ice mechanics and grounding zone processes and to understand how changes at the poles are connected to water resources and infrastructure in the communities most affected by sea-level rise.

    design:
    columns: '1'
    design:
      columns: '1'
  
  - block: portfolio
    id: research
    content:
      title: "Research Projects"
      filters:
        folders:
          - research
      sort_by: 'Date'
      sort_ascending: false
    design:
      view: showcase
      columns: '1'
        
  
  - block: collection
    id: post
    content:
      title: Latest News
      subtitle:
      text:
      count: 5
      filters:
        author: ''
        category: ''
        exclude_featured: false
        publication_type: ''
        tag: ''
      offset: 0
      order: desc
      page_type: post
    design:
      view: card
      columns: '1'

  - block: people
    id: people
    content:
      title: "Our Team"
      text: ""
      filters:
        folders:
          - authors
    design:
      view: card
      columns: '3'



  - block: markdown
    id: fieldwork
    content:
      title: "Fieldwork"
      text: |
         We develop new observational and modeling approaches to understand how ice sheets, oceans, and coastal systems evolve in a changing climate. Our research focuses on remote sensing of ice dynamics, radar imaging of englacial structure, and the use of geophysical observations to improve predictions of sea level rise and coastal vulnerability. We combine radar-based measurements, airborne and satellite remote sensing, and high-performance computing with physical modeling and data assimilation to investigate how englacial properties, basal sliding, subglacial hydrology, and ocean driven melt shape glacier change. These tools allow us to address fundamental questions about ice mechanics and grounding zone processes and to understand how changes at the poles are connected to water resources and infrastructure in the communities most affected by sea-level rise.

    design:
    columns: '1'
    design:
      columns: '1'
    design:
      view: card
  
  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: IMG_0733_andrew_driving_vhf.JPG
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

  - block: collection
    id: publication
    content:
      title: Recent Publications
      text: ""
      count: 5
    design:
      view: citation
      columns: '1'

  - block: contact
    id: contact
    content:
      title: Contact
      text: |-
        Are you an undergraduate student planning to apply to graduate school in the next few years? A graduate student or postdoc looking for postdoc opportunities? Someone who is super interested about polar oceanography, fundamental ice mechanics, or radioglaciology and interested in tackling these questions from observational, modeling, and theoretical perspectives? Reach out!
      email: aohoffman@ldeo.columbia.edu
      phone: 509 540 4877
      address:
        street: 6100 Main St.
        city: Houston
        region: TX
        postcode: '77005'
        country: United States
        country_code: US
      coordinates:
        latitude: '29.719370342775083'
        longitude: '-95.40227869879237'
      directions: Enter Building 1 and take the stairs to Office 200 on Floor 2
      office_hours:
        - 'Monday 10:00 to 13:00'
        - 'Wednesday 09:00 to 10:00'
      appointment_url: 'https://calendly.com'
      #contact_links:
      #  - icon: comments
      #    icon_pack: fas
      #    name: Discuss on Forum
      #    link: 'https://discourse.gohugo.io'
    
      # Automatically link email and phone or display as text?
      autolink: true
    
      # Email form provider
      form:
        provider: netlify
        formspree:
          id:
        netlify:
          # Enable CAPTCHA challenge to reduce spam?
          captcha: false
    design:
      columns: '1'

  - block: markdown
    content:
      title:
      subtitle: ''
      text:
    design:
      columns: '1'
      background:
        image: 
          filename: IMG_6933_skiway3.jpg
          filters:
            brightness: 1
          parallax: false
          position: center
          size: cover
          text_color_light: true
      spacing:
        padding: ['0px', '0', '0px', '0']
      css_class: fullscreen

---
