---
title: Detailed Report on Malicious Activities and Spam Package Abuse in npm Community
date: 2024-08-14T03:31:38+08:00
draft: false
summary: This report details widespread malicious activities and spam package abuse within the npm community.
---

**IMPORTANT NOTE: I am still investigating this incident. Please stay tuned for updates.**

This report provides a comprehensive analysis of recent malicious activities and spam package abuse within the npm community. It focuses on the patterns and impacts of these actions on the npm ecosystem.

## Malicious Activities

### Meaningless Content

A significant number of packages have been observed that contain no useful code or functionality. These packages primarily serve to clutter the npm registry without offering any value to developers. Such meaningless content increases the difficulty for users to find and use genuine, useful packages.

### Random Name Accounts

The creation of numerous accounts with meaningless usernames has been observed. These accounts are often linked to randomly generated organizations, which are used to avoid namespace conflicts. This practice complicates the task of identifying and managing spam sources.

### Keyword Stuffing

Spam packages often include a large number of irrelevant keywords in their `package.json` files to manipulate search results. For example, a search for "uuid validate" on the [Web Archive](https://web.archive.org/web/20240813180911/https://www.npmjs.com/search?q=uuid%20validate) reveals that spam packages, such as [@dramaorg/psychic-couscous](https://www.npmjs.com/package/@dramaorg/psychic-couscous), include over 700 keywords. This tactic interferes with the npm search algorithm, leading to skewed search results and making it harder for users to find relevant packages.

### Template-Based Content

The content of many spam packages follows a limited set of templates. These include:

- **Empty Packages**: Packages like [@kazaferixm/api-light](https://www.npmjs.com/package/@kazaferixm/api-light) contain no actual code.
- **Templated Packages**: Packages such as [@diotoborg/dolores-praesentium-assumenda](https://www.npmjs.com/package/@diotoborg/dolores-praesentium-assumenda) use a fixed template to generate their content. This template-based approach is evident as similar content can be found in other spam packages like [@micromint1npm/aperiam-perferendis-suscipit](https://www.npmjs.com/package/@micromint1npm/aperiam-perferendis-suscipit).

### Circular Dependencies

Spam packages often create dependencies among themselves within the same spam organization to artificially boost their search rankings. For instance, packages from the spam organization [@diotoborg](https://www.npmjs.com/org/diotoborg) have an average of 29 dependencies on other packages from the same organization. This interdependence can lead to packages like [@diotoborg/dolores-praesentium-assumenda](https://www.npmjs.com/package/@diotoborg/dolores-praesentium-assumenda) being referenced by up to 580 other spam packages, significantly impacting search results.

### Copying README Files from Popular Packages

Some spam packages copy README files from well-known packages, which can mislead developers. For example, [@diotoborg/ratione-error-odio](https://www.npmjs.com/package/@diotoborg/ratione-error-odio) has a README identical to [pnpm](https://www.npmjs.com/package/pnpm), potentially causing confusion among developers and leading to issues with package imports.

## Specific Example

A notable case is the package [@diotoborg/dolores-praesentium-assumenda](https://www.npmjs.com/package/@diotoborg/dolores-praesentium-assumenda), which features a unique README compared to [@patrtorg/illum-sapiente-quos](https://www.npmjs.com/package/@patrtorg/illum-sapiente-quos). The README for [@patrtorg/illum-sapiente-quos](https://www.npmjs.com/package/@patrtorg/illum-sapiente-quos) is copied from [fast-xml-parser](https://www.npmjs.com/package/fast-xml-parser), further illustrating the misleading practices used by spam package publishers.

## Impact on npm Community

### Integrity of Search Results

The manipulation of search rankings by spam packages disrupts the reliability of search results. This can lead developers to download and use packages that do not meet their needs, affecting the overall quality and security of their projects.

### Misleading Developers

Spam packages often mislead developers by using legitimate README files from well-known packages. This deception can result in failed imports and other technical issues, impacting developers' workflows and productivity.

### Potential Infrastructure Strain

The mass creation of spam packages and their interdependencies can place undue strain on npm's infrastructure. This could potentially degrade the performance and reliability of the npm registry.

## Violations of npm Terms

The observed activities contravene several sections of the npm Open-Source Terms:

1. **Acceptable Use**  
   - **Section:** [Acceptable Use](https://docs.npmjs.com/policies/open-source-terms#acceptable-use)
   - **Clause:** "Accounts and content must adhere to the acceptable use policies and should not undermine the integrity of the npm registry."
   - **Reason:** The creation and distribution of spam packages with misleading content violate the principles of maintaining a safe and friendly environment.

2. **Acceptable Content**  
   - **Section:** [Acceptable Content](https://docs.npmjs.com/policies/open-source-terms#acceptable-content)
   - **Clause:** "Administrators at npm reserve the right to delete content deemed unacceptable."
   - **Reason:** The use of misleading package names and content to manipulate search results fits the criteria for unacceptable content.

3. **Friendly Harassment-Free Space**  
   - **Section:** [Friendly Harassment-Free Space](https://docs.npmjs.com/policies/conduct#friendly-harassment-free-space)
   - **Clause:** "Spamming, trolling, and other attention-seeking behaviors are not tolerated."
   - **Reason:** The intentional creation of spam packages to manipulate search results and mislead users is a form of spamming.

4. **Enforcement of Acceptable Use**  
   - **Section:** [Enforcement of Acceptable Use](https://docs.npmjs.com/policies/open-source-terms#enforcement-of-acceptable-use)
   - **Clause:** "npm may investigate and prosecute violations to the fullest extent."
   - **Reason:** The scale and impact of these activities justify npm's investigation and potential enforcement actions.

## Spam Package Publishers

Here are some of the identified publishers involved in spam package activities:

```text
vanthuanbt26
erboladaiorg76
quochoanglm58
diotobtea
luongconghieufomo
micromint1npm
diotoborg
womorg
hishprorg
patrtorg
devtea2026
npmtuanmap
taktikorg
erboladaiorg
zitterorg
```

## Conclusion

The malicious activities outlined in this report present a significant threat to the npm community. Immediate and effective measures are necessary to preserve the integrity and security of the npm registry.

## Temp Area

Real-time update to this incident.

[(Maybe) the root cause](https://www.web3isgoinggreat.com/single/teaxyz-causes-open-source-software-spam-problems-again)

> However, this does not explain many of the SEO behaviors mentioned above. In addition, many of the packages we found did not have any activity related to tea.xyz, such as [@diotoborg/esse-accusantium-ratione](https://www.npmjs.com/package/@diotoborg/esse-accusantium-ratione)
