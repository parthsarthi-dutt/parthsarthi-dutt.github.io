import re
import codecs

with open('index.html', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Navbar Resume & Hire Me
nav_target = r'<a href="mailto:parthsarthiduttofficial@gmail.com" class="nav-cta">Hire Me</a>'
nav_replace = r'<div style="display:flex; gap:14px;"><a href="#" id="nav-resume-btn" target="_blank" class="btn btn-ghost" style="padding:9px 22px; font-size:.68rem; letter-spacing:2px; display:flex; align-items:center;">Resume</a><a href="mailto:parthsarthiduttofficial@gmail.com?subject=Job%20Opportunity" class="nav-cta" id="nav-hire-me">Hire Me</a></div>'
content = content.replace(nav_target, nav_replace)

# 2. Add id's to Hero section
content = content.replace('<div class="hero-tag">', '<div class="hero-tag" id="hero-tag">')
content = content.replace('<h1 class="hero-name">', '<h1 class="hero-name" id="hero-name">')
content = content.replace('<p class="hero-desc">', '<p class="hero-desc" id="hero-desc">')
content = content.replace('<div class="hero-stats">', '<div class="hero-stats" id="hero-stats">')
content = content.replace('<div class="card-name">Parthsarthi Dutt</div>', '<div class="card-name" id="card-name">Parthsarthi Dutt</div>')
content = content.replace('<div class="card-role">Competitive Programmer · DSAI</div>', '<div class="card-role" id="card-role">Competitive Programmer · DSAI</div>')
content = content.replace('<div class="card-badges">', '<div class="card-badges" id="card-badges">')
content = content.replace('<div class="card-socials">', '<div class="card-socials" id="card-socials">')

# 3. Replace entire sections with containers
# Profiles
profiles_regex = r'<div class="profiles-wrap">.*?</section>'
profiles_replace = r'''<div class="profiles-wrap" id="profiles-container"></div>
</section>'''
content = re.sub(profiles_regex, profiles_replace, content, flags=re.DOTALL)

# Experience
exp_regex = r'<div class="exp-grid">.*?</section>'
exp_replace = r'''<div class="exp-grid" id="experience-container"></div>
</section>'''
content = re.sub(exp_regex, exp_replace, content, flags=re.DOTALL)

# Education
edu_regex = r'<div class="edu-grid">.*?</section>'
edu_replace = r'''<div class="edu-grid" id="education-container"></div>
  <div class="edu-card cert-card reveal" id="certifications-container"></div>
</section>'''
content = re.sub(edu_regex, edu_replace, content, flags=re.DOTALL)

# Skills
skills_regex = r'<div class="skills-layout">.*?</section>'
skills_replace = r'''<div class="skills-layout" id="skills-container"></div>
</section>'''
content = re.sub(skills_regex, skills_replace, content, flags=re.DOTALL)

# Achievements Timeline
timeline_regex = r'<div class="timeline">.*?</div>\s*</div>\s*<div>\s*<div class="icpc-gallery">'
timeline_replace = r'''<div class="timeline" id="timeline-container"></div>
    </div>
    <div>
      <div class="icpc-gallery">'''
content = re.sub(timeline_regex, timeline_replace, content, flags=re.DOTALL)

# Projects
projects_regex = r'<div class="projects-grid">.*?</section>'
projects_replace = r'''<div class="projects-grid" id="projects-container"></div>
</section>'''
content = re.sub(projects_regex, projects_replace, content, flags=re.DOTALL)

# Contact
contact_regex = r'<div class="contact-grid">.*?</div>\s*<div style="text-align:center"><a href="mailto:parthsarthiduttofficial@gmail.com" class="btn btn-primary">'
contact_replace = r'''<div class="contact-grid" id="contact-container"></div>
    <div style="text-align:center; display:flex; justify-content:center; gap:20px; flex-wrap:wrap;">
      <a href="#" id="contact-resume-btn" target="_blank" class="btn btn-ghost">Download Resume</a>
      <a href="mailto:parthsarthiduttofficial@gmail.com?subject=Job%20Opportunity" class="btn btn-primary">Get in Touch</a>'''
content = re.sub(contact_regex, contact_replace, content, flags=re.DOTALL)

# Inject <script src="data.js"> before the main script
script_injection = r'''<script src="data.js"></script>
<script>
// --- DATA INJECTION --- //
function renderPortfolio() {
  // 1. Navbar & Contact Resume buttons
  document.getElementById('nav-resume-btn').href = PORTFOLIO_DATA.resumeLink;
  document.getElementById('contact-resume-btn').href = PORTFOLIO_DATA.resumeLink;
  
  // 2. Hero
  document.getElementById('hero-tag').textContent = PORTFOLIO_DATA.hero.tag;
  document.getElementById('hero-name').innerHTML = PORTFOLIO_DATA.hero.name + '<em>' + PORTFOLIO_DATA.hero.nameEm + '</em>';
  document.getElementById('hero-desc').innerHTML = PORTFOLIO_DATA.hero.descHTML;
  document.getElementById('hero-stats').innerHTML = PORTFOLIO_DATA.hero.stats.map(s => 
    '<div class="hstat"><div class="hstat-val">' + s.val + '</div><div class="hstat-key">' + s.key + '</div></div>'
  ).join('');

  document.getElementById('card-name').textContent = PORTFOLIO_DATA.profileCard.name;
  document.getElementById('card-role').textContent = PORTFOLIO_DATA.profileCard.role;
  document.getElementById('card-badges').innerHTML = PORTFOLIO_DATA.profileCard.badges.map(b => 
    '<span class="cbadge ' + b.class + '">' + b.text + '</span>'
  ).join('');
  document.getElementById('card-socials').innerHTML = PORTFOLIO_DATA.profileCard.socials.map(s => 
    '<a href="' + s.link + '" target="_blank" class="csocial" title="' + s.title + '">' + s.svg + '</a>'
  ).join('');

  // 3. Profiles & Ranks
  document.getElementById('profiles-container').innerHTML = `
    <h5 class="sec-title1">Profiles</h5>
    <div class="pf-row pf-row-3 reveal in">
      ${PORTFOLIO_DATA.profiles.map(p => `
        <div class="pf-card" onclick="openModal('${p.id}')">
          <img src="${p.logo}" class="pf-logo" alt="${p.platform}" ${p.logoStyle ? 'style="'+p.logoStyle+'"' : ''}>
          <div class="pf-top-bar" style="background:${p.color}"></div>
          <div class="pf-platform">${p.platform}</div>
          <div class="pf-handle">${p.handle}</div>
          ${p.ratingHTML}
          <div class="pf-rank">${p.rank}</div>
          <div class="pf-divider"></div>
          <div class="pf-stats">
            ${p.stats.map(s => `<div class="pf-stat"><div class="pf-sv">${s.v}</div><div class="pf-sk">${s.k}</div></div>`).join('')}
          </div>
          <a href="${p.link}" target="_blank" class="pf-ext-link" onclick="event.stopPropagation()">Open Profile <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg></a>
        </div>
      `).join('')}
    </div>
    <h5 class="sec-title1" style="margin-top: 80px;">Ranks</h5>
    <div class="pf-row pf-row-3 reveal in">
      ${PORTFOLIO_DATA.ranks.map(r => `
        <div class="pf-card" onclick="openModal('${r.id}')">
          <div class="pf-top-bar" style="background:${r.color}"></div>
          <div class="pf-platform">${r.platform}</div>
          ${r.ratingHTML}
          <div class="pf-rank">${r.rank}</div>
          <div class="pf-divider"></div>
          <div class="pf-stats">
            ${r.stats.map(s => `<div class="pf-stat"><div class="pf-sv">${s.v}</div><div class="pf-sk">${s.k}</div></div>`).join('')}
          </div>
          <a href="${r.link}" target="_blank" class="pf-ext-link" onclick="event.stopPropagation()">${r.btnText} <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg></a>
        </div>
      `).join('')}
    </div>
  `;

  // 4. Experience
  document.getElementById('experience-container').innerHTML = PORTFOLIO_DATA.experience.map(e => `
    <div class="exp-card reveal in">
      <div class="exp-accent" style="background:${e.color}"></div>
      <div class="exp-top">
        <div>
          <div class="exp-title">${e.title}</div>
          <div class="exp-company">${e.company}</div>
        </div>
        <div class="exp-meta">
          <div class="exp-period">${e.period}</div>
          <div class="exp-type">${e.type}</div>
        </div>
      </div>
      <ul class="exp-bullets">
        ${e.bullets.map(b => `<li>${b}</li>`).join('')}
      </ul>
      <div class="exp-tags">
        ${e.tags.map(t => `<span class="exp-tag">${t}</span>`).join('')}
      </div>
    </div>
  `).join('');

  // 5. Education & Certs
  document.getElementById('education-container').innerHTML = PORTFOLIO_DATA.education.map(e => `
    <div class="edu-card reveal in" onclick="openModal('${e.id}')">
      <div class="edu-accent-bar" style="background:${e.color}"></div>
      <div class="edu-year">${e.year}</div>
      <div class="edu-degree">${e.degree}</div>
      <div class="edu-inst">${e.inst}</div>
      <div class="edu-gpa">${e.gpa}</div>
      <div class="edu-tags">${e.tags.map(t => `<span class="edu-tag">${t}</span>`).join('')}</div>
    </div>
  `).join('');

  document.getElementById('certifications-container').innerHTML = `
    <div class="edu-accent-bar" style="background:var(--gold-dim)"></div>
    <div class="edu-year">Contest Achievements</div>
    <div class="edu-degree">Awards & Certifications</div>
    <div class="edu-inst">ICPC · Meta · Amazon · Codeforces · CodeChef</div>
    <div style="margin-top:16px">
      ${PORTFOLIO_DATA.certifications.map(c => `<div class="cert-row"><span class="cert-name">${c.name}</span><span class="cert-yr" ${c.yrColor ? 'style="color:'+c.yrColor+'"' : ''}>${c.year}</span></div>`).join('')}
    </div>
  `;

  // 6. Skills
  document.getElementById('skills-container').innerHTML = `
    <div>
      <div class="sg-title reveal in">Algorithms & Data Structures</div>
      ${PORTFOLIO_DATA.skillsDS.map(s => `<div class="skill-row reveal in"><div class="skill-top"><span class="skill-name">${s.name}</span><span class="skill-lvl">${s.lvl}</span></div><div class="skill-bar"><div class="skill-fill go" style="width:${s.w}"></div></div></div>`).join('')}
      
      <div class="sg-title reveal in" style="margin-top:36px">Programming Languages</div>
      ${PORTFOLIO_DATA.skillsLang.map(s => `<div class="skill-row reveal in"><div class="skill-top"><span class="skill-name">${s.name}</span><span class="skill-lvl">${s.lvl}</span></div><div class="skill-bar"><div class="skill-fill go" style="width:${s.w}"></div></div></div>`).join('')}
    </div>
    <div>
      <div class="sg-title reveal in">Technologies & Frameworks</div>
      <div class="tools-grid" style="margin-bottom:36px">
        ${PORTFOLIO_DATA.tools.map(t => `<div class="tool-pill reveal in">${t}</div>`).join('')}
      </div>
      <div class="sg-title reveal in" style="margin-top: 60px;">Interests & Strengths</div>
      <div class="interest-grid reveal in">
        ${PORTFOLIO_DATA.interests.map(i => `<div class="interest-card"><div class="int-label">${i.label}</div><div class="int-text">${i.text}</div></div>`).join('')}
      </div>
    </div>
  `;

  // 7. Timeline
  document.getElementById('timeline-container').innerHTML = `
    <div class="tl-line"></div>
    ${PORTFOLIO_DATA.icpcJourney.map(t => `
      <div class="tl-item reveal in" onclick="openModal('${t.id}')">
        <div class="tl-dot"></div><div class="tl-connector"></div>
        <div class="tl-meta"><span class="tl-year">${t.year}</span><span class="tl-badge ${t.badgeClass}">${t.badgeText}</span></div>
        <div class="tl-title">${t.title}</div>
        <div class="tl-desc">${t.desc}</div>
        <div class="tl-hint">Click for details →</div>
      </div>
    `).join('')}
  `;

  // 8. Projects
  document.getElementById('projects-container').innerHTML = PORTFOLIO_DATA.projects.map(p => `
    <div class="proj-card reveal in" onclick="openModal('${p.id}')">
      <div class="proj-acc" style="--accent:${p.accent}"></div>
      <div class="proj-num">${p.num}</div>
      <div class="proj-name">${p.name}</div>
      <div class="proj-desc">${p.desc}</div>
      <div class="proj-tags">${p.tags.map(t => `<span class="proj-tag">${t}</span>`).join('')}</div>
      ${p.link ? `<a href="${p.link}" target="_blank" class="proj-link" onclick="event.stopPropagation()">View on GitHub <svg width="11" height="11" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5"><path d="M18 13v6a2 2 0 01-2 2H5a2 2 0 01-2-2V8a2 2 0 012-2h6"/><polyline points="15 3 21 3 21 9"/><line x1="10" y1="14" x2="21" y2="3"/></svg></a>` : ''}
    </div>
  `).join('');

  // 9. Contact Links
  const clinksHTML = [
    '<a href="mailto:parthsarthiduttofficial@gmail.com?subject=Job%20Opportunity" class="clink"><div class="clink-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="1.5"><path d="M4 4h16c1.1 0 2 .9 2 2v12c0 1.1-.9 2-2 2H4c-1.1 0-2-.9-2-2V6c0-1.1.9-2 2-2z"/><polyline points="22,6 12,12 2,6"/></svg></div><div><span class="clink-label">Email</span><span class="clink-val">parthsarthiduttofficial@gmail.com</span></div></a>',
    '<a href="https://github.com/parthsarthi-dutt" target="_blank" class="clink"><div class="clink-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M12 0C5.374 0 0 5.373 0 12c0 5.302 3.438 9.8 8.207 11.387.599.111.793-.261.793-.577v-2.234c-3.338.726-4.033-1.416-4.033-1.416-.546-1.387-1.333-1.756-1.333-1.756-1.089-.745.083-.729.083-.729 1.205.084 1.839 1.237 1.839 1.237 1.07 1.834 2.807 1.304 3.492.997.107-.775.418-1.305.762-1.604-2.665-.305-5.467-1.334-5.467-5.931 0-1.311.469-2.381 1.236-3.221-.124-.303-.535-1.524.117-3.176 0 0 1.008-.322 3.301 1.23A11.509 11.509 0 0112 5.803c1.02.005 2.047.138 3.006.404 2.291-1.552 3.297-1.23 3.297-1.23.653 1.653.242 2.874.118 3.176.77.84 1.235 1.911 1.235 3.221 0 4.609-2.807 5.624-5.479 5.921.43.372.823 1.102.823 2.222v3.293c0 .319.192.694.801.576C20.566 21.797 24 17.3 24 12c0-6.627-5.373-12-12-12z"/></svg></div><div><span class="clink-label">GitHub</span><span class="clink-val">github.com/parthsarthi-dutt</span></div></a>',
    '<a href="https://www.linkedin.com/in/parthsarthi-dutt-b32886189/" target="_blank" class="clink"><div class="clink-icon"><svg width="18" height="18" viewBox="0 0 24 24" fill="currentColor"><path d="M20.447 20.452h-3.554v-5.569c0-1.328-.027-3.037-1.852-3.037-1.853 0-2.136 1.445-2.136 2.939v5.667H9.351V9h3.414v1.561h.046c.477-.9 1.637-1.85 3.37-1.85 3.601 0 4.267 2.37 4.267 5.455v6.286zM5.337 7.433c-1.144 0-2.063-.926-2.063-2.065 0-1.138.92-2.063 2.063-2.063 1.14 0 2.064.925 2.064 2.063 0 1.139-.925 2.065-2.064 2.065zm1.782 13.019H3.555V9h3.564v11.452zM22.225 0H1.771C.792 0 0 .774 0 1.729v20.542C0 23.227.792 24 1.771 24h20.451C23.2 24 24 23.227 24 22.271V1.729C24 .774 23.2 0 22.222 0h.003z"/></svg></div><div><span class="clink-label">LinkedIn</span><span class="clink-val">Parthsarthi Dutt</span></div></a>',
    '<a href="https://codeforces.com/profile/parthsarthidutt_45" target="_blank" class="clink"><div class="clink-icon" style="font-family:\'Playfair Display\',serif;font-size:.95rem;font-weight:700;color:var(--gold-dim)">CF</div><div><span class="clink-label">Codeforces</span><span class="clink-val">Expert · 1649 · parthsarthidutt_45</span></div></a>'
  ];
  document.getElementById('contact-container').innerHTML = clinksHTML.join('');
}
document.addEventListener("DOMContentLoaded", renderPortfolio);
// --- END DATA INJECTION --- //
</script>
<script>'''

content = content.replace('<script>\n/* AVATAR */', script_injection + '\n/* AVATAR */')
content = content.replace("const M=", "const M=PORTFOLIO_DATA.modals; //")

with open('index.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Refactored index.html successfully")
