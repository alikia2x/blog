---
title: 关于我
---

[English Version](/en/about)

贴贴喵(≧∇≦)

学生开发者，你可以叫我寒寒，或者alikia。

喜欢看番玩游戏，喜欢写代码，喜欢折腾。

想了解寒寒的作品，可以到[作品](../works/)一文去看看～。

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
  btnCopy.innerText='Successfully copied!';
  setTimeout(()=>{
    btnCopy.innerText='Copy';
  }, 1500);
});
</script>
