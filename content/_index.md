---
# Leave the homepage title empty to use the site title
title:
date: 2025-04-10
type: landing

sections:
  - block: hero
    content:
      title: |
        Oceans and Cryosphere Group
    text: |
      <div class="video-background">
        <iframe src="https://vimeo.com/manage/videos/1074445072?background=1" frameborder="0" webkitallowfullscreen mozallowfullscreen allowfullscreen></iframe>
      </div>
    design:
      background:
        color: '#000000'
        text_color_light: true
    spacing:
      padding: ['0', '0', '0', '0']

  - block: markdown
    id: about
    content:
      title: "About Us"
      text: |
        We are a research group at Rice University focusing on oceans, ice, and climate.
    design:
      columns: '1'
  
  - block: portfolio
    id: research
    content:
      title: "Research Projects"
      filters:
        folders:
          - project
      sort_by: 'Date'
      sort_ascending: false
    design:
      view: showcase
      columns: '1'
        
  
  - block: collection
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
      filters:
      - field: superuser
        value: true
    design:
      view: card
      columns: '3'
  
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
    content:
      title: Latest Preprints
      text: ""
      count: 5
      filters:
        folders:
          - publication
        publication_type: 'article'
    design:
      view: citation
      columns: '1'
  - block: contact
    id: contact
    content:
      title: Contact
      text: |-
        Are you... An undergraduate student planning to apply to graduate school in the next few years? A graduate student or postdoc looking for postdoc opportunities? Someone who is super interested about fundamental ice mechanics or radioglaciology and interested in tackling these questions from observational, modeling, and theoretical perspectives? Reach out!
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
        latitude: '30.031'
        longitude: '-95.418'
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
        padding: ['20px', '0', '20px', '0']
      css_class: fullscreen

---
