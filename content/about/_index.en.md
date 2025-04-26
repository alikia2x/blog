---
title: About Me
---

Hi. I'm alikia2x, a student developer.

I love coding, anime, game & listening to SVS works.

> SVS: Singing Voice Synthesis, eg: VOCALOID.

You can view my work [here](../works/).

## OpenPGP PUBLIC KEY

> 1DF6 3AC2 19F0 FFCB 8C0F  
> E628 3B3C 33D2 1735 89BF

<button class="btnCopy">Copy</button>

[See on Ubuntu OpenPGP Keyserver](https://keyserver.ubuntu.com/pks/lookup?search=1DF63AC219F0FFCB8C0FE6283B3C33D2173589BF&fingerprint=on&op=index)

<style>
.btnCopy{
    text-decoration: underline;
}
</style>

<script>
const btnCopy = document.querySelector('.btnCopy');

btnCopy.addEventListener('click', function() {
  const value = '1DF63AC219F0FFCB8C0FE6283B3C33D2173589BF';
  const el = document.createElement('textarea');
  el.value = value;
  document.body.appendChild(el);
  el.select();
  document.execCommand('copy');
  document.body.removeChild(el);
  btnCopy.innerText='Successfully copied.';
  setTimeout(()=>{
    btnCopy.innerText='Copy';
  }, 1500);
});
</script>
