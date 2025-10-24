---
layout: post
title: "One solution for \"Javascript is required to view this map.\" in Drupal 6 GMap module"
date: 2009-02-09T13:25:48.000Z
permalink: /content/one-solution-javascript-required-view-map-drupal-6-gmap-module
---

I've been using <a href="http://drupal.org/project/gmap">GMap</a> module for Drupal 6 for a while. Once I changed the theme from Garland to my own. The map page said only "Javascript is required to view this map".

I googled and found that I should include a javascript tag via drupal_add_js() function, but the scripts are already there when I did view source. Comparing with the working source, the missing piece is

<code>&lt;script src="http://maps.google.com/maps?SOME_VALUE" type="text/javascript"&gt;&lt;/script&gt;</code>

which is not included in a Drupal variable $script.

After comparing the page.tpl.php of the two themes line-by-line, the problem is that there was no $head in my new theme. I just inserted 

<code>&lt;?php print $head ?&gt;</code>

before the line

<code>&lt;?php print $styles ?&gt;</code>

 and the map appears.
