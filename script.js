// ================================================================
// InteliHeads — script.js
// ================================================================

(function () {
  'use strict';

  // ── NAV: sticky active + mobile toggle ──────────────────────
  const navLinks = document.querySelectorAll('.nav-links a');
  const sections = document.querySelectorAll('section[id]');
  const hamburger = document.getElementById('hamburger');
  const navList = document.getElementById('nav-links');

  function setActiveNav() {
    let current = '';
    sections.forEach((sec) => {
      if (window.scrollY >= sec.offsetTop - 100) {
        current = sec.id;
      }
    });
    navLinks.forEach((a) => {
      a.classList.toggle('active', a.getAttribute('href') === '#' + current);
    });
  }

  if (hamburger && navList) {
    hamburger.addEventListener('click', () => {
      navList.classList.toggle('open');
      hamburger.classList.toggle('is-open');
    });
    navList.querySelectorAll('a').forEach((a) => {
      a.addEventListener('click', () => navList.classList.remove('open'));
    });
  }

  window.addEventListener('scroll', setActiveNav, { passive: true });
  setActiveNav();

  // ── SMOOTH SCROLL for anchor links ──────────────────────────
  document.querySelectorAll('a[href^="#"]').forEach((anchor) => {
    anchor.addEventListener('click', function (e) {
      const target = document.querySelector(this.getAttribute('href'));
      if (!target) return;
      e.preventDefault();
      const offset = 70;
      const top = target.getBoundingClientRect().top + window.scrollY - offset;
      window.scrollTo({ top, behavior: 'smooth' });
    });
  });

  // ── INTERSECTION OBSERVER: fade-in on scroll ────────────────
  const fadeEls = document.querySelectorAll('.fade-in');
  const observer = new IntersectionObserver(
    (entries) => {
      entries.forEach((entry) => {
        if (entry.isIntersecting) {
          entry.target.classList.add('visible');
          observer.unobserve(entry.target);
        }
      });
    },
    { threshold: 0.12 }
  );
  fadeEls.forEach((el) => observer.observe(el));

  // ── CONTACT FORM: basic submit handler ──────────────────────
  const form = document.getElementById('contact-form');
  if (form) {
    form.addEventListener('submit', function (e) {
      e.preventDefault();
      const btn = form.querySelector('button[type="submit"]');
      const original = btn.textContent;
      btn.textContent = 'Sending…';
      btn.disabled = true;
      setTimeout(() => {
        btn.textContent = '✓ Message Sent';
        btn.style.background = '#22c55e';
        btn.style.color = '#fff';
        setTimeout(() => {
          btn.textContent = original;
          btn.style.background = '';
          btn.style.color = '';
          btn.disabled = false;
          form.reset();
        }, 2800);
      }, 1200);
    });
  }

  // ── PRODUCT ITEMS: expand/collapse description ───────────────
  document.querySelectorAll('.product-item').forEach((item) => {
    item.addEventListener('click', (e) => {
      e.preventDefault();
      const expanded = item.getAttribute('aria-expanded') === 'true';
      document.querySelectorAll('.product-item').forEach((i) =>
        i.setAttribute('aria-expanded', 'false')
      );
      item.setAttribute('aria-expanded', expanded ? 'false' : 'true');
    });
  });
})();