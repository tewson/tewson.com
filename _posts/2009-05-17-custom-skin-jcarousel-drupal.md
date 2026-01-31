---
layout: post
title: "Using Custom Skins for jCarousel in Drupal"
date: 2009-05-17T16:09:50.000Z
permalink: /content/using-custom-skins-jcarousel-drupal
---

[jCarousel](http://sorgalla.com/projects/jcarousel) is a very nice slide show plug-in for [jQuery](http://jquery.com). There is also a [Drupal module](http://drupal.org/project/jcarousel) for jCarousel.

Using jCarousel in Drupal is quite easy. After enabling jCarousel module, you just assign an ID to a list and call a PHP function jcarousel_add('#your-list-id') in your theme file or somewhere like a view's header (don't for get to choose PHP input).

But what if you want to create your own skin for jCarousel? It can be quite confusing for those who don't code much (or enough - like me) so I will explain here step by step.

1. You have to know that the function jcarousel_add() can take up to 4 parameters (I couldn't find this in the jCarousel module's help page so I looked in the jcarousel.module file itself), $selector, $options, $skin, and $skin_path.
2. $selector is your jQuery selector for the list you want to enable jCarousel. $options is an associative array for jCarousel configuration. The details are [here](http://sorgalla.com/projects/jcarousel/#Configuration). $skin is the skin name. $skin_path is your custom skin's css file path (it has to be an internal path such as "sites/all/modules/jcarousel/jcarousel/skins/tango/skin.css" for Tango skin).
3. You need to create a wrapper element, such as div, with class="jcarousel-skin-*skin_name*" for your jCarousel-enabled list.
4. You may copy and modify skin.css from the existing skins (tango or ie7). Don't forget to change the class selector .jcarousel-skin-tango or .jcarousel-skin-ie7 to your own one. This is where I got stuck -_-".
5. Make sure that your $skin_path is correct and enjoy theming. :D
