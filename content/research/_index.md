---
title: Research
date: 2025-04-10
type: landing

sections:
  - block: markdown
    content:
      title: ""
      text: |
        <div class="research-carousel">

          <div class="research-slide active">
            <h2 class="research-slide-title">Ice Flow</h2>
            <p class="research-slide-body">Englacial stresses cause ice to creep internally and the rate of creep depends strongly on temperature and the evolving microstructure of crystal grains. In our group, we model glacier and ice-sheet motion to understand how englacial viscosity of the ice sheet and assumptions about slip at the ice-base interface affect glacier retreat. Using the finite element method and models like icepack and elmer/ice, we can solve equations that describe glacier flow and use some of the unique data our group collects to constrain physical processes that contribute to motion.</p>
          </div>

          <div class="research-slide">
            <h2 class="research-slide-title">Multi-Element Radar</h2>
            <p class="research-slide-body">In our group, we also develop and use multi-element radar systems to image the internal structure, englacial properties, and basal conditions of glaciers and ice sheets. These systems can be used to geolocate off-nadir energy and construct 3D images of the ice-base topography and the 3D englacial structure of the ice sheet. Repeating these surveys, we can also use multipass radar interferometry to map vertical displacement, strain rates, and vertical velocity. These data provide distributed observations of englacial deformation that can then be used in ice-flow model initialization.</p>
          </div>

          <div class="research-slide">
            <h2 class="research-slide-title">Firn</h2>
            <p class="research-slide-body">Firn is the porous layer of snow that compacts into glacier ice. Firn density, temperature, and enthalpy evolution affect surface elevation change and set the speed at which light can travel through the near surface. Our group uses firn models that represent compaction, heat transport, and meltwater percolation and inverse methods to assimilate observations of compaction to initialize poorly constrained densification parameters. These constraints improve the interpretation of satellite altimetry trends, and can be used to reconstruct past climate from firn observations.</p>
          </div>

          <div class="research-slide">
            <h2 class="research-slide-title">Submarine Ice-Shelf Melt</h2>
            <p class="research-slide-body">Much of West Antarctica's observed mass loss since the early 1990s is linked to submarine melting of ice shelves. Our group is developing methods that use time series of high-resolution stereo satellite imagery to map elevation change over floating ice shelves. Images can be combined to produce digital elevation models (DEM) of the ice shelf sheet surface, which can then be co-registered and differenced to produce estimates of basal melt rates. High resolution maps of submarine melt can then be used to initialize ocean cavity models and understand the drivers of heat transport to the ice-ocean interface.</p>
          </div>

          <div class="research-slide">
            <h2 class="research-slide-title">Sea-Level Geophysics</h2>
            <p class="research-slide-body">Along the Gulf Coast, relative sea level rise is impacted by subsidence connected to fluid extraction and land use. As part of local fieldwork, we combine multi-mission InSAR and GNSS observations with drone-borne SAR observations to map contemporary land motion at neighborhood scales. Using Bayesian poromechanical models we can then project subsidence under scenarios of recharge, pumping, and extraction. These modeling and remote observations complement a growing network of GNSS interferometric reflectometry tide-gauge stations our group is building in southeastern Texas. Together, these data and models can be used to represent regional processes contributing to vertical land motion (VLM) in probabilistic sea-level projection frameworks.</p>
          </div>

          <div class="research-carousel-nav">
            <button class="research-prev" aria-label="Previous">&#8592;</button>
            <div class="research-dots"></div>
            <button class="research-next" aria-label="Next">&#8594;</button>
          </div>

        </div>

        <script>
        (function() {
          var slides = document.querySelectorAll('.research-slide');
          var dotsContainer = document.querySelector('.research-dots');
          var current = 0;

          slides.forEach(function(_, i) {
            var dot = document.createElement('button');
            dot.className = 'research-dot' + (i === 0 ? ' active' : '');
            dot.setAttribute('aria-label', 'Slide ' + (i + 1));
            dot.addEventListener('click', function() { goTo(i); });
            dotsContainer.appendChild(dot);
          });

          function goTo(n) {
            slides[current].classList.remove('active');
            document.querySelectorAll('.research-dot')[current].classList.remove('active');
            current = (n + slides.length) % slides.length;
            slides[current].classList.add('active');
            document.querySelectorAll('.research-dot')[current].classList.add('active');
          }

          document.querySelector('.research-prev').addEventListener('click', function() { goTo(current - 1); });
          document.querySelector('.research-next').addEventListener('click', function() { goTo(current + 1); });
        })();
        </script>

    design:
      columns: '1'
---
