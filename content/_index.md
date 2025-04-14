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
      text: |
        <div class="video-hero-wrapper" style="width: 100%; height: auto; overflow: hidden;">
          <div style="padding-top: 56.25%; position: relative;">
            <iframe
              src="https://player.vimeo.com/video/1074445072?h=91ad82fd50&autoplay=1&loop=1&muted=1&background=1"
              frameborder="0"
              allow="autoplay; fullscreen"
              allowfullscreen
              style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"
              title="EGRIP ground-based UHF radar surveys 2024">
            </iframe>
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
    id: about
    content:
      title: "About Us"
      text: |
        <div class="row">
          <div class="col-md-4 text-center">
            <img src="/images/rice_logo.jpg"
               alt="Rice R Logo"
               class="mx-auto d-block"
               style="height: 240px; width: 240px; object-fit: contain; border-radius: 100%; box-shadow: 0 2px 20px rgba(0,0,0,0.2); margin-bottom: 10px;" />
            <h3 style="margin: 10px 0;">Oceans and Cryosphere Group</h3>
            <a href="https://github.com/hoffmaao/hoffmaao.github.io" target="_blank" style="font-size: 1.5rem;">
            <i class="fab fa-github" aria-hidden="true"></i>
            </a>
          </div>
          <div class="col-md-8">
            <p>
              We develop new observational and modeling approaches to understand how ice sheets, oceans, and coastal systems evolve in a changing climate. Our research focuses on remote sensing of ice dynamics, radar imaging of englacial structure, and the use of geophysical observations to improve predictions of sea level rise and coastal vulnerability.
            </p>
          </div>
        </div>
    design:
      columns: '1'


  - block: markdown
    id: research
    content:
      title: "Research Areas"
      text: |
        <div style="position: relative; width: 100%; max-width: 1200px; margin: auto;">
          <img src="/images/research_approach_Rice_website.jpg" alt="Research overview diagram"
               style="width: 100%; height: auto; border-radius: 10px;" />

          <!-- Example Overlay Links -->
          <a href="/projects/ice-ocean/" style="position: absolute; top: 82%; left: 76%; transform: translate(-50%, -50%);
              padding: 5px 10px; background-color: rgba(0,0,0,0.6); color: white; text-decoration: none; border-radius: 6px;">
            Ice–Ocean Interactions
          </a>

          <a href="/projects/sea-level/" style="position: absolute; top: 4%; left: 65%; transform: translate(-50%, -50%);
              padding: 5px 10px; background-color: rgba(0,0,0,0.6); color: white; text-decoration: none; border-radius: 6px;">
            Sea-Level Monitoring
          </a>

          <a href="/projects/radar/" style="position: absolute; top: 15%; left: 6%; transform: translate(-50%, -50%);
              padding: 5px 10px; background-color: rgba(0,0,0,0.6); color: white; text-decoration: none; border-radius: 6px;">
            Radar & Remote Sensing
          </a>
        </div>
    design:
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
      user_groups:
        - Faculty
        - Grad Students
        - Alumni
    design:
      show_interests: false
      show_role: true
      show_social: true
      view: card
      columns: "3"

  - block: markdown
    id: fieldwork
    content:
      title: "Fieldwork"
      text: |
        Our field campaigns span polar ice sheets and coastal urban environments to investigate how ice, ocean, and infrastructure systems evolve in a changing climate.

        Much of our work focuses on the deployment of airborne and ground-basedradar systems to map englacial structure, measure vertical ice motion, and image subglacial topography near grounding lines. We work in remote regions of Antarctica and Greenland, including the margins of the ice sheet where ice interacts with the ocean.

        Our team has also begun deploying terrestrial radar interferometers, GNSS instruments, and satellite-linked sensors in coastal regions of the U.S. to monitor infrastructure stress, subsidence, and sea-level rise.

        We believe fieldwork is a place of shared exploration, creativity, and learning. Our group is committed to inclusive field practices and ensuring early-career researchers are supported as leaders in the field.

        ### Current & Recent Field Sites
        - **EGRIP, Greenland** – Vertical ice velocity and radar calibration
        - **Amundsen Sea Embayment, Antarctica** – Swath radar mapping of subglacial topography
        - **Beardmore Glacier, Antarctica** – Ground-based ApRES surveys and englacial reflectivity analysis
        - **Gulf Coast, Texas** – Terrestrial radar interferometry for dam and levee monitoring

        <br>

        
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
      title: Join us
      text: |-
        Are you a recent graduate or an undergraduate student planning to apply to graduate school in the next couple of years? A graduate student or postdoc looking for postdoc opportunities? Someone who is super interested about polar oceanography, fundamental ice mechanics, or radioglaciology and interested in tackling these questions from observational, modeling, and theoretical perspectives? Reach out!
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

---
