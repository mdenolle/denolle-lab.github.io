---
title: "Denolle Lab - People"
layout: gridlay
excerpt: "Denolle Lab: People"
sitemap: false
permalink: /people/
---

# People
---


If graduate student come with  For new applicants and incoming people, please see our [group guidelines](https://github.com/Denolle-Lab/working_as_a_group/blob/main/onboarding.md). Our group also defined a [working contract](https://github.com/Denolle-Lab/working_as_a_group/blob/main/Work_contract.md).

Jump to [postdocs](#postdocs), [graduate students](#graduate-students), [undergraduate researchers](#undergraduate-researchers), [affiliated graduate students](#affiliated-graduate-students), and [alumni](#alumni).

<!-- ## Staff ------------------------------->
{% assign number_printed = 0 %}
{% for member in site.data.team_members %}
{% assign even_odd = number_printed | modulo: 2 %}

{% if even_odd == 0 %}
<div class="row">
{% endif %}

<div class="col-sm-6 clearfix">
  <img src="{{ site.url }}{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="rounded-circle mx-auto d-block" style="width:150px;height:150px;object-fit:cover;" alt="{{ member.name }}" />
  <h4>{{ member.name }}</h4>
  <br> {{ member.info }}  <br><b>email </b>: <{{ member.email }}>  <br><b> PhD </b>: {{ member.education1 }}  
 
  <ul style="overflow: hidden">
  {% if member.cv %}
      <li><a href="{{ member.cv }}" target="_blank">CV</a></li>
    {% endif %}


 {% if member.number_educ == 1 %}
  <li> {{ member.education1 }} </li>
  {% endif %}

  {% if member.number_educ == 2 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  {% endif %}

  {% if member.number_educ == 3 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  {% endif %}

  {% if member.number_educ == 4 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  {% endif %} 

  {% if member.number_educ == 5 %}
  <li> {{ member.education1 }} </li>
  <li> {{ member.education2 }} </li>
  <li> {{ member.education3 }} </li>
  <li> {{ member.education4 }} </li>
  <li> {{ member.education5 }} </li>
  {% endif %} 
  </ul>
</div>

{% assign number_printed = number_printed | plus: 1 %}

{% if even_odd == 1 %}
</div>
{% endif %}

{% endfor %}

{% assign even_odd = number_printed | modulo: 2 %}
{% if even_odd == 1 %}
</div>
{% endif %}
