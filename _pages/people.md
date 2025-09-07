---
title: "Denolle Lab - People"
layout: gridlay
excerpt: "Denolle Lab: People"
sitemap: false
permalink: /people
---

# People
---


<!-- If graduate student come with  For new applicants and incoming people, please see our [group guidelines](https://github.com/Denolle-Lab/working_as_a_group/blob/main/onboarding.md). Our group also defined a [working contract](https://github.com/Denolle-Lab/working_as_a_group/blob/main/Work_contract.md). -->

<!-- Jump to [postdocs](#postdocs), [graduate students](#graduate-students), [undergraduate researchers](#undergraduate-researchers), [affiliated graduate students](#affiliated-graduate-students), and [alumni](#alumni). -->

<!-- ---
layout: page
title: "Team Members"
permalink: /team_members/
--- -->

<!-- # Team Members -->

<div class="container">
  <div class="row">
    {% for member in site.data.team_members %}
    <div class="col-md-4 col-sm-6 mb-4">
      <div class="card text-center">
        <a href="{{ site.baseurl }}/people/{{ member.id }}">
          <img src="{{ site.baseurl }}/images/teampic/{{ member.photo }}" class="rounded-circle mx-auto d-block" style="width:150px;height:150px;object-fit:cover;" alt="{{ member.name }}">
        </a>
        <div class="card-body">
          <h5 class="card-title">{{ member.name }}</h5>
          <p class="card-text">{{ member.short_description }}</p>
          {% if member.cv %}
            <a href="{{ member.cv }}" class="btn btn-outline-primary btn-sm" target="_blank">CV</a>
          {% endif %}
          {% if member.email %}
            <a href="mailto:{{ member.email }}" class="btn btn-outline-secondary btn-sm">Email</a>
          {% endif %}
          {% if member.website %}
            <a href="{{ member.website }}" class="btn btn-outline-info btn-sm" target="_blank">Website</a>
          {% endif %}
          {% if member.scholar %}
            <a href="{{ member.scholar }}" target="_blank">📚</a>
          {% endif %}
          {% if member.orcid %}
            <a href="{{ member.orcid }}" target="_blank">🟢</a>
          {% endif %}
          {% if member.github %}
            <a href="{{ member.github }}" target="_blank"><img src="https://cdn.jsdelivr.net/gh/simple-icons/simple-icons/icons/github.svg" width="20" alt="GitHub"></a>
          {% endif %}
          {% if member.linkedin %}
            <a href="{{ member.linkedin }}" target="_blank"></a>
          {% endif %}
          {% if member.email %}
            <a href="mailto:{{ member.email }}">✉️</a>
          {% endif %}
          <!-- <div> -->
        <!-- </div> -->
        </div>
      </div>
    </div>
    {% endfor %}
  </div>
</div>