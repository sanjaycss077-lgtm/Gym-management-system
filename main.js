// Nav toggle for mobile
function toggleNav() {
  document.querySelector('.nav-links').classList.toggle('open');
}

// Auto-dismiss flashes after 4 seconds
document.querySelectorAll('.flash').forEach(el => {
  setTimeout(() => el.remove(), 4000);
});

// Show "Copied!" message on share input click
function showCopied(input) {
  const msg = document.getElementById('copied-msg');
  if (msg) {
    msg.style.display = 'inline';
    setTimeout(() => msg.style.display = 'none', 2000);
  }
}

// Animate capacity bars on load
window.addEventListener('load', () => {
  document.querySelectorAll('.capacity-fill').forEach(bar => {
    const w = bar.style.width;
    bar.style.width = '0';
    setTimeout(() => bar.style.width = w, 200);
  });
});

// Highlight active nav based on scroll (homepage only)
const navLinks = document.querySelectorAll('.nav-link');
navLinks.forEach(link => {
  if (link.href === window.location.href) link.classList.add('active');
});
