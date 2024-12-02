# HPCC Coworking Hours: 4 March 2021

The HPC Carpentries Task Force holds coworking hours every other Thursday, with
two time slots intended to provide adequate coverage for our global
constituency. Check your local times below, and join whichever is most
convenient. See you soon!

<!-- Important links to define, placed up top for convenience -->

[earlier]:
  https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210304T1200&msg=HPC+Carpentries+Coworking+Hour+1
[evening]:
  https://www.timeanddate.com/worldclock/fixedtime.html?iso=20210304T2200&msg=HPC+Carpentries+Coworking+Hour+2
[last-cowork]: https://codimd.carpentries.org/UGZiD5GZSgmFSAeFMaa-GQ?view
[last-coord]: https://codimd.carpentries.org/zgd6BdqmTiWCArrVbTzVkQ

#### Check your local times

These two meeting times provide the least-painful coverage for the six
non-polar continents. Folks in Antarctica and aboard a space station are
invited to join whichever is most convenient 😉

- [12:00 UTC][earlier] &mdash; better for Africa, Asia, and Europe
- [22:00 UTC][evening] &mdash; better for the Americas and Australia

### Virtual Venue

Both meetings will use [Google Meet -URL redacted-].

### Callbacks to Previous Meetings

- [Previous Coworking Hour][last-cowork]
- [Previous Coordination Meeting][last-coord]
- Archive of old [Minutes][minutes]

---

## Earlier Meeting (Africa, Asia, and Europe)

### Participants

- _name and pronouns_
- Trevor Keller (he/they)
- Alan O'Cais

### Minutes

#### Action Items from Previous Meeting

The following Proposals were presented at our [previous Coordination
Meeting][last-coord]. Each would need 5 votes in favor to satisfy the quorum.

- [Martha's Rules proposal](https://github.com/hpc-carpentry/coordination/issues/28)
  to adopt a GitHub-based process for group decision-making.
- [Democratic Process proposal](https://github.com/hpc-carpentry/coordination/issues/36)
  to adopt a consensus-seeking representative governance model. An election
  will be held separately.

If you have not yet responded, please do so now.

#### Maintainers Needed

[hpc-intro][hpc-intro] has an active community of maintainers, but the rest of
our repositories are a little sparse. Please take a look at the
[Maintainers Teams](https://github.com/hpc-carpentry/coordination/issues/32)
and, if interested, volunteer.

Should we archive inactive lessons? Is anybody working with
[Chapel][hpc-chapel]?

#### Outstanding PRs

Several PRs on [hpc-python][hpc-python] have been open for months without
feedback. Please take a moment to review.

- Merged
  [Lean on remote carpentries-theme (#27)](https://github.com/hpc-carpentry/hpc-python/pull/27)
  using admin privileges. This PR duplicates efforts in hpc-info, etc., which
  were approved.
- Approved & merged
  [Replace Makefile with Snakefile (#28)](https://github.com/hpc-carpentry/hpc-python/pull/28),
  which cleans up some language.
- Patched my changes on
  [Use profiles for snakemake cluster configuration (#29)](https://github.com/hpc-carpentry/hpc-python/pull/29)
  and merged.

#### Other Business

- JupyterLab is an increasingly common interface to HPC systems and there are a
  **lot** of plugins available
  - C++, Julia, Octave, R, Ruby, Matlab, ...
  - plugin for Xpra lets the admins abstract away the SSH tunneling stuff, so
    the users just get pretty, hardware-accelerated visuals.
  - Might be interesting to have an (alternative) episode that covers this
    interface and how to get a terminal there

---

## Later Meeting (Americas & Australia)

### Participants

- _name and pronouns_
- Trevor Keller (he/they)
- Anthony Shaw (he/any)(NeSI)
- Mike Renfro
- Wes Harrell (he/any) (NeSI)
- Callum Walley (he/any)
- Dini Senanayake (he/any)(NeSI)

Large contingent from [NeSI](https://www.nesi.org.nz) (NZ eScience
Infrastructure) Application Support team! Training is a big component, so
they're here to help :-)

### Minutes

Mike & Wes are both getting ready to deploy site-specific builds of the HPC
Intro materials.

#### Action Items from Previous Meeting

The following Proposals were presented at our [previous Coordination
Meeting][last-coord]. Each would need 5 votes in favor to satisfy the quorum.

- [Martha's Rules proposal](https://github.com/hpc-carpentry/coordination/issues/28)
  to adopt a GitHub-based process for group decision-making.
- [Democratic Process proposal](https://github.com/hpc-carpentry/coordination/issues/36)
  to adopt a consensus-seeking representative governance model. An election
  will be held separately.

If you have not yet responded, please do so now.

#### NeSI

Sent by Megan Guidry (training lead), NeSI has maintained their own training
material & borrowed some from HPC Carpentry. They would like to adopt our
templated lesson material to reduce their maintenance overhead, and hopefully
contribute back to this effort.

We spent some time on introductions, and a fast-paced crash course on the
contents of the repository (esp. what & where to make changes).

---

<!--HPC Carpentry References-->

[coordination]: https://github.com/hpc-carpentry/coordination
[minutes]: https://github.com/hpc-carpentry/coordination/tree/main/minutes
[website]: https://github.com/hpc-carpentry/hpc-carpentry.github.io
[hpc-chapel]: https://github.com/hpc-carpentry/hpc-chapel
[hpc-intro]: https://github.com/carpentries-incubator/hpc-intro
[hpc-parallel]: https://github.com/hpc-carpentry/hpc-parallel-novice
[hpc-python]: https://github.com/hpc-carpentry/hpc-python
[hpc-shell]: https://github.com/hpc-carpentry/hpc-shell

<!--Carpentries References-->

[conduct]:
  https://docs.carpentries.org/topic_folders/policies/code-of-conduct.html
[invite]: https://swc-slack-invite.herokuapp.com/
[license]: https://creativecommons.org/licenses/by/4.0/
[slack]: https://swcarpentry.slack.com
